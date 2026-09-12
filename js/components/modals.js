/**
 * L'ORATORE - Modal Management System
 * Handles Miniguida, Profile Editing, and Legal Modals (Privacy, Termini, Contatti)
 */

const Modals = {
  currentGuideStep: 1,
  totalGuideSteps: 4,

  guideSteps: [
    {
      title: "1. Forma le Squadre e Scegli la Pedina",
      desc: "Dividetevi in 2, 3 o 4 squadre e scegliete il vostro personaggio tra le 10 pedine illustrate. A ogni turno, la squadra attiva nomina il proprio <strong>Oratore</strong>, mentre le squadre avversarie compongono la <strong>Giuria Imparziale</strong>.",
      icon: "👥"
    },
    {
      title: "2. Scegli la Sfida di Narrazione",
      desc: "<strong>Parole Proibite:</strong> L'oratore ha 2 minuti per raccontare la storia senza mai pronunciare le 5 parole vietate. La giuria aziona il Buzzer a ogni errore!<br><br><strong>Parole da Usare:</strong> 30 secondi di studio lessicale, poi 2 minuti per tessere un discorso inserendo con eleganza tutti e 5 i vocaboli chiave.",
      icon: "🎯"
    },
    {
      title: "3. Avanzamento sul Tabellone (24 Caselle)",
      desc: "Meno infrazioni commetti e più vocaboli integri con coerenza, più passi guadagna la tua squadra! Occhio alle caselle speciali: <em>🎣 Canna da Pesca</em>, <em>📍 Checkpoint</em>, <em>♟️ Mossa del Cavallo</em> e <em>✖️2 Bonus Doppio</em>.",
      icon: "🎲"
    },
    {
      title: "4. Traguardo Finale e Vittoria",
      desc: "La prima squadra che raggiunge la casella 24 taglia il <strong>Traguardo</strong> e conquista il titolo di <em>Miglior Oratore dell'Anno</em>!",
      icon: "🏆"
    }
  ],

  openMiniguida() {
    this.currentGuideStep = 1;
    this.renderGuideStep();
    const modal = document.getElementById('miniguida-modal');
    if (modal) modal.classList.remove('hidden');
  },

  openMiniguidaModal() {
    this.openMiniguida();
  },

  closeMiniguida() {
    const modal = document.getElementById('miniguida-modal');
    if (modal) modal.classList.add('hidden');
  },

  closeMiniguidaModal() {
    this.closeMiniguida();
  },

  renderGuideStep() {
    const step = this.guideSteps[this.currentGuideStep - 1];
    const iconEl = document.getElementById('guide-step-icon');
    const titleEl = document.getElementById('guide-step-title');
    const descEl = document.getElementById('guide-step-desc');
    const numEl = document.getElementById('guide-step-num');

    if (iconEl) iconEl.textContent = step.icon;
    if (titleEl) titleEl.textContent = step.title;
    if (descEl) descEl.innerHTML = step.desc;
    if (numEl) numEl.textContent = `Passo ${this.currentGuideStep} di ${this.totalGuideSteps}`;

    const prevBtn = document.getElementById('guide-prev-btn');
    const nextBtn = document.getElementById('guide-next-btn');

    if (prevBtn) prevBtn.disabled = this.currentGuideStep === 1;
    if (nextBtn) {
      nextBtn.textContent = this.currentGuideStep === this.totalGuideSteps ? "Ho Capito! ✅" : "Avanti ➔";
    }
  },

  nextGuideStep() {
    if (this.currentGuideStep < this.totalGuideSteps) {
      this.currentGuideStep++;
      this.renderGuideStep();
    } else {
      this.closeMiniguida();
    }
  },

  prevGuideStep() {
    if (this.currentGuideStep > 1) {
      this.currentGuideStep--;
      this.renderGuideStep();
    }
  },

  selectedAvatar: 'https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/6.png',

  openProfileModal() {
    const modal = document.getElementById('edit-profile-modal');
    const nameInput = document.getElementById('edit-profile-name');
    const schoolInput = document.getElementById('edit-profile-school');
    const grid = document.getElementById('oratore-edit-avatar-grid');
    if (!modal) return;

    // Carica profilo salvato o default
    const savedName = localStorage.getItem('loratore_user_name') || 'Prof. Memmo';
    const savedSchool = localStorage.getItem('loratore_user_school') || '';
    const savedAvatar = localStorage.getItem('loratore_user_avatar') || 'https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/6.png';
    this.selectedAvatar = savedAvatar;

    if (nameInput) nameInput.value = savedName;
    if (schoolInput) schoolInput.value = savedSchool;

    if (grid) {
      grid.innerHTML = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15].map(num => {
        const url = `assets/avatars/${num}.png`;
        const cdnUrl = `https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/${num}.png`;
        const isSelected = this.selectedAvatar.includes(`${num}.png`);
        return `
          <div class="avatar-option ${isSelected ? 'active' : ''}" 
               onclick="Modals.selectAvatar(this, '${url}')"
               style="width: 46px; height: 46px; border-radius: 50%; border: 3px solid ${isSelected ? 'var(--accent-gold)' : 'transparent'}; cursor: pointer; overflow: hidden; transition: transform 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.4); background: #ffffff; display: flex; align-items: center; justify-content: center; transform: ${isSelected ? 'scale(1.1)' : 'scale(1)'};">
            <img src="${url}" onerror="this.src='${cdnUrl}'" alt="Avatar ${num}" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
        `;
      }).join('');
    }

    modal.classList.remove('hidden');
    const userDropdown = document.getElementById('user-dropdown');
    if (userDropdown) userDropdown.classList.add('hidden');
  },

  selectAvatar(element, avatarUrl) {
    this.selectedAvatar = avatarUrl;
    document.querySelectorAll('#oratore-edit-avatar-grid .avatar-option').forEach(opt => {
      opt.classList.remove('active');
      opt.style.borderColor = 'transparent';
      opt.style.transform = 'scale(1)';
    });
    if (element) {
      element.classList.add('active');
      element.style.borderColor = 'var(--accent-gold)';
      element.style.transform = 'scale(1.1)';
    }
  },

  saveProfileData() {
    const nameInput = document.getElementById('edit-profile-name');
    const schoolInput = document.getElementById('edit-profile-school');
    const newName = nameInput ? nameInput.value.trim() : 'Prof. Memmo';
    const newSchool = schoolInput ? schoolInput.value.trim() : '';

    localStorage.setItem('loratore_user_name', newName);
    localStorage.setItem('loratore_user_school', newSchool);
    localStorage.setItem('loratore_user_avatar', this.selectedAvatar);

    // Aggiorna interfaccia Header e Dropdown
    const headerName = document.getElementById('header-user-name');
    const dropdownName = document.getElementById('dropdown-user-name');
    const headerAvatar = document.getElementById('header-user-avatar');

    if (headerName) headerName.textContent = newName.toUpperCase();
    if (dropdownName) dropdownName.textContent = newName.toUpperCase();
    if (headerAvatar) headerAvatar.src = this.selectedAvatar;

    this.closeProfileModal();
    alert("✅ Profilo salvato con successo!");
  },

  closeProfileModal() {
    const modal = document.getElementById('edit-profile-modal');
    if (modal) modal.classList.add('hidden');
  },

  openLegalModal(type) {
    const modal = document.getElementById('legal-modal');
    const title = document.getElementById('legal-modal-title');
    const body = document.getElementById('legal-modal-body');
    if (!modal || !title || !body) return;

    if (type === 'privacy') {
      title.innerHTML = '<i class="fa-solid fa-shield"></i> Informativa sulla Privacy';
      body.innerHTML = `
        <p>I dati raccolti all'interno dell'Ecosistema Prof. Memmo sono trattati nel rispetto della normativa GDPR e utilizzati esclusivamente a fini didattici e di autenticazione per l'accesso ai giochi.</p>
        <p style="margin-top:10px;">Nessun dato viene ceduto a terze parti o utilizzato a scopo pubblicitario.</p>
      `;
    } else if (type === 'termini') {
      title.innerHTML = '<i class="fa-solid fa-scroll"></i> Termini di Servizio & Licenza';
      body.innerHTML = `
        <p>&copy; 2026 Guglielmo Piersanti. Tutti i contenuti presenti su questo sito sono di proprietà dell'autore e sono protetti tramite deposito e marcatura temporale presso Patamu.</p>
        <p style="margin-top:10px;">I contenuti sono inoltre distribuiti con licenza <em>Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)</em>.</p>
      `;
    } else if (type === 'contatti') {
      title.innerHTML = '<i class="fa-solid fa-envelope"></i> Contatti & Supporto';
      body.innerHTML = `
        <p>Per segnalazioni, collaborazioni o informazioni sull'Ecosistema Didattico Prof. Memmo:</p>
        <p style="margin-top:10px;"><strong>Email:</strong> <a href="mailto:prof.memmo@gmail.com" style="color:var(--accent-gold);">prof.memmo@gmail.com</a></p>
        <p style="margin-top:10px;"><strong>Hub Didattico:</strong> <a href="https://prof-memmo.github.io/games/" target="_blank" style="color:var(--accent-gold);">prof-memmo.github.io/games</a></p>
      `;
    }

    modal.classList.remove('hidden');
  },

  closeLegalModal() {
    const modal = document.getElementById('legal-modal');
    if (modal) modal.classList.add('hidden');
  }
};

window.Modals = Modals;
