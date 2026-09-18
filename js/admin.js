/**
 * L'ORATORE - Standalone Admin Matrix & Bulk Text Parser (1.440 Slots)
 * 12 Mazzi Tematici × 6 Livelli QCER × 20 Slot per combinazione = 1.440 Carte Didattiche
 */

const OratoreAdmin = {
  levels: [
    { id: 'a1', sigla: 'A1', nome: 'Il Narratore in Erba', badge: '🐣 A1 • Primaria 1ª-3ª' },
    { id: 'a2', sigla: 'A2', nome: "L'Apprendista Cantastorie", badge: '🌿 A2 • Primaria 4ª-5ª' },
    { id: 'b1', sigla: 'B1', nome: "L'Oratore della Piazza", badge: '🎙️ B1 • Scuola Media' },
    { id: 'b2', sigla: 'B2', nome: 'Il Maestro di Retorica', badge: '📜 B2 • Biennio Sup.' },
    { id: 'c1', sigla: 'C1', nome: "Il Filosofo dell'Areopago", badge: '🏛️ C1 • Triennio Sup.' },
    { id: 'c2', sigla: 'C2', nome: 'Il Sommo Accademico', badge: '👑 C2 • Debate & Maturità' }
  ],

  decks: [
    { id: 'accoglienza', emoji: '🎒', nome: 'Accoglienza & Primi Giorni' },
    { id: 'emozioni', emoji: '🎭', nome: 'Emozioni, Relazioni & Empatia' },
    { id: 'diritti', emoji: '🏛️', nome: 'Diritti, Legalità & Costituzione' },
    { id: 'digitale', emoji: '🤖', nome: 'Digitale, IA & Futuro' },
    { id: 'clima', emoji: '🌍', nome: 'Clima, Natura & Terra' },
    { id: 'dilemmi', emoji: '⚖️', nome: 'Dilemmi Etici & Scelte Morali' },
    { id: 'mistero', emoji: '🕵️', nome: 'Mistero, Indagini & Giallo' },
    { id: 'epica', emoji: '🏺', nome: 'Mito & Epica Classica' },
    { id: 'favole', emoji: '🐉', nome: 'Favole, Fiabe & Simboli' },
    { id: 'storia', emoji: '⏳', nome: 'Grandi Figure & Storia' },
    { id: 'avventura', emoji: '🧭', nome: 'Viaggi, Esplorazioni & Avventura' },
    { id: 'filosofia', emoji: '💡', nome: 'Filosofia, Idee & Debate' }
  ],

  maxSlotsPerCombination: 20,
  activeLevelFilter: 'all',
  activeDeckFilter: 'all',

  cardsMap: {}, // Key: `${level}_${deck}_${slot}` -> Card Object

  async init() {
    // 0. Sincronizza metadata se presenti globalmente
    if (window.L_ORATORE_DEFAULT_CARDS) {
      if (window.L_ORATORE_DEFAULT_CARDS.livelli && window.L_ORATORE_DEFAULT_CARDS.livelli.length > 0) {
        this.levels = window.L_ORATORE_DEFAULT_CARDS.livelli;
      }
      if (window.L_ORATORE_DEFAULT_CARDS.mazzi && window.L_ORATORE_DEFAULT_CARDS.mazzi.length > 0) {
        this.decks = window.L_ORATORE_DEFAULT_CARDS.mazzi;
      }
    }

    await this.loadAllCards();
    this.renderMatrix();
  },

  async loadAllCards() {
    this.cardsMap = {};

    // 1. Carica da data/consegne.json locale con cache-buster orario
    try {
      const res = await fetch('data/consegne.json?v=' + Date.now());
      if (res.ok) {
        const json = await res.json();
        if (json.livelli && json.livelli.length > 0) this.levels = json.livelli;
        if (json.mazzi && json.mazzi.length > 0) this.decks = json.mazzi;
        (json.carte || []).forEach(c => {
          const key = `${c.livello || 'b1'}_${c.mazzo}_${c.slot || 1}`;
          this.cardsMap[key] = c;
        });
      }
    } catch (e) {
      console.warn("Base JSON fetch error, falling back to window object:", e);
    }

    // 2. Se non sono state caricate da fetch, leggi da cards-data.js globale
    if (Object.keys(this.cardsMap).length === 0 && window.L_ORATORE_DEFAULT_CARDS && window.L_ORATORE_DEFAULT_CARDS.carte) {
      if (window.L_ORATORE_DEFAULT_CARDS.livelli) this.levels = window.L_ORATORE_DEFAULT_CARDS.livelli;
      if (window.L_ORATORE_DEFAULT_CARDS.mazzi) this.decks = window.L_ORATORE_DEFAULT_CARDS.mazzi;
      window.L_ORATORE_DEFAULT_CARDS.carte.forEach(c => {
        const key = `${c.livello || 'b1'}_${c.mazzo}_${c.slot || 1}`;
        this.cardsMap[key] = c;
      });
    }

    // 3. Carica eventuali override personalizzati salvati localmente
    const localStored = localStorage.getItem('loratore_custom_cards');
    if (localStored) {
      try {
        const custom = JSON.parse(localStored);
        Object.keys(custom).forEach(k => {
          if (custom[k] && custom[k].titolo) {
            this.cardsMap[k] = custom[k];
          }
        });
      } catch (err) {}
    }
  },

  renderMatrix() {
    const container = document.getElementById('oratore-matrix-container');
    if (!container) return;

    let filledCount = 0;
    const totalSlots = this.levels.length * this.decks.length * this.maxSlotsPerCombination; // 6 * 12 * 20 = 1440

    // Calcolo totale slot compilati
    Object.keys(this.cardsMap).forEach(() => {
      filledCount++;
    });

    let html = `
      <div style="background:#070a13; border: 1.5px solid #d4af37; border-radius: 14px; padding: 20px; color:#fff; margin-bottom: 25px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 15px;">
          <div>
            <h3 style="font-size: 1.3rem; color: #d4af37; margin:0;"><i class="fa-solid fa-table-cells"></i> Matrice de L'Oratore (1.440 Slot Totali)</h3>
            <p style="font-size: 0.85rem; color: #94a3b8; margin: 4px 0 0 0;">12 Mazzi Tematici × 6 Livelli QCER × 20 Slot per combinazione</p>
          </div>
          <div id="matrix-stats-pill" style="background: rgba(212, 175, 55, 0.15); border: 1px solid #d4af37; padding: 6px 16px; border-radius: 20px; font-weight: 700; color: #f1c40f;">
            📊 Slot Compilati: <strong>${filledCount} / ${totalSlots}</strong> (${Math.round(filledCount / totalSlots * 100)}%)
          </div>
        </div>

        <!-- Filtri Rapidi (Livello & Mazzo) -->
        <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 15px;">
          <div style="display: flex; gap: 8px; overflow-x: auto; padding-bottom: 6px; align-items: center;">
            <span style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; white-space: nowrap;">Filtra Livello:</span>
            <button class="btn btn-sm" onclick="OratoreAdmin.filterLevel('all')" style="background: ${this.activeLevelFilter === 'all' ? '#d4af37' : '#1e293b'}; color: ${this.activeLevelFilter === 'all' ? '#000' : '#fff'}; border: 1px solid #475569; padding: 4px 10px; border-radius: 20px; cursor:pointer; font-weight: 700;">Tutti i Livelli</button>
            ${this.levels.map(l => `
              <button class="btn btn-sm" onclick="OratoreAdmin.filterLevel('${l.id}')" style="background: ${this.activeLevelFilter === l.id ? '#d4af37' : '#0d1220'}; color: ${this.activeLevelFilter === l.id ? '#000' : '#d4af37'}; border: 1px solid #d4af37; padding: 4px 10px; border-radius: 20px; cursor:pointer; font-weight: 700;">
                ${l.badge || l.nome}
              </button>
            `).join('')}
          </div>

          <div style="display: flex; gap: 6px; overflow-x: auto; padding-bottom: 6px; align-items: center;">
            <span style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; white-space: nowrap;">Filtra Mazzo:</span>
            <button class="btn btn-sm" onclick="OratoreAdmin.filterDeck('all')" style="background: ${this.activeDeckFilter === 'all' ? '#38bdf8' : '#1e293b'}; color: ${this.activeDeckFilter === 'all' ? '#000' : '#fff'}; border: 1px solid #475569; padding: 4px 8px; border-radius: 20px; cursor:pointer; font-size: 0.78rem;">Tutti i Mazzi (12)</button>
            ${this.decks.map(d => `
              <button class="btn btn-sm" onclick="OratoreAdmin.filterDeck('${d.id}')" style="background: ${this.activeDeckFilter === d.id ? '#38bdf8' : '#0d1220'}; color: ${this.activeDeckFilter === d.id ? '#000' : '#cbd5e1'}; border: 1px solid #334155; padding: 4px 8px; border-radius: 20px; cursor:pointer; font-size: 0.78rem;">
                ${d.emoji} ${d.nome.split('&')[0].trim()}
              </button>
            `).join('')}
          </div>
        </div>

        <!-- Tabella Matrice a 20 Slot -->
        <div style="overflow-x: auto; max-height: 600px; border: 1px solid rgba(212,175,55,0.2); border-radius: 8px;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.82rem; text-align: left;">
            <thead>
              <tr style="background: #0d1220; border-bottom: 2px solid #d4af37; color: #d4af37; position: sticky; top: 0; z-index: 2;">
                <th style="padding: 10px; width: 140px; background: #0d1220;">Livello (QCER)</th>
                <th style="padding: 10px; width: 200px; background: #0d1220;">Mazzo Tematico</th>
                <th style="padding: 10px; text-align: center; background: #0d1220;">Slot Disponibili (20 Carte per combinazione)</th>
              </tr>
            </thead>
            <tbody>
    `;

    this.levels.forEach(l => {
      this.decks.forEach(d => {
        const isLevelMatch = (this.activeLevelFilter === 'all' || this.activeLevelFilter === l.id);
        const isDeckMatch = (this.activeDeckFilter === 'all' || this.activeDeckFilter === d.id);
        const displayStyle = (isLevelMatch && isDeckMatch) ? '' : 'none';

        html += `<tr class="matrix-row matrix-row-${l.id} matrix-row-deck-${d.id}" style="border-bottom: 1px solid rgba(255,255,255,0.08); display: ${displayStyle};">
          <td style="padding: 10px; font-weight: 700; color: #f1c40f; vertical-align: middle;">${l.sigla || l.id.toUpperCase()} • ${l.nome}</td>
          <td style="padding: 10px; color: #cbd5e1; vertical-align: middle;"><strong>${d.emoji} ${d.nome}</strong></td>
          <td style="padding: 10px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 6px;">
        `;

        for (let s = 1; s <= this.maxSlotsPerCombination; s++) {
          const key = `${l.id}_${d.id}_${s}`;
          const card = this.cardsMap[key];
          if (card) {
            html += `
              <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; border-radius: 6px; padding: 4px 6px; cursor: pointer; text-align: left; transition: transform 0.15s;" onclick="OratoreAdmin.openEditSlotModal('${l.id}', '${d.id}', ${s})" title="${card.titolo}\n\n${card.incipit}">
                <div style="color: #34d399; font-weight: 700; font-size: 0.72rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">🟢 #${s} ${card.titolo}</div>
                <div style="color: #94a3b8; font-size: 0.65rem;">Modifica carta</div>
              </div>
            `;
          } else {
            html += `
              <div style="background: rgba(255, 255, 255, 0.03); border: 1px dashed rgba(255, 255, 255, 0.2); border-radius: 6px; padding: 4px 6px; cursor: pointer; text-align: center;" onclick="OratoreAdmin.openEditSlotModal('${l.id}', '${d.id}', ${s})">
                <span style="color: #64748b; font-size: 0.68rem;">⚪ Slot #${s} (Vuoto)</span>
              </div>
            `;
          }
        }

        html += `
            </div>
          </td>
        </tr>`;
      });
    });

    html += `
            </tbody>
          </table>
        </div>
      </div>
    `;

    container.innerHTML = html;
  },

  filterLevel(lvl) {
    this.activeLevelFilter = lvl;
    this.renderMatrix();
  },

  filterDeck(deckId) {
    this.activeDeckFilter = deckId;
    this.renderMatrix();
  },

  parseWordText(rawText, defaultLevel, defaultDeck) {
    if (!rawText || !rawText.trim()) return [];

    const lines = rawText.split(/\r?\n/);
    const parsedCards = [];
    let currentCard = null;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) return;

      const matchNew = trimmed.match(/^(\d+)[\.\)\:\-]\s*(.*)$/i) || trimmed.match(/^(Traccia|Carta|Incipit)\s*(\d+)[\.\:\-]?\s*(.*)$/i);
      
      if (matchNew) {
        if (currentCard && currentCard.titolo) {
          parsedCards.push(currentCard);
        }
        const titlePart = matchNew[2] || matchNew[3] || 'Nuova Traccia';
        currentCard = {
          titolo: titlePart.trim(),
          incipit: '',
          parole_proibite: [],
          parole_da_usare: [],
          livello: defaultLevel || 'b1',
          mazzo: defaultDeck || 'accoglienza'
        };
        return;
      }

      if (!currentCard) {
        currentCard = {
          titolo: 'Traccia 1',
          incipit: '',
          parole_proibite: [],
          parole_da_usare: [],
          livello: defaultLevel || 'b1',
          mazzo: defaultDeck || 'accoglienza'
        };
      }

      const lower = trimmed.toLowerCase();
      if (lower.startsWith('incipit:') || lower.startsWith('testo:')) {
        currentCard.incipit = trimmed.replace(/^(incipit|testo)\s*:\s*/i, '').trim();
      } else if (lower.startsWith('parole proibite:') || lower.startsWith('vietate:') || lower.startsWith('proibite:')) {
        const wordsStr = trimmed.replace(/^(parole proibite|vietate|proibite)\s*:\s*/i, '');
        currentCard.parole_proibite = wordsStr.split(/[,;\-\/]/).map(w => w.trim()).filter(Boolean);
      } else if (lower.startsWith('parole da usare:') || lower.startsWith('usare:') || lower.startsWith('vocaboli:')) {
        const wordsStr = trimmed.replace(/^(parole da usare|usare|vocaboli)\s*:\s*/i, '');
        currentCard.parole_da_usare = wordsStr.split(/[,;\-\/]/).map(w => w.trim()).filter(Boolean);
      } else if (lower.startsWith('livello:') || lower.startsWith('qcer:')) {
        const lvlStr = trimmed.replace(/^(livello|qcer)\s*:\s*/i, '').trim().toLowerCase();
        if (['a1', 'a2', 'b1', 'b2', 'c1', 'c2'].includes(lvlStr)) {
          currentCard.livello = lvlStr;
        }
      } else if (lower.startsWith('mazzo:') || lower.startsWith('categoria:')) {
        const mazzoStr = trimmed.replace(/^(mazzo|categoria)\s*:\s*/i, '').trim().toLowerCase();
        const foundMazzo = OratoreAdmin.decks.find(d => d.id.includes(mazzoStr) || d.nome.toLowerCase().includes(mazzoStr));
        if (foundMazzo) currentCard.mazzo = foundMazzo.id;
      } else if (!currentCard.incipit) {
        currentCard.incipit = (currentCard.incipit ? currentCard.incipit + ' ' : '') + trimmed;
      }
    });

    if (currentCard && (currentCard.titolo || currentCard.incipit)) {
      parsedCards.push(currentCard);
    }

    return parsedCards;
  },

  async executeBulkImport() {
    const rawText = document.getElementById('oratore-bulk-textarea').value;
    const defaultLevel = document.getElementById('oratore-bulk-level-select').value;
    const defaultDeck = document.getElementById('oratore-bulk-deck-select').value;

    const cards = this.parseWordText(rawText, defaultLevel, defaultDeck);

    if (cards.length === 0) {
      alert("⚠️ Nessun incipit valido riconosciuto nel testo. Assicurati di usare un elenco numerato (es. '1. Titolo', 'Incipit: ...', 'Parole Proibite: ...').");
      return;
    }

    const previewDiv = document.getElementById('oratore-bulk-preview');
    if (previewDiv) {
      previewDiv.innerHTML = `
        <div style="background: rgba(16, 185, 129, 0.1); border: 1.5px solid #10b981; border-radius: 12px; padding: 15px; margin-top: 15px; color: #fff;">
          <h4 style="color: #34d399; margin: 0 0 8px 0;"><i class="fa-solid fa-circle-check"></i> Riconosciuti ${cards.length} Incipit nel testo:</h4>
          <ul style="padding-left: 20px; font-size: 0.85rem; line-height: 1.5; margin-bottom: 15px; max-height: 200px; overflow-y: auto;">
            ${cards.map((c, i) => `<li><strong>${i + 1}. ${c.titolo}</strong> [${c.livello.toUpperCase()} • ${c.mazzo}] — ${c.incipit.substring(0, 60)}...</li>`).join('')}
          </ul>
          <button class="btn btn-primary" onclick="OratoreAdmin.saveCardsLocallyAndSync(${JSON.stringify(cards).replace(/"/g, '&quot;')})" style="background: #10b981; border: none; padding: 10px 20px; font-weight: 700; cursor: pointer; border-radius: 8px; color: #fff;">
            💾 Conferma e Smista ${cards.length} Carte negli Slot
          </button>
        </div>
      `;
    }
  },

  saveCardsLocallyAndSync(cards) {
    const custom = JSON.parse(localStorage.getItem('loratore_custom_cards') || '{}');

    cards.forEach(c => {
      let targetSlot = 1;
      for (let s = 1; s <= this.maxSlotsPerCombination; s++) {
        const key = `${c.livello}_${c.mazzo}_${s}`;
        if (!this.cardsMap[key]) {
          targetSlot = s;
          break;
        }
      }

      const key = `${c.livello}_${c.mazzo}_${targetSlot}`;
      const cardData = {
        id: `card_${c.livello}_${c.mazzo}_slot${targetSlot}`,
        titolo: c.titolo,
        incipit: c.incipit,
        parole_proibite: c.parole_proibite.length > 0 ? c.parole_proibite : ["Parola 1", "Parola 2", "Parola 3", "Parola 4", "Parola 5"],
        parole_da_usare: c.parole_da_usare.length > 0 ? c.parole_da_usare : ["Termine 1", "Termine 2", "Termine 3", "Termine 4", "Termine 5"],
        livello: c.livello,
        mazzo: c.mazzo,
        slot: targetSlot
      };

      custom[key] = cardData;
      this.cardsMap[key] = cardData;
    });

    localStorage.setItem('loratore_custom_cards', JSON.stringify(custom));
    alert(`✅ Smistate con successo ${cards.length} carte negli slot della matrice de L'Oratore!`);
    this.renderMatrix();
  },

  openEditSlotModal(levelId, deckId, slotNum) {
    const key = `${levelId}_${deckId}_${slotNum}`;
    const card = this.cardsMap[key] || {
      titolo: '',
      incipit: '',
      parole_proibite: [],
      parole_da_usare: []
    };

    const levelObj = this.levels.find(l => l.id === levelId) || { sigla: levelId, nome: levelId };
    const deckObj = this.decks.find(d => d.id === deckId) || { emoji: '🎲', nome: deckId };

    const modalTitle = document.getElementById('slot-modal-title');
    const modalBody = document.getElementById('slot-modal-body');
    const modal = document.getElementById('slot-edit-modal');

    if (!modalTitle || !modalBody || !modal) return;

    modalTitle.innerHTML = `<i class="fa-solid fa-pen-to-square"></i> Slot #${slotNum} • ${deckObj.emoji} ${deckObj.nome} (${levelObj.sigla || levelId.toUpperCase()})`;
    modalBody.innerHTML = `
      <div style="margin-bottom: 12px;">
        <label style="display:block; font-size: 0.8rem; font-weight:700; color: #94a3b8; margin-bottom:4px;">Titolo Traccia:</label>
        <input type="text" id="slot-edit-title" value="${card.titolo || ''}" style="width:100%; padding:8px 12px; background:#0d1220; border:1px solid #d4af37; border-radius:8px; color:#fff;">
      </div>
      <div style="margin-bottom: 12px;">
        <label style="display:block; font-size: 0.8rem; font-weight:700; color: #94a3b8; margin-bottom:4px;">Incipit Narrativo:</label>
        <textarea id="slot-edit-incipit" rows="4" style="width:100%; padding:8px 12px; background:#0d1220; border:1px solid #d4af37; border-radius:8px; color:#fff; font-size:0.85rem; line-height:1.4;">${card.incipit || ''}</textarea>
      </div>
      <div style="margin-bottom: 12px;">
        <label style="display:block; font-size: 0.8rem; font-weight:700; color: #f87171; margin-bottom:4px;">5 Parole Proibite (separate da virgola):</label>
        <input type="text" id="slot-edit-proibite" value="${(card.parole_proibite || []).join(', ')}" style="width:100%; padding:8px 12px; background:#0d1220; border:1px solid #f87171; border-radius:8px; color:#fff;">
      </div>
      <div style="margin-bottom: 15px;">
        <label style="display:block; font-size: 0.8rem; font-weight:700; color: #34d399; margin-bottom:4px;">5 Parole da Usare (separate da virgola):</label>
        <input type="text" id="slot-edit-usare" value="${(card.parole_da_usare || []).join(', ')}" style="width:100%; padding:8px 12px; background:#0d1220; border:1px solid #34d399; border-radius:8px; color:#fff;">
      </div>
      <div style="display:flex; justify-content:space-between; gap:10px;">
        <button class="btn btn-secondary" onclick="document.getElementById('slot-edit-modal').classList.add('hidden')" style="padding:8px 16px; border-radius:8px; cursor:pointer;">Annulla</button>
        <button class="btn btn-primary" onclick="OratoreAdmin.saveSingleSlot('${levelId}', '${deckId}', ${slotNum})" style="background:#d4af37; color:#000; font-weight:700; padding:8px 18px; border:none; border-radius:8px; cursor:pointer;">💾 Salva Slot</button>
      </div>
    `;

    modal.classList.remove('hidden');
  },

  saveSingleSlot(levelId, deckId, slotNum) {
    const title = document.getElementById('slot-edit-title').value.trim();
    const incipit = document.getElementById('slot-edit-incipit').value.trim();
    const proibite = document.getElementById('slot-edit-proibite').value.split(',').map(w => w.trim()).filter(Boolean);
    const usare = document.getElementById('slot-edit-usare').value.split(',').map(w => w.trim()).filter(Boolean);

    const key = `${levelId}_${deckId}_${slotNum}`;
    const cardData = {
      id: `card_${levelId}_${deckId}_slot${slotNum}`,
      titolo: title,
      incipit: incipit,
      parole_proibite: proibite,
      parole_da_usare: usare,
      livello: levelId,
      mazzo: deckId,
      slot: slotNum
    };

    const custom = JSON.parse(localStorage.getItem('loratore_custom_cards') || '{}');
    custom[key] = cardData;
    localStorage.setItem('loratore_custom_cards', JSON.stringify(custom));

    this.cardsMap[key] = cardData;
    document.getElementById('slot-edit-modal').classList.add('hidden');
    alert(`✅ Slot #${slotNum} salvato con successo!`);
    this.renderMatrix();
  }
};

window.OratoreAdmin = OratoreAdmin;
window.addEventListener('DOMContentLoaded', () => OratoreAdmin.init());
