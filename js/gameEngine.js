/**
 * L'ORATORE - Core Game Engine v3.0
 * Features:
 * - 6 Difficulty Levels (A1, A2, B1, B2, C1, C2)
 * - Round-Based Shared Thematic Challenge (Round Category selection)
 * - Ops! Storia Turn Sequence: 2-Min Card -> Summary Screen -> Full Board Animation -> Next Turn/Round
 * - Firestore Card Syncing
 */

const GameEngine = {
  data: null,
  gameState: {
    mode: 'PROIBITE', // 'PROIBITE' | 'USARE'
    selectedLevel: 'b1', // 'a1'..'c2'
    currentRound: 1,
    roundChoosingTeamIdx: 0,
    currentRoundDeck: 'epica',
    turnInCurrentRound: 0,
    
    teamsCount: 2,
    teams: [],
    currentTeamIdx: 0,
    
    turnTimer: 120,
    timerInterval: null,
    timeRemaining: 120,
    isTimerRunning: false,
    
    currentCard: null,
    usedCardIds: new Set(),
    penaltiesThisTurn: 0,
    wordsHitThisTurn: [false, false, false, false, false],
    selectedOratorLevel: null,
    stepsGainedThisTurn: 0,
    bonusTimeNextTurn: 0,
    specialTileTriggered: null,
    isGameFinished: false
  },

  async loadData() {
    // 1. Inizializzazione sincrona immediata se disponibile in window
    if (window.L_ORATORE_DEFAULT_CARDS) {
      try {
        this.data = JSON.parse(JSON.stringify(window.L_ORATORE_DEFAULT_CARDS));
      } catch (err) {
        this.data = window.L_ORATORE_DEFAULT_CARDS;
      }
    }

    try {
      const res = await fetch('data/consegne.json');
      if (res && res.ok) {
        const fetchedData = await res.json();
        if (fetchedData && fetchedData.carte && fetchedData.carte.length > 0) {
          this.data = fetchedData;
        }
      }
    } catch (e) {
      console.warn("Local fetch warning (using embedded cards-data.js):", e);
    }

    if (!this.data) {
      this.data = { carte: [], livelli: [], mazzi: [] };
    }

    // Sincronizzazione LiveEditor Overrides e Firestore
    if (window.LiveEditor && window.LiveEditor.overrides) {
      Object.values(window.LiveEditor.overrides).forEach(item => {
        const c = item.data || item;
        if (c && c.mazzo && c.livello) {
          const existingIdx = this.data.carte.findIndex(base => base.id === c.id || (base.mazzo === c.mazzo && base.livello === c.livello && (c.slot ? base.slot === c.slot : base.titolo === c.titolo)));
          if (existingIdx >= 0) {
            this.data.carte[existingIdx] = { ...this.data.carte[existingIdx], ...c };
          } else {
            this.data.carte.push(c);
          }
        }
      });
    }

    // Sincronizzazione da custom cards locali
    const localStored = localStorage.getItem('loratore_custom_cards') || localStorage.getItem('loratore_didactic_overrides');
    if (localStored) {
      try {
        const custom = JSON.parse(localStored);
        Object.values(custom).forEach(item => {
          const c = item.data || item;
          if (c && c.mazzo && c.livello) {
            const existingIdx = this.data.carte.findIndex(base => base.id === c.id || (base.mazzo === c.mazzo && base.livello === c.livello && (c.slot ? base.slot === c.slot : base.titolo === c.titolo)));
            if (existingIdx >= 0) {
              this.data.carte[existingIdx] = { ...this.data.carte[existingIdx], ...c };
            } else {
              this.data.carte.push(c);
            }
          }
        });
      } catch (lErr) {}
    }

    return this.data;
  },

  initGame(teamsList, mode, levelId) {
    this.gameState.teams = teamsList.map((t, idx) => ({
      ...t,
      id: t.id || `team_${idx + 1}`,
      position: 1,
      score: 0
    }));
    this.gameState.teamsCount = teamsList.length;
    this.gameState.mode = mode || 'PROIBITE';
    this.gameState.selectedLevel = levelId || 'b1';
    
    this.gameState.currentRound = 1;
    this.gameState.roundChoosingTeamIdx = 0;
    this.gameState.turnInCurrentRound = 0;
    this.gameState.currentTeamIdx = 0;
    
    this.gameState.usedCardIds.clear();
    this.gameState.bonusTimeNextTurn = 0;
    this.gameState.isGameFinished = false;

    // Avvia la scelta della Categoria per il Round 1
    this.startRoundCategorySelection();
  },

  // 1. Schermata Scelta Categoria per il Round
  startRoundCategorySelection() {
    this.stopTimer();
    const choosingTeam = this.gameState.teams[this.gameState.roundChoosingTeamIdx];
    const header = document.getElementById('round-category-header');
    const grid = document.getElementById('round-decks-grid');
    if (!header || !grid || !choosingTeam) return;

    header.innerHTML = `
      <div style="background: rgba(255,255,255,0.06); border: 1px solid ${choosingTeam.color}88; padding: 6px 18px; border-radius: 30px; margin-bottom: 14px; display: inline-flex; align-items: center; gap: 8px;">
        <span style="width: 10px; height: 10px; border-radius: 50%; background: ${choosingTeam.color}; box-shadow: 0 0 10px ${choosingTeam.color}; display: inline-block;"></span>
        <span style="color: ${choosingTeam.color}; font-weight: 800; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Round ${this.gameState.currentRound}</span>
      </div>
      <h2 class="setup-title" style="color: ${choosingTeam.color}; font-size: 1.85rem; font-weight: 900; display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;">
        <img src="${choosingTeam.avatar}" style="width: 44px; height: 44px; border-radius: 50%; border: 2.5px solid ${choosingTeam.color}; box-shadow: 0 0 16px ${choosingTeam.color}88; object-fit: contain; background: #000;">
        <span>${choosingTeam.name}, è il tuo turno! Scegli la categoria del round!</span>
      </h2>
      <p class="setup-subtitle" style="font-size: 1rem; color: #cbd5e1; margin-top: 6px;">Tutte le squadre in questo Round si sfideranno su tracce della categoria che stai per scegliere.</p>
    `;

    const defaultDecks = [
      { id: 'epica', emoji: '🏺', nome: 'Mito & Epica Classica', descrizione: "Eroi immortali, mostri mitologici, profezie e grandi viaggi dell'antichità." },
      { id: 'medioevo', emoji: '👑', nome: 'Medioevo & Cavalieri', descrizione: "Castelli sotto assedio, tornei cavallereschi, intrighi di corte e leggende feudali." },
      { id: 'fantascienza', emoji: '🚀', nome: 'Fantascienza & Futuro', descrizione: "Esplorazioni interstellari, intelligenze artificiali, mondi alieni e viaggi temporali." },
      { id: 'teatro', emoji: '🎭', nome: 'Teatro & Spettacolo', descrizione: "Commedie, tragedie, colpi di scena sul palco e il fascino della recitazione." },
      { id: 'letteratura', emoji: '📜', nome: 'Letteratura & Poesia', descrizione: "Grandi capolavori, poeti visionari, misteri narrativi e romanzi senza tempo." },
      { id: 'civilta', emoji: '🌍', nome: 'Mondo, Storia & Civiltà', descrizione: "Grandi civiltà del passato, rotte commerciali, scoperte geografiche e culture del mondo." },
      { id: 'scienza', emoji: '🧪', nome: 'Scienza, Natura & Misteri', descrizione: "Scoperte rivoluzionarie, abissi oceanici, fenomeni cosmici e sfide ambientali." },
      { id: 'party', emoji: '🧩', nome: 'Party & Creatività Libera', descrizione: "Situazioni assurde, paradossi divertenti, dibattiti accesi e improvvisazione pura." }
    ];

    const mazzi = (this.data && this.data.mazzi && this.data.mazzi.length > 0) ? this.data.mazzi : defaultDecks;
    grid.innerHTML = mazzi.map(m => `
      <div class="deck-choice-card" onclick="GameEngine.selectRoundDeck('${m.id}')">
        <div class="deck-card-top">
          <span class="deck-card-emoji">${m.emoji}</span>
          <h3 class="deck-card-title">${m.nome}</h3>
        </div>
        <p class="deck-card-desc">${m.descrizione}</p>
      </div>
    `).join('');

    App.showView('view-round-select-category');
  },

  selectRoundDeck(deckId) {
    this.gameState.currentRoundDeck = deckId;
    this.gameState.turnInCurrentRound = 0;
    this.gameState.currentTeamIdx = this.gameState.roundChoosingTeamIdx;
    
    if (window.AudioEngine && window.AudioEngine.playChime) {
      window.AudioEngine.playChime();
    }

    this.startTurn();
  },

  // 2. Avvio del Turno di Discorso (2 Minuti)
  startTurn() {
    this.stopTimer();
    this.gameState.penaltiesThisTurn = 0;
    this.gameState.wordsHitThisTurn = [false, false, false, false, false];
    this.gameState.specialTileTriggered = null;

    // Estrai carta della categoria del round e del livello scelto
    this.pickNextCard();

    // Calcola durata timer (120s base + eventuale bonus)
    let duration = this.gameState.turnTimer;
    if (this.gameState.bonusTimeNextTurn > 0) {
      duration += this.gameState.bonusTimeNextTurn;
      this.gameState.bonusTimeNextTurn = 0;
    }

    this.gameState.timeRemaining = duration;
    this.updateTimerUI();
    this.renderTurnUI();

    App.showView('view-game');
  },

  pickNextCard() {
    if (!this.data || !this.data.carte || this.data.carte.length === 0) return;

    const deckId = this.gameState.currentRoundDeck;
    const levelId = this.gameState.selectedLevel;

    // 1. Cerca carte non ancora usate per questo mazzo e livello
    let available = this.data.carte.filter(c => {
      const matchDeck = (c.mazzo === deckId);
      const matchLevel = (!c.livello || c.livello === levelId);
      return matchDeck && matchLevel && !this.gameState.usedCardIds.has(c.id);
    });

    // 2. Se finite, cerca nel mazzo qualsiasi livello non ancora usato
    if (available.length === 0) {
      available = this.data.carte.filter(c => c.mazzo === deckId && !this.gameState.usedCardIds.has(c.id));
    }

    // 3. Se tutte le carte del mazzo sono state usate, azzera usedCardIds per questo mazzo
    if (available.length === 0) {
      available = this.data.carte.filter(c => c.mazzo === deckId);
    }

    // 4. Fallback generale su tutte le carte
    if (available.length === 0) {
      available = this.data.carte;
    }

    const randomCard = available[Math.floor(Math.random() * available.length)];
    this.gameState.currentCard = randomCard;
    if (randomCard && randomCard.id) {
      this.gameState.usedCardIds.add(randomCard.id);
    }
  },

  renderTurnUI() {
    const currentTeam = this.gameState.teams[this.gameState.currentTeamIdx];
    const card = this.gameState.currentCard;
    if (!currentTeam || !card) return;

    // Info Squadra HUD
    const teamAvatar = document.getElementById('turn-team-avatar');
    const teamName = document.getElementById('turn-team-name');
    const teamSub = document.getElementById('turn-team-sub');
    const hudPill = document.getElementById('active-team-hud-pill');

    if (teamAvatar) teamAvatar.src = currentTeam.avatar;
    if (teamName) {
      teamName.textContent = currentTeam.name;
      teamName.style.color = currentTeam.color;
    }
    if (teamSub) teamSub.textContent = `Turno ${this.gameState.turnInCurrentRound + 1} di ${this.gameState.teamsCount}`;
    if (hudPill) hudPill.style.borderColor = currentTeam.color;

    // Round HUD Pill (Solo Round X)
    const roundLabel = document.getElementById('hud-round-label');
    if (roundLabel) roundLabel.textContent = `Round ${this.gameState.currentRound}`;

    // Info Carta
    const deckTag = document.getElementById('card-deck-tag');
    const levelBadge = document.getElementById('card-level-badge');
    const cardTitle = document.getElementById('card-title');
    const cardIncipit = document.getElementById('card-incipit');

    const mazzoObj = this.data && this.data.mazzi ? this.data.mazzi.find(m => m.id === this.gameState.currentRoundDeck) : null;
    const levelObj = this.data && this.data.livelli ? this.data.livelli.find(l => l.id === this.gameState.selectedLevel) : null;

    if (deckTag && mazzoObj) deckTag.innerHTML = `${mazzoObj.emoji} ${mazzoObj.nome}`;
    if (levelBadge && levelObj) levelBadge.innerHTML = levelObj.badge;
    if (cardTitle) cardTitle.textContent = card.titolo || "Titolo Traccia";
    if (cardIncipit) cardIncipit.textContent = card.incipit || "Incipit narrativo...";

    // Parole Proibite vs Parole da Usare (Estrae in modo difensivo con fallback sicuri)
    const wordsHeader = document.getElementById('card-words-header');
    const wordsGrid = document.getElementById('card-words-grid');

    const proibite = (card.parole_proibite && card.parole_proibite.length > 0) ? card.parole_proibite :
                    (card.paroleProibite && card.paroleProibite.length > 0) ? card.paroleProibite :
                    (card.vietate && card.vietate.length > 0) ? card.vietate :
                    ["Parola 1", "Parola 2", "Parola 3", "Parola 4", "Parola 5"];

    const usare = (card.parole_da_usare && card.parole_da_usare.length > 0) ? card.parole_da_usare :
                 (card.paroleDaUsare && card.paroleDaUsare.length > 0) ? card.paroleDaUsare :
                 (card.usare && card.usare.length > 0) ? card.usare :
                 ["Termine 1", "Termine 2", "Termine 3", "Termine 4", "Termine 5"];

    const words = this.gameState.mode === 'PROIBITE' ? proibite : usare;

    if (wordsHeader) {
      wordsHeader.innerHTML = this.gameState.mode === 'PROIBITE' 
        ? `<i class="fa-solid fa-ban" style="color: var(--danger-color);"></i> 5 PAROLE PROIBITE (VIETATE):` 
        : `<i class="fa-solid fa-bullseye" style="color: var(--success-color);"></i> 5 VOCABOLI DA INSERIRE NEL DISCORSO:`;
      wordsHeader.style.color = this.gameState.mode === 'PROIBITE' ? "#f87171" : "#34d399";
    }

    if (wordsGrid) {
      const isUsare = this.gameState.mode === 'USARE';
      wordsGrid.innerHTML = (words || []).map((w, idx) => `
        <div class="word-chip ${isUsare ? 'mode-usare' : ''}" id="word-chip-${idx}" onclick="GameEngine.toggleWord(${idx})">
          <span>${w}</span>
        </div>
      `).join('');
    }

    // Reset badge buzzer
    const buzzerBadge = document.getElementById('buzzer-count-badge');
    if (buzzerBadge) buzzerBadge.textContent = '0';
  },

  toggleWord(idx) {
    this.gameState.wordsHitThisTurn[idx] = !this.gameState.wordsHitThisTurn[idx];
    const chip = document.getElementById(`word-chip-${idx}`);
    if (chip) {
      chip.classList.toggle('selected', this.gameState.wordsHitThisTurn[idx]);
    }
    if (this.gameState.mode === 'PROIBITE' && this.gameState.wordsHitThisTurn[idx]) {
      this.triggerBuzzer();
    } else if (this.gameState.mode === 'USARE' && this.gameState.wordsHitThisTurn[idx]) {
      if (window.AudioEngine && window.AudioEngine.playChime) window.AudioEngine.playChime();
    }
  },

  triggerBuzzer() {
    this.gameState.penaltiesThisTurn++;
    if (window.AudioEngine && window.AudioEngine.playBuzzer) window.AudioEngine.playBuzzer();

    const badge = document.getElementById('buzzer-count-badge');
    if (badge) badge.textContent = this.gameState.penaltiesThisTurn;

    const buzzerBtn = document.getElementById('btn-buzzer-penalty');
    if (buzzerBtn) {
      buzzerBtn.style.transform = 'scale(0.95)';
      setTimeout(() => buzzerBtn.style.transform = 'none', 150);
    }
  },

  startTimer() {
    if (this.gameState.isTimerRunning) return;
    this.gameState.isTimerRunning = true;
    const btn = document.getElementById('timer-toggle-btn');
    if (btn) btn.innerHTML = '<i class="fa-solid fa-pause"></i> Pausa';

    this.gameState.timerInterval = setInterval(() => {
      this.gameState.timeRemaining--;
      if (this.gameState.timeRemaining <= 5 && this.gameState.timeRemaining > 0) {
        if (window.AudioEngine && window.AudioEngine.playTick) window.AudioEngine.playTick();
      }
      this.updateTimerUI();

      if (this.gameState.timeRemaining <= 0) {
        this.stopTimer();
        if (window.AudioEngine && window.AudioEngine.playBuzzer) window.AudioEngine.playBuzzer();
        this.finishTurn();
      }
    }, 1000);
  },

  stopTimer() {
    this.gameState.isTimerRunning = false;
    if (this.gameState.timerInterval) {
      clearInterval(this.gameState.timerInterval);
      this.gameState.timerInterval = null;
    }
    const btn = document.getElementById('timer-toggle-btn');
    if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i> Avvia Discorso';
  },

  toggleTimer() {
    if (this.gameState.isTimerRunning) {
      this.stopTimer();
    } else {
      this.startTimer();
    }
  },

  updateTimerUI() {
    const mins = Math.floor(this.gameState.timeRemaining / 60);
    const secs = this.gameState.timeRemaining % 60;
    const formatted = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

    const digits = document.getElementById('timer-digits');
    if (digits) digits.textContent = formatted;

    const progressCircle = document.getElementById('timer-progress');
    if (progressCircle) {
      const percentage = (this.gameState.timeRemaining / this.gameState.turnTimer) * 100;
      progressCircle.style.strokeDashoffset = 100 - percentage;
    }
  },

  // 3. Conclusione Turno -> Calcolo Passi & Mostra SUMMARY (Stile Ops! Storia)
  calculateFinalSteps() {
    const level = this.gameState.selectedOratorLevel;
    if (level === null || level === undefined) {
      return null;
    }
    if (level === 0) {
      return 0;
    }

    if (this.gameState.mode === 'PROIBITE') {
      // Livello Oratore - Penalità Buzzer
      return Math.max(0, level - this.gameState.penaltiesThisTurn);
    } else {
      // Modalità Lessico (Parole da Usare)
      const countUsed = this.gameState.wordsHitThisTurn.filter(Boolean).length;
      let vocabMod = 0;
      if (countUsed === 5) vocabMod = 1;
      else if (countUsed <= 1) vocabMod = -1;
      return Math.min(4, Math.max(0, level + vocabMod));
    }
  },

  selectOratorLevel(level) {
    this.gameState.selectedOratorLevel = level;
    const finalSteps = this.calculateFinalSteps();
    this.gameState.stepsGainedThisTurn = (finalSteps !== null) ? finalSteps : 0;
    if (window.AudioEngine && window.AudioEngine.playChime) {
      window.AudioEngine.playChime();
    }
    this.renderSummaryUI();
  },

  finishTurn() {
    this.stopTimer();
    this.gameState.selectedOratorLevel = null; // Nessuna preselezione automatica (stato neutro)
    this.gameState.stepsGainedThisTurn = 0;
    this.renderSummaryUI();
    App.showView('view-summary');
  },

  renderSummaryUI() {
    const box = document.getElementById('turn-summary-box');
    const currentTeam = this.gameState.teams[this.gameState.currentTeamIdx];
    if (!box || !currentTeam) return;

    const isProibite = this.gameState.mode === 'PROIBITE';
    const countUsed = this.gameState.wordsHitThisTurn.filter(Boolean).length;
    const currentLevel = this.gameState.selectedOratorLevel;
    const isLevelSelected = (currentLevel !== null && currentLevel !== undefined);
    const steps = isLevelSelected ? this.gameState.stepsGainedThisTurn : null;

    box.innerHTML = `
      <div class="summary-card">
        <div class="summary-team-header">
          <img src="${currentTeam.avatar}" alt="${currentTeam.name}" class="summary-team-avatar" style="border-color: ${currentTeam.color}">
          <div>
            <h2 class="summary-title" style="color: ${currentTeam.color}">${currentTeam.name}</h2>
            <div class="summary-subtitle">Discorso Concluso • Round ${this.gameState.currentRound}</div>
          </div>
        </div>

        <!-- Valutazione Docente: Livelli dell'Oratore -->
        <div class="orator-levels-box">
          <div class="orator-levels-title">
            <i class="fa-solid fa-gavel" style="color: var(--accent-gold);"></i> Valutazione Docente: Livello dell'Oratore
          </div>
          <div class="orator-levels-grid">
            <div class="orator-level-btn ${currentLevel === 3 ? 'active' : ''}" onclick="GameEngine.selectOratorLevel(3)">
              <div class="orator-level-badge">🥇</div>
              <div class="orator-level-info">
                <div class="orator-level-name">Grande Oratore</div>
                <div class="orator-level-pts">+3 Passi Base</div>
              </div>
            </div>
            <div class="orator-level-btn ${currentLevel === 2 ? 'active' : ''}" onclick="GameEngine.selectOratorLevel(2)">
              <div class="orator-level-badge">🥈</div>
              <div class="orator-level-info">
                <div class="orator-level-name">Buon Narratore</div>
                <div class="orator-level-pts">+2 Passi Base</div>
              </div>
            </div>
            <div class="orator-level-btn ${currentLevel === 1 ? 'active' : ''}" onclick="GameEngine.selectOratorLevel(1)">
              <div class="orator-level-badge">🥉</div>
              <div class="orator-level-info">
                <div class="orator-level-name">Apprendista</div>
                <div class="orator-level-pts">+1 Passo Base</div>
              </div>
            </div>
            <div class="orator-level-btn ${currentLevel === 0 ? 'active' : ''}" onclick="GameEngine.selectOratorLevel(0)">
              <div class="orator-level-badge">⚪</div>
              <div class="orator-level-info">
                <div class="orator-level-name">Passo / Rinuncia</div>
                <div class="orator-level-pts">0 Passi</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Dettaglio Vincoli e Statistiche -->
        <div class="summary-stats-box">
          ${isProibite ? `
            <div class="summary-stat-row">
              <span><i class="fa-solid fa-bell" style="color: var(--danger-color);"></i> Penalità / Errori Buzzer:</span>
              <span class="summary-stat-val" style="color: ${this.gameState.penaltiesThisTurn === 0 ? 'var(--success-color)' : 'var(--danger-color)'};">
                ${this.gameState.penaltiesThisTurn} ${this.gameState.penaltiesThisTurn === 0 ? '🎉 (Nessun errore buzzer!)' : `(-${this.gameState.penaltiesThisTurn} ${this.gameState.penaltiesThisTurn === 1 ? 'passo' : 'passi'})`}
              </span>
            </div>
          ` : `
            <div class="summary-stat-row">
              <span><i class="fa-solid fa-bullseye" style="color: var(--success-color);"></i> Vocaboli Chiave Inseriti:</span>
              <span class="summary-stat-val" style="color: var(--success-color);">${countUsed} / 5 ${countUsed === 5 ? '🌟 (+1 Bonus!)' : (countUsed <= 1 ? '⚠️ (-1)' : '')}</span>
            </div>
          `}
        </div>

        <div class="summary-steps-highlight ${!isLevelSelected ? 'pending' : ''}">
          <i class="fa-solid fa-shoe-prints"></i>
          <span>Avanzamento Finale: <strong>${isLevelSelected ? `+${steps} ${steps === 1 ? 'Casella' : 'Caselle'}` : `<span style="color: #94a3b8; font-weight: 500; font-size: 0.95rem;">(In attesa della valutazione...)</span>`}</strong></span>
        </div>

        <button class="btn btn-primary btn-giant" style="width: 100%; padding: 16px;" ${!isLevelSelected ? 'disabled' : ''} onclick="GameEngine.goToBoard()">
          <i class="fa-solid ${isLevelSelected ? 'fa-chess-board' : 'fa-hand-pointer'}"></i> ${isLevelSelected ? 'Vai al Tabellone & Muovi Pedina' : 'Seleziona un Livello per Procedere'}
        </button>
      </div>
    `;
  },

  // 4. Mostra Tabellone & Anima Pedina (Stile Ops! Storia)
  goToBoard() {
    if (this.gameState.selectedOratorLevel === null || this.gameState.selectedOratorLevel === undefined) {
      alert("Seleziona prima il Livello dell'Oratore per convalidare il turno!");
      return;
    }
    const currentTeam = this.gameState.teams[this.gameState.currentTeamIdx];
    if (!currentTeam) return;

    App.showView('view-game-board');

    const oldPos = currentTeam.position || 1;
    let newPos = Math.min(24, oldPos + this.gameState.stepsGainedThisTurn);

    // Renderizza stato iniziale pedine
    BoardEngine.renderPawns(this.gameState.teams);
    this.renderScoreboard();

    const statusSub = document.getElementById('board-status-sub');
    if (statusSub) {
      statusSub.innerHTML = `<span style="color:${currentTeam.color}"><strong>${currentTeam.name}</strong> avanza di +${this.gameState.stepsGainedThisTurn} caselle...</span>`;
    }

    // Anima movimento pedina passo-passo
    BoardEngine.animatePawnStepByStep(currentTeam.id, oldPos, newPos, () => {
      currentTeam.position = newPos;

      // Controllo Caselle Speciali
      let specialMsg = '';
      if (BoardEngine.specialTiles && BoardEngine.specialTiles[newPos]) {
        const special = BoardEngine.specialTiles[newPos];
        if (special.type === 'TEMPO_X2') {
          this.gameState.bonusTimeNextTurn = 30;
          specialMsg = ` • <span style="color:#f1c40f">✖️2 <strong>${special.label}!</strong> ${special.desc}</span>`;
        } else if (special.type === 'PESCA_CARTA') {
          this.gameState.bonusTimeNextTurn = 30;
          specialMsg = ` • <span style="color:#38bdf8">🎣 <strong>${special.label}!</strong> ${special.desc}</span>`;
        } else if (special.type === 'PEDINA_BONUS') {
          const forwardPos = Math.min(24, newPos + 1);
          currentTeam.position = forwardPos;
          specialMsg = ` • <span style="color:#a855f7">♟️ <strong>${special.label}!</strong> Avanza a casella ${forwardPos}</span>`;
          BoardEngine.renderPawns(this.gameState.teams);
        } else if (special.type === 'CHECKPOINT') {
          specialMsg = ` • <span style="color:#4ade80">📍 <strong>${special.label}!</strong> Punto di controllo raggiunto</span>`;
        }
      }

      if (statusSub) {
        statusSub.innerHTML = `<span style="color:${currentTeam.color}"><strong>${currentTeam.name}</strong> ha raggiunto la Casella ${currentTeam.position} / 24</span>${specialMsg}`;
      }

      this.renderScoreboard();

      // Controllo Vittoria Finale
      if (currentTeam.position >= 24) {
        this.gameState.isGameFinished = true;
        if (window.AudioEngine && window.AudioEngine.playFanfare) window.AudioEngine.playFanfare();
        alert(`🏆 VITTORIA FINALE!\n\n${currentTeam.name} ha raggiunto il Traguardo 24 e trionfa nella sfida dell'Oratore!`);
        
        const btnAction = document.getElementById('btn-board-next-action');
        if (btnAction) {
          btnAction.innerHTML = `<i class="fa-solid fa-trophy"></i> Nuova Partita`;
          btnAction.onclick = () => App.showView('view-welcome');
        }
        return;
      }

      // Aggiorna pulsante di azione successivo
      const btnAction = document.getElementById('btn-board-next-action');
      const isRoundFinished = (this.gameState.turnInCurrentRound >= this.gameState.teams.length - 1);

      if (btnAction) {
        if (isRoundFinished) {
          btnAction.innerHTML = `<i class="fa-solid fa-flag-checkered"></i> <span>Concludi Round ${this.gameState.currentRound}</span>`;
          btnAction.onclick = () => GameEngine.proceedAfterBoard();
        } else {
          const nextTeamIdx = (this.gameState.currentTeamIdx + 1) % this.gameState.teams.length;
          const nextTeam = this.gameState.teams[nextTeamIdx];
          btnAction.innerHTML = `<i class="fa-solid fa-arrow-right"></i> <span>Turno Prossimo: ${nextTeam ? nextTeam.name : 'Squadra'}</span>`;
          btnAction.onclick = () => GameEngine.proceedAfterBoard();
        }
      }
    });
  },

  // 5. Passaggio al turno o round successivo
  proceedAfterBoard() {
    if (this.gameState.isGameFinished) {
      App.showView('view-welcome');
      return;
    }

    const isRoundFinished = (this.gameState.turnInCurrentRound >= this.gameState.teams.length - 1);

    if (isRoundFinished) {
      // Round Concluso -> Passa la scelta della categoria alla squadra successiva
      this.gameState.currentRound++;
      this.gameState.roundChoosingTeamIdx = (this.gameState.roundChoosingTeamIdx + 1) % this.gameState.teams.length;
      this.startRoundCategorySelection();
    } else {
      // Prossimo Turno nello stesso Round (stessa categoria)
      this.gameState.turnInCurrentRound++;
      this.gameState.currentTeamIdx = (this.gameState.currentTeamIdx + 1) % this.gameState.teams.length;
      this.startTurn();
    }
  },

  renderScoreboard() {
    const strip = document.getElementById('teams-scoreboard-strip');
    if (!strip) return;

    strip.innerHTML = this.gameState.teams.map((t, idx) => `
      <div class="team-score-card ${idx === this.gameState.currentTeamIdx ? 'current' : ''}" style="border-color: ${t.color}">
        <div style="display:flex; align-items:center; justify-content:center; gap:6px; margin-bottom:4px;">
          <img src="${t.avatar}" style="width:24px; height:24px; border-radius:50%; object-fit:cover; border: 1.5px solid ${t.color};">
          <span class="team-score-name" style="color: ${t.color}">${t.name}</span>
        </div>
        <div class="team-score-pos">Casella ${t.position || 1} / 24</div>
      </div>
    `).join('');
  }
};

window.GameEngine = GameEngine;
