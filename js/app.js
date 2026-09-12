/**
 * L'ORATORE - Main Application Controller v3.0
 * Handles 4-Step Setup Flow, 10 Giant Pawns Selection, 6 Difficulty Levels, and View Routing
 */

const App = {
  currentView: 'view-welcome',
  availablePawns: [
    'assets/pedine/1.png',
    'assets/pedine/2.png',
    'assets/pedine/3.png',
    'assets/pedine/4.png',
    'assets/pedine/5.png',
    'assets/pedine/6.png',
    'assets/pedine/7.png',
    'assets/pedine/8.png',
    'assets/pedine/9.png',
    'assets/pedine/10.png'
  ],

  teamColorPalettes: ['#ef4444', '#3b82f6', '#10b981', '#f59e0b'],
  teamDefaultNames: ['Squadra Rossa', 'Squadra Blu', 'Squadra Verde', 'Squadra Gialla'],

  selectedSetup: {
    teamsCount: 2,
    teams: [],
    currentPawnTeamIdx: 0,
    mode: 'PROIBITE', // 'PROIBITE' | 'USARE'
    level: 'b1'       // 'a1'..'c2'
  },

  async init() {
    await GameEngine.loadData();
    if (window.AudioEngine && window.AudioEngine.init) window.AudioEngine.init();
    this.renderLevelGrid();

    // Chiudi dropdown utente cliccando fuori
    document.addEventListener('click', (e) => {
      const dd = document.getElementById('user-dropdown');
      const trigger = document.getElementById('user-menu-trigger');
      if (dd && trigger && !trigger.contains(e.target) && !dd.contains(e.target)) {
        dd.classList.add('hidden');
      }
    });

    // Gestione tasto indietro/avanti nativo del browser
    window.addEventListener('popstate', (e) => {
      if (e.state && e.state.view) {
        this.showView(e.state.view, false);
      } else {
        this.showView('view-home', false);
      }
    });

    // Imposta stato iniziale cronologia
    if (!window.history.state) {
      window.history.replaceState({ view: 'view-home' }, '', '#home');
    }

    console.log("L'Oratore v3.0 initialized with 6 QCER levels, shared round categories, and Ops! Storia turn flow.");
  },

  showView(viewId, pushHistory = true) {
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    const target = document.getElementById(viewId);
    if (target) {
      target.classList.add('active');
      this.currentView = viewId;
    }

    if (pushHistory && window.history && (!window.history.state || window.history.state.view !== viewId)) {
      window.history.pushState({ view: viewId }, '', '#' + viewId.replace('view-', ''));
    }

    // Update bottom nav active state
    document.querySelectorAll('.bottom-bar .tab-item').forEach(tab => {
      if (tab.getAttribute('data-view') === viewId) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  toggleUserDropdown(event) {
    if (event) event.stopPropagation();
    const dd = document.getElementById('user-dropdown');
    if (dd) dd.classList.toggle('hidden');
  },

  startSetupFlow() {
    this.selectedSetup = {
      teamsCount: null,
      teams: [],
      currentPawnTeamIdx: 0,
      mode: null,
      level: null
    };
    this.showView('view-setup-teams');
  },

  // Step 1: Scelta Numero Squadre
  selectTeamsCount(count) {
    this.selectedSetup.teamsCount = count;
    this.selectedSetup.teams = [];
    for (let i = 0; i < count; i++) {
      this.selectedSetup.teams.push({
        id: `team_${i + 1}`,
        name: this.teamDefaultNames[i],
        color: this.teamColorPalettes[i],
        avatar: null,
        position: 1,
        score: 0
      });
    }

    this.selectedSetup.currentPawnTeamIdx = 0;
    this.renderPawnPicker();
    this.showView('view-setup-pawns');
  },

  // Step 2: Scelta Pedine Giganti (10 Personaggi con selezione cromatica dinamica)
  renderPawnPicker() {
    const currentTeam = this.selectedSetup.teams[this.selectedSetup.currentPawnTeamIdx];
    const teamHeader = document.getElementById('pawn-team-picker-header');
    const pawnGrid = document.getElementById('pawns-choice-grid');
    if (!teamHeader || !pawnGrid || !currentTeam) return;

    // Pedine già scelte dalle squadre precedenti
    const chosenByPrevTeams = {};
    for (let i = 0; i < this.selectedSetup.currentPawnTeamIdx; i++) {
      const prev = this.selectedSetup.teams[i];
      if (prev && prev.avatar) {
        chosenByPrevTeams[prev.avatar] = prev;
      }
    }

    teamHeader.innerHTML = `
      <span class="setup-step-badge">Passo 2 di 4</span>
      <h2 class="setup-title" style="color:${currentTeam.color}">
        <i class="fa-solid fa-chess-pawn"></i> Scegli la Pedina per ${currentTeam.name}
      </h2>
      <p class="setup-subtitle">Squadra ${this.selectedSetup.currentPawnTeamIdx + 1} di ${this.selectedSetup.teamsCount}: clicca su un personaggio per sceglierlo e procedere.</p>
    `;

    // Rimuovi eventuale vecchio wrapper conferma se presente
    const oldConfirm = document.getElementById('pawn-confirm-wrap');
    if (oldConfirm) oldConfirm.remove();

    pawnGrid.innerHTML = this.availablePawns.map((pawnSrc, idx) => {
      const isTakenByPrev = chosenByPrevTeams[pawnSrc];
      const isSelectedByCurrent = (currentTeam.avatar === pawnSrc);

      if (isTakenByPrev) {
        return `
          <div class="pawn-choice-card-giant taken" style="border: 2px solid ${isTakenByPrev.color}; opacity: 0.45; cursor: not-allowed; position: relative;">
            <div style="position: absolute; top: 6px; right: 6px; background: ${isTakenByPrev.color}; color: white; font-size: 0.7rem; font-weight: 800; padding: 2px 6px; border-radius: 6px;">${isTakenByPrev.name}</div>
            <img src="${pawnSrc}" alt="Personaggio ${idx + 1}" class="pawn-choice-img" style="filter: grayscale(60%);">
            <span class="pawn-choice-label" style="color: ${isTakenByPrev.color}; font-weight: 700;">${isTakenByPrev.name}</span>
          </div>
        `;
      }

      return `
        <div class="pawn-choice-card-giant ${isSelectedByCurrent ? 'selected' : ''}" 
             onclick="App.selectPawnCandidate('${pawnSrc}')" 
             style="border: 2px solid rgba(255,255,255,0.15); cursor: pointer; transition: all 0.2s;"
             onmouseover="this.style.borderColor='${currentTeam.color}'; this.style.transform='scale(1.05)';"
             onmouseout="this.style.borderColor='rgba(255,255,255,0.15)'; this.style.transform='scale(1)';">
          <img src="${pawnSrc}" alt="Personaggio ${idx + 1}" class="pawn-choice-img">
          <span class="pawn-choice-label">Personaggio ${idx + 1}</span>
        </div>
      `;
    }).join('');
  },

  selectPawnCandidate(pawnSrc) {
    const currentTeam = this.selectedSetup.teams[this.selectedSetup.currentPawnTeamIdx];
    if (!currentTeam) return;
    currentTeam.avatar = pawnSrc;

    if (window.AudioEngine && window.AudioEngine.playChime) {
      window.AudioEngine.playChime();
    } else if (window.AudioEngine && window.AudioEngine.playTick) {
      window.AudioEngine.playTick();
    }

    if (this.selectedSetup.currentPawnTeamIdx < this.selectedSetup.teamsCount - 1) {
      this.selectedSetup.currentPawnTeamIdx++;
      this.renderPawnPicker();
    } else {
      const confirmWrap = document.getElementById('pawn-confirm-wrap');
      if (confirmWrap) confirmWrap.remove();
      this.showView('view-setup-mode');
    }
  },

  defaultLevels: [
    {
      id: "a1",
      nome: "Il Narratore in Erba",
      sigla: "A1",
      badge: "🐣 A1 • Primaria 1ª-3ª / Kids",
      descrizione: "Frasi minime, lessico concreto e visivo, narrazione fiabesca e immediata."
    },
    {
      id: "a2",
      nome: "L'Apprendista Cantastorie",
      sigla: "A2",
      badge: "🌿 A2 • Primaria 4ª-5ª / Junior",
      descrizione: "Racconto lineare di eventi, favole e avventure con lessico di base."
    },
    {
      id: "b1",
      nome: "L'Oratore della Piazza",
      sigla: "B1",
      badge: "🎙️ B1 • Scuola Media / Standard",
      descrizione: "Miti, leggende, narrazione strutturata e sfide di gruppo."
    },
    {
      id: "b2",
      nome: "Il Maestro di Retorica",
      sigla: "B2",
      badge: "📜 B2 • Biennio Superiori / Esperto",
      descrizione: "Argomentazione, coesione testuale, prime sfide retoriche e lessico specifico."
    },
    {
      id: "c1",
      nome: "Il Filosofo dell'Areopago",
      sigla: "C1",
      badge: "🏛️ C1 • Triennio Superiori / Master",
      descrizione: "Dilemmi etici, complessità concettuale, registri linguistici formali e aulici."
    },
    {
      id: "c2",
      nome: "Il Sommo Accademico",
      sigla: "C2",
      badge: "👑 C2 • Debate & Maturità / Campioni",
      descrizione: "Retorica classica d'élite, confutazione dialettica e padronanza assoluta della lingua."
    }
  ],

  // Step 3: Scelta Modalità (Proibite vs Usare)
  selectMode(mode) {
    this.selectedSetup.mode = mode;
    this.renderLevelGrid();
    this.showView('view-setup-level');
  },

  // Step 4: Scelta Livello di Difficoltà (6 Livelli QCER)
  renderLevelGrid() {
    const grid = document.getElementById('levels-six-grid');
    if (!grid) return;

    const livelli = (GameEngine.data && GameEngine.data.livelli && GameEngine.data.livelli.length > 0)
      ? GameEngine.data.livelli
      : this.defaultLevels;
    
    grid.innerHTML = livelli.map(l => `
      <div class="level-six-card ${this.selectedSetup.level === l.id ? 'selected' : ''}" id="level-card-${l.id}" onclick="App.selectLevel('${l.id}')">
        <div class="level-card-top">
          <h3 class="level-card-title">${l.nome}</h3>
          <span class="level-qcer-badge">${l.sigla}</span>
        </div>
        <div class="level-card-badge">${l.badge}</div>
        <p class="level-card-desc">${l.descrizione}</p>
      </div>
    `).join('');
  },

  selectLevel(levelId) {
    this.selectedSetup.level = levelId;
    
    if (window.AudioEngine && window.AudioEngine.playChime) {
      window.AudioEngine.playChime();
    } else if (window.AudioEngine && window.AudioEngine.playTick) {
      window.AudioEngine.playTick();
    }

    // Passa immediatamente alla scelta della categoria del round
    GameEngine.initGame(
      this.selectedSetup.teams,
      this.selectedSetup.mode,
      this.selectedSetup.level
    );
  },

  confirmLevelAndStart() {
    this.selectLevel(this.selectedSetup.level || 'b1');
  },

  confirmLogout() {
    if (confirm("Vuoi davvero uscire dalla sessione di gioco?")) {
      window.location.href = "https://prof-memmo.github.io/games/";
    }
  }
};

window.App = App;
window.addEventListener('DOMContentLoaded', () => App.init());
