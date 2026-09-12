/**
 * LIVE EDITOR DIDATTICO (LiveEditor) - L'Oratore
 * Consente al Docente / Amministratore (prof.memmo@gmail.com o in modalità locale) di:
 * 1. ✏️ Modificare al volo la carta attiva (Titolo, Incipit, 5 Parole Proibite, 5 Parole da Usare, Livello QCER, Mazzo)
 * 2. ➕ Aggiungere un Nuovo Incipit / Nuova Carta personalizzata
 * 3. Salvataggio e sincronizzazione in tempo reale su Firestore con fallback in localStorage.
 */

(function() {
  'use strict';

  window.LiveEditor = {
    platformKey: 'oratore',
    platformName: "L'Oratore",
    overrides: {},
    isLoaded: false,
    _originalCache: {},

    init: async function() {
      // Carica da Firestore se connesso
      const db = window.fbDb || (typeof firebase !== 'undefined' && firebase.firestore ? firebase.firestore() : null);
      if (db) {
        try {
          const snapshot = await db.collection('hub_didactic_overrides')
            .where('platform', '==', this.platformKey)
            .get();

          this.overrides = {};
          snapshot.forEach(doc => {
            this.overrides[doc.id] = { docId: doc.id, ...doc.data() };
          });
          this.isLoaded = true;
          console.log(`✏️ LiveEditor [L'Oratore]: ${Object.keys(this.overrides).length} override caricati da Firestore.`);
        } catch (e) {
          console.warn("LiveEditor Firestore sync offline/fallback:", e);
        }
      }

      // Carica anche da localStorage
      try {
        const localData = localStorage.getItem('loratore_didactic_overrides');
        if (localData) {
          const parsed = JSON.parse(localData);
          this.overrides = { ...this.overrides, ...parsed };
        }
      } catch (err) {}

      this.injectLiveButtons();
    },

    isAdmin: function() {
      // Admin page sempre abilitata se autenticato come admin
      if (typeof window !== 'undefined' && window.location && window.location.pathname.includes('admin')) {
        // Verifica se presente sessione admin
      }
      // Controllo Firebase Auth
      if (typeof firebase !== 'undefined' && firebase.auth && firebase.auth().currentUser) {
        const fbUser = firebase.auth().currentUser;
        if (fbUser.email && fbUser.email.toLowerCase() === 'prof.memmo@gmail.com') return true;
      }
      // Controllo sessioni memorizzate
      try {
        for (let k of ['hub_user_session', 'oratore_user', 'pm_oratore_user', 'hub_user', 'fanta_user', 'corte_user_session']) {
          const raw = localStorage.getItem(k);
          if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed.email && parsed.email.toLowerCase() === 'prof.memmo@gmail.com') return true;
            if (parsed.role === 'admin') return true;
          }
        }
      } catch (e) {}

      // Default: solo per amministratore
      return false;
    },

    injectLiveButtons: function() {
      // Il Live Editor è riservato esclusivamente all'Amministratore (Prof. Memmo)
      if (!this.isAdmin()) {
        const existingBtn = document.getElementById('btn-live-edit-card');
        if (existingBtn) existingBtn.remove();
        return;
      }

      // Aggiunge il pulsante ✏️ Modifica Carta nella barra delle azioni o sulla carta attiva
      const cardMeta = document.querySelector('.card-meta-row');
      if (cardMeta && !document.getElementById('btn-live-edit-card')) {
        const editBtn = document.createElement('button');
        editBtn.id = 'btn-live-edit-card';
        editBtn.type = 'button';
        editBtn.className = 'btn-live-edit-active';
        editBtn.innerHTML = '<i class="fa-solid fa-pen-to-square"></i> <span>✏️ Modifica Carta</span>';
        editBtn.title = 'Modifica al volo il testo, le parole vietate e i dettagli di questa carta (Admin)';
        editBtn.onclick = () => {
          if (window.GameEngine && window.GameEngine.gameState && window.GameEngine.gameState.currentCard) {
            LiveEditor.openCardEditorModal(window.GameEngine.gameState.currentCard);
          }
        };
        cardMeta.appendChild(editBtn);
      }
    },

    openCardEditorModal: function(card) {
      if (!this.isAdmin() || !card) return;
      let modal = document.getElementById('live-editor-modal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'live-editor-modal';
        modal.className = 'legal-modal';
        document.body.appendChild(modal);
      }

      const cardId = card.id || `card_${card.mazzo}_${card.livello}_${card.slot || '1'}`;
      const proibiteStr = Array.isArray(card.paroleProibite) ? card.paroleProibite.join(', ') : (card.paroleProibite || '');
      const usareStr = Array.isArray(card.paroleDaUsare) ? card.paroleDaUsare.join(', ') : (card.paroleDaUsare || '');

      modal.innerHTML = `
        <div class="legal-modal-content" style="max-width: 640px; background: #070a13; border: 2px solid #d4af37; border-radius: 16px; padding: 25px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); text-align: left;">
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(212,175,55,0.3); padding-bottom:12px; margin-bottom:18px;">
            <h3 style="color:#d4af37; margin:0; font-size:1.25rem; display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-pen-to-square"></i> ✏️ Modifica Carta in Tempo Reale
            </h3>
            <span class="close-legal" style="font-size:1.8rem; cursor:pointer; color:#94a3b8;" onclick="LiveEditor.closeModal()">&times;</span>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom:12px;">
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Mazzo / Categoria:</label>
              <select id="edit-card-mazzo" style="width:100%; padding:8px 10px; background:#000; border:1px solid #d4af37; border-radius:6px; color:#fff; font-size:0.85rem;">
                <option value="epica" ${card.mazzo === 'epica' ? 'selected' : ''}>🏺 Mito & Epica</option>
                <option value="medioevo" ${card.mazzo === 'medioevo' ? 'selected' : ''}>👑 Medioevo & Cavalieri</option>
                <option value="fantascienza" ${card.mazzo === 'fantascienza' ? 'selected' : ''}>🚀 Fantascienza & Futuro</option>
                <option value="teatro" ${card.mazzo === 'teatro' ? 'selected' : ''}>🎭 Teatro & Spettacolo</option>
                <option value="letteratura" ${card.mazzo === 'letteratura' ? 'selected' : ''}>📜 Letteratura & Poesia</option>
                <option value="civilta" ${card.mazzo === 'civilta' ? 'selected' : ''}>🌍 Mondo, Storia & Civiltà</option>
                <option value="scienza" ${card.mazzo === 'scienza' ? 'selected' : ''}>🧪 Scienza & Natura</option>
                <option value="party" ${card.mazzo === 'party' ? 'selected' : ''}>🧩 Party & Creatività</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Livello QCER:</label>
              <select id="edit-card-livello" style="width:100%; padding:8px 10px; background:#000; border:1px solid #d4af37; border-radius:6px; color:#fff; font-size:0.85rem;">
                <option value="a1" ${card.livello === 'a1' ? 'selected' : ''}>🐣 A1 • Narratore in Erba</option>
                <option value="a2" ${card.livello === 'a2' ? 'selected' : ''}>🌿 A2 • Apprendista Cantastorie</option>
                <option value="b1" ${card.livello === 'b1' ? 'selected' : ''}>🎙️ B1 • Oratore della Piazza</option>
                <option value="b2" ${card.livello === 'b2' ? 'selected' : ''}>📜 B2 • Maestro di Retorica</option>
                <option value="c1" ${card.livello === 'c1' ? 'selected' : ''}>🏛️ C1 • Filosofo Areopago</option>
                <option value="c2" ${card.livello === 'c2' ? 'selected' : ''}>👑 C2 • Sommo Accademico</option>
              </select>
            </div>
          </div>

          <div style="margin-bottom:12px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Titolo della Traccia:</label>
            <input type="text" id="edit-card-titolo" value="${(card.titolo || '').replace(/"/g, '&quot;')}" style="width:100%; padding:10px; background:#000; border:1px solid rgba(212,175,55,0.5); border-radius:6px; color:#fff; font-size:0.9rem; font-weight:700;">
          </div>

          <div style="margin-bottom:12px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Incipit Narrativo d'Autore (Contesto & Traccia):</label>
            <textarea id="edit-card-incipit" rows="3" style="width:100%; padding:10px; background:#000; border:1px solid rgba(212,175,55,0.5); border-radius:6px; color:#fff; font-size:0.85rem; line-height:1.4;">${card.incipit || ''}</textarea>
          </div>

          <div style="margin-bottom:12px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#ef4444; margin-bottom:4px;">🚫 5 Parole Proibite (separate da virgola):</label>
            <input type="text" id="edit-card-proibite" value="${proibiteStr.replace(/"/g, '&quot;')}" style="width:100%; padding:8px 10px; background:#000; border:1px solid #ef4444; border-radius:6px; color:#fff; font-size:0.85rem;">
          </div>

          <div style="margin-bottom:18px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#10b981; margin-bottom:4px;">🎯 5 Parole da Usare (separate da virgola):</label>
            <input type="text" id="edit-card-usare" value="${usareStr.replace(/"/g, '&quot;')}" style="width:100%; padding:8px 10px; background:#000; border:1px solid #10b981; border-radius:6px; color:#fff; font-size:0.85rem;">
          </div>

          <div style="display:flex; justify-content:flex-end; gap:10px; border-top:1px solid rgba(255,255,255,0.1); padding-top:14px;">
            <button class="btn btn-secondary" onclick="LiveEditor.closeModal()" style="padding:8px 16px; font-size:0.85rem;">Annulla</button>
            <button class="btn btn-primary" onclick="LiveEditor.saveCardEdit('${cardId}')" style="background:#d4af37; color:#000; font-weight:800; padding:8px 20px; font-size:0.85rem; border:none; border-radius:20px; cursor:pointer;">
              <i class="fa-solid fa-cloud-arrow-up"></i> Salva & Sincronizza su Firestore
            </button>
          </div>
        </div>
      `;

      modal.classList.remove('hidden');
      modal.style.display = 'flex';
    },

    openAddIncipitModal: function(defaultDeck = 'epica', defaultLevel = 'b1') {
      if (!this.isAdmin()) return;
      let modal = document.getElementById('live-editor-modal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'live-editor-modal';
        modal.className = 'legal-modal';
        document.body.appendChild(modal);
      }

      modal.innerHTML = `
        <div class="legal-modal-content" style="max-width: 640px; background: #070a13; border: 2px solid #d4af37; border-radius: 16px; padding: 25px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); text-align: left;">
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(212,175,55,0.3); padding-bottom:12px; margin-bottom:18px;">
            <h3 style="color:#d4af37; margin:0; font-size:1.25rem; display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-plus-circle"></i> ➕ Aggiungi Nuovo Incipit Didattico
            </h3>
            <span class="close-legal" style="font-size:1.8rem; cursor:pointer; color:#94a3b8;" onclick="LiveEditor.closeModal()">&times;</span>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom:12px;">
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Mazzo / Categoria:</label>
              <select id="new-card-mazzo" style="width:100%; padding:8px 10px; background:#000; border:1px solid #d4af37; border-radius:6px; color:#fff; font-size:0.85rem;">
                <option value="epica" ${defaultDeck === 'epica' ? 'selected' : ''}>🏺 Mito & Epica</option>
                <option value="medioevo" ${defaultDeck === 'medioevo' ? 'selected' : ''}>👑 Medioevo & Cavalieri</option>
                <option value="fantascienza" ${defaultDeck === 'fantascienza' ? 'selected' : ''}>🚀 Fantascienza & Futuro</option>
                <option value="teatro" ${defaultDeck === 'teatro' ? 'selected' : ''}>🎭 Teatro & Spettacolo</option>
                <option value="letteratura" ${defaultDeck === 'letteratura' ? 'selected' : ''}>📜 Letteratura & Poesia</option>
                <option value="civilta" ${defaultDeck === 'civilta' ? 'selected' : ''}>🌍 Mondo, Storia & Civiltà</option>
                <option value="scienza" ${defaultDeck === 'scienza' ? 'selected' : ''}>🧪 Scienza & Natura</option>
                <option value="party" ${defaultDeck === 'party' ? 'selected' : ''}>🧩 Party & Creatività</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Livello QCER:</label>
              <select id="new-card-livello" style="width:100%; padding:8px 10px; background:#000; border:1px solid #d4af37; border-radius:6px; color:#fff; font-size:0.85rem;">
                <option value="a1" ${defaultLevel === 'a1' ? 'selected' : ''}>🐣 A1 • Narratore in Erba</option>
                <option value="a2" ${defaultLevel === 'a2' ? 'selected' : ''}>🌿 A2 • Apprendista Cantastorie</option>
                <option value="b1" ${defaultLevel === 'b1' ? 'selected' : ''}>🎙️ B1 • Oratore della Piazza</option>
                <option value="b2" ${defaultLevel === 'b2' ? 'selected' : ''}>📜 B2 • Maestro di Retorica</option>
                <option value="c1" ${defaultLevel === 'c1' ? 'selected' : ''}>🏛️ C1 • Filosofo Areopago</option>
                <option value="c2" ${defaultLevel === 'c2' ? 'selected' : ''}>👑 C2 • Sommo Accademico</option>
              </select>
            </div>
          </div>

          <div style="margin-bottom:12px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Titolo della Traccia:</label>
            <input type="text" id="new-card-titolo" placeholder="Es. L'Esilio del Poeta..." style="width:100%; padding:10px; background:#000; border:1px solid rgba(212,175,55,0.5); border-radius:6px; color:#fff; font-size:0.9rem; font-weight:700;">
          </div>

          <div style="margin-bottom:12px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#94a3b8; margin-bottom:4px;">Incipit Narrativo d'Autore (Contesto & Traccia):</label>
            <textarea id="new-card-incipit" rows="3" placeholder="Scrivi l'incipit che introduce l'oratore alla situazione retorica..." style="width:100%; padding:10px; background:#000; border:1px solid rgba(212,175,55,0.5); border-radius:6px; color:#fff; font-size:0.85rem; line-height:1.4;"></textarea>
          </div>

          <div style="margin-bottom:12px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#ef4444; margin-bottom:4px;">🚫 5 Parole Proibite (separate da virgola):</label>
            <input type="text" id="new-card-proibite" placeholder="Parola 1, Parola 2, Parola 3, Parola 4, Parola 5" style="width:100%; padding:8px 10px; background:#000; border:1px solid #ef4444; border-radius:6px; color:#fff; font-size:0.85rem;">
          </div>

          <div style="margin-bottom:18px;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:#10b981; margin-bottom:4px;">🎯 5 Parole da Usare (separate da virgola):</label>
            <input type="text" id="new-card-usare" placeholder="Termine 1, Termine 2, Termine 3, Termine 4, Termine 5" style="width:100%; padding:8px 10px; background:#000; border:1px solid #10b981; border-radius:6px; color:#fff; font-size:0.85rem;">
          </div>

          <div style="display:flex; justify-content:flex-end; gap:10px; border-top:1px solid rgba(255,255,255,0.1); padding-top:14px;">
            <button class="btn btn-secondary" onclick="LiveEditor.closeModal()" style="padding:8px 16px; font-size:0.85rem;">Annulla</button>
            <button class="btn btn-primary" onclick="LiveEditor.saveNewCard()" style="background:#d4af37; color:#000; font-weight:800; padding:8px 20px; font-size:0.85rem; border:none; border-radius:20px; cursor:pointer;">
              <i class="fa-solid fa-cloud-arrow-up"></i> Salva & Aggiungi su Firestore
            </button>
          </div>
        </div>
      `;

      modal.classList.remove('hidden');
      modal.style.display = 'flex';
    },

    saveCardEdit: async function(cardId) {
      const mazzo = document.getElementById('edit-card-mazzo').value;
      const livello = document.getElementById('edit-card-livello').value;
      const titolo = document.getElementById('edit-card-titolo').value.trim();
      const incipit = document.getElementById('edit-card-incipit').value.trim();
      const proibiteRaw = document.getElementById('edit-card-proibite').value.trim();
      const usareRaw = document.getElementById('edit-card-usare').value.trim();

      if (!titolo || !incipit) {
        alert("Inserisci almeno il Titolo e l'Incipit della carta.");
        return;
      }

      const paroleProibite = proibiteRaw.split(',').map(s => s.trim()).filter(Boolean);
      const paroleDaUsare = usareRaw.split(',').map(s => s.trim()).filter(Boolean);

      const updatedData = {
        id: cardId,
        mazzo,
        livello,
        titolo,
        incipit,
        paroleProibite,
        paroleDaUsare,
        updatedAt: new Date().toISOString()
      };

      // 1. Salva in memoria locale & localStorage
      this.overrides[cardId] = {
        platform: this.platformKey,
        data: updatedData,
        timestamp: Date.now()
      };
      try {
        localStorage.setItem('loratore_didactic_overrides', JSON.stringify(this.overrides));
      } catch (e) {}

      // 2. Salva in tempo reale su Firestore
      const db = window.fbDb || (typeof firebase !== 'undefined' && firebase.firestore ? firebase.firestore() : null);
      if (db) {
        try {
          await db.collection('hub_didactic_overrides').doc(cardId).set({
            platform: this.platformKey,
            data: updatedData,
            timestamp: firebase.firestore.FieldValue.serverTimestamp()
          }, { merge: true });
          console.log(`🔥 Carta ${cardId} salvata e sincronizzata su Firestore.`);
        } catch (fErr) {
          console.warn("Firestore sync non riuscito, salvato in locale:", fErr);
        }
      }

      // 3. Aggiorna in tempo reale la sessione di gioco attiva
      if (window.GameEngine) {
        if (window.GameEngine.gameState && window.GameEngine.gameState.currentCard) {
          window.GameEngine.gameState.currentCard = { ...window.GameEngine.gameState.currentCard, ...updatedData };
          window.GameEngine.renderCardUI();
        }
        if (window.GameEngine.data && window.GameEngine.data.carte) {
          const idx = window.GameEngine.data.carte.findIndex(c => c.id === cardId);
          if (idx >= 0) window.GameEngine.data.carte[idx] = { ...window.GameEngine.data.carte[idx], ...updatedData };
        }
      }

      // 4. Aggiorna admin matrix se presente
      if (window.OratoreAdmin && window.OratoreAdmin.renderMatrix) {
        window.OratoreAdmin.renderMatrix();
      }

      this.closeModal();
      alert("✅ Carta modificata e sincronizzata con successo!");
    },

    saveNewCard: async function() {
      const mazzo = document.getElementById('new-card-mazzo').value;
      const livello = document.getElementById('new-card-livello').value;
      const titolo = document.getElementById('new-card-titolo').value.trim();
      const incipit = document.getElementById('new-card-incipit').value.trim();
      const proibiteRaw = document.getElementById('new-card-proibite').value.trim();
      const usareRaw = document.getElementById('new-card-usare').value.trim();

      if (!titolo || !incipit) {
        alert("Inserisci almeno il Titolo e l'Incipit della nuova traccia.");
        return;
      }

      const paroleProibite = proibiteRaw.split(',').map(s => s.trim()).filter(Boolean);
      const paroleDaUsare = usareRaw.split(',').map(s => s.trim()).filter(Boolean);
      const newId = `custom_${Date.now()}`;

      const newCardData = {
        id: newId,
        mazzo,
        livello,
        titolo,
        incipit,
        paroleProibite,
        paroleDaUsare,
        isCustom: true,
        createdAt: new Date().toISOString()
      };

      // 1. Salva in localStorage
      this.overrides[newId] = {
        platform: this.platformKey,
        data: newCardData,
        timestamp: Date.now()
      };
      try {
        localStorage.setItem('loratore_didactic_overrides', JSON.stringify(this.overrides));
      } catch (e) {}

      // 2. Salva in Firestore
      const db = window.fbDb || (typeof firebase !== 'undefined' && firebase.firestore ? firebase.firestore() : null);
      if (db) {
        try {
          await db.collection('hub_didactic_overrides').doc(newId).set({
            platform: this.platformKey,
            data: newCardData,
            timestamp: firebase.firestore.FieldValue.serverTimestamp()
          });
          console.log(`🔥 Nuovo Incipit ${newId} aggiunto su Firestore!`);
        } catch (fErr) {
          console.warn("Firestore sync non riuscito, salvato in locale:", fErr);
        }
      }

      // 3. Aggiunge alla sessione attiva
      if (window.GameEngine && window.GameEngine.data && window.GameEngine.data.carte) {
        window.GameEngine.data.carte.push(newCardData);
      }

      if (window.OratoreAdmin && window.OratoreAdmin.renderMatrix) {
        window.OratoreAdmin.renderMatrix();
      }

      this.closeModal();
      alert("✅ Nuovo Incipit aggiunto e sincronizzato con successo!");
    },

    closeModal: function() {
      const modal = document.getElementById('live-editor-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.style.display = 'none';
      }
    }
  };

  // Inizializzazione automatica al caricamento DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => window.LiveEditor.init());
  } else {
    window.LiveEditor.init();
  }
})();
