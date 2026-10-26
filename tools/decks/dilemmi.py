# Mazzo: dilemmi
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            'Il vaso di fiori rotto',
            'Giocando a palla in salotto hai rotto il vaso preferito della nonna. Devi decidere se confessare subito o dare la colpa al gatto.',
            ['Vaso', 'Gatto', 'Rotto', 'Bugia', 'Nonna'],
            ['Confessione', 'Sincerità', 'Scusa', 'Riparare', 'Coraggio']
        ),
        (
            'La moneta trovata sotto il banco',
            "Trovi una moneta da due euro sul pavimento dell'aula. Decidi se tenerla per comprare le caramelle o portarla alla maestra.",
            ['Soldi', 'Due euro', 'Tasca', 'Caramelle', 'Mio'],
            ['Proprietario', 'Restituire', 'Onestà', 'Maestra', 'Fiducia']
        ),
        (
            "L'ultimo biscotto al cioccolato",
            'È rimasto un solo biscotto nel piatto e anche il tuo fratellino lo desidera. Spiega perché lasciarlo a lui ti fa sentire più felice.',
            ['Biscotto', 'Cioccolato', 'Fame', 'Mio', 'Fratello'],
            ['Generosità', 'Rinuncia', 'Sorriso', 'Affetto', 'Dividere']
        ),
        (
            "L'amico nuovo o il compagno di sempre",
            "C'è un bambino nuovo da solo e il tuo migliore amico vuole giocare solo con te. Spiega come fare spazio a tutti e due.",
            ['Amico', 'Nuovo', 'Solo', 'Gelosia', 'Scegliere'],
            ['Inclusione', 'Accoglienza', 'Trio', 'Compagnia', 'Insieme']
        ),
        (
            'La promessa di non dire il nascondiglio',
            "Nel gioco a nascondino un compagno ti chiede dove si è nascosto l'altro. Decidi se mantenere il segreto del gioco o fare la spia.",
            ['Nascondiglio', 'Spia', 'Dire', 'Cercare', 'Vincere'],
            ['Fedeltà', 'Patto', 'Lealtà', 'Gioco pulito', 'Silenzio']
        ),
        (
            'Il disegno più bello ma non tuo',
            "La maestra loda un disegno sul banco pensando sia tuo, ma l'ha fatto il tuo vicino. Trova le parole per dare il merito al vero autore.",
            ['Disegno', 'Bravo', 'Maestra', 'Mio', 'Lode'],
            ['Verità', 'Merito', 'Compagno', 'Onestà', 'Riconoscimento']
        ),
        (
            'La fila per lo scivolo',
            "Hai fretta di salire sullo scivolo prima che suoni la campanella, ma c'è una fila ordinata. Spiega perché non devi saltare il turno.",
            ['Scivolo', 'Saltare', 'Primo', 'Fretta', 'Spingere'],
            ['Turno', 'Pazienza', 'Rispetto', 'Regola', 'Ordine']
        ),
        (
            'Il giocattolo prestato e rovinato',
            'Hai rovinato senza volerlo la macchinina prestata da un compagno. Spiega come dirglielo con dolcezza offrendo un tuo gioco in cambio.',
            ['Macchinina', 'Rotta', 'Prestato', 'Paura', 'Nascondere'],
            ['Incidente', 'Scusa', 'Rimedio', 'Scambio', 'Amicizia']
        ),
        (
            'Mangiare la verdura o dire una bugia',
            'Non vuoi finire i fagiolini nel piatto. Decidi se dire alla mamma che non ti piacciono con sincerità o nasconderli nel tovagliolo.',
            ['Verdura', 'Fagiolini', 'Schifo', 'Nascondere', 'Tovagliolo'],
            ['Franchezza', 'Gusto', 'Assaggio', 'Dialogo', 'Sincerità']
        ),
        (
            'Il segreto dello scherzo fatto al compagno',
            'Tutti ridono per uno scherzo pesante a un bambino timido. Scegli se unirti alle risate o dire che lo scherzo non è divertente.',
            ['Ridere', 'Scherzo', 'Tutti', 'Bullo', 'Presa in giro'],
            ['Fermarsi', 'Sensibilità', 'Difesa', 'Coraggio', 'Rispetto']
        ),
        (
            'Prestare i pennarelli nuovi',
            'Hai una scatola di pennarelli profumati appena comprata. Un compagno senza colori te li chiede: scegli se tenerli perfetti o condividerli.',
            ['Pennarelli', 'Profumo', 'Nuovi', 'Miei', 'Rovinare'],
            ['Condivisione', 'Generosità', 'Cura', 'Amicizia', 'Uso comune']
        ),
        (
            'La figurina doppia promessa a due amici',
            'Hai una figurina rara che serve a due compagni diversi. Trova un modo giusto e trasparente per decidere a chi darla senza litigi.',
            ['Figurina', 'Rara', 'Doppia', 'Litigare', 'Promessa'],
            ['Equità', 'Trasparenza', 'Sorteggio', 'Accordo', 'Amicizia']
        ),
        (
            'Dire che sei stato tu a far cadere la colla',
            'Il pavimento è pieno di colla appiccicosa e la maestra è severa. Scegli se fare un passo avanti e prenderti la responsabilità.',
            ['Colla', 'Punizione', 'Urlare', 'Chi è stato', 'Zitto'],
            ['Responsabilità', 'Passo avanti', 'Fermezza', 'Onestà', 'Rimedio']
        ),
        (
            'Il compagno che fa fatica a correre',
            'Durante la staffetta il tuo compagno zoppica e la squadra rischia di perdere. Decidi se incoraggiarlo con calore o arrabbiarti.',
            ['Staffetta', 'Perdere', 'Lento', 'Arrabbiarsi', 'Corsa'],
            ['Incoraggiamento', 'Spirito di squadra', 'Sostegno', 'Comprensione', 'Insieme']
        ),
        (
            'Il libro strappato per distrazione',
            'Voltando la pagina di fretta hai fatto uno strappo sul libro della biblioteca. Decidi se incollarlo subito e dirlo alla bibliotecaria.',
            ['Libro', 'Strappo', 'Biblioteca', 'Nascondere', 'Scaffale'],
            ['Nastro adesivo', 'Cura', 'Segnalazione', 'Riparazione', 'Sincerità']
        ),
        (
            'Il segreto confidato dalla sorellina',
            'La sorellina ti ha detto che vuole arrampicarsi su un muretto pericoloso. Scegli se avvisare i genitori rompendo il patto per proteggerla.',
            ['Muretto', 'Cadere', 'Genitori', 'Spia', 'Segreto'],
            ['Protezione', 'Sicurezza', 'Prudenza', 'Affetto', 'Salute']
        ),
        (
            'Dividere la torta di compleanno',
            'Tocca a te tagliare le fette: decidi se fare una fetta gigante per te o fare tutte le porzioni identiche per gli invitati.',
            ['Torta', 'Fetta', 'Grande', 'Festa', 'Mangiare'],
            ['Uguaglianza', 'Porzione equa', 'Ospiti', 'Equità', 'Festa']
        ),
        (
            'Aiutare chi non ti ha aiutato prima',
            'Un compagno che ieri non ti ha passato la palla oggi ti chiede una matita. Decidi se vendicarti o essere generoso dimostrando maturità.',
            ['Vendetta', 'Ieri', 'Matita', 'Cattivo', 'Rivalersi'],
            ['Superamento', 'Generosità', 'Lezione positiva', 'Apertura', 'Bontà']
        ),
        (
            'Il temporale e il cucciolo fuori',
            "Hai paura del buio ma senti il gattino dei vicini che miagola sotto il diluvio. Trova il coraggio di uscire con l'ombrello per soccorrerlo.",
            ['Gatto', 'Pioggia', 'Buio', 'Paura', 'Letto'],
            ['Soccorso', 'Ombrello', 'Coraggio', 'Protezione', 'Compassione']
        ),
        (
            'Dire di no al capo del gruppo',
            'Il bambino più popolare dice a tutti di non parlare con un compagno nuovo. Trova la voce ferma per rifiutare questo ordine ingiusto.',
            ['Capo', 'Non parlare', 'Nuovo', 'Popolare', 'Paura'],
            ['Disobbedienza giusta', 'Voce libera', 'Autonomia', 'Giustizia', 'Accoglienza']
        ),
    ],
    "a2": [
        (
            'Copiare la risposta difficile per prendere dieci',
            "Durante la verifica di matematica, il foglio del compagno bravissimo è scoperto davanti ai tuoi occhi. Scegli l'onestà del tuo voto.",
            ['Copiare', 'Dieci', 'Matematica', 'Guardare', 'Voto'],
            ['Onestà intellettuale', 'Farina del mio sacco', 'Verità del voto', 'Autostima', 'Impegno']
        ),
        (
            "Difendere l'amico colpevole o dire la verità?",
            'Il tuo migliore amico ha lanciato un gessetto rompendo la lavagna interattiva. La maestra chiede chi sia stato minacciando punizioni collettive.',
            ['Gessetto', 'Spia', 'Lavagna', 'Punizione per tutti', 'Amico'],
            ['Verità liberatoria', 'Responsabilità personale', 'Integrità', 'Consiglio leale', 'Giustizia']
        ),
        (
            "Il fallo non visto dall'arbitro in finale",
            "Hai toccato la palla di mano segnando il goal della vittoria ma l'arbitro non se n'è accorto. Decidi se confessare il tocco all'arbitro.",
            ['Mano', 'Goal', 'Arbitro', 'Vincere', 'Coppa'],
            ['Fair play', 'Autodenuncia sportiva', 'Lealtà assoluta', 'Onore sportivo', 'Spirito olimpico']
        ),
        (
            'Il compagno emarginato alla festa di compleanno',
            'Festeggi il compleanno a casa. La tua cerchia ristretta non vuole invitare il compagno con difficoltà relazionali. Prendi posizione.',
            ['Festa', 'Invito', 'Cerchia', 'Strano', 'Escludere'],
            ["Diritto d'invito", 'Accoglienza integrale', 'Coraggio civico', 'Inclusione autentica', 'Festa di tutti']
        ),
        (
            'Mantenere un segreto pericoloso: la fuga da scuola',
            'Un amico ti confida che vuole scappare dal cortile durante la ricreazione per fare una bravata. Scegli se fermarlo con la forza o dirlo ai docenti.',
            ['Fuga', 'Cortile', 'Bravata', 'Spia', 'Segreto'],
            ['Incolumità personale', 'Prevenzione del pericolo', 'Responsabilità matura', 'Intervento urgente', 'Vera protezione']
        ),
        (
            'Trovare un portafoglio pieno di banconote',
            "Trovi un portafoglio con documenti e centocinquanta euro vicino alla biblioteca. Decidi di consegnarlo alle forze dell'ordine senza toccare nulla.",
            ['Portafoglio', 'Soldi', 'Tasca', 'Comprare', 'Nessuno vede'],
            ['Consegna integrale', 'Restituzione civile', 'Senso del dovere', 'Onestà indiscutibile', 'Riconoscenza del proprietario']
        ),
        (
            'Il dilemma della lealtà verso il gruppo dei pari',
            'Il gruppo decide di boicottare la lezione del professore facendo rumore continuo. Scegli se aggregarti per non essere emarginato o dissociarti.',
            ['Branco', 'Gruppo', 'Professore', 'Casino', 'Paura di restare solo'],
            ['Dissociazione critica', "Rispetto dell'insegnamento", 'Autonomia di giudizio', 'Libertà morale', 'Fermezza']
        ),
        (
            'Il vestito strappato della sorella maggiore',
            "Hai preso in prestito di nascosto la giacca di tua sorella e l'hai macchiata indelebilmente. Confessa subito l'uso non autorizzato.",
            ['Giacca', 'Sorella', 'Macchia', 'Nascosto', 'Armadio'],
            ['Assunzione di colpa', "Rispetto dell'altrui proprietà", "Riconoscimento dell'errore", 'Riparazione economica', 'Scuse sincere']
        ),
        (
            'La vittoria della squadra avversaria meritata sul campo',
            'Avete perso la finale per un punto contro una squadra che ha giocato magnificamente. Guida i tuoi compagni ad applaudire i vincitori.',
            ['Perso', 'Rabbia', 'Arbitro corrotto', 'Coppa', 'Piangere'],
            ['Riconoscimento del merito', 'Applauso leale', 'Sportività autentica', 'Accettazione della sconfitta', 'Onore agli avversari']
        ),
        (
            "L'animale randagio ferito sulla strada",
            'Stai correndo per non perdere la lezione di nuoto ma trovi un gattino con la zampa rotta. Scegli se fermarti per soccorrerlo perdendo la gara.',
            ['Nuoto', 'Gara', 'Tardi', 'Gatto', 'Zampa'],
            ['Priorità della vita', 'Soccorso immediato', 'Compassione attiva', 'Rinuncia al primato', "Cura dell'inerme"]
        ),
        (
            'Il premio del concorso letterario e il dubbio sul plagio',
            'Hai scritto una favola magnifica che vince il primo premio, ma ricordi di esserti ispirato troppo a un vecchio libro letto da piccolo. Chiari il dubbio.',
            ['Premio', 'Vinto', 'Plagio', 'Copiato', 'Silenzio'],
            ['Trasparenza intellettuale', 'Ispirazione leale', 'Verifica delle fonti', "Onestà dell'autore", 'Rettitudine']
        ),
        (
            'La rivelazione di un voto sbagliato a tuo favore',
            "Il docente si è confuso e ti ha segnato nove anziché sei sul registro elettronico. Vai alla cattedra per correggere l'errore a tuo svantaggio.",
            ['Errore', 'Nove', 'Registro', 'Silenzio', 'Fortuna'],
            ['Correzione doverosa', 'Incorruttibilità morale', 'Verità della valutazione', 'Stima del docente', 'Coscienza pulita']
        ),
        (
            'La donazione della paghetta per la raccolta fondi',
            'Avevi risparmiato per mesi per comprare un videogame. A scuola organizzano una colletta per i terremotati: decidi di donare i tuoi risparmi.',
            ['Videogame', 'Paghetta', 'Risparmi', 'Miei', 'Comprare'],
            ['Solidarietà operosa', 'Donazione disinteressata', 'Sostegno alle vittime', 'Altruismo concreto', 'Valore umano']
        ),
        (
            'Prendere posizione contro il cyber-derisione anonima',
            'In un gruppo classe viene diffuso un fotomontaggio umiliante di un compagno. Prendi la parola pubblicamente per chiedere la rimozione immediata.',
            ['Fotomontaggio', 'Ridere', 'Chat', 'Anonimo', 'Vergogna'],
            ['Denuncia pubblica', 'Solidarietà alla vittima', 'Decoro digitale', 'Fermare la violenza', 'Responsabilità di gruppo']
        ),
        (
            'La cura del parco abbandonato invece dei compiti facili',
            "Il sabato pomeriggio puoi scegliere se giocare al computer o unirti ai volontari che puliscono la pineta della città. Scegli l'impegno civico.",
            ['Sabato', 'Computer', 'Dormire', 'Spazzatura', 'Volontari'],
            ['Impegno civico', 'Cura del territorio', 'Cittadinanza attiva', 'Lavoro condiviso', 'Bellezza pubblica']
        ),
        (
            'Il patto tra fratelli di fronte al rimprovero dei genitori',
            'Tuo fratello ha commesso una sciocchezza e i genitori sospettano di entrambi. Spiega come aiutarlo a dire la verità senza fare la spia.',
            ['Genitori', 'Punizione', 'Fratello', 'Colpa', 'Spia'],
            ['Accompagnamento fraterno', "Aiuto all'ammissione", 'Verità liberatoria', 'Pace familiare', 'Maturazione congiunta']
        ),
        (
            "L'accoglienza dello studente straniero a casa",
            'La tua famiglia ha abitudini rigide. Convinci i tuoi genitori a ospitare per il fine settimana un compagno appena arrivato da un paese in guerra.',
            ['Straniero', 'Casa nostra', 'Abitudini', 'Guerra', 'Ospiti'],
            ['Ospitalità concreta', "Apertura all'alterità", 'Condivisione domestica', 'Ponte interculturale', 'Calore umano']
        ),
        (
            'La rinuncia al ruolo da protagonista nella recita',
            'Sei stato scelto come protagonista, ma un tuo compagno timido ha un talento incredibile e sognava quella parte. Proponi di cedere la scena.',
            ['Protagonista', 'Recita', 'Mio', 'Applausi', 'Cedere'],
            ['Generosità di palco', "Valorizzazione dell'altro", 'Umiltà artistica', "Donazione dell'opportunità", 'Squadra teatrale']
        ),
        (
            "Il silenzio di fronte a un insulto per spezzare l'odio",
            'Un compagno ti urla una provocazione volgare in corridoio. Scegli di non rispondere con la violenza, disarmandolo con uno sguardo sereno e fermo.',
            ['Insulto', 'Pugno', 'Rivalersi', 'Urlare', 'Faccia'],
            ['Risposta disarmante', 'Fermezza nonviolenta', 'Spezzare la catena', "Superamento dell'ira", 'Dignità sovrana']
        ),
        (
            "Il manifesto dell'onestà quotidiana",
            "Concludi il percorso con un'orazione sull'integrità morale: fare la cosa giusta anche e soprattutto quando nessuno ci sta guardando.",
            ['Nessuno vede', 'Furbizia', 'Regole', 'Nascondersi', 'Vantaggio'],
            ['Integrità morale', 'Coscienza interiore', 'Azione disinteressata', 'Rettitudine quotidiana', 'Dignità della persona']
        ),
    ],
    "b1": [
        (
            "Il dilemma del testimone nell'atto vandalico",
            'Hai visto chiaramente due compagni distruggere i distributori automatici della scuola. Se parli sarai etichettato come traditore; se taci pagherà tutta la scuola.',
            ['Spia', 'Traditore', 'Distributori', 'Tutti pagano', 'Preside'],
            ['Omertà versus legalità', 'Responsabilità comunitaria', 'Rifiuto della complicità', 'Coraggio civile', 'Tutela della scuola']
        ),
        (
            'La divulgazione non consensuale di foto intime (Revenge Porn)',
            'Un amico ti mostra una foto intima ricevuta da una coetanea e vuole inoltrarla. Fermalo con parole irrevocabili sul reato e sulla devastazione morale.',
            ['Foto intima', 'Inoltrare', 'Ridere', 'Giro', 'Chat'],
            ["Violazione dell'intimità", 'Reato penale di revenge porn', 'Distruzione biografica', 'Inviolabilità della persona', 'Interruzione immediata']
        ),
        (
            "La scelta tra l'allenamento decisivo e l'assistenza al parente malato",
            'Sei il capitano della squadra prima della finale regionale, ma tuo nonno ricoverato chiede la tua presenza al suo capezzale. Pondera la priorità.',
            ['Finale', 'Partita', 'Coppa', 'Ospedale', 'Nonno'],
            ['Gerarchia degli affetti', 'Priorità esistenziale', 'Dovere filiale', 'Presenza insostituibile', 'Maturità della scelta']
        ),
        (
            "Il dilemma dell'autoriciclaggio di un testo premiato",
            "Hai la possibilità di presentare lo stesso saggio già premiato in un altro concorso con montepremi in denaro dove il regolamento è ambiguo. Scegli l'etica.",
            ['Concorso', 'Soldi', 'Testo vecchio', 'Regolamento', 'Furbizia'],
            ['Etica della ricerca', 'Originalità autoriale', 'Lealtà verso i concorrenti', 'Integrità artistica', 'Trasparenza']
        ),
        (
            'La difesa del docente ingiustamente diffamato sui social',
            "Gli studenti hanno creato un profilo anonimo per ridicolizzare un professore esigente ma onesto. Prendi le sue difese nell'assemblea di istituto.",
            ['Professore', 'Pagina meme', 'Insulti', 'Severo', 'Ridere'],
            ['Dignità professionale', 'Lotta alla diffamazione', 'Coraggio del dissenso', 'Stima educativa', 'Rifiuto della gogna']
        ),
        (
            'Il soccorso a un rivale ferito durante la campestre',
            "Stai per vincere la campestre provinciale quando vedi il tuo storico rivale accasciarsi con una distorsione grave. Ti fermi per soccorrerlo sacrificando l'oro.",
            ['Primo', 'Vincere', 'Medaglia', 'Cadere', 'Traguardo'],
            ['Eroismo sportivo', 'Sacrificio della vittoria', 'Soccorso al rivale', 'Valore fraterno', 'Memoria esemplare']
        ),
        (
            'Il consumo di carne e il dilemma del benessere animale',
            "Dopo aver visto un documentario sugli allevamenti intensivi, affronti la discussione familiare sulla transizione verso un'alimentazione vegetariana etica.",
            ['Carne', 'Hamburger', 'Vegetariano', 'Macello', 'Tradizione'],
            ['Zootecnia intensiva', 'Sofferenza animale', 'Consapevolezza etica', 'Scelta alimentare', 'Coerenza morale']
        ),
        (
            'La custodia di una confidenza su tendenze autolesionistiche',
            "Un'amica ti mostra tagli sulle braccia chiedendoti di giurare di non dirlo a nessuno. Rompi il giuramento per salvarle la vita rivolgendoti allo psicologo.",
            ['Giuramento', 'Tagli', 'Segreto', 'Tradire', 'Braccia'],
            ['Rottura del patto per la vita', 'Soccorso psicologico', 'Prevenzione del danno', 'Amore responsabile', 'Intervento salvifico']
        ),
        (
            'Il rifiuto di un regalo costoso da un compagno facoltoso',
            "Un compagno ricco ti regala scarpe firmate per farsi perdonare un comportamento arrogante. Rifiuta spiegando che il rispetto e l'affetto non si comprano.",
            ['Scarpe', 'Regalo', 'Soldi', 'Ricco', 'Perdonare'],
            ["Incorruttibilità dell'affetto", 'Dignità personale', 'Rifiuto del compiacimento', 'Rispetto autentico', 'Eguaglianza morale']
        ),
        (
            "L'accettazione della sconfitta per un vizio di forma non rilevato",
            'La giuria ha assegnato il premio alla tua classe ignorando che avete sforato il tempo massimo di cinque minuti. Sali sul palco e autodenunciati.',
            ['Premio', 'Tempo', 'Cinque minuti', 'Nessuno sa', 'Coppa'],
            ['Autodenuncia formale', 'Lealtà regolamentare', 'Giustizia sostanziale', 'Esemplarità civica', 'Integrità']
        ),
        (
            "La tentazione dell'antidoping nei tornei agonistici giovanili",
            'Un compagno di squadra ti propone integratori illegali per migliorare le prestazioni atletiche prima delle selezioni. Rifiuta e denuncia il fornitore.',
            ['Sostanze', 'Vincere', 'Forte', 'Integratori', 'Doping'],
            ['Rifiuto del doping', 'Tutela della salute', 'Purezza della competizione', 'Sport leale', 'Legalità agonistica']
        ),
        (
            "Il dilemma del lavoro minorile nell'acquisto di capi firmati",
            "Tutti vogliono le sneakers all'ultima moda cucite da coetanei sfruttati nel sud-est asiatico. Sostieni la scelta del boicottaggio consapevole.",
            ['Scarpe', 'Moda', 'Tutti hanno', 'Bambini poveri', 'Comprare'],
            ['Boicottaggio consapevole', 'Filiere dello sfruttamento', 'Responsabilità del consumatore', 'Dignità del lavoro', 'Scelta controcorrente']
        ),
        (
            "Il contrasto all'isolamento del compagno nello spettro autistico",
            'Durante i lavori di gruppo nessuno vuole includere il ragazzo con disabilità per timore di abbassare la media dei voti. Esigi di lavorare con lui.',
            ['Voto', 'Lavoro di gruppo', 'Disabile', 'Rallenta', 'Media'],
            ['Inclusione sostanziale', 'Ricchezza della neurodiversità', 'Cooperazione umana', 'Pari dignità', 'Valore oltre la media']
        ),
        (
            'La riparazione spontanea di un danno anonimo',
            "Camminando di sera hai urtato e rotto lo specchietto di un'auto in sosta. Non c'è nessuno: scegli di lasciare un biglietto coi tuoi recapiti.",
            ['Specchietto', 'Auto', 'Scappare', 'Nessuno vede', 'Biglietto'],
            ['Risarcimento spontaneo', 'Onestà anonima', 'Responsabilità civile', 'Senso civico', 'Rettitudine interiore']
        ),
        (
            'La rinuncia a una vacanza per aiutare la famiglia in difficoltà',
            "I tuoi genitori attraversano una crisi economica improvvisa. Rinuncia con serenità al campo estivo all'estero per non gravare sul bilancio familiare.",
            ['Campo estivo', 'Inghilterra', 'Vacanze', 'Soldi', 'Voglio andare'],
            ['Solidarietà intrafamiliare', 'Consapevolezza economica', 'Rinuncia matura', 'Adesione alle difficoltà', 'Affetto filiale']
        ),
        (
            'Il dovere di denunciare lo spaccio nei pressi della scuola',
            'Vedi persone adulte vendere sostanze ai ragazzini delle medie fuori dai cancelli. Supera la paura e rivolgiti alle autorità con senso civico.',
            ['Droga', 'Spacciatore', 'Paura', 'Polizia', 'Fatti miei'],
            ['Presidio di sicurezza', 'Protezione dei più deboli', 'Senso dello Stato', 'Resistenza alla criminalità', 'Incolumità pubblica']
        ),
        (
            "L'equità nella divisione delle mansioni domestiche",
            'I tuoi fratelli lasciano che sia sempre tua sorella o tua madre a sparecchiare e pulire la casa. Esigi la parità assoluta dei compiti domestici.',
            ['Mamma fa tutto', 'Femmine', 'Pulire', 'Sparecchiare', 'Comodo'],
            ['Parità di genere domestica', 'Condivisione del lavoro di cura', 'Superamento del patriarcato', 'Corresponsabilità', 'Giustizia familiare']
        ),
        (
            'La tutela della dignità del senza dimora davanti alla scuola',
            "Alcuni compagni lanciano insulti a un clochard che dorme sulla panchina vicina all'istituto. Intervieni per proteggerlo offrendo una bevanda calda.",
            ['Barbone', 'Puzza', 'Insulti', 'Panchina', 'Ridere'],
            ['Dignità inviolabile', "Riconoscimento dell'umanità", 'Gesto solidale', "Difesa dell'emarginato", 'Fratellanza']
        ),
        (
            'Il coraggio di confessare la perdita di un oggetto affidato',
            "Un amico ti ha affidato un orologio ricordo di suo nonno e l'hai smarrito durante un'escursione. Affronta la confessione guardandolo negli occhi.",
            ['Orologio', 'Perso', 'Nonno', 'Paura', 'Bugia'],
            ['Confessione leale', 'Sguardo limpido', 'Dolore condiviso', 'Riparazione possibile', "Profondità dell'amicizia"]
        ),
        (
            "L'appello alla Coscienza Libera",
            "Pronuncia un'orazione sull'indipendenza della bussola etica personale: la vera misura dell'uomo si vede da come sceglie nei momenti di solitudine morale.",
            ['Bussola', 'Scegliere', 'Giusto e sbagliato', 'Tutti fanno così', 'Fine'],
            ['Autonomia morale', 'Bussola della coscienza', 'Solitudine deliberativa', 'Fedeltà ai valori', 'Statura etica']
        ),
    ],
    "b2": [
        (
            'Il dilemma del carrello ferroviario (Trolley Problem)',
            "Un carrello senza freni sta per travolgere cinque operai sui binari. Puoi deviarlo su un binario secondario dove c'è un solo operaio. Analizza il bivio etico.",
            ['Carrello', 'Trolley', 'Cinque o uno', 'Leva', 'Uccidere'],
            ['Deontologia vs utilitarismo', 'Dottrina del doppio effetto', 'Calcolo felicifico benthamiano', 'Inviolabilità kantiana', 'Aporia morale']
        ),
        (
            'Il Whistleblower e la violazione del segreto aziendale',
            "Un ingegnere scopre che la sua multinazionale nasconde dati sulla tossicità cancerogena di un farmaco. Valuta il tradimento dell'accordo rispetto alla salute pubblica.",
            ['Segreto industriale', 'Contratto', 'Licenziamento', 'Farmaco', 'Silenzio'],
            ['Whistleblowing civico', "Prevalenza dell'interesse pubblico", 'Etica della responsabilità', 'Dovere testimoniale', 'Trasparenza salvifica']
        ),
        (
            'La donazione obbligatoria di organi: solidarietà o esproprio corporeo?',
            "Analizza il principio del silenzio-assenso per i trapianti: è dovere civico donare gli organi post-mortem per salvare vite o lesione dell'autodeterminazione?",
            ['Organi', 'Morte', 'Trapianto', 'Esproprio', 'Silenzio assenso'],
            ['Autodeterminazione corporea', 'Dovere di solidarietà estrema', 'Inviolabilità della salma', 'Biotecnologia salvavita', 'Patto biologico']
        ),
        (
            'La selezione degli embrioni contro malattie genetiche',
            'La diagnosi pre-impianto consente di scartare embrioni portatori di gravi patologie. Discuti il confine sottile tra prevenzione terapeutica ed eugenetica selettiva.',
            ['Embrioni', 'Malattie', 'Bambini perfetti', 'Scartare', 'DNA'],
            ['Diagnosi genetica pre-impianto', 'Eugenetica liberale', 'Tutela della vita nascente', 'Fuga dalla sofferenza', 'Confine bioetico']
        ),
        (
            "La disobbedienza civile verso la legge sull'immigrazione clandestina",
            "Un sindaco decide di fornire residenza anagrafica e cure mediche a migranti irregolari in contrasto con i decreti ministeriali. Difendi o contesta l'atto.",
            ['Sindaco', 'Decreto', 'Clandestini', 'Ubbidire alla legge', 'Prefetto'],
            ['Disobbedienza istituzionale', "Primatocostituzionale dell'uomo", 'Conflitto tra legalità e giustizia', 'Obiezione di coscienza', 'Doveri inderogabili']
        ),
        (
            'Il suicidio medicalmente assistito e la dignità del fine vita',
            'Un paziente affetto da malattia degenerativa incurabile e sofferenze intollerabili chiede di porre fine alla propria vita. Valuta le istanze di libertà e sacralità della vita.',
            ['Eutanasia', 'Morire', 'Dolore', 'Suicidio', 'Medici'],
            ['Suicidio assistito', 'Autodeterminazione terapeutica', 'Sacralità vs dignità della vita', 'Sentenza della Consulta', 'Accompagnamento palliativo']
        ),
        (
            'La sorveglianza sanitaria obbligatoria durante le pandemie',
            'Il confinamento forzato (lockdown) e il passaporto vaccinale per contenere un virus letale: fino a che punto lo Stato può comprimere le libertà individuali?',
            ['Lockdown', 'Vaccino obbligatorio', 'Libertà mia', 'Chiusi in casa', 'Virus'],
            ['Tutela della salute pubblica (Art. 32)', 'Compressione proporzionata delle libertà', 'Solidarietà epidemiologica', 'Stato di necessità sanitaria', 'Diritti inviolabili']
        ),
        (
            'La maternità surrogata (GPA): solidarietà o mercificazione del corpo?',
            'Una donna porta a termine una gravidanza per conto di una coppia sterile. Dibatti tra il diritto alla genitorialità e il divieto di mercificazione del corpo femminile.',
            ['Utero in affitto', 'Bambino comprato', 'Gravidanza', 'Genitori', 'Soldi'],
            ['Gestazione per altri (GPA)', 'Mercificazione corporale', 'Dono solidale disinteressato', 'Tutela del nascituro', 'Sfruttamento economico']
        ),
        (
            'Il diritto di sciopero nei servizi pubblici essenziali',
            'I medici o i ferrovieri che scioperano paralizzano trasporti e pronto soccorso per ottenere salari equi. Bilancia il diritto di sciopero con i diritti degli utenti.',
            ['Sciopero', 'Treni fermi', 'Ospedali chiusi', 'Disagi', 'Diritto'],
            ['Sciopero nei servizi essenziali', 'Bilanciamento dei diritti costituzionali', 'Precettazione prefettizia', 'Dignità della contrattazione', 'Garanzia dei servizi minimi']
        ),
        (
            'La prostituzione: libertà di autodeterminazione o violenza strutturale?',
            'Rifletti sulla legalizzazione del lavoro sessuale: è una libera scelta professionale su base contrattuale o la perpetuazione della subordinazione patriarcale?',
            ['Prostituzione', 'Sesso a pagamento', 'Tasse sui bordelli', 'Corpo mio', 'Clienti'],
            ['Sex work e autodeterminazione', 'Modello abolizionista nordico', 'Violenza sistemica di genere', 'Sfruttamento e vulnerabilità', 'Dignità della persona']
        ),
        (
            'La pena capitale: è mai moralmente giustificabile per crimini mostruosi?',
            "Di fronte a un genocida reo confesso di migliaia di omicidi, dimostra l'illegittimità etica e giuridica assoluta dello Stato che si fa boia omicida.",
            ['Pena di morte', 'Sedia elettrica', 'Mostro', 'Uccidere', 'Meritata'],
            ['Abolizionismo universale', 'Inviolabilità della vita dal potere statale', 'Fallacia della retribuzione sanguinaria', 'Beccaria e i Lumi', 'Rieducazione penale']
        ),
        (
            'La sperimentazione animale nella ricerca biomedica salvavita',
            'Sostanze chimiche testate su primati e roditori per sviluppare terapie oncologiche umane. Esamina il conflitto tra dovere verso la salute umana e diritti degli animali.',
            ['Animali', 'Cavie', 'Cancro', 'Laboratorio', 'Topi'],
            ['Sperimentazione animale', 'Principio delle 3R (Replacement, Reduction, Refinement)', 'Status morale dei non-umani', 'Progresso farmacologico', 'Metodi alternativi in vitro']
        ),
        (
            "La tassazione sull'eredità e la mobilità sociale",
            "Un'imposta del cinquanta per cento sulle grandi successioni patrimoniali per finanziare l'istruzione universale gratuita dei giovani privi di risorse. Dibattila.",
            ['Eredità', 'Tassa di successione', 'Soldi dei genitori', 'Stato ladro', 'Figli ricchi'],
            ['Giustizia distributiva intergenerazionale', 'Pari opportunità di partenza', 'Concentrazione dinastica del capitale', 'Meritocrazia sostanziale', 'Progressività fiscale']
        ),
        (
            "Il diritto all'armamento per legittima difesa domiciliare",
            "La legge sulla legittima difesa consente l'uso di armi da fuoco contro ladri introdottisi in casa. Analizza i pericoli della proliferazione delle armi private.",
            ['Pistola in casa', 'Sparare al ladro', 'Legittima difesa', 'Sicurezza', 'Difendersi da soli'],
            ['Monopolio statale della forza', 'Proporzionalità della difesa', 'Deriva armata sociale', 'Inviolabilità della vita', 'Stato di diritto garantista']
        ),
        (
            'La censura dei libri controversi nelle biblioteche scolastiche',
            "Gruppi di genitori chiedono di rimuovere romanzi che trattano temi sessuali o religiosi complessi. Difendi l'autonomia didattica e la libertà di lettura.",
            ['Libri vietati', 'Censura', 'Genitori arrabbiati', 'Togliere dalla biblioteca', 'Scandalo'],
            ['Libertà di espressione letteraria', 'Pluralismo formativo', "Rifiuto dell'indice dei libri proibiti", 'Pensiero critico giovanile', 'Autonomia scolastica']
        ),
        (
            "Il conflitto d'interesse del magistrato candidato politico",
            'Un pubblico ministero famoso lascia la toga per candidarsi alle elezioni politiche nel collegio in cui ha indagato. Analizza la lesione della terzietà percepita.',
            ['Magistrato', 'Politica', 'Candidarsi', 'Giudice imparziale', 'Voti'],
            ['Terzietà della giurisdizione', 'Separazione tra giustizia e politica', "Fiducia nell'ordine giudiziario", 'Imparzialità sostanziale e apparente', 'Porte girevoli']
        ),
        (
            'Il debito degli Stati verso i fondi sovrani e i sacrifici sociali',
            'Uno Stato in crisi debitoria deve tagliare pensioni e sanità per rimborsare creditori internazionali o dichiarare default selettivo a tutela del popolo?',
            ['Default', 'Debito pubblico', 'Tagli alla sanità', 'Banche', 'Pagare tutto'],
            ['Sovranità democratica del debito', 'Priorità dei diritti umani sui crediti', 'Austerità distruttiva', 'Debito odioso', 'Clausole di salvaguardia']
        ),
        (
            'Il diritto di voto ai sedicenni: maturità democratica o azzardo?',
            "Argomenta sull'abbassamento dell'età elettorale a sedici anni: riconoscimento dell'autonomia civica dei giovani o esposizione a facili derive demagogiche?",
            ['Voto a 16 anni', 'Giovani immaturi', 'Elezioni', 'Politica a scuola', 'Troppo presto'],
            ['Allargamento del suffragio', 'Rappresentanza del futuro', 'Maturità civica giovanile', 'Interessi generazionali', 'Partecipazione democratica']
        ),
        (
            'La responsabilità morale delle industrie di combustibili fossili',
            "Documenti interni dimostrano che le compagnie petrolifere conoscevano l'impatto climatico fin dagli anni settanta mentendo al pubblico. Chiedine il risarcimento.",
            ['Petrolieri', 'Bugie', 'Sapevano già', 'Soldi', 'Tribunale'],
            ['Frode climatica deliberata', 'Responsabilità civile per danni globali', 'Negazionismo organizzato', 'Riparazioni ambientali', 'Verità storica']
        ),
        (
            "Il manifesto dell'Etica Pubblica e dell'Incorruttibilità",
            "Pronuncia un'orazione di chiusura sulla fedeltà ai principi supremi: l'uomo etico preferisce subire il torto piuttosto che commetterlo.",
            ['Socrate', 'Subire il torto', 'Commettere ingiustizia', 'Furbi', 'Fine'],
            ["Primato dell'integrità", 'Massima socratica', 'Etica della testimonianza', 'Rettitudine incorruttibile', "Dignità dell'essere umano"]
        ),
    ],
    "c1": [
        (
            "L'aporia dell'imperativo categorico kantiano nel dovere di veridicità",
            "Analizza il celebre saggio di Kant Su un presunto diritto di mentire per amore dell'umanità: è lecito mentire all'assassino per salvare l'amico nascosto in casa?",
            ['Kant', "Mentire all'assassino", 'Verità sempre', 'Bugia', 'Salvare la vita'],
            ['Imperativo categorico deontologico', 'Dovere incondizionato di veridicità', 'Rigidità morale kantiana', 'Benjamin Constant e la replica', 'Etica dei doveri verso se stessi']
        ),
        (
            "L'utilitarismo della regola versus utilitarismo dell'atto in John Stuart Mill",
            "Distingui la massimizzazione contingente dell'utile nel singolo atto dalla formulazione di regole generali la cui adozione universale genera la massima felicità.",
            ['Mill', 'Utilitarismo', 'Felicità', 'Utile', 'Piacere'],
            ["Utilitarismo dell'atto vs regola", 'Calcolo felicifico qualitativo', 'Diritti morali secondari', 'Massimizzazione del benessere', 'Eudaimonia sociale']
        ),
        (
            "L'etica della responsabilità versus l'etica dell'intenzione in Max Weber",
            'Esporrai la conferenza La politica come professione: la tragica frattura tra chi agisce secondo principi puri (Gesinnung) e chi risponde delle conseguenze prevedibili (Verantwortung).',
            ['Weber', 'Intenzione', 'Responsabilità', 'Politico', 'Conseguenze'],
            ["Gesinnungsethik (etica dell'intenzione)", 'Verantwortungsethik (etica della responsabilità)', 'Patto con le potenze diaboliche', 'Tragicità della decisione politica', "Maturità dell'oratore"]
        ),
        (
            'La Genealogia della Morale di Nietzsche e la morale dei signori e degli schiavi',
            "Decostruisci l'origine storica dei concetti di buono e malvagio: come la rivolta degli schiavi nella morale abbia trasformato il risentimento impotente in dogma virtuoso.",
            ['Nietzsche', 'Morale', 'Schiavi', 'Signori', 'Risentimento'],
            ['Genealogia nietzscheana', 'Ressentiment ebraico-cristiano', 'Volontà di potenza creatrice', 'Moralina reattiva', 'Trasvalutazione di tutti i valori']
        ),
        (
            "Il dilemma della colpa tragica (Hamartia) nell'Antigone e nell'Edipo Re",
            "Indaga attraverso la Poetica di Aristotele e l'estetica hegeliana il conflitto insolubile in cui entrambe le parti in causa difendono un valore legittimo e sacro.",
            ['Hegel', 'Edipo', 'Antigone', 'Colpa', 'Destino'],
            ['Hamartia aristotelica', 'Conflitto tragico hegeliano', 'Monoliti etici contrapposti', 'Tragicità della condizione umana', 'Catarsi dello scacco']
        ),
        (
            "L'etica della cura (Care Ethics) di Carol Gilligan contro l'astrattezza maschile",
            'Presenta la critica alla scala dello sviluppo morale di Kohlberg: la giustizia basata sui diritti formali individuali ignora la trama relazionale e la cura dei legami.',
            ['Gilligan', 'Kohlberg', 'Donne', 'Cura', 'Diritti astratti'],
            ['In a Different Voice', 'Etica della cura relazionale', "Critica all'universalismo astratto", 'Vulnerabilità interdipendente', "Pedagogia dell'ascolto"]
        ),
        (
            'Il concetto di Male Radicale e Male Banale in Immanuel Kant e Hannah Arendt',
            "Dall'inversione della massima dell'arbitrio nel saggio kantiano sulla religione all'assenza di pensiero e conformismo burocratico di Eichmann a Gerusalemme.",
            ['Kant', 'Arendt', 'Eichmann', 'Male radicale', 'Burocrazia'],
            ['Male radicale kantiano', 'Banalità del male arendtiana', 'Incapacità di giudizio morale', 'Perversione delle massime', "Eclissi dell'autonomia critica"]
        ),
        (
            "L'asimmetria della responsabilità verso il Volto dell'Altro in Emmanuel Levinas",
            "Dimostra come l'imperativo etico non nasca da un contratto tra eguali, ma dall'interpellazione vulnerabile dell'Altro che mi precede e mi rende ostaggio sacro.",
            ['Levinas', 'Volto', 'Altro', 'Contratto', 'Ostaggio'],
            ["Epifania dell'Alterità", 'Asimmetria etica radicale', "Incondizionatezza dell'ostaggio", 'Comandamento tu non ucciderai', "Trascendenza dell'Altro"]
        ),
        (
            'Il dilemma del male minore e la teoria della guerra giusta (Just War Theory)',
            "Da Agostino e Tommaso d'Aquino a Michael Walzer: analizza le condizioni rigorose dello ius ad bellum e dello ius in bello nell'orizzonte degli armamenti nucleari.",
            ['Guerra giusta', 'Walzer', 'Agostino', 'Male minore', 'Bombe'],
            ['Ius ad bellum e ius in bello', 'Proporzionalità e immunità dei civili', 'Dottrina della suprema emergenza', 'Aporia della deterrenza atomica', 'Etica bellica']
        ),
        (
            'La bioetica laica versus la bioetica cattolica: disponibilità della vita',
            "Metti a confronto il paradigma della sacralità della vita (indisponibilità ontologica) con il paradigma della qualità della vita fondato sull'autonomia cosciente.",
            ['Sacralità', 'Qualità della vita', 'Chiesa', 'Laici', 'Dio padrone'],
            ['Indisponibilità ontologica', 'Autodeterminazione e qualità', 'Persona versus essere umano biologico', 'Consenso informato radicale', 'Pluralismo bioetico']
        ),
        (
            "L'etica del discorso e la fondazione pragmatica trascendentale di Karl-Otto Apel",
            "Dimostra come chiunque apra un dibattito argomentativo riconosca già implicitamente l'eguaglianza e la pari dignità di tutti i partecipanti, pena l'autocontraddizione.",
            ['Apel', 'Discorso', 'Parlare', 'Contraddizione', 'Litigare'],
            ['Pragmatica trascendentale', 'Comunità ideale della comunicazione', 'Autocontraddizione performativa', 'Norme etiche a priori', 'Inclusione argomentativa']
        ),
        (
            'Il dilemma del liberismo anarco-capitalista in Robert Nozick',
            'Esponi la teoria del titolo valido in Anarchia, Stato e Utopia: la redistribuzione fiscale forzata equivale al lavoro schiavo e viola la proprietà di sé.',
            ['Nozick', 'Tasse schiavitù', 'Stato minimo', 'Proprietà', 'Ricchi'],
            ['Self-ownership nozickiana', 'Stato ultraminimo', 'Teoria del titolo valido (Entitlement)', 'Inviolabilità della proprietà', 'Critica al pattern distributivo']
        ),
        (
            "La virtù aristotelica e l'educazione del carattere in Alasdair MacIntyre",
            "Attraverso Dopo la virtù, denuncia il fallimento del progetto illuminista di fondare la morale sull'individuo astratto, riproponendo le comunità di pratiche teleologiche.",
            ['MacIntyre', 'Dopo la virtù', 'Illuminismo', 'Regole', 'Comunità'],
            ['Tradizione teleologica aristotelica', 'Comunità di pratiche', 'Narrazione biografica unificata', 'Virtù e beni interni', "Superamento dell'emotivismo"]
        ),
        (
            'Il dilemma della tortura di emergenza (Ticking Time Bomb Scenario)',
            "Un terrorista ha piazzato un ordigno nucleare che esploderà tra un'ora in una metropoli. È lecito violare il divieto assoluto di tortura per estorcergli il codice?",
            ['Tortura', 'Bomba a orologeria', 'Polizia', 'Salvare la città', 'Uccidere'],
            ['Ticking time bomb problem', 'Divieto assoluto di tortura (Ius cogens)', 'Aporia deontologica', "Fessura nell'ordinamento democratico", "Argine all'inquisizione"]
        ),
        (
            "L'esperimento della stanza degli orrori e il dovere di rettitudine in Cicerone",
            'Riprendi il De Officiis: la distinzione tra Honestum (il moralmente retto) e Utile (il conveniente), dimostrando che ciò che è turpe non può mai essere veramente vantaggioso.',
            ['Cicerone', 'De Officiis', 'Utile', 'Onesto', 'Vantaggio'],
            ['Honestum e Utile ciceroniano', 'Incompatibilità tra turpitudine e utile', 'Dovere civico repubblicano', 'Armonia morale stoica', 'Primato della rettitudine']
        ),
        (
            'Il relativismo etico e la confutazione del nichilismo morale in Leo Strauss',
            'Analizza la critica straussiana alla modernità: se la giustizia è solo convenzione storica contingente, allora il cannibalismo e la democrazia sono sullo stesso piano.',
            ['Strauss', 'Relativismo', 'Diritto naturale', 'Tutto relativo', 'Nichilismo'],
            ['Diritto naturale classico', 'Nichilismo assiologico contemporaneo', 'Tirannide e relativismo', 'Crisi della filosofia politica', 'Criterio trascendente']
        ),
        (
            "L'etica ambientalista della responsabilità asimmetrica verso le generazioni venture",
            'Poiché i nascituri tra due secoli non possono votare né citarci in giudizio, fonda il nostro dovere categorico di preservare il pianeta su basi non contrattualistiche.',
            ['Nascituri', 'Votare', 'Futuro', 'Contratto', 'Noi decidiamo'],
            ['Asimmetria generazionale non contrattuale', 'Dovere categorico verso i posteri', 'Eredità ontologica', 'Custodia fiduciaria globale', 'Giustizia intergenerazionale']
        ),
        (
            'La dialettica della purezza delle mani in Jean-Paul Sartre e Albert Camus',
            "Metti a confronto l'opera Le mani sporche di Sartre con I giusti di Camus: fino a che punto è lecito macchiarsi le mani di crimini in nome della rivoluzione?",
            ['Mani sporche', 'Sartre', 'Camus', 'Rivoluzione', 'Bomba'],
            ['Les Mains sales sartriane', 'Limite inviolabile camusiano', "Tragicità dell'azione politica", 'Omicidio politico e sacrificio', 'Puro mezzo e fine nobile']
        ),
        (
            "L'enigma del perdono sovrano nel dramma della Shoah di Simon Wiesenthal",
            'Nel libro Il girasole, un soldato nazista morente chiede perdono a un prigioniero ebreo per i crimini commessi. Aveva il prigioniero il diritto di concedere il perdono?',
            ['Wiesenthal', 'Girasole', 'Nazista', 'Perdono', 'Shoah'],
            ['Aporia del perdono vicario', 'Incommensurabilità del genocidio', 'Silenzio testimoniale', 'Giustizia versus riconciliazione', "Tragedia dell'espiazione"]
        ),
        (
            "L'Orazione per la Sovranità della Coscienza Morale",
            "Pronuncia l'arringa conclusiva: nessun ordine di superiore, nessuna legge ingiusta, nessuna convenienza di Stato può assolvere l'uomo che abdica alla propria coscienza.",
            ['Ordini ricevuti', 'Legge dello Stato', 'Comandante', 'Obbedire', 'Assolto'],
            ['Inviolabilità della coscienza', 'Tribunale interiore', "Rifiuto dell'obbedienza cieca", 'Supremazia della dignità', 'Eternità della morale']
        ),
    ],
    "c2": [
        (
            "L'aporia dell'Altro assoluto e l'ospitalità incondizionata in Jacques Derrida",
            "Delinea la tensione strutturale irrisolvibile tra la legge universale dell'ospitalità incondizionata e le leggi condizionate del diritto d'asilo e degli Stati sovrani.",
            ['Derrida', 'Ospitalità', 'Leggi', 'Confini', 'Stato'],
            ['Ospitalità incondizionata vs condizionale', 'Aporia derridiana', 'Eteronomia radicale', 'Sovranità disarmata', 'Apertura messianica']
        ),
        (
            'La decostruzione del concetto di Giustizia oltre il Diritto',
            "Pronuncia una summa sulla celebre formula: Il diritto è decostruibile perché è posto, la Giustizia è indecostruibile perché è la richiesta infinita dell'Altro.",
            ['Diritto', 'Giustizia', 'Leggi', 'Decostruire', 'Tribunali'],
            ['Indecostruibilità della giustizia', 'Decostruibilità del diritto positivo', "Richiesta infinita dell'Altro", 'Trascendenza immanente', 'Singolarità irriducibile']
        ),
        (
            "L'archetipo dell'Antigone: il dissidio insanabile tra Nomos e Themis",
            "Rivisita la lettura heideggeriana del coro dell'Antigone: il deinon, l'uomo come la più tremenda delle creature, lacerato tra la legge secolare e la sacralità dell'origine.",
            ['Antigone', 'Creonte', 'Deinon', 'Sepoltura', 'Dèi'],
            ['Deinon heideggeriano', 'Themis primigenia', 'Nomos della polis', 'Lacerazione originaria', 'Tragicità metafisica']
        ),
        (
            'La violenza divina e il messianismo rivoluzionario in Walter Benjamin',
            'Nel saggio Per la critica della violenza, indaga la violenza divina pura: non pone diritto né lo conserva, ma distrugge il nesso fatale tra colpa e sanzione giuridica.',
            ['Benjamin', 'Violenza divina', 'Colpa', 'Diritto', 'Sangue'],
            ['Violenza pura o divina', 'Distruzione del mito fatale', 'Espiazione non cruenta', 'Messianismo redentore', 'Rottura del continuum']
        ),
        (
            "L'interruzione etica dell'essere e l'Altrimenti che essere in Levinas",
            "Dimostra come la soggettività etica non sia un'affermazione del conatus essendi, ma una sostituzione originaria: farsi carico della persecuzione dell'altro fino all'espiazione.",
            ['Levinas', 'Conatus', 'Essere', 'Io', 'Sostituzione'],
            ['Altrimenti che essere', 'Kenosi del conatus essendi', 'Sostituzione etica originaria', 'Vulnerabilità infinita', "Trascendenza dell'Altro"]
        ),
        (
            "L'enigma del perdono dell'imperdonabile in Vladimir Jankélévitch",
            'Di fronte ai campi di sterminio, analizza la tesi radicale: il perdono è morto nei campi della morte. È possibile perdonare quando i carnefici non chiedono perdono?',
            ['Jankélévitch', 'Perdonare', 'Auschwitz', 'Carnefici', 'Morte'],
            ['Imperdonabilità ontologica', 'Rifiuto della grazia a buon mercato', 'Memoria inestinguibile', 'Aporia del perdono puro', 'Fiducia tradita']
        ),
        (
            "La figura dell'Homo Sacer e lo stato di eccezione perenne in Giorgio Agamben",
            'Analizza come la riduzione della vita a nuda vita (zoé) privata di ogni forma e diritto (bios) sia diventata il paradigma politico segreto della modernità globale.',
            ['Agamben', 'Homo sacer', 'Nuda vita', 'Campo', 'Eccezione'],
            ['Nuda vita versus forma-di-vita', 'Bando sovrano e homo sacer', 'Paradigma biopolitico moderno', 'Disattivazione del dispositivo', 'Inoperosità salvifica']
        ),
        (
            "L'impossibilità dell'etica nel nichilismo estremo di Cioran",
            "Fai un'arringa dialettica con le vette dell'abisso: quando ogni azione umana è vana e transitoria, l'astensione dall'essere e il silenzio diventano l'unica forma di purezza morale.",
            ['Cioran', 'Niente', 'Inutile', 'Morte', 'Suicidio'],
            ['Lucidità nichilista radicale', 'Inconveniente di essere nati', 'Estetica della disperazione', 'Astensione sovrana', 'Purezza del silenzio']
        ),
        (
            'La giustizia riparativa (Restorative Justice) come superamento della vendetta penale',
            "Pronuncia un'orazione magistrale sul ribaltamento della logica carceraria: l'incontro dialettico disarmato tra colpevole e vittima per guarire la frattura sociale.",
            ['Carcere', 'Vendetta', 'Punire', 'Occhio per occhio', 'Cella'],
            ['Giustizia riparativa circolare', 'Riparazione del legame sociale', 'Superamento del retribuzionismo', 'Riconciliazione comunitaria', 'Verità trasformativa']
        ),
        (
            'La parresìa socratica di fronte ai Trenta Tiranni di Atene',
            "Evoca l'episodio storico in cui Socrate rifiutò l'ordine dei tiranni di arrestare Leone di Salamina per metterlo a morte, rischiando deliberatamente la vita per non compiere ingiustizia.",
            ['Socrate', 'Trenta Tiranni', 'Leone di Salamina', 'Paura', 'Obbedire'],
            ['Parresìa socratica intransigente', 'Rifiuto del comando ingiusto', "Primato del bene sull'incolumità", 'Testimonianza eroica della legge interiore', "Immortalità dell'anima"]
        ),
        (
            "L'archetipo del sacrificio di Isacco nel Timore e Tremore di Kierkegaard",
            "Sviscera la sospensione teleologica dell'etica: Abramo che sale sul monte Moria superando il dovere morale del padre universale per obbedire alla fede paradossale nell'Assoluto.",
            ['Abramo', 'Isacco', 'Kierkegaard', 'Sacrificio', 'Fede'],
            ["Sospensione teleologica dell'etica", 'Cavaliere della fede', "Paradosso dell'Assoluto", 'Solitudine di Abramo', 'Trepidazione e fede']
        ),
        (
            "L'etica della terra e la sacralità biocentrica in Albert Schweitzer",
            "Commenta la dottrina del Rispetto per la Vita (Ehrfurcht vor dem Leben): l'uomo è vita che vuole vivere in mezzo a vita che vuole vivere, senza gerarchie di valore ontologico.",
            ['Schweitzer', 'Vita', 'Rispetto', 'Uccidere', 'Animali'],
            ['Ehrfurcht vor dem Leben', 'Simmetria ontologica del vivente', 'Mistica della responsabilità universale', 'Solidarietà cosmica', 'Inviolabilità di ogni creatura']
        ),
        (
            'La colpa metafisica e la responsabilità storica in Karl Jaspers',
            'Distingui nel saggio La questione della colpa le quattro dimensioni: colpa criminale, politica, morale e la colpa metafisica di essere sopravvissuti mentre altri venivano trucidati.',
            ['Jaspers', 'Colpa tedesca', 'Tribunale', 'Guerra', 'Sopravvivere'],
            ['Colpa metafisica universale', 'Solidarietà ontologica tra gli uomini', 'Responsabilità storica incomprimibile', 'Metanoia spirituale', 'Purificazione del giudizio']
        ),
        (
            "La decostruzione del contrattualismo e l'aporia dei diritti animali",
            "Dimostra con Tom Regan e Peter Singer come l'etica basata sull'accordo tra soggetti razionali capaci di reciprocità escluda ingiustamente i soggetti-di-una-vita non umani.",
            ['Singer', 'Regan', 'Animali', 'Contratto', 'Diritti umani solo'],
            ['Soggetti-di-una-vita', 'Superamento dello specismo antropocentrico', 'Capacità senziente', 'Deontologia estesa', 'Comunità morale allargata']
        ),
        (
            "L'enigma del male gratuito e la confessione di Stavrogin in Dostoevskij",
            "Analizza ne I demoni l'abisso della corruzione dell'anima: compiere il male supremo non per passione né per tornaconto, ma per la pura vertigine della distruzione del sacro.",
            ['Dostoevskij', 'Stavrogin', 'Demoni', 'Male', 'Peccato'],
            ['Vertigine del male gratuito', 'Ateismo nichilista dostoevskiano', "Desolazione dell'anima corrotta", 'Richiesta disperata di perdono', 'Redenzione e inferno']
        ),
        (
            'La bioetica della procreazione e la genitorialità responsabile in Jürgen Habermas',
            "Nel saggio Il futuro della natura umana, argomenta contro l'editing genetico migliorativo: la persona programmata perde la possibilità di considerarsi autore autonomo della propria vita.",
            ['Habermas', 'DNA', 'Bambini su misura', 'Programmare', 'Genitori'],
            ['Autonomia biografica originaria', 'Indisponibilità della casualità naturale', 'Pari dignità tra generazioni', 'Eugenetica migliorativa decostruita', 'Auto-comprensione della specie']
        ),
        (
            "L'etica della resistenza e il dovere della testimonianza in Primo Levi",
            "Rivisita I sommersi e i salvati: la zona grigia dove vittime e carnefici si confondono, e l'urgenza straziante di testimoniare per chi ha toccato il fondo e non è tornato.",
            ['Primo Levi', 'Auschwitz', 'Zona grigia', 'Testimone', 'Sommersi e salvati'],
            ['Zona grigia morale', 'Dovere testimoniale incorruttibile', 'Vergogna del superstite', 'Incommensurabilità del lager', 'Memoria vigile']
        ),
        (
            'Il ripensamento della Sovranità: da potere di morte a custodia del vivente',
            "Pronuncia un'orazione che teorizzi la trasfigurazione definitiva del concetto politico di sovranità: dal diritto arcaico di uccidere e punire al dovere cosmico di custodire la vita.",
            ['Sovranità', 'Uccidere', 'Stato', 'Spada', 'Potere'],
            ['Sovranità trasfigurata', 'Custodia incondizionata della vita', 'Disarmo del Leviatano', "Nomos dell'amore fraterno", 'Trionfo della civiltà']
        ),
        (
            'Il silenzio contemplativo di fronte al mistero del Bene Supremo',
            "Dimostra come, al culmine di ogni speculazione etica, il Bene oltrepassi le categorie logiche per risplendere, come il Sole platonico, al di là dell'essere e del dicibile.",
            ['Platone', 'Bene', 'Sole', 'Parole', "Oltre l'essere"],
            ['Agathon platonico', "Epekeina tes ousias (al di là dell'essenza)", 'Luce sorgiva ineffabile', 'Estasi della rettitudine', "Silenzio dell'adorazione"]
        ),
        (
            "L'Inno all'Inviolabile: il Giuramento Supremo dell'Oratore Giusto",
            "Chiudi il corso magistrale dei Dilemmi con l'orazione che consacra la coscienza come fiamma eterna che nessuna tirannia, nessuna minaccia e nessuna lusinga potrà mai spegnere.",
            ['Fine', 'Fiamma', 'Tiranno', 'Morire', 'Giuramento'],
            ['Fiamma eterna della coscienza', "Magistero dell'Oratore Giusto", "Trionfo dell'Inviolabile", 'Inno supremo alla Verità', "Vittoria perenne dell'Anima"]
        ),
    ],
}
