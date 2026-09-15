/**
 * L'ORATORE - Board & Pawns Engine (25 Cells HD)
 * Manages 25-cell snake track, pawn coordinates, step-by-step animations, and special tiles
 */

const BoardEngine = {
  totalCells: 24,
  specialTiles: {
    6: { type: "PESCA_CARTA", label: "Canna da Pesca", icon: "🎣", desc: "Hai pescato un bonus: +30s nel tuo prossimo discorso!" },
    12: { type: "CHECKPOINT", label: "Punto di Controllo", icon: "📍", desc: "Traguardo intermedio: la squadra ha superato la prima metà del percorso!" },
    18: { type: "PEDINA_BONUS", label: "Mossa del Cavallo", icon: "♟️", desc: "Scacco al tabellone: balzo immediato alla casella 19!" },
    21: { type: "TEMPO_X2", label: "Super Raddoppio", icon: "✖️2", desc: "Super Raddoppio: i passi del tuo prossimo discorso valgono doppio!" },
    24: { type: "TRAGUARDO", label: "Traguardo 24", icon: "🏆", desc: "Vittoria Finale della Partita!" }
  },

  // Coordinate percentuali esatte per le 24 caselle reali sul tracciato grafico di assets/tabellone/1.png (1920x1080)
  coordinates: [
    { x: 13.28, y: 13.06 }, // 1: START (col 1, row 1)
    { x: 13.28, y: 27.59 }, // 2: (col 1, row 2)
    { x: 21.46, y: 27.59 }, // 3: (col 2, row 2)
    { x: 29.64, y: 27.59 }, // 4: (col 3, row 2)
    { x: 29.64, y: 13.06 }, // 5: (col 3, row 1)
    { x: 37.81, y: 13.06 }, // 6: Canna da pesca (col 4, row 1)
    { x: 45.99, y: 13.06 }, // 7: (col 5, row 1)
    { x: 45.99, y: 27.59 }, // 8: (col 5, row 2)
    { x: 45.99, y: 42.13 }, // 9: (col 5, row 3)
    { x: 45.99, y: 56.67 }, // 10: (col 5, row 4)
    { x: 37.81, y: 56.67 }, // 11: (col 4, row 4)
    { x: 29.64, y: 56.67 }, // 12: Segnaposto (col 3, row 4)
    { x: 21.46, y: 56.67 }, // 13: (col 2, row 4)
    { x: 21.46, y: 71.20 }, // 14: (col 2, row 5)
    { x: 21.46, y: 85.74 }, // 15: (col 2, row 6)
    { x: 29.64, y: 85.74 }, // 16: (col 3, row 6)
    { x: 37.81, y: 85.74 }, // 17: (col 4, row 6)
    { x: 45.99, y: 85.74 }, // 18: Pedina scacchi (col 5, row 6)
    { x: 54.17, y: 85.74 }, // 19: (col 6, row 6)
    { x: 62.34, y: 85.74 }, // 20: (col 7, row 6)
    { x: 70.52, y: 85.74 }, // 21: x2 (col 8, row 6)
    { x: 78.70, y: 85.74 }, // 22: (col 9, row 6)
    { x: 78.70, y: 71.20 }, // 23: (col 9, row 5)
    { x: 78.70, y: 56.67 }  // 24: TRAGUARDO FINALE (col 9, row 4)
  ],

  renderPawns(teams) {
    const layer = document.getElementById('pawns-layer');
    if (!layer) return;

    layer.innerHTML = '';
    if (!teams || teams.length === 0) return;

    teams.forEach((team, idx) => {
      const pos = Math.max(1, Math.min(this.totalCells, team.position || 1));
      const coord = this.coordinates[pos - 1] || { x: 10, y: 88 };

      const offsetX = (idx % 2 === 0 ? -1 : 1) * (idx > 1 ? 8 : 4);
      const offsetY = (idx < 2 ? -1 : 1) * 6;

      const pawnEl = document.createElement('div');
      pawnEl.className = 'board-pawn';
      pawnEl.id = `pawn-team-${team.id}`;
      pawnEl.style.left = `calc(${coord.x}% + ${offsetX}px)`;
      pawnEl.style.top = `calc(${coord.y}% + ${offsetY}px)`;
      pawnEl.style.borderColor = team.color || '#fff';
      pawnEl.title = `${team.name} (Casella ${pos})`;
      pawnEl.innerHTML = `<img src="${team.avatar}" alt="${team.name}" style="width:100%; height:100%; border-radius:50%; object-fit:cover; display:block;">`;

      layer.appendChild(pawnEl);
    });
  },

  animatePawnStepByStep(teamId, fromPos, toPos, callback) {
    const pawn = document.getElementById(`pawn-team-${teamId}`);
    if (!pawn || fromPos === toPos) {
      if (callback) callback();
      return;
    }

    const direction = toPos > fromPos ? 1 : -1;
    let current = fromPos;

    const stepInterval = setInterval(() => {
      current += direction;
      const clamped = Math.max(1, Math.min(this.totalCells, current));
      const coord = this.coordinates[clamped - 1];

      pawn.style.transform = 'translate(-50%, -50%) scale(1.3)';
      pawn.style.left = `${coord.x}%`;
      pawn.style.top = `${coord.y}%`;

      if (window.AudioEngine && window.AudioEngine.playTick) {
        window.AudioEngine.playTick();
      }

      if (current === toPos) {
        clearInterval(stepInterval);
        setTimeout(() => {
          pawn.style.transform = 'translate(-50%, -50%) scale(1)';
          if (callback) callback();
        }, 300);
      }
    }, 280);
  }
};

window.BoardEngine = BoardEngine;
