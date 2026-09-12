/**
 * Prof. Memmo — Firebase Init & Ecosystem Auth
 * L'Oratore
 */

(function () {
  'use strict';

  // Configurazione Firebase Centrale Unificato Prof. Memmo (prof-memmo-hub)
  const firebaseConfig = {
    apiKey: "AIzaSyD-n2m-kYEuzGXPMKclZTggf4Y5Zm8_cdM",
    authDomain: "prof-memmo-hub.firebaseapp.com",
    projectId: "prof-memmo-hub",
    storageBucket: "prof-memmo-hub.firebasestorage.app",
    messagingSenderId: "839149485689",
    appId: "1:839149485689:web:04ee4fa6237d94d0b71ea8"
  };

  if (typeof firebase !== 'undefined' && !firebase.apps.length) {
    try {
      firebase.initializeApp(firebaseConfig);
      window.fbAuth = firebase.auth();
      window.fbDb = firebase.firestore();
      console.log("Firebase Ecosistema Prof. Memmo inizializzato con successo.");
    } catch (e) {
      console.warn("Inizializzazione Firebase in modalità fallback locale:", e);
    }
  }
})();
