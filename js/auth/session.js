/**
 * Prof. Memmo — Session & Auto-Routing Manager
 * L'Oratore
 */

window.Auth = {
  user: null,
  role: 'guest', // 'viandante' | 'docente' | 'studente' | 'admin' | 'guest'
  plan: 'base',  // 'viandante' | 'docente_didattico' | 'docente_ecosistema' | 'base'
  name: 'Ospite',
  avatar: 'https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/branding/prof-memmo/avatar.png',
  xp: 150,

  init: async function () {
    // 1. Check local session storage first
    const cachedUser = localStorage.getItem('pm_oratore_user');
    if (cachedUser) {
      try {
        const parsed = JSON.parse(cachedUser);
        this.user = parsed;
        this.role = parsed.role || 'guest';
        this.plan = parsed.plan || 'base';
        this.name = parsed.name || 'Oratore';
        this.avatar = parsed.avatar || this.avatar;
        this.xp = parsed.xp || 150;
      } catch (e) {
        localStorage.removeItem('pm_oratore_user');
      }
    }

    // 2. Listen to Firebase Auth if present
    if (window.fbAuth) {
      window.fbAuth.onAuthStateChanged(async (fbUser) => {
        if (fbUser) {
          await this.handleFirebaseUser(fbUser);
        } else {
          this.updateUI();
          this.routeUser();
        }
      });
    } else {
      this.updateUI();
      this.routeUser();
    }
  },

  handleFirebaseUser: async function (fbUser) {
    this.user = fbUser;
    this.name = fbUser.displayName || fbUser.email.split('@')[0];

    try {
      if (window.fbDb) {
        const doc = await window.fbDb.collection('hub_users').doc(fbUser.uid).get();
        if (doc.exists) {
          const data = doc.data();
          this.role = data.role || 'studente';
          this.plan = data.subscription || data.abbonamento || 'base';
          if (data.anagrafica && data.anagrafica.nome) {
            this.name = data.anagrafica.nome;
          }
          if (data.avatar) {
            this.avatar = data.avatar;
          }
        }
      }
    } catch (e) {
      console.warn("Lettura profilo hub_users in fallback:", e);
    }

    this.saveSession();
    this.updateUI();
    this.routeUser();
  },

  saveSession: function () {
    localStorage.setItem('pm_oratore_user', JSON.stringify({
      role: this.role,
      plan: this.plan,
      name: this.name,
      avatar: this.avatar,
      xp: this.xp
    }));
  },

  updateUI: function () {
    const nameEl = document.getElementById('header-user-name');
    const avatarEl = document.getElementById('header-user-avatar');
    const xpEl = document.getElementById('dropdown-user-xp');

    if (nameEl) nameEl.textContent = this.name;
    if (avatarEl) avatarEl.src = this.avatar;
    if (xpEl) xpEl.textContent = `${this.xp} XP`;
  },

  // Auto-Routing Diretto: Il Viandante va nel Party, il Docente va nella Classe
  routeUser: function () {
    if (this.role === 'viandante' || this.plan === 'viandante' || this.role === 'amico') {
      console.log("Auto-routing attivo: Profilo Viandante rilevato -> Apertura diretta Modalità Party.");
      if (window.App) window.App.showPartyViewDirect();
    } else if (this.role === 'docente' || this.role === 'admin') {
      console.log("Auto-routing attivo: Profilo Docente rilevato -> Apertura diretta Modalità Classe LIM.");
      if (window.App) window.App.showClasseViewDirect();
    } else {
      // Default: Mostra schermata di benvenuto/selezione
      if (window.App) window.App.showWelcomeView();
    }
  },

  logout: function () {
    if (window.fbAuth) {
      window.fbAuth.signOut();
    }
    localStorage.removeItem('pm_oratore_user');
    this.role = 'guest';
    this.plan = 'base';
    this.name = 'Ospite';
    this.routeUser();
  },

  // Demo Switcher per testare comodamente i ruoli senza login esterno
  setSimulatedRole: function (newRole, newPlan) {
    this.role = newRole;
    this.plan = newPlan;
    this.name = newRole === 'viandante' ? 'Marco (Viandante)' : 'Prof. Rossi';
    this.saveSession();
    this.updateUI();
    this.routeUser();
  }
};
