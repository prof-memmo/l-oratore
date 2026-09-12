/**
 * Prof. Memmo — Session & Auto-Routing Manager
 * L'Oratore
 */

window.Auth = {
  user: null,
  role: 'guest', // 'viandante' | 'docente' | 'studente' | 'admin' | 'guest'
  plan: 'base',  // 'viandante' | 'docente_didattico' | 'docente_ecosistema' | 'base'
  name: 'Prof. Memmo',
  avatar: 'https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/6.png',
  xp: 150,

  getSafeAvatarUrl: function (avatar, isSuperAdmin) {
    const defaultAvatar = 'https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/6.png';
    if (isSuperAdmin && (!avatar || avatar === '1' || avatar === 'assets/avatars/1.png' || avatar === 'assets/pedine/1.png' || String(avatar).includes('1.png'))) {
      return defaultAvatar;
    }
    if (!avatar) return defaultAvatar;
    const aStr = String(avatar).trim();
    if (!aStr || aStr === 'null' || aStr === 'undefined' || aStr === 'default') return defaultAvatar;
    if (aStr.startsWith('http://') || aStr.startsWith('https://') || aStr.startsWith('data:')) return aStr;
    if (/^\d+$/.test(aStr)) return `https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/${aStr}.png`;
    if (aStr.startsWith('assets/avatars/')) return `https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/${aStr}`;
    if (aStr.startsWith('shared/')) return `https://prof-memmo.github.io/prof-memmo-gestione-siti/${aStr}`;
    if (aStr.includes('.png') || aStr.includes('.jpg') || aStr.includes('.jpeg') || aStr.includes('.webp')) {
      const cleanName = aStr.split('/').pop();
      return `https://prof-memmo.github.io/prof-memmo-gestione-siti/shared/assets/avatars/${cleanName}`;
    }
    return defaultAvatar;
  },

  init: async function () {
    // 1. Check local session storage first
    const cachedUser = localStorage.getItem('pm_oratore_user');
    if (cachedUser) {
      try {
        const parsed = JSON.parse(cachedUser);
        this.user = parsed;
        this.role = parsed.role || 'guest';
        this.plan = parsed.plan || 'base';
        this.name = parsed.name || 'Prof. Memmo';
        const isSuperAdmin = (this.role === 'admin' || (parsed.email && parsed.email.toLowerCase() === 'prof.memmo@gmail.com'));
        this.avatar = this.getSafeAvatarUrl(parsed.avatar, isSuperAdmin);
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
    const email = fbUser.email ? fbUser.email.toLowerCase() : '';
    const isSuperAdmin = (email === 'prof.memmo@gmail.com');
    this.user = fbUser;
    this.name = isSuperAdmin ? 'Prof. Memmo' : (fbUser.displayName || fbUser.email.split('@')[0]);

    try {
      if (window.fbDb) {
        const doc = await window.fbDb.collection('hub_users').doc(fbUser.uid).get();
        if (doc.exists) {
          const data = doc.data() || {};
          this.role = (data.role === 'admin' || isSuperAdmin) ? 'admin' : (data.role || 'studente');
          this.plan = data.subscription || data.abbonamento || (isSuperAdmin ? 'docente_ecosistema' : 'base');
          if (data.anagrafica && data.anagrafica.nome) {
            this.name = data.anagrafica.nome;
          }
          const rawAvatar = data.avatar || (data.anagrafica && data.anagrafica.avatar) || fbUser.photoURL || '';
          this.avatar = this.getSafeAvatarUrl(rawAvatar, isSuperAdmin);
        } else {
          this.role = isSuperAdmin ? 'admin' : 'studente';
          this.plan = isSuperAdmin ? 'docente_ecosistema' : 'base';
          this.avatar = this.getSafeAvatarUrl('', isSuperAdmin);
        }
      }
    } catch (e) {
      console.warn("Lettura profilo hub_users in fallback:", e);
      if (isSuperAdmin) {
        this.role = 'admin';
        this.plan = 'docente_ecosistema';
        this.avatar = this.getSafeAvatarUrl('', true);
      }
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
    const isSuperAdmin = (this.user && this.user.email && this.user.email.toLowerCase() === 'prof.memmo@gmail.com') || (this.role === 'admin');
    const safeAvatar = this.getSafeAvatarUrl(this.avatar, isSuperAdmin);
    this.avatar = safeAvatar;

    const nameEl = document.getElementById('header-user-name');
    const roleEl = document.getElementById('header-user-role');
    const roleSubEl = document.getElementById('dropdown-user-role-sub');
    const avatarEl = document.getElementById('header-user-avatar');
    const xpEl = document.getElementById('dropdown-user-xp');

    if (nameEl) nameEl.textContent = this.name.toUpperCase();
    const roleLabel = (this.role === 'admin' ? 'AMMINISTRATORE' : (this.role === 'docente' ? 'DOCENTE' : (this.role === 'viandante' ? 'VIANDANTE' : 'STUDENTE')));
    if (roleEl) roleEl.textContent = roleLabel;
    if (roleSubEl) roleSubEl.textContent = roleLabel;
    if (avatarEl) avatarEl.src = safeAvatar;
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
