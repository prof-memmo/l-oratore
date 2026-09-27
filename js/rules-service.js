/**
 * ===================================================================
 * RULES-SERVICE.JS - Modulo Centralizzato e Dinamico del Regolamento
 * Progetto: L'Oratore (Ecosistema Prof. Memmo)
 * ===================================================================
 * 
 * - Preserva fedelmente lo stile grafico nativo de L'Oratore (.glass-card, oro classico, icone retoriche)
 * - Sincronizzazione Realtime Firestore su collezione "oratore_settings" / doc "official_rules"
 * - Fallback istantaneo offline con zero-flicker (localStorage + default)
 * - Live Editor per Super-Admin (prof.memmo@gmail.com) in admin.html
 */

(function(window) {
    'use strict';

    const SUPER_ADMIN_EMAIL = 'prof.memmo@gmail.com';

    const DEFAULT_ORATORE_RULES_TEXT = `1. Obiettivo del Gioco
Lo scopo di ogni squadra è portare la propria pedina per prima al Traguardo (Casella 24), sostenendo discorsi oratori da 2 minuti su incipit narrativi estratti casualmente.

2. I 6 Livelli di Difficoltà (QCER)
Nel setup iniziale si seleziona il livello calibrato sul gruppo: da A1 (Narratore in Erba) fino a C2 (Sommo Accademico / Debate).

3. Round a Categorie Condivise
All'inizio di ogni Round, la squadra di turno sceglie la Categoria Tematica. Tutte le squadre affrontano una traccia inedita della stessa categoria per quel round!

4. Modalità di Sfida
Parole Proibite: L'oratore parla per 2 minuti senza pronunciare le 5 parole vietate. 0 penalità = 3 passi, 1 penalità = 2 passi, 2 penalità = 1 passo, 3+ penalità = 0 passi.
Parole da Usare: L'oratore deve inserire nel discorso i 5 vocaboli chiave in modo coerente (+1 punto per ogni parola utilizzata correttamente).

5. Caselle Speciali sul Tabellone
• Casella 6 (🎣 Canna da Pesca): La squadra che vi atterra guadagna +30 secondi extra nel suo turno di discorso successivo (150s totali).
• Casella 12 (📍 Punto di Controllo): Traguardo intermedio a metà percorso che sancisce l'ingresso nella seconda metà del tabellone.
• Casella 18 (♟️ Mossa del Cavallo): Balzo immediato! La pedina avanza subito alla Casella 19.
• Casella 21 (✖️2 Super Raddoppio): I passi ottenuti con il discorso del turno successivo varranno doppio per la volata finale.
• Casella 24 (🏆 Traguardo Finale): Conquista il tabellone e proclama la vittoria finale della partita!

6. Benessere degli Studenti e Pausa Digitale
A tutela del benessere cognitivo ed emotivo, dopo 45 minuti di attività oratoria è prevista una pausa di distensione per consentire la riflessione e il confronto costruttivo tra pari.

7. Codice Etico e Spirito della Retorica
Il dibattito e l'improvvisazione oratoria devono svolgersi sempre nell'intento educativo e nel rispetto reciproco, valorizzando l'ascolto attivo, l'empatia e l'inclusione.`;

    const RulesService = {
        _gameKey: 'oratore',
        _collectionName: 'oratore_settings',
        _docId: 'official_rules',
        _storageKey: 'oratore_rules_official_text',
        _rawText: '',
        _lastUpdated: null,
        _updatedBy: '',
        _isInitialized: false,
        _listeners: [],
        _unsubscribeFirestore: null,

        getDefaultText() {
            return DEFAULT_ORATORE_RULES_TEXT.trim();
        },

        isSuperAdmin(email) {
            const fbUserEmail = (window.fbAuth && window.fbAuth.currentUser && window.fbAuth.currentUser.email) ||
                                (window.firebase && window.firebase.auth && window.firebase.auth().currentUser && window.firebase.auth().currentUser.email);
            const userEmail = (email || fbUserEmail || (window.currentUser && window.currentUser.email) || window.currentUserEmail || '').toLowerCase();
            return userEmail === SUPER_ADMIN_EMAIL.toLowerCase();
        },

        getRawText() {
            return (this._rawText && this._rawText.trim().length > 0) ? this._rawText : this.getDefaultText();
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
            const text = this.getRawText();
            this._listeners.forEach(cb => {
                try {
                    cb(text);
                } catch (e) {
                    console.error("Errore listener RulesService (Oratore):", e);
                }
            });
        },

        async init() {
            // 1. Caricamento istantaneo da cache locale o default (Zero-flicker)
            try {
                const cached = localStorage.getItem(this._storageKey);
                if (cached) {
                    const parsed = JSON.parse(cached);
                    if (parsed && parsed.text) {
                        this._rawText = parsed.text;
                        this._lastUpdated = parsed.lastUpdated || null;
                        this._updatedBy = parsed.updatedBy || '';
                    }
                }
            } catch (e) {
                console.warn("Errore lettura cache regolamento Oratore:", e);
            }

            if (!this._rawText) {
                this._rawText = this.getDefaultText();
            }

            this._notify();

            // 2. Setup listener Firestore Realtime
            if (this._isInitialized) return;
            this._isInitialized = true;

            const db = window.fbDb || (window.firebase && window.firebase.firestore ? window.firebase.firestore() : null);
            if (!db) {
                console.info("Firestore non ancora disponibile per Oratore. Uso cache locale.");
                return;
            }

            try {
                this._unsubscribeFirestore = db.collection(this._collectionName).doc(this._docId)
                    .onSnapshot(docSnap => {
                        if (docSnap.exists) {
                            const data = docSnap.data();
                            if (data && data.text) {
                                this._rawText = data.text;
                                this._lastUpdated = data.lastUpdated || null;
                                this._updatedBy = data.updatedBy || '';

                                try {
                                    localStorage.setItem(this._storageKey, JSON.stringify({
                                        text: this._rawText,
                                        lastUpdated: this._lastUpdated,
                                        updatedBy: this._updatedBy
                                    }));
                                } catch (e) {}

                                this._notify();
                            }
                        }
                    }, err => {
                        console.warn("Firestore snapshot regolamento Oratore (normale se offline):", err.message);
                    });
            } catch (err) {
                console.warn("Inizializzazione Firestore listener regolamento Oratore fallita:", err);
            }
        },

        async saveToCloud(newText) {
            const db = window.fbDb || (window.firebase && window.firebase.firestore ? window.firebase.firestore() : null);
            if (!db) {
                throw new Error("Firestore non disponibile. Verifica la connessione a Internet.");
            }

            const fbUser = (window.fbAuth && window.fbAuth.currentUser) ||
                           (window.firebase && window.firebase.auth && window.firebase.auth().currentUser);
            const userEmail = (fbUser && fbUser.email ? fbUser.email : (window.currentUserEmail || '')).toLowerCase();

            if (!this.isSuperAdmin(userEmail)) {
                throw new Error("Accesso negato: solo il Super-Admin (" + SUPER_ADMIN_EMAIL + ") può salvare il regolamento.");
            }

            const cleanText = (newText || '').trim();
            if (!cleanText) {
                throw new Error("Il testo del regolamento non può essere vuoto.");
            }

            const nowIso = new Date().toISOString();
            const payload = {
                text: cleanText,
                lastUpdated: nowIso,
                updatedBy: userEmail,
                gameKey: this._gameKey
            };

            await db.collection(this._collectionName).doc(this._docId).set(payload, { merge: true });

            this._rawText = cleanText;
            this._lastUpdated = nowIso;
            this._updatedBy = userEmail;

            try {
                localStorage.setItem(this._storageKey, JSON.stringify({
                    text: this._rawText,
                    lastUpdated: this._lastUpdated,
                    updatedBy: this._updatedBy
                }));
            } catch (e) {}

            this._notify();
            return { success: true, lastUpdated: nowIso };
        },

        // Parsing automatico in sezioni
        parseTextToItems(text) {
            const src = (text || this.getRawText()).trim();
            if (!src) return [];

            const blocks = src.split(/\n\s*\n/).map(b => b.trim()).filter(Boolean);
            const items = [];

            blocks.forEach((block, index) => {
                const lines = block.split('\n').map(l => l.trim()).filter(Boolean);
                if (lines.length === 0) return;

                let firstLine = lines[0].replace(/^[\u2022\*\-]\s*/, '').trim();
                let title = '';
                let content = '';

                const matchNumbered = firstLine.match(/^(\d+[\.\)]\s*)(.*)$/);
                if (matchNumbered) {
                    firstLine = matchNumbered[2].trim();
                }

                if (lines.length > 1) {
                    title = firstLine;
                    content = lines.slice(1).join('\n').trim();
                } else {
                    const colonMatch = firstLine.match(/^([^:]{3,60}):\s*(.+)$/);
                    if (colonMatch) {
                        title = colonMatch[1].trim();
                        content = colonMatch[2].trim();
                    } else {
                        content = firstLine;
                    }
                }

                if (title) {
                    title = title.replace(/:\s*$/, '').trim();
                }

                items.push({
                    index: index + 1,
                    title: title,
                    text: content || title,
                    fullText: block
                });
            });

            return items;
        },

        // ===================================================================
        // VISTA PUBBLICA / GIOCO (#view-regolamento in index.html)
        // Stile nativo de L'Oratore: .glass-card, oro classico, icona bilancia
        // ===================================================================
        renderPublicView(containerId = 'view-regolamento-container') {
            const container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
            if (!container) return;

            const items = this.parseTextToItems();

            container.innerHTML = `
                <div class="glass-card" style="max-width: 900px; margin: 0 auto; padding: 30px;">
                    <div style="border-bottom: 1px solid rgba(212, 175, 55, 0.2); padding-bottom: 15px; margin-bottom: 20px;">
                        <h2 style="font-size: 1.6rem; color: var(--accent-gold); margin-bottom: 8px;">
                            <i class="fa-solid fa-scale-balanced"></i> Regolamento Ufficiale de L'Oratore
                        </h2>
                        <p style="font-size: 0.88rem; color: var(--text-muted); margin: 0;">
                            Il gioco di retorica, narrazione e improvvisazione per la scuola e il gioco in famiglia.
                        </p>
                    </div>

                    <div style="font-size: 0.95rem; line-height: 1.7; color: var(--text-main);">
                        ${items.map(item => `
                            <div style="margin-top: 22px;">
                                <h3 style="color: var(--accent-gold); margin-bottom: 6px; font-size: 1.15rem;">
                                    ${item.index}. ${item.title || `Regola ${item.index}`}
                                </h3>
                                <div style="color: var(--text-main); font-size: 0.95rem; line-height: 1.7;">
                                    ${item.text.split('\n').map(l => {
                                        const trimmed = l.trim();
                                        if (trimmed.startsWith('•') || trimmed.startsWith('-')) {
                                            return `<div style="padding-left: 12px; margin-bottom: 4px;">${trimmed}</div>`;
                                        }
                                        return `<p style="margin: 0 0 8px 0;">${trimmed}</p>`;
                                    }).join('')}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        },

        // ===================================================================
        // VISTA SUPER-ADMIN LIVE EDITOR (admin.html)
        // ===================================================================
        renderAdminEditor(containerId = 'oratore-rules-editor-container') {
            const container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
            if (!container) return;

            const text = this.getRawText();
            const fbUser = (window.fbAuth && window.fbAuth.currentUser) || 
                           (window.firebase && window.firebase.auth && window.firebase.auth().currentUser);
            const userEmail = fbUser ? (fbUser.email || '') : (window.currentUserEmail || '');
            const isAuthAdmin = userEmail.toLowerCase() === SUPER_ADMIN_EMAIL.toLowerCase();

            container.innerHTML = `
                <div class="glass-card" style="border: 2px solid #d4af37; border-radius: 16px; padding: 25px; margin-top: 25px;">
                    <div style="margin-bottom: 16px; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <h3 style="margin: 0 0 6px 0; font-size: 1.3rem; color: #d4af37; display: flex; align-items: center; gap: 8px;">
                                <i class="fa-solid fa-scale-balanced"></i> Regolamento Ufficiale • Live Editor Cloud
                            </h3>
                            <p style="margin: 0; font-size: 0.88rem; color: #cbd5e1; line-height: 1.4;">
                                Modifica il testo del Regolamento in tempo reale. I cambiamenti verranno sincronizzati istantaneamente sul gioco.
                            </p>
                        </div>
                        <div>
                            ${isAuthAdmin ? `
                                <span style="font-size: 0.75rem; background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); padding: 4px 10px; border-radius: 20px; display: inline-flex; align-items: center; gap: 5px;">
                                    <i class="fa-solid fa-circle-check"></i> Super-Admin Autenticato (${userEmail})
                                </span>
                            ` : `
                                <span style="font-size: 0.75rem; background: rgba(212, 175, 55, 0.15); color: #d4af37; border: 1px solid rgba(212, 175, 55, 0.3); padding: 4px 10px; border-radius: 20px; display: inline-flex; align-items: center; gap: 5px;">
                                    <i class="fa-solid fa-cloud-arrow-up"></i> Cloud Sync (${SUPER_ADMIN_EMAIL})
                                </span>
                            `}
                        </div>
                    </div>

                    <div style="margin-bottom: 18px;">
                        <textarea id="oratore-rules-textarea" rows="16" style="width: 100%; box-sizing: border-box; background: #070a13; border: 1px solid rgba(212,175,55,0.4); border-radius: 8px; color: #fff; padding: 14px; font-size: 0.9rem; line-height: 1.6; font-family: inherit; resize: vertical; outline: none;" placeholder="Inserisci i punti del regolamento numerati...">${text}</textarea>
                    </div>

                    <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
                        <button type="button" id="btn-save-oratore-rules" onclick="window.OratoreRulesService.handleSaveButton()" style="background: #d4af37; color: #000000; border: none; padding: 12px 24px; border-radius: 25px; font-weight: 800; font-size: 0.88rem; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3); text-transform: uppercase; letter-spacing: 0.5px;">
                            <i class="fa-solid fa-floppy-disk"></i> SALVA REGOLAMENTO
                        </button>
                        
                        <button type="button" onclick="window.OratoreRulesService.handleResetButton()" style="background: transparent; color: #aaa; border: 1px solid rgba(255,255,255,0.2); padding: 10px 18px; border-radius: 20px; font-size: 0.82rem; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
                            <i class="fa-solid fa-rotate-left"></i> Ripristina Predefinito
                        </button>
                    </div>
                </div>
            `;
        },

        async handleSaveButton() {
            const textarea = document.getElementById('oratore-rules-textarea');
            if (!textarea) return;

            const btn = document.getElementById('btn-save-oratore-rules');
            const originalHtml = btn ? btn.innerHTML : '';
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> SALVATAGGIO...`;
            }

            try {
                await this.saveToCloud(textarea.value);
                if (btn) {
                    btn.innerHTML = `<i class="fa-solid fa-check"></i> SALVATO CON SUCCESSO!`;
                    btn.style.background = '#22c55e';
                    btn.style.color = '#fff';
                }
                setTimeout(() => {
                    if (btn) {
                        btn.disabled = false;
                        btn.innerHTML = originalHtml;
                        btn.style.background = '#d4af37';
                        btn.style.color = '#000';
                    }
                }, 2000);
            } catch (err) {
                alert("Errore salvataggio: " + (err.message || err));
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = originalHtml;
                }
            }
        },

        handleResetButton() {
            if (!confirm("Vuoi ripristinare il testo del regolamento a quello predefinito ufficiale de L'Oratore?")) return;
            const textarea = document.getElementById('oratore-rules-textarea');
            if (textarea) {
                textarea.value = this.getDefaultText();
            }
        }
    };

    window.RulesService = RulesService;
    window.OratoreRulesService = RulesService;

    // Auto-inizializzazione al caricamento
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => RulesService.init());
    } else {
        RulesService.init();
    }

})(window);
