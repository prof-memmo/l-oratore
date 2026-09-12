/**
 * Prof. Memmo — Firebase Init & Ecosystem Auth
 * L'Oratore
 */

(function () {
  'use strict';

  // Configurazione Firebase compatibile con l'Ecosistema Prof. Memmo
  const firebaseConfig = {
    apiKey: "AIzaSyD-sample-placeholder-key",
    authDomain: "prof-memmo.firebaseapp.com",
    projectId: "prof-memmo",
    storageBucket: "prof-memmo.appspot.com",
    messagingSenderId: "1234567890",
    appId: "1:1234567890:web:abcdef123456"
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
