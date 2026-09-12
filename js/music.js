/**
 * L'ORATORE - Audio & Music Player System
 * WebAudio synthesizer for low-latency SFX + 15 Tracks Background Music Player
 */

const AudioEngine = {
  ctx: null,
  isMuted: false,
  isPlayingMusic: false,
  currentTrackIndex: 0,
  audioEl: null,

  tracks: [
    { title: "Aventure - Close Friends", src: "assets/audio/Aventure - Close Friends (freetouse.com).mp3" },
    { title: "Burgundy - Chances", src: "assets/audio/Burgundy - Chances (freetouse.com).mp3" },
    { title: "Epic Spectrum - Forgiveness", src: "assets/audio/Epic Spectrum - Forgiveness (freetouse.com).mp3" },
    { title: "Hazelwood - At Ease", src: "assets/audio/Hazelwood - At Ease (freetouse.com).mp3" },
    { title: "Hazelwood - Coming Of Age", src: "assets/audio/Hazelwood - Coming Of Age (freetouse.com).mp3" },
    { title: "Johny Grimes - Senseless", src: "assets/audio/Johny Grimes - Senseless (freetouse.com).mp3" },
    { title: "Nebulite - A New Day", src: "assets/audio/Nebulite - A New Day (freetouse.com).mp3" },
    { title: "Nebulite - Kyoto", src: "assets/audio/Nebulite - Kyoto (freetouse.com).mp3" },
    { title: "Nebulite - Mountain", src: "assets/audio/Nebulite - Mountain (freetouse.com).mp3" },
    { title: "Piki - 9am, meeeh", src: "assets/audio/Piki - 9am, meeeh (freetouse.com).mp3" },
    { title: "Pufino - Soaked", src: "assets/audio/Pufino - Soaked (freetouse.com).mp3" },
    { title: "Waesto - Morning", src: "assets/audio/Waesto - Morning (freetouse.com).mp3" },
    { title: "Zambolino - Smooth Place", src: "assets/audio/Zambolino - Smooth Place (freetouse.com).mp3" },
    { title: "massobeats - peach prosecco", src: "assets/audio/massobeats - peach prosecco (freetouse.com).mp3" },
    { title: "tubebackr & Filo - Morning Sun", src: "assets/audio/tubebackr & Filo Starquez - Morning Sun (freetouse.com).mp3" }
  ],

  init() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.ctx = new AudioContext();
      }
    } catch (e) {
      console.warn("AudioContext not supported");
    }

    this.audioEl = new Audio();
    this.audioEl.loop = false;
    this.audioEl.addEventListener('ended', () => this.nextTrack());
    this.updateUI();
  },

  resumeCtx() {
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  },

  playBuzzer() {
    if (this.isMuted) return;
    this.resumeCtx();
    if (!this.ctx) return;

    // Dual harsh sawtooth buzzer
    const osc1 = this.ctx.createOscillator();
    const osc2 = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc1.type = 'sawtooth';
    osc2.type = 'sawtooth';

    osc1.frequency.setValueAtTime(140, this.ctx.currentTime);
    osc2.frequency.setValueAtTime(148, this.ctx.currentTime);

    gain.gain.setValueAtTime(0.3, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.35);

    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(this.ctx.destination);

    osc1.start();
    osc2.start();
    osc1.stop(this.ctx.currentTime + 0.35);
    osc2.stop(this.ctx.currentTime + 0.35);
  },

  playChime() {
    if (this.isMuted) return;
    this.resumeCtx();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(587.33, this.ctx.currentTime); // D5
    osc.frequency.setValueAtTime(880.00, this.ctx.currentTime + 0.1); // A5

    gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.4);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.4);
  },

  playTick() {
    if (this.isMuted) return;
    this.resumeCtx();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(800, this.ctx.currentTime);

    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.05);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.05);
  },

  playFanfare() {
    if (this.isMuted) return;
    this.resumeCtx();
    if (!this.ctx) return;

    const notes = [523.25, 659.25, 783.99, 1046.50];
    notes.forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime + idx * 0.12);

      gain.gain.setValueAtTime(0.25, this.ctx.currentTime + idx * 0.12);
      gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + idx * 0.12 + 0.35);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(this.ctx.currentTime + idx * 0.12);
      osc.stop(this.ctx.currentTime + idx * 0.12 + 0.35);
    });
  },

  togglePlay() {
    this.resumeCtx();
    this.isPlayingMusic = !this.isPlayingMusic;
    if (this.isPlayingMusic) {
      this.playCurrentTrack();
    } else {
      if (this.audioEl) this.audioEl.pause();
    }
    this.updateUI();
  },

  playCurrentTrack() {
    const track = this.tracks[this.currentTrackIndex];
    if (this.audioEl && track) {
      this.audioEl.src = track.src;
      this.audioEl.play().catch(() => {
        console.log("Audio autoplay prevented by browser policy");
      });
    }
    this.updateUI();
  },

  nextTrack() {
    this.currentTrackIndex = (this.currentTrackIndex + 1) % this.tracks.length;
    if (this.isPlayingMusic) {
      this.playCurrentTrack();
    } else {
      this.updateUI();
    }
  },

  prevTrack() {
    this.currentTrackIndex = (this.currentTrackIndex - 1 + this.tracks.length) % this.tracks.length;
    if (this.isPlayingMusic) {
      this.playCurrentTrack();
    } else {
      this.updateUI();
    }
  },

  toggleMute() {
    this.isMuted = !this.isMuted;
    if (this.audioEl) {
      this.audioEl.muted = this.isMuted;
    }
    this.updateUI();
  },

  updateUI() {
    const titleEl = document.getElementById('music-track-title');
    const playBtn = document.getElementById('music-play-btn');
    const muteToggleBtn = document.getElementById('music-mute-toggle-btn');

    if (titleEl && this.tracks[this.currentTrackIndex]) {
      titleEl.textContent = this.tracks[this.currentTrackIndex].title;
    }
    if (playBtn) {
      playBtn.innerHTML = this.isPlayingMusic 
        ? '<i class="fa-solid fa-pause"></i>' 
        : '<i class="fa-solid fa-play"></i>';
    }
    if (muteToggleBtn) {
      muteToggleBtn.innerHTML = this.isMuted
        ? '<i class="fa-solid fa-volume-xmark"></i> Attiva Musica'
        : '<i class="fa-solid fa-volume-high"></i> Disattiva Musica';
    }
  }
};

window.AudioEngine = AudioEngine;
