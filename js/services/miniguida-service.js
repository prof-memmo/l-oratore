/**
 * ===================================================================
 * MINIGUIDA-SERVICE.JS - Modulo Dinamico per Tutorial / Miniguida
 * Progetto: L'Oratore (Ecosistema Prof. Memmo)
 * ===================================================================
 */

(function(window) {
    'use strict';

    const SUPER_ADMIN_EMAIL = 'prof.memmo@gmail.com';

    const DEFAULT_MINIGUIDA = {
        title: "Come si gioca?",
        themeColor: "#d4af37",
        steps: [
            {
                icon: "👥",
                title: "Forma le Squadre e Scegli la Pedina",
                text: "Dividetevi in 2, 3 o 4 squadre e scegliete il personaggio. A ogni turno, la squadra attiva nomina il proprio <strong>Oratore</strong>, mentre gli avversari compongono la <strong>Giuria</strong>."
            },
            {
                icon: "🎯",
                title: "Scegli la Sfida di Narrazione",
                text: "<strong>Parole Proibite o da Usare:</strong> L'oratore ha 2 minuti per parlare evitando le 5 parole vietate o inserendo i vocaboli chiave richiesti."
            },
            {
                icon: "🎲",
                title: "Avanzamento sul Tabellone",
                text: "Meno errori commetti, più caselle avanzi sul tabellone! Attento alle caselle speciali come la <em>Canna da Pesca</em> o la <em>Mossa del Cavallo</em>."
            },
            {
                icon: "🏆",
                title: "Traguardo Finale e Vittoria",
                text: "La prima squadra che raggiunge la casella 24 taglia il <strong>Traguardo</strong> e conquista il titolo di <em>Miglior Oratore dell'Anno</em>!"
            }
        ]
    };

    const MiniguidaService = {
        _gameKey: 'oratore',
        _collectionName: 'oratore_settings',
        _docId: 'miniguida',
        _storageKey: 'oratore_miniguida_data',
        _data: null,
        _currentStep: 0,
        _isInitialized: false,
        _listeners: [],

        getDefaultData() {
            return JSON.parse(JSON.stringify(DEFAULT_MINIGUIDA));
        },

        getData() {
            return this._data || this.getDefaultData();
        },

        subscribe(callback) {
            if (typeof callback === 'function' && !this._listeners.includes(callback)) {
                this._listeners.push(callback);
            }
            return () => {
                this._listeners = this._listeners.filter(cb => cb !== callback);
            };
        },

        _notify() {
            const data = this.getData();
            this._listeners.forEach(cb => {
                try { cb(data); } catch (e) { console.error("Errore listener MiniguidaService:", e); }
            });
            this.renderModal();
        },

        async init() {
            try {
                const cached = localStorage.getItem(this._storageKey);
                if (cached) {
                    this._data = JSON.parse(cached);
                }
            } catch (e) {
                console.warn("Errore lettura cache miniguida:", e);
            }

            if (!this._data) {
                this._data = this.getDefaultData();
            }

            this._notify();

            if (this._isInitialized) return;
            this._isInitialized = true;

            const db = window.fbDb || (window.firebase && window.firebase.firestore ? window.firebase.firestore() : null);
            if (!db) return;

            try {
                db.collection(this._collectionName).doc(this._docId)
                    .onSnapshot(docSnap => {
                        if (docSnap.exists) {
                            const data = docSnap.data();
                            if (data && data.steps && Array.isArray(data.steps)) {
                                this._data = data;
                                try { localStorage.setItem(this._storageKey, JSON.stringify(data)); } catch (e) {}
                                this._notify();
                            }
                        }
                    }, err => {
                        console.warn("Firestore snapshot miniguida (offline ok):", err.message);
                    });
            } catch (e) {
                console.warn("Init Firestore miniguida fallita:", e);
            }
        },

        async saveToCloud(newData) {
            const db = window.fbDb || (window.firebase && window.firebase.firestore ? window.firebase.firestore() : null);
            this._data = newData;
            try { localStorage.setItem(this._storageKey, JSON.stringify(newData)); } catch (e) {}
            this._notify();

            if (!db) return true;

            const payload = {
                title: newData.title || DEFAULT_MINIGUIDA.title,
                themeColor: newData.themeColor || DEFAULT_MINIGUIDA.themeColor,
                steps: newData.steps || DEFAULT_MINIGUIDA.steps,
                lastUpdated: new Date().toISOString(),
                updatedBy: SUPER_ADMIN_EMAIL
            };

            await db.collection(this._collectionName).doc(this._docId).set(payload, { merge: true });
            return true;
        },

        // Gestione Modal Gioco
        openModal() {
            this._currentStep = 0;
            this.renderModal();
            const modal = document.getElementById('miniguida-modal');
            if (modal) {
                modal.classList.remove('hidden');
                modal.style.display = 'flex';
            }
        },

        closeModal() {
            const modal = document.getElementById('miniguida-modal');
            if (modal) {
                modal.classList.add('hidden');
                modal.style.display = 'none';
            }
        },

        nextStep() {
            const total = (this._data && this._data.steps) ? this._data.steps.length : DEFAULT_MINIGUIDA.steps.length;
            if (this._currentStep < total - 1) {
                this._currentStep++;
                this.renderModal();
            } else {
                this.closeModal();
            }
        },

        prevStep() {
            if (this._currentStep > 0) {
                this._currentStep--;
                this.renderModal();
            }
        },

        renderModal() {
            const data = this.getData();
            const total = data.steps.length;
            if (this._currentStep >= total) this._currentStep = 0;
            const current = data.steps[this._currentStep] || data.steps[0];

            const titleEl = document.getElementById('guide-modal-title') || document.getElementById('miniguida-title');
            const iconEl = document.getElementById('guide-step-icon');
            const stepTitleEl = document.getElementById('guide-step-title');
            const descEl = document.getElementById('guide-step-desc');
            const numEl = document.getElementById('guide-step-num');
            const prevBtn = document.getElementById('guide-prev-btn');
            const nextBtn = document.getElementById('guide-next-btn');

            if (titleEl) titleEl.innerText = data.title || "Come si gioca?";
            if (iconEl) iconEl.innerHTML = current.icon || "👥";
            if (stepTitleEl) stepTitleEl.innerHTML = current.title ? `${this._currentStep + 1}. ${current.title}` : `Passo ${this._currentStep + 1}`;
            if (descEl) descEl.innerHTML = current.text || "";
            if (numEl) numEl.innerText = `Passo ${this._currentStep + 1} di ${total}`;
            if (prevBtn) prevBtn.disabled = this._currentStep === 0;
            if (nextBtn) nextBtn.innerText = this._currentStep === total - 1 ? "Ho Capito! ✅" : "Avanti ➔";
        },

        // Render Live Editor nella Dashboard Admin
        renderAdminEditor(containerId = 'oratore-miniguida-editor-container') {
            const container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
            if (!container) return;

            const data = this.getData();

            container.innerHTML = `
                <div class="glass-card" style="border: 2px solid #d4af37; border-radius: 16px; padding: 25px; margin-top: 25px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">
                        <div>
                            <h3 style="margin: 0 0 6px 0; font-size: 1.3rem; color: #d4af37; display: flex; align-items: center; gap: 8px;">
                                <i class="fa-solid fa-chalkboard-user"></i> Miniguida &amp; Tutorial • Live Editor
                            </h3>
                            <p style="margin: 0; font-size: 0.88rem; color: #cbd5e1; line-height: 1.4;">
                                Modifica i passi della miniguida mostrata agli studenti e collauda il risultato in tempo reale nell'anteprima.
                            </p>
                        </div>
                    </div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: start;">
                        <!-- Colonna Sinistra: Form Modifica -->
                        <div>
                            <div style="margin-bottom: 15px;">
                                <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #94a3b8; margin-bottom: 6px;">Titolo Modale:</label>
                                <input type="text" id="admin-miniguida-title" value="${data.title || 'Come si gioca?'}" style="width: 100%; padding: 10px; background: #070a13; border: 1px solid #d4af37; border-radius: 8px; color: #fff; font-size: 0.9rem;" oninput="window.OratoreMiniguidaService.updatePreviewFromForm()">
                            </div>

                            <div id="admin-miniguida-steps-list">
                                ${data.steps.map((step, idx) => `
                                    <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(212,175,55,0.3); border-radius: 10px; padding: 12px; margin-bottom: 12px;" data-step-index="${idx}">
                                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                            <strong style="color: #d4af37; font-size: 0.85rem;">Passo ${idx + 1}</strong>
                                            <div style="display: flex; gap: 6px; align-items: center;">
                                                <input type="text" class="step-icon-input" value="${step.icon || '👥'}" style="width: 45px; text-align: center; padding: 4px; background: #070a13; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; color: #fff; font-size: 0.9rem;" title="Emoji o Icona" oninput="window.OratoreMiniguidaService.updatePreviewFromForm()">
                                                <button type="button" onclick="window.OratoreMiniguidaService.removeStep(${idx})" style="background: #ef4444; color: #fff; border: none; border-radius: 6px; padding: 4px 8px; font-size: 0.75rem; cursor: pointer;">✕</button>
                                            </div>
                                        </div>
                                        <input type="text" class="step-title-input" value="${step.title || ''}" placeholder="Titolo passo..." style="width: 100%; padding: 6px 10px; background: #070a13; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; color: #fff; font-size: 0.85rem; margin-bottom: 6px;" oninput="window.OratoreMiniguidaService.updatePreviewFromForm()">
                                        <textarea class="step-text-input" rows="3" style="width: 100%; padding: 8px 10px; background: #070a13; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; color: #fff; font-size: 0.85rem; line-height: 1.4; resize: vertical;" placeholder="Testo descrittivo..." oninput="window.OratoreMiniguidaService.updatePreviewFromForm()">${step.text || ''}</textarea>
                                    </div>
                                `).join('')}
                            </div>

                            <button type="button" onclick="window.OratoreMiniguidaService.addStep()" style="background: transparent; border: 1px dashed #d4af37; color: #d4af37; width: 100%; padding: 10px; border-radius: 8px; font-weight: 700; cursor: pointer; margin-bottom: 15px;">
                                <i class="fa-solid fa-plus"></i> Aggiungi Nuovo Passo
                            </button>

                            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                                <button type="button" id="btn-save-miniguida" onclick="window.OratoreMiniguidaService.handleSaveButton()" style="background: #d4af37; color: #000; border: none; padding: 12px 24px; border-radius: 25px; font-weight: 800; font-size: 0.88rem; cursor: pointer; display: inline-flex; align-items: center; gap: 8px;">
                                    <i class="fa-solid fa-floppy-disk"></i> SALVA MINIGUIDA
                                </button>
                                <button type="button" onclick="window.OratoreMiniguidaService.handleResetButton()" style="background: transparent; color: #aaa; border: 1px solid rgba(255,255,255,0.2); padding: 10px 18px; border-radius: 20px; font-size: 0.82rem; cursor: pointer;">
                                    <i class="fa-solid fa-rotate-left"></i> Ripristina Predefiniti
                                </button>
                            </div>
                        </div>

                        <!-- Colonna Destra: Live Interactive Preview -->
                        <div>
                            <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #94a3b8; margin-bottom: 6px;">Anteprima Live (Come appare sulla LIM):</label>
                            <div style="background: white; border-radius: 20px; padding: 20px; color: #1e293b; display: flex; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); min-height: 420px; position: relative;">
                                <div style="width: 35%; background: #f8fafc; display: flex; align-items: flex-end; justify-content: center; border-right: 1.5px solid #f1f5f9; padding-top: 15px;">
                                    <img src="assets/prof_memmo_full.jpg" onerror="this.src='https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/branding/prof-memmo/prof-memmo-full.jpg';" alt="Prof Memmo" style="width: 120%; object-fit: contain; mix-blend-mode: multiply;">
                                </div>
                                <div style="flex: 1; padding: 15px 20px; display: flex; flex-direction: column; justify-content: space-between;">
                                    <div>
                                        <h3 id="preview-modal-title" style="color: #d4af37; margin: 0 0 15px 0; font-size: 1.3rem; font-weight: 900; text-transform: uppercase; text-align: center;">${data.title || 'Come si gioca?'}</h3>
                                        <div style="text-align: center; margin-top: 15px;">
                                            <div id="preview-step-icon" style="font-size: 3.5rem; margin-bottom: 10px;">${data.steps[0]?.icon || '👥'}</div>
                                            <h4 id="preview-step-title" style="margin: 0 0 8px 0; color: #0f172a; font-size: 1.05rem; font-weight: 800;">1. ${data.steps[0]?.title || ''}</h4>
                                            <div id="preview-step-text" style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${data.steps[0]?.text || ''}</div>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 12px;">
                                        <span id="preview-step-num" style="font-size: 0.75rem; font-weight: 700; color: #94a3b8;">Passo 1 di ${data.steps.length}</span>
                                        <div style="display: flex; gap: 6px;">
                                            <button type="button" onclick="window.OratoreMiniguidaService.previewStepPrev()" style="background: #f1f5f9; color: #475569; border: none; padding: 6px 12px; border-radius: 8px; font-size: 0.8rem; font-weight: 700; cursor: pointer;">◀</button>
                                            <button type="button" onclick="window.OratoreMiniguidaService.previewStepNext()" style="background: #d4af37; color: #000; border: none; padding: 6px 16px; border-radius: 8px; font-size: 0.8rem; font-weight: 800; cursor: pointer;">Avanti ▶</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        },

        _previewIndex: 0,

        getFormData() {
            const titleInput = document.getElementById('admin-miniguida-title');
            const stepBlocks = document.querySelectorAll('#admin-miniguida-steps-list > div');
            const steps = [];

            stepBlocks.forEach(block => {
                const icon = block.querySelector('.step-icon-input')?.value || '👥';
                const title = block.querySelector('.step-title-input')?.value || '';
                const text = block.querySelector('.step-text-input')?.value || '';
                steps.push({ icon, title, text });
            });

            return {
                title: titleInput ? titleInput.value : 'Come si gioca?',
                themeColor: '#d4af37',
                steps: steps.length > 0 ? steps : this.getDefaultData().steps
            };
        },

        updatePreviewFromForm() {
            const data = this.getFormData();
            const total = data.steps.length;
            if (this._previewIndex >= total) this._previewIndex = total - 1;
            if (this._previewIndex < 0) this._previewIndex = 0;

            const curr = data.steps[this._previewIndex] || data.steps[0];
            const titleEl = document.getElementById('preview-modal-title');
            const iconEl = document.getElementById('preview-step-icon');
            const stepTitleEl = document.getElementById('preview-step-title');
            const textEl = document.getElementById('preview-step-text');
            const numEl = document.getElementById('preview-step-num');

            if (titleEl) titleEl.innerText = data.title;
            if (iconEl) iconEl.innerHTML = curr?.icon || '👥';
            if (stepTitleEl) stepTitleEl.innerHTML = `${this._previewIndex + 1}. ${curr?.title || ''}`;
            if (textEl) textEl.innerHTML = curr?.text || '';
            if (numEl) numEl.innerText = `Passo ${this._previewIndex + 1} di ${total}`;
        },

        previewStepNext() {
            const data = this.getFormData();
            if (this._previewIndex < data.steps.length - 1) {
                this._previewIndex++;
                this.updatePreviewFromForm();
            }
        },

        previewStepPrev() {
            if (this._previewIndex > 0) {
                this._previewIndex--;
                this.updatePreviewFromForm();
            }
        },

        addStep() {
            const data = this.getFormData();
            data.steps.push({
                icon: '⭐',
                title: 'Nuovo Passo',
                text: 'Inserisci qui la spiegazione della regola...'
            });
            this._data = data;
            this.renderAdminEditor();
        },

        removeStep(idx) {
            const data = this.getFormData();
            if (data.steps.length <= 1) {
                alert("La miniguida deve avere almeno un passo!");
                return;
            }
            data.steps.splice(idx, 1);
            this._data = data;
            this.renderAdminEditor();
        },

        async handleSaveButton() {
            const data = this.getFormData();
            const btn = document.getElementById('btn-save-miniguida');
            const orig = btn ? btn.innerHTML : '';
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> SALVATAGGIO...`;
            }

            try {
                await this.saveToCloud(data);
                if (btn) {
                    btn.innerHTML = `<i class="fa-solid fa-check"></i> MINIGUIDA SALVATA!`;
                    btn.style.background = '#22c55e';
                    btn.style.color = '#fff';
                }
                setTimeout(() => {
                    if (btn) {
                        btn.disabled = false;
                        btn.innerHTML = orig;
                        btn.style.background = '#d4af37';
                        btn.style.color = '#000';
                    }
                }, 2000);
            } catch (err) {
                alert("Errore durante il salvataggio: " + (err.message || err));
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = orig;
                }
            }
        },

        handleResetButton() {
            if (!confirm("Vuoi ripristinare i passi della miniguida ai valori predefiniti?")) return;
            this._data = this.getDefaultData();
            this.renderAdminEditor();
        }
    };

    window.MiniguidaService = MiniguidaService;
    window.OratoreMiniguidaService = MiniguidaService;

    // Inizializzazione automatica
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => MiniguidaService.init());
    } else {
        MiniguidaService.init();
    }
})(window);
