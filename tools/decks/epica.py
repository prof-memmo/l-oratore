# Mazzo: epica
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            'Il volo di Icaro e le ali di cera',
            "Sei il piccolo Icaro con le ali piumate costruite dal papà. Racconta l'emozione di staccare i piedi da terra prima di avvicinarti troppo al sole.",
            ['Ali', 'Sole', 'Cera', 'Cadere', 'Mare'],
            ['Volo', 'Piume', 'Cielo', 'Libertà', 'Brezza']
        ),
        (
            'Il cavallo di Troia di legno',
            'Sei un soldato greco nascosto nella pancia buia del grande cavallo di legno. Descrivi il silenzio prima di uscire nella notte.',
            ['Cavallo', 'Legno', 'Troia', 'Soldati', 'Pancia'],
            ['Silenzio', 'Notte', 'Astuzia', 'Porte', 'Vittoria']
        ),
        (
            'La forza prodigiosa del piccolo Ercole',
            'Sei il piccolo Ercole nella culla e due serpenti si avvicinano. Spiega come li afferri senza paura trasformando il pericolo in un gioco.',
            ['Ercole', 'Serpenti', 'Culla', 'Forza', 'Paura'],
            ['Crescita', 'Muscoli', 'Coraggio', 'Sorriso', 'Prodigio']
        ),
        (
            'Il filo rosso di Arianna nel labirinto',
            'Sei la principessa Arianna. Consegna il gomitolo magico a Teseo spiegandogli come riavvolgerlo per uscire dal labirinto buio.',
            ['Filo', 'Gomitolo', 'Teseo', 'Labirinto', 'Mostro'],
            ['Guida', 'Strada', 'Uscita', 'Luce', 'Salvezza']
        ),
        (
            'Il canto melodioso di Orfeo con la lira',
            "Sei Orfeo e suoni la tua lira d'oro. Racconta come la tua musica dolcissima faccia calmare le onde del mare e fermare i leoni feroci.",
            ['Orfeo', 'Lira', 'Canto', 'Animali', 'Musica'],
            ['Melodia', 'Armonia', 'Dolcezza', 'Incanto', 'Pace']
        ),
        (
            "Il carro d'oro del dio Sole (Febo)",
            'Sei Febo Apollo che guida il carro di fuoco attraverso il cielo azzurro. Descrivi come risvegli la terra baciando le cime degli alberi.',
            ['Carro', 'Apollo', 'Sole', 'Fuoco', 'Cavalli'],
            ['Luce', 'Alba', 'Raggi', 'Mattino', 'Calore']
        ),
        (
            'Il tocco dorato di Re Mida',
            "Sei il re Mida e ogni cosa che tocchi diventa oro zecchino, persino una pera matura. Spiega perché preferisci il profumo dei fiori all'oro freddo.",
            ['Oro', 'Mida', 'Toccare', 'Ricco', 'Mangiare'],
            ['Desiderio', 'Pentimento', 'Natura', 'Abbraccio', 'Semplicità']
        ),
        (
            'Pegaso il cavallo alato bianco',
            'Hai accarezzato la criniera di Pegaso, il cavallo con le ali che beve alla fonte. Descrivi il suo balzo leggero verso le nuvole.',
            ['Cavallo', 'Ali', 'Volare', 'Pegaso', 'Bianco'],
            ['Criniera', 'Galoppo', 'Nuvole', 'Fonte', 'Leggerezza']
        ),
        (
            'Il dono del fuoco di Prometeo',
            'Sei il titano Prometeo che porta una scintilla rubata agli dèi dentro una canna cava. Dona il fuoco agli uomini infreddoliti.',
            ['Prometeo', 'Fuoco', 'Rubare', 'Dèi', 'Freddo'],
            ['Scintilla', 'Dono', 'Fiamma', 'Calore', 'Civiltà']
        ),
        (
            "La mela d'oro e la gara di bellezza",
            "Sei Paride e tre dee ti chiedono a chi appartenga la mela più splendida. Spiega com'è difficile scegliere senza far arrabbiare nessuno.",
            ['Mela', 'Paride', 'Dee', 'Oro', 'Bella'],
            ['Scelta', 'Dono', 'Giudizio', 'Splendore', 'Discordia']
        ),
        (
            'Lo scudo lucido di Perseo contro Medusa',
            'Sei Perseo che guarda il riflesso della terribile Medusa nello scudo di bronzo per non farti pietrificare. Racconta il tuo piano astuto.',
            ['Medusa', 'Pietra', 'Scudo', 'Serpenti', 'Guardare'],
            ['Riflesso', 'Specchio', 'Astuzia', 'Bronzo', 'Vittoria']
        ),
        (
            'La corsa veloce di Atalanta nei boschi',
            'Sei Atalanta, la ragazza più veloce della Grecia. Sfida i cacciatori spiegando che nessuno può battere le tue gambe scattanti.',
            ['Corsa', 'Atalanta', 'Vincere', 'Gambe', 'Mele'],
            ['Foresta', 'Velocità', 'Vento', 'Libertà', 'Balzo']
        ),
        (
            "L'elmo dell'invisibilità di Ade",
            "Hai indossato l'elmo fatato che ti rende invisibile a tutti. Racconta come ti muovi piano per esplorare senza farti notare.",
            ['Elmo', 'Invisibile', 'Vedere', 'Scomparire', 'Testa'],
            ['Magia', 'Passo silenzioso', 'Ombra', 'Segreto', 'Protezione']
        ),
        (
            'Il canto delle Sirene sul mare blu',
            'Sei un marinaio sulla nave di Ulisse con le orecchie tappate di cera. Guarda le sirene sulle rocce e immagina la loro melodia incantata.',
            ['Sirene', 'Ulisse', 'Cera', 'Canto', 'Rocce'],
            ['Onde', 'Incanto', 'Nave', 'Rotta', 'Resistenza']
        ),
        (
            'Il cane Argo che riconosce il padrone',
            "Sei il vecchio cane Argo che aspetta Ulisse da vent'anni. Descrivi la felicità di scodinzolare un'ultima volta vedendolo tornare.",
            ['Argo', 'Cane', 'Ulisse', 'Vecchio', 'Morire'],
            ['Fedeltà', 'Riconoscimento', 'Festa', 'Ritorno', 'Affetto']
        ),
        (
            "La faretra dalle frecce d'argento di Diana",
            'Sei la dea Diana a caccia nella radura illuminata dalla luna. Parla della tua amicizia con i cervi e gli alberi della foresta.',
            ['Diana', 'Caccia', 'Luna', 'Frecce', 'Arco'],
            ['Selva', 'Cervo', 'Notte', 'Argento', 'Rispetto']
        ),
        (
            'Il gigante Polifemo e il trucco di Nessuno',
            "Sei Ulisse nella grotta buia. Spiega al ciclope con voce tranquilla che il tuo nome è 'Nessuno' per preparare la salvezza dei compagni.",
            ['Polifemo', 'Ciclope', 'Occhio', 'Nessuno', 'Grotta'],
            ['Astuzia', 'Nome', 'Inganno', 'Pecore', 'Fuga']
        ),
        (
            "L'albero sacro delle mele delle Esperidi",
            "Hai raggiunto il giardino fatato custodito dal drago. Ammira i frutti d'oro che brillano tra i rami profumati.",
            ['Esperidi', 'Drago', 'Mele', 'Giardino', 'Oro'],
            ['Custodia', 'Frutto', 'Meraviglia', 'Tramonto', 'Sogno']
        ),
        (
            'La zattera di Ulisse sbattuta dalle onde',
            "Il mare in tempesta ha rotto la zattera e nuoti verso l'isola dei Feaci. Fai coraggio a te stesso per raggiungere la riva.",
            ['Zattera', 'Onde', 'Naufragio', 'Ulisse', 'Acqua'],
            ['Bracciata', 'Riva', 'Speranza', 'Salvezza', 'Spiaggia']
        ),
        (
            'La nascita della dea Atena dalla saggezza',
            "Dalla testa di Zeus nasce la dea con l'elmo e la civetta. Spiega perché l'intelligenza e la sapienza sono più forti della spada.",
            ['Atena', 'Zeus', 'Testa', 'Civetta', 'Guerra'],
            ['Sapienza', 'Intelligenza', 'Luce', 'Giustizia', 'Pensiero']
        ),
    ],
    "a2": [
        (
            "L'ira funesta di Achille e la tenda dell'orgoglio",
            "Sei il leggendario Achille. Spiega ai principi greci perché ti rifiuti di combattere dopo l'offesa ricevuta da Agamennone.",
            ['Achille', 'Ira', 'Agamennone', 'Tenda', 'Guerra'],
            ['Orgoglio', 'Offesa', 'Onore', 'Ritiro', 'Guerriero']
        ),
        (
            "L'addio commovente tra Ettore e Andromaca",
            "Sei Ettore alle porte Scee. Togli l'elmo piumato che spaventa il piccolo Astianatte e saluta tua moglie prima della battaglia.",
            ['Ettore', 'Andromaca', 'Elmo', 'Piangere', 'Bambino'],
            ['Commiato', 'Patria', 'Destino', 'Bacio', 'Affetto']
        ),
        (
            "L'astuzia di Penelope e la tela infinita",
            'Sei la regina Penelope. Spiega alle ancelle perché disfi di notte la tela tessuta di giorno per ingannare i Proci prepotenti.',
            ['Penelope', 'Tela', 'Proci', 'Notte', 'Giorno'],
            ['Attesa', 'Astuzia', 'Fedeltà', 'Inganno nobile', 'Speranza']
        ),
        (
            'La discesa di Orfeo negli Inferi per Euridice',
            "Sei Orfeo davanti al trono di Plutone e Proserpina. Canta con tutto il tuo cuore per commuovere gli dèi dell'oltretomba.",
            ['Plutone', 'Inferno', 'Morta', 'Euridice', 'Voltare'],
            ['Preghiera', 'Canto sublime', 'Pietà divina', 'Amore immortale', 'Supplica']
        ),
        (
            "La fatica di Ercole contro l'Idra di Lerna",
            'Sei Ercole e affronti il mostro a nove teste: ogni volta che ne tagli una, ne ricrescono due. Chiama Iolao per bruciare i colli.',
            ['Idra', 'Teste', 'Tagliare', 'Mostro', 'Palude'],
            ['Fuoco', 'Tenacia', 'Collaborazione', 'Astuzia tattica', 'Vittoria']
        ),
        (
            'Il dilemma di Paride e la scelta del destino',
            "Sei Paride sul monte Ida: Atena ti offre la sapienza, Era il potere, Afrodite l'amore di Elena. Giustifica la tua scelta fatale.",
            ['Atena', 'Era', 'Afrodite', 'Elena', 'Mela'],
            ['Bivio mitico', 'Passione', 'Fato', 'Bellezza suprema', 'Svolto fatale']
        ),
        (
            'La navigazione di Ulisse tra Scilla e Cariddi',
            "Sei al timone della nave nello stretto di Messina: da un lato il vortice marino che inghiotte, dall'altro il mostro a sei teste. Guida i marinai.",
            ['Scilla', 'Cariddi', 'Vortice', 'Mostro', 'Navigare'],
            ['Stretto periglioso', 'Scelta tragica', 'Fermezza al timone', 'Rotta obbligata', 'Coraggio marinaro']
        ),
        (
            'La nascita di Roma: il solco di Romolo e Remo',
            "Sei Romolo che traccia il solco sacro con l'aratro sul colle Palatino. Avverti chiunque oserà superare quel confine armato.",
            ['Romolo', 'Remo', 'Uccidere', 'Solco', 'Mura'],
            ['Confine sacro', 'Fondazione', 'Urbe', 'Legge prima', 'Destino imperiale']
        ),
        (
            'La corsa di Fidippide da Maratona ad Atene',
            'Sei il messaggero greco che corre senza sosta per quarantadue chilometri per annunciare la vittoria sui Persiani prima di crollare.',
            ['Correre', 'Maratona', 'Atene', 'Persiani', 'Morire'],
            ['Nenikekamen (Abbiamo vinto)', 'Messaggio di libertà', 'Respiro estremo', 'Eroismo civico', 'Gloria perenne']
        ),
        (
            'Il cavallo immortale Balio che piange la morte di Patroclo',
            'Sei uno dei cavalli divini di Achille. Descrivi il dolore per la caduta del giovane eroe che ti accarezzava la criniera.',
            ['Cavallo', 'Patroclo', 'Achille', 'Piangere', 'Guerra'],
            ['Lacrime divine', 'Dolore immortale', 'Fedeltà animale', 'Lutto', 'Guerriero caduto']
        ),
        (
            'La trasformazione di Dafne in albero di alloro',
            'Sei la ninfa Dafne inseguita da Apollo. Prega la Madre Terra di mutare la tua forma in corteccia verde pur di salvare la libertà.',
            ['Apollo', 'Dafne', 'Alloro', 'Scappare', 'Albero'],
            ['Metamorfosi', 'Corteccia', 'Verginità sacra', 'Salvezza vegetale', 'Foglie eterne']
        ),
        (
            'Il vaso di Pandora e la nascita della Speranza',
            "Sei Pandora e hai aperto per curiosità lo scrigno proibito liberando tutti i mali nel mondo. Trattieni sul fondo l'ultimo dono prezioso.",
            ['Vaso', 'Pandora', 'Mali', 'Curiosità', 'Aprire'],
            ['Speranza superstite', 'Fondo dello scrigno', 'Conforto umano', "Luce nell'ombra", 'Dono divino']
        ),
        (
            'La sfida di Aracne contro la dea Atena al telaio',
            "Sei la giovane tessitrice Aracne. Mostra la perfezione della tua tela sfidando la dea dell'arte senza temere la punizione.",
            ['Aracne', 'Atena', 'Telaio', 'Ragno', 'Tessere'],
            ['Maestria artistica', 'Hybris e talento', 'Trame mirabili', 'Metamorfosi tessile', 'Orgoglio artigiano']
        ),
        (
            "Il ritorno di Ulisse e la prova dell'arco",
            'Sei Ulisse mascherato da vecchio mendicante. Prendi in mano il tuo grande arco che nessun pretendente è riuscito a tendere.',
            ['Arco', 'Mendicante', 'Proci', 'Frecce', 'Tendere'],
            ['Prova regale', 'Riconoscimento epico', "Tensione dell'arco", 'Bersaglio trafitto', 'Giustizia sovrana']
        ),
        (
            "Il supplizio di Tantalo nell'Ade",
            "Immerso nell'acqua fresca fino al mento con frutti maturi sui rami, l'acqua si ritira e i rami si alzano ogni volta che tenti di bere o mangiare.",
            ['Tantalo', 'Fame', 'Sete', 'Acqua', 'Frutta'],
            ['Supplizio eterno', 'Desiderio inappagabile', 'Castigo divino', 'Frustrazione mitica', 'Superbia punita']
        ),
        (
            'La discesa di Enea agli Inferi con la Sibilla',
            "Sei Enea guidato dalla Sibilla Cumana col ramo d'oro tra le mani. Cerchi l'ombra di tuo padre Anchise per conoscere il futuro di Roma.",
            ['Enea', 'Sibilla', "Ramo d'oro", 'Anchise', 'Inferno'],
            ['Pietas filiale', 'Oltretomba virgiliano', 'Profezia storica', 'Guida sapiente', 'Futura grandezza']
        ),
        (
            "Il labirinto di Dedalo e il rimorso dell'architetto",
            'Sei Dedalo, il geniale inventore del labirinto di Creta. Esprimi il rimorso per aver costruito una prigione così crudele per il Minotauro.',
            ['Dedalo', 'Labirinto', 'Minotauro', 'Costruire', 'Creta'],
            ['Ingegno architettonico', 'Rimorso morale', 'Prigione inestricabile', 'Creatura mostruosa', 'Responsabilità']
        ),
        (
            'La profezia di Cassandra inascoltata a Troia',
            'Sei la principessa Cassandra. Annuncia disperata ai concittadini che il cavallo di legno porterà la rovina della città mentre tutti ridono.',
            ['Cassandra', 'Profezia', 'Cavallo', 'Ridere', 'Troia'],
            ['Parola inascoltata', 'Verità tragica', 'Fato ineluttabile', 'Dolore profetico', 'Mura in fiamme']
        ),
        (
            'La generosità di Nausicaa sulla spiaggia dei Feaci',
            'Sei la principessa Nausicaa. Trovi un naufrago coperto di salsedine e vestilo con tuniche pulite prima di condurlo a palazzo reale.',
            ['Nausicaa', 'Ulisse', 'Spiaggia', 'Palla', 'Vestiti'],
            ['Accoglienza nobile', 'Pietà per il naufrago', 'Regalità gentile', 'Ospitalità omerica', 'Soccorso']
        ),
        (
            "Il giuramento dell'eroe classico",
            "Concludi il viaggio nell'epica antica con un discorso solenne: non è la vittoria che fa l'eroe, ma la dignità di lottare per la giustizia fino alla fine.",
            ['Vincere', 'Perdere', 'Spada', 'Eroe', 'Morire'],
            ['Dignità eroica', 'Valore morale', 'Lotta senza riserve', 'Memoria imperitura', "Luce dell'ideale"]
        ),
    ],
    "b1": [
        (
            'Il duello tra Ettore e Achille sotto le mura di Troia',
            "Sei Ettore rimasto solo fuori dalle mura Scee. Vedi avanzare Achille splendente d'armi divine: affronta il destino della patria.",
            ['Ettore', 'Achille', 'Troia', 'Scappare', 'Mura'],
            ['Fato ineluttabile', 'Onore troiano', 'Duello supremo', 'Sacrificio supremo', 'Epos omerico']
        ),
        (
            "L'orazione funebre di Pericle per i caduti ateniesi",
            "Rivisita Tucidide: pronuncia l'elogio funebre per i primi caduti della guerra peloponnesiaca celebrando la democrazia aperta di Atene.",
            ['Pericle', 'Atene', 'Caduti', 'Guerra', 'Discorso'],
            ['Democrazia deliberativa', 'Polis aperta', 'Esemplarità civica', 'Monumento vivente', 'Gloria democratica']
        ),
        (
            "La pietas di Enea tra il dovere verso Roma e l'amore di Didone",
            'Sei il pio Enea nel porto di Cartagine. Spiega alla regina Didone perché devi abbandonare la passione per obbedire al comando degli dèi.',
            ['Didone', 'Cartagine', 'Amore', 'Roma', 'Partire'],
            ['Pietas virgiliana', 'Imperativo del destino', 'Lacerazione interiore', 'Dovere sacro', 'Obbedienza al fato']
        ),
        (
            'Il mito della caverna di Platone: il risveglio del filosofo',
            "Descrivi il prigioniero liberato dalle catene che esce all'aperto, scopre la luce del Sole e sceglie di tornare nell'ombra per liberare i compagni.",
            ['Caverna', 'Ombre', 'Catene', 'Sole', 'Platone'],
            ['Disvelamento ontologico', 'Luce intelligibile', 'Ritorno liberatorio', 'Dovere pedagogico', 'Idea del Bene']
        ),
        (
            'Il riscatto del corpo di Ettore: Priamo alla tenda di Achille',
            "Sei l'anziano re Priamo che bacia le mani omicide che gli hanno ucciso i figli, supplicando la restituzione del cadavere di Ettore.",
            ['Priamo', 'Achille', 'Baciare le mani', 'Cadavere', 'Ettore'],
            ['Pietà universale', 'Commozione tragica', "Riconoscimento dell'umano", 'Lutto paterno', 'Riscattare il figlio']
        ),
        (
            "Il mito di Er e la scelta della vita nell'aldilà",
            'Ripercorri la visione del guerriero resuscitato nella Repubblica di Platone: le anime scelgono il modello della loro prossima incarnazione terrena.',
            ['Er', 'Anime', 'Scelta', 'Reincarnazione', 'Platone'],
            ["Libera scelta dell'anima", 'Fuso di Necessità', 'Responsabilità morale', 'Fiume Lete', 'Saggezza filosofica']
        ),
        (
            "La metamorfosi di Narciso e la trappola dello specchio d'acqua",
            "Sei il giovane Narciso che contempla il proprio volto riflesso nella fonte limpida. Analizza l'inganno mortale dell'auto-adorazione sterile.",
            ['Narciso', 'Specchio', 'Bello', 'Acqua', 'Fiore'],
            ['Narcisismo fatale', 'Illusione speculare', 'Incomunicabilità amorosa', 'Vana bellezza', 'Consunzione ontologica']
        ),
        (
            "Il canto di Ulisse nell'Inferno di Dante: Fatti non foste...",
            "Rivivi il XXVI canto della Commedia: l'orazione picciola con cui il vecchio Ulisse spinge i compagni oltre le Colonne d'Ercole per seguir virtute e canoscenza.",
            ['Ulisse', 'Dante', "Colonne d'Ercole", 'Inferno', 'Naufragio'],
            ['Folle volo dantesco', 'Virtute e canoscenza', 'Infrangere il confine', 'Orazione picciola', 'Ardore gnoseologico']
        ),
        (
            'La ribellione di Antigone contro il decreto tirannico di Creonte',
            'Sei Antigone davanti al tribunale di Tebe. Difendi il seppellimento del fratello Polinice invocando le leggi non scritte degli dèi.',
            ['Antigone', 'Creonte', 'Polinice', 'Sepoltura', 'Legge dello Stato'],
            ['Leggi non scritte (Agrapta nomima)', 'Pietà fraterna', 'Resistenza alla tirannide', 'Themis divina', 'Coscienza indomita']
        ),
        (
            'Il mito di Prometeo incatenato sulla rupe del Caucaso',
            "Sei Prometeo incatenato mentre l'aquila di Zeus ti dilania il fegato. Dichiara che preferisci questa sofferenza all'essere servo del tiranno dell'Olimpo.",
            ['Prometeo', 'Aquila', 'Zeus', 'Catene', 'Roccia'],
            ['Resistenza titanica', 'Odio per la tirannide', "Custodia dell'umano", 'Veggenza incorruttibile', 'Orgoglio insorto']
        ),
        (
            "La follia di Aiace e la caduta dell'onore omerico",
            'Sei Aiace Telamonio che si risveglia dalla follia scoprendo di aver trucidato le greggi scambiandole per i generali achei. Prepara il commiato dalla vita.',
            ['Aiace', 'Follia', 'Pecore', 'Armi di Achille', 'Spada'],
            ['Vergogna insostenibile', "Morte sull'elsa", 'Onore aristocratico', 'Disillusione guerriera', 'Commiato tragico']
        ),
        (
            'Il sacrificio di Ifigenia in Aulide per i venti favorevoli',
            "Sei la giovane figlia di Agamennone condotta all'altare sacrificale. Pronuncia le tue ultime parole perdonando il padre per la salvezza della flotta greca.",
            ['Ifigenia', 'Sacrificio', 'Agamennone', 'Vento', 'Altare'],
            ['Sacrificio innocente', 'Ragion di Stato arcaica', 'Perdono filiale', 'Vittima sacrificale', 'Partenza della flotta']
        ),
        (
            'Il viaggio degli Argonauti attraverso le Simplegadi',
            "Sei Giasone alla guida dell'Argo: le rocce semoventi che si scontrano frantumando le navi. Lancia la colomba per calcolare il passaggio.",
            ['Argonauti', 'Giasone', 'Rocce', 'Simplegadi', 'Nave'],
            ['Rocce semoventi', 'Colomba esploratrice', 'Fendere i flutti', 'Impresa collettiva', 'Trionfo della concordia']
        ),
        (
            "Il mito di Sisifo: la perseveranza contro l'assurdo",
            "Condannato a spingere un enorme masso fino alla cima del monte per vederlo rotolare giù all'infinito. Dimostra come la sfida perseverante vinca gli dèi.",
            ['Sisifo', 'Masso', 'Rotolare', 'Montagna', 'Castigo'],
            ['Perseveranza titanica', "Tragicità dell'assurdo", 'Coscienza insorta', 'Superamento della condanna', 'Fatica nobile']
        ),
        (
            "Il riconoscimento di Penelope: il segreto del letto d'ulivo",
            "Sei Ulisse tornato a Itaca. Rivela il segreto intimo conosciuto solo da te e Penelope: il letto nuziale intagliato nel tronco vivo dell'ulivo.",
            ['Letto', 'Ulivo', 'Penelope', 'Tronco', 'Radici'],
            ['Letto nuziale inamovibile', 'Radici viventi', 'Riconoscimento nuziale', 'Segreto condiviso', 'Compiutezza del ritorno']
        ),
        (
            'La contesa tra Atena e Poseidone per il patronato della città',
            "Sull'Acropoli, Poseidone dona il cavallo da guerra e la sorgente salata, Atena dona l'ulivo della pace e del nutrimento. Celebra il dono dell'ulivo.",
            ['Poseidone', 'Atena', 'Cavallo', 'Ulivo', 'Città'],
            ['Patronato di Atene', 'Dono della pace', 'Vittoria della sapienza', 'Fecondità agricola', 'Scelta civica']
        ),
        (
            "Il mito di Filemone e Bauci: l'ospitalità premiata",
            "Due anziani sposi poveri accolgono due viandanti sconosciuti dividendo l'ultima pagnotta, scoprendo che sono Zeus ed Ermes. Celebra la sacralità dell'ospite.",
            ['Filemone', 'Bauci', 'Poveri', 'Zeus', 'Cena'],
            ['Xenia sacra', 'Ospitalità disinteressata', 'Trasfigurazione divina', 'Amore coniugale perenne', 'Dono condiviso']
        ),
        (
            'La profezia del cieco Tiresia nel regno dei morti',
            "Sei il veggente tebano nell'Ade omerica. Predici a Ulisse i pericoli futuri: l'isola dei buoi del Sole e la morte dolce che verrà dal mare.",
            ['Tiresia', 'Ulisse', 'Inferno', 'Buoi del Sole', 'Profezia'],
            ['Veggenza mantica', "Vaticinio dell'Ade", 'Ammonimento sacro', 'Ritorno travagliato', 'Destino del navigatore']
        ),
        (
            'La morte gloriosa di Leonida alle Termopili',
            "Sei il re spartano con i trecento alle porte calde. Rispondi al re persiano che intima di consegnare le armi con l'immortale: 'Molon labe' (Vieni a prenderle).",
            ['Leonida', 'Sparta', 'Termopili', 'Trecento', 'Arrendersi'],
            ['Molon labe', 'Obbedienza alle leggi spartane', 'Barriera di scudi', 'Sacrificio per la libertà', 'Gloria imperitura']
        ),
        (
            "Il manifesto dell'Oratore Epico: il canto che vince il tempo",
            "Pronuncia l'orazione conclusiva del modulo epico: gli imperi crollano e gli eserciti svaniscono nella polvere, ma la parola poetica rende immortale l'onore.",
            ['Guerra', 'Polvere', 'Spade', 'Poesia', 'Fine'],
            ['Immortalità del canto epico', 'Trionfo della parola poetica', "Vittoria sull'oblio", 'Memoria dei giusti', 'Gloria immortale']
        ),
    ],
    "b2": [
        (
            'La concezione aristotelica della tragedia e la catarsi (Poetica)',
            "Analizza come la tragedia classica purifichi le passioni attraverso il terrore (phobos) e la pietà (eleos) scaturiti dall'errore dell'eroe (hamartia).",
            ['Aristotele', 'Catarsi', 'Tragedia', 'Paura', 'Piangere'],
            ['Catarsi aristotelica', 'Eleos e phobos', "Hamartia dell'eroe nobile", 'Purificazione delle passioni', 'Mimesi drammatica']
        ),
        (
            'La nascita della tragedia dallo spirito della musica in Nietzsche',
            "Delinea la contesa perenne tra l'impulso apollineo (forma, misura, sogno) e l'ebbrezza dionisiaca (abisso, dissoluzione del sé, musica travolgente).",
            ['Nietzsche', 'Apollo', 'Dioniso', 'Tragedia', 'Grecia'],
            ['Dialettica apollineo-dionisiaca', 'Ebbrezza e forma plastica', "Smembramento dell'individuo", 'Canto corale dionisiaco', 'Intuizione tragica']
        ),
        (
            "L'archetipo dell'eroe riluttante: da Achille ad Amleto",
            "Confronta l'epica arcaica dell'azione impavida con l'eroismo problematico della modernità, dove la coscienza morale paralizza il braccio vendicatore.",
            ['Achille', 'Amleto', 'Dubbio', 'Spada', 'Eroe'],
            ['Eroe problematico', 'Frattura della volontà', 'Coscienza introspettiva', "Superamento dell'epos monolitico", 'Tragicità moderna']
        ),
        (
            "La contesa tra le leggi scritte e non scritte nell'Antigone sofoclea",
            "Nel conflitto tra Creonte e Antigone, decostruisci l'unilateralità di entrambe le posizioni secondo la celebre lettura della Fenomenologia hegeliana.",
            ['Hegel', 'Antigone', 'Creonte', 'Stato', 'Famiglia'],
            ['Unilateralità etica hegeliana', 'Agrapta nomima immutabili', 'Ragione politica statale', 'Collisione tragica', 'Riconciliazione finale']
        ),
        (
            "Il mito platonico dell'Androgino nel Simposio",
            "Attraverso il discorso di Aristofane, illustra l'origine mitica dell'amore: la ricerca disperata e feconda della metà perduta tagliata dagli dèi invidiosi.",
            ['Simposio', 'Platone', 'Metà', 'Tagliati a metà', 'Amore'],
            ["Mito dell'androgino originario", "Nostalgia dell'interezza", 'Eros come mancanza ontologica', "Ricomposizione dell'unità", 'Metafora della passione']
        ),
        (
            "La fondazione mitica di Roma nell'Eneide come teodicea imperiale",
            'Mostra come Virgilio trasformi la sofferenza dei vinti troiani nella legittimazione sacrale della Pax Augustea e del destino civilizzatore di Roma.',
            ['Virgilio', 'Eneide', 'Augusto', 'Troia', 'Roma'],
            ['Pax Augustea provvidenziale', 'Teodicea del dominio romano', 'Pietas e fatum', 'Missione civilizzatrice', 'Dolore dei vinti']
        ),
        (
            'Il mito di Prometeo tra esaltazione tecnica e punizione divina',
            "Dalla versione esiodea alla riscrittura goethiana: Prometeo come simbolo dell'emancipazione scientifica umana o incarnazione dell'arrogante hybris mortale?",
            ['Prometeo', 'Goethe', 'Esiodo', 'Tecnica', 'Ribelle'],
            ['Hybris prometeica moderna', 'Emancipazione titanica', "Riscatto dell'homo faber", 'Castigo cosmico', 'Rifiuto della sottomissione']
        ),
        (
            'La discesa agli Inferi (Katabasis) come rito iniziatico universale',
            "Da Gilgamesh a Odisseo, da Enea a Dante: dimostra come nessun eroe possa compiere la propria missione senza aver attraversato l'ombra della morte.",
            ['Katabasis', 'Inferno', 'Morte', 'Discesa', 'Dante'],
            ['Rito iniziatico di katabasis', 'Confronto con le ombre ancestrali', 'Morte simbolica e rinascita', 'Conoscenza iniziatica', 'Archetipo universale']
        ),
        (
            "La follia d'amore e la perdita del senno nell'Orlando Furioso",
            "Analizza l'epica rinascimentale di Ludovico Ariosto: il più grande cavaliere cristiano che si spoglia delle armi e devasta i boschi per gelosia d'amore.",
            ['Orlando', 'Ariosto', 'Angelica', 'Follia', 'Luna'],
            ['Epos ariostesco disincantato', 'Follia erotica devastatrice', 'Senno smarrito sulla Luna', 'Ironia cavalleresca', "Fragilità dell'eroe"]
        ),
        (
            "La pietà per il nemico caduto nell'Iliade e nell'Eneide",
            "Metti a confronto il commosso incontro notturno tra Priamo e Achille con il tragico finale virgiliano dell'uccisione di Turno da parte di Enea.",
            ['Priamo', 'Achille', 'Turno', 'Enea', 'Uccidere'],
            ['Pietà omerica universale', 'Tragicità virgiliana finale', 'Vendetta versus misericordia', 'Dolore del vincitore', 'Umanità della tragedia']
        ),
        (
            "Il mito di Sisifo reinterpretato nell'esistenzialismo di Albert Camus",
            "Bisogna immaginare Sisifo felice. Dimostra come la rivolta cosciente contro l'assurdo trasformi la condanna degli dèi in trionfo dell'uomo.",
            ['Camus', 'Sisifo', 'Felice', 'Assurdo', 'Masso'],
            ['Rivolta cosciente camusiana', "Superamento dell'assurdo", 'Fedeltà alla fatica terrestre', 'Trionfo senza speranza ultraterrena', "Dignità dell'azione pura"]
        ),
        (
            "La figura di Medea: barbarie esotica o denuncia dell'ipocrisia greca?",
            "Nel capolavoro di Euripide, analizza l'orazione di Medea alle donne di Corinto: la condizione di subordinazione della straniera tradita nella polis patriarcale.",
            ['Medea', 'Euripide', 'Figli uccisi', 'Giasone', 'Maga'],
            ['Tragedia euripidea dissacrante', 'Condizione della donna straniera', 'Lacerazione vendicativa estrema', 'Denuncia della polis patriarcale', 'Eros distruttivo']
        ),
        (
            "L'inganno di Nessuno e il potere nominativo del linguaggio",
            "Come Ulisse nell'Odissea sconfigge la forza bruta di Polifemo attraverso il gioco verbale: nominarsi Outis (Nessuno) per negare la propria presenza e salvarsi.",
            ['Nessuno', 'Polifemo', 'Parola', 'Ciclope', 'Nome'],
            ['Potere nominativo e ontologico', 'Outis/Metis omerica', 'Sottomissione della violenza al Logos', 'Astuzia linguistica suprema', 'Salvezza nominativa']
        ),
        (
            "Il destino dell'eroe e l'orizzonte invalicabile dell'Ananke (Fato)",
            "Dimostra come nella tragedia greca la vera grandezza dell'eroe non risieda nella fuga dal fato, ma nell'assumersi la responsabilità totale del proprio destino già scritto.",
            ['Fato', 'Ananke', 'Destino', 'Fuggire', 'Colpa'],
            ['Ananke cieca e sovrana', 'Assunzione eroica del destino', 'Amor fati tragico', 'Grandezza morale dello scacco', 'Conflitto tra libertà e necessità']
        ),
        (
            'La contesa tra le generazioni divine: Titanomachia e Gigantomachia',
            'Ripercorri la successione da Urano a Crono e da Crono a Zeus: la vittoria faticosa del cosmo ordinato e razionale contro il caos mostruoso primordiale.',
            ['Urano', 'Crono', 'Zeus', 'Giganti', 'Guerra degli dèi'],
            ['Titanomachia cosmogonica', 'Transizione dal Caos al Kosmos', "Razionalizzazione dell'Olimpo", 'Mito di successione dinastico', 'Trionfo della giustizia olimpica']
        ),
        (
            "L'epos cavalleresco cristiano della Chanson de Roland",
            "L'arcivescovo Turpino e Orlando a Roncisvalle: il rifiuto orgoglioso di suonare l'olifante e il martirio per la fede contro l'invasione saracena.",
            ['Roland', 'Olifante', 'Roncisvalle', 'Carlo Magno', 'Spada'],
            ['Chanson de geste medievale', 'Orgoglio cavalleresco mortale', 'Martirio per la cristianità', "Rifiuto del richiamo d'aiuto", 'Spada Durlindana']
        ),
        (
            'Il mito del buon selvaggio e la terra dei Feaci',
            "Analizza Scheria nell'Odissea: un'utopia marittima isolata dal mondo dove non esistono guerre, le navi navigano col pensiero e regna la perfetta concordia.",
            ['Feaci', 'Alcinoo', 'Utopia', 'Navi', 'Scheria'],
            ['Utopia feacia omerica', 'Navigazione telepatica mirabile', 'Società pacifica ideale', 'Ospitalità incondizionata arcaica', 'Specchio edenico']
        ),
        (
            "La metamorfosi e l'instabilità delle forme nelle Metamorfosi di Ovidio",
            'Dimostra come il poema ovidiano non sia una raccolta di favole, ma una cosmologia filosofica eraclitea: tutto muta, nulla perisce, la materia scorre perenne.',
            ['Ovidio', 'Metamorfosi', 'Cambiare', 'Pietra', 'Piante'],
            ['Cosmologia del divenire perenne', 'Palingenesi universale ovidiana', 'Fluire instabile delle forme', "Armonia dell'essere mutabile", 'Poesia cosmica']
        ),
        (
            "L'orazione di Ettore contro i presagi avversi: 'Un solo presagio è il migliore...'",
            "Quando Polidamante consiglia la ritirata per un'aquila che perde un serpente, Ettore risponde: 'Un solo presagio è supremo: combattere per la patria!'.",
            ['Presagi', 'Aquila', 'Paura', 'Ritirata', 'Uccelli'],
            ['Rigetto della superstizione fatale', 'Dovere civico supremo', 'Fermezza patriottica indomita', "Parola d'ordine omerica", 'Coraggio della disperazione']
        ),
        (
            "L'appello alla Memoria Eterea dell'Epica",
            "Concludi il corso biennale: gli eroi antichi vivono finché una voce viva ne pronuncia i nomi, risvegliando il fuoco del coraggio e dell'onore nelle nuove generazioni.",
            ['Nomi', 'Eroi', 'Dimenticare', 'Ricordo', 'Fine'],
            ['Custodia del fuoco epico', 'Memoria vivente dei miti', "Resurrezione oratoria dell'antico", 'Eredità della grandezza', 'Fulgore eterno del mito']
        ),
    ],
    "c1": [
        (
            "L'ermeneutica della tragedia greca nella filosofia di G.W.F. Hegel",
            "Esporrai la teoria hegeliana dell'Estetica: la tragedia classica come manifestazione sensibile della collisione tra potenze etiche sostanziali entrambe necessarie.",
            ['Hegel', 'Tragedia', 'Estetica', 'Collisione', 'Ragione'],
            ['Collisione etica hegeliana', "Manifestazione dell'Idea", 'Giustizia sostanziale universale', 'Riconciliazione dello spirito', 'Dialettica tragica']
        ),
        (
            "L'Iliade o il poema della forza secondo Simone Weil",
            'Commenta il celebre saggio del 1940: la forza non è ciò che trionfa, ma ciò che pietrifica sia chi la subisce sia chi la esercita, trasformando gli uomini in cose.',
            ['Simone Weil', 'Forza', 'Iliade', 'Pietra', 'Guerra'],
            ['Poema della forza weiliano', "Cosificazione dell'essere umano", 'Petrificazione del guerriero', 'Imparzialità omerica tragica', 'Grazia e compassione']
        ),
        (
            "Il mito platonico della caverna come allegoria dell'emancipazione ontologica",
            "Ripercorri la linea divisa e il passaggio da Eikasia e Pistis (doxa) a Dianoia e Noesis (episteme): il percorso ascensionale del filosofo verso l'Idea del Bene.",
            ['Platone', 'Caverna', 'Doxa', 'Episteme', 'Sole'],
            ['Ascesa noetica platonica', 'Metafora della linea divisa', "Sole come fonte dell'essere", 'Responsabilità catabatica del saggio', 'Emancipazione politica']
        ),
        (
            'La decostruzione del mito di Edipo nella psicoanalisi freudiana e lacaniana',
            "Dall'interpretazione freudiana del parricidio e dell'incesto alla lettura lacaniana dell'Edipo come iscrizione originaria della Legge del Padre e castrazione simbolica.",
            ['Freud', 'Lacan', 'Complesso di Edipo', 'Padre', 'Madre'],
            ['Iscrizione della Legge del Padre', 'Complesso edipico universale', 'Castrazione simbolica lacaniana', 'Desiderio inconscio primordiale', 'Struttura del soggetto']
        ),
        (
            "L'apologia dell'ospitalità omerica (Xenia) e il sacro del forestiero",
            "Indaga la Xenia nell'epos arcaico: lo straniero è protetto da Zeus Xenios perché chiunque potrebbe essere un dio mascherato venuto a saggiare la giustizia dei mortali.",
            ['Zeus', 'Straniero', 'Xenia', 'Ospitalità', 'Casa'],
            ['Istituzione sacra della Xenia', 'Teofania potenziale dello straniero', 'Zeus Xenios custode', 'Patto ospitale incondizionato', 'Civiltà omerica del dono']
        ),
        (
            'La dialettica del servo-padrone nella Fenomenologia dello Spirito',
            "Dimostra come la lotta a morte per il riconoscimento intersoggettivo rovesci le posizioni: il padrone ozioso regredisce, mentre il servo attraverso il lavoro conquista l'autocoscienza.",
            ['Servo', 'Padrone', 'Lotta', 'Morte', 'Hegel'],
            ['Lotta per il riconoscimento', 'Paura della morte assoluta', 'Formatura del lavoro (Bildung)', 'Autocoscienza liberata', 'Dialettica servo-padrone']
        ),
        (
            'Il Prometeo liberato di Percy Bysshe Shelley: la vittoria del perdono',
            "A differenza del mito eschileo perduto, il dramma romantico mostra Prometeo che ritratta la maledizione contro Giove, trionfando sulla tirannide non con l'odio ma con l'amore.",
            ['Shelley', 'Prometeo', 'Perdono', 'Odio', 'Giove'],
            ['Epos romantico shelleyano', 'Superamento della vendetta', 'Vittoria del perdono rigeneratore', "Trionfo dell'Amore universale", 'Caduta del tiranno celeste']
        ),
        (
            "L'archetipo dell'Ulissismo tra Dante e James Joyce",
            "Metti a confronto l'eroe dantesco punito per aver oltrepassato il confine divino con Leopold Bloom che attraversa la ferialità moderna di Dublino in un'odissea interiore.",
            ['Dante', 'Joyce', 'Ulisse', 'Bloom', 'Dublino'],
            ['Monologo interiore joyciano', 'Folle volo dantesco punito', 'Odissea moderna del quotidiano', 'Epifania letteraria profana', "Trascendenza dell'itineranza"]
        ),
        (
            'Il mito della nascita di Venere e il concetto di Kalokagathia',
            "Dalla Teogonia esiodea al Neoplatonismo di Marsilio Ficino e Botticelli: l'indissolubile unità classica di Bellezza formale e Bontà etica (Kalòs kai Agathòs).",
            ['Venere', 'Botticelli', 'Bellezza', 'Bontà', 'Mare'],
            ['Ideale di Kalokagathia', 'Eros neoplatonico ficiniano', 'Splendore del Bene', 'Teogonia della grazia', 'Ascesa estetica']
        ),
        (
            'La colpa ontologica e il destino in Martin Heidegger: Il detto di Anassimandro',
            "Commenta il più antico frammento filosofico: 'Donde le cose hanno la loro nascita, là hanno anche la dissoluzione secondo la necessità; esse pagano infatti l'ammenda...'.",
            ['Anassimandro', 'Heidegger', 'Frammento', 'Colpa', 'Tempo'],
            ['Detto di Anassimandro heideggeriano', "Debito dell'essere presente", 'Ordine del tempo cosmico', 'Riconciliazione col Fondamento', 'Disvelamento aurorale']
        ),
        (
            "L'ira funesta di Achille come tema strutturante dell'intera Iliade",
            "Dimostra come la Menis (ira sacra) non sia un semplice scatto d'ira individuale, ma una frattura cosmica che sconvolge il cosmo morale degli eroi finché non viene pacificata.",
            ['Ira', 'Achille', 'Menis', 'Iliade', 'Arrabbiato'],
            ['Menis cosmica archetipica', 'Struttura compositiva omerica', "Rottura dell'ordine comunitario", 'Pacificazione nel lutto condiviso', 'Mistica del poema']
        ),
        (
            "La teologia politica dell'Orestea di Eschilo e la nascita dell'Areopago",
            "Analizza la trilogia eschilea: il superamento della vendetta arcaica di sangue (Erinni) attraverso l'istituzione del tribunale democratico della città (Eumenidi).",
            ['Eschilo', 'Oreste', 'Erinni', 'Vendetta', 'Atene'],
            ['Transizione dallo ius talionis', "Istituzione dell'Areopago democratico", 'Trasfigurazione delle Erinni in Eumenidi', 'Trionfo della giustizia cittadina', 'Palingenesi civica']
        ),
        (
            "Il mito del doppio e l'enigma di Narciso in Paul Valéry e Rilke",
            "Indaga attraverso la poesia moderna l'angoscia della scissione interiore: guardarsi vivere invece di vivere, la poesia che si fa specchio mortale del proprio stesso canto.",
            ['Narciso', 'Valéry', 'Rilke', 'Specchio', 'Poesia'],
            ["Scissione dell'autocoscienza", "Vertigine dell'auto-riflessione", 'Narciso moderno valéryano', 'Canto orfico rilkeano', 'Abisso della rappresentazione']
        ),
        (
            'La pietas virgiliana come dolore del mondo (Sunt lacrimae rerum)',
            "Nel I libro dell'Eneide, Enea contempla le pitture della guerra di Troia a Cartagine esclamando: 'Sunt lacrimae rerum et mentem mortalia tangunt'. Commenta.",
            ['Virgilio', 'Lacrime', 'Cartagine', 'Troia', 'Dolore'],
            ['Sunt lacrimae rerum virgiliano', 'Melanconia cosmica della storia', 'Compassione universale per i vinti', 'Partecipazione al dramma umano', 'Pietas come sofferenza']
        ),
        (
            "L'archetipo dell'eroe fondatore e il patto sociale in Thomas Hobbes",
            "Come il mito del Leviatano riprende la mostruosità biblica per fondare l'ordine politico: la rinuncia alla libertà illimitata dello stato di natura in cambio della pace sovrana.",
            ['Hobbes', 'Leviatano', 'Stato di natura', 'Paura della morte', 'Patto'],
            ['Costruzione del Leviatano sovrano', 'Stato di natura belluino', 'Uscita dal caos primordiale', 'Patto di soggezione e unione', 'Monopolio della spada legale']
        ),
        (
            "La morte di Socrate nel Fedone: l'immortalità dell'anima e il gallo ad Asclepio",
            "Le ultime parole del filosofo morente: 'Critone, dobbiamo un gallo ad Asclepio: dateglielo, non ve ne dimenticate!'. La morte come guarigione finale dell'anima dal corpo.",
            ['Socrate', 'Fedone', 'Gallo', 'Asclepio', 'Cicuta'],
            ['Ultime parole socratiche', 'Gallo ad Asclepio come guarigione', "Immortalità noetica dell'anima", 'Serenità di fronte alla morte', 'Eredità filosofica suprema']
        ),
        (
            'Il viaggio di Gilgamesh e il rifiuto tragico della morte',
            "Dal più antico poema dell'umanità: il re di Uruk che piange l'amico Enkidu e attraversa le acque della morte per cercare la pianta dell'immortalità, fallendo nobilmente.",
            ['Gilgamesh', 'Enkidu', 'Morte', 'Uruk', 'Pianta'],
            ['Epos sumero-babilonese di Gilgamesh', 'Angoscia della finitudine biologica', 'Rifiuto tragico della mortalità', 'Perdita del fiore della giovinezza', 'Ritorno alle mura della città']
        ),
        (
            "La desacralizzazione del mito nell'illuminismo di Horkheimer e Adorno",
            "Nella Dialettica dell'Illuminismo, analizza l'incontro tra Ulisse e le Sirene: l'eroe borghese legato all'albero maestro che consuma esteticamente il mito mentre gli operai remano muti.",
            ['Adorno', 'Horkheimer', 'Sirene', 'Ulisse', 'Illuminismo'],
            ["Dialettica dell'Illuminismo", 'Ulisse prototipo borghese', 'Autocostrizione del soggetto', 'Consumo estetico anestetizzato', 'Lavoro sottomesso dei rematori']
        ),
        (
            'Il sacrificio di Abramo e la sospensione teleologica della morale in Kierkegaard',
            'Analizza Timore e Tremore: la contraddizione assoluta tra il dovere etico universale (non uccidere il figlio) e il comando divino singolare che richiede la fede paradossale.',
            ['Kierkegaard', 'Abramo', 'Isacco', 'Etica', 'Fede'],
            ["Sospensione teleologica dell'etico", 'Paradosso assoluto della fede', 'Solitudine angosciosa del cavaliere', 'Trascendenza del comando divino', 'Singolarità davanti a Dio']
        ),
        (
            "L'orazione per l'Agorà Classica: il ritorno del Mito nel Cuore Moderno",
            "Pronuncia l'arringa magistrale che consacra il mito classico non come reliquia archeologica, ma come alfabeto eterno dei desideri, delle colpe e delle speranze umane.",
            ['Mito', 'Passato', 'Museo', 'Favole', 'Fine'],
            ['Alfabeto ontologico universale', 'Vigore imperituro del mito classico', 'Luce per la coscienza contemporanea', 'Agorà eterna dello spirito', "Magistero dell'Oratore Epico"]
        ),
    ],
    "c2": [
        (
            "L'ontologia dell'Ananke e l'abisso del Fato nell'epos arcaico",
            'Dimostra di fronte al consesso supremo come il Fato (Ananke o Moira) non sia una volontà personale divina, ma la necessità cieca, ontologica e pre-cosmica a cui gli stessi dèi sono sottomessi.',
            ['Fato', 'Ananke', 'Dèi', 'Moira', 'Necessità'],
            ['Necessità ontologica cieca (Ananke)', 'Invalicabilità della Moira arcaica', 'Subordinazione degli immortali al Fato', "Tragicità metafisica dell'essere", "Abisso primordiale dell'origine"]
        ),
        (
            "La de-costruzione della grandezza omerica: l'anti-eroe Tersite",
            "Rileggi l'episodio del II libro dell'Iliade: Tersite, il soldato deforme che urla la verità contro la vanità dei re achei, bastonato da Odisseo tra le risa della folla complice.",
            ['Tersite', 'Odisseo', 'Bastone', 'Brutto', 'Re'],
            ['Parresìa plebea di Tersite', 'Verità sovversiva dei subalterni', 'Violenza repressiva aristocratica', "Decostruzione dell'epos eroico", "Tragicità dell'emarginato veritiero"]
        ),
        (
            "L'archetipo dell'Omphalos: Delphi e l'ombelico del mondo",
            "Evoca il santuario apollineo di Delfi: il punto sacro dove le due aquile di Zeus si incontrarono, e il monito eterno 'Gnothi seauton' (Conosci te stesso) inciso sul frontone.",
            ['Delfi', 'Apollo', 'Ombelico', 'Pizia', 'Conosci te stesso'],
            ['Omphalos cosmico primordiale', 'Gnothi seauton apollineo', 'Misura del limite umano', 'Responso oracolare oracolare', "Centro sacro dell'ecumene"]
        ),
        (
            "La catarsi tragica come rigenerazione dell'ordine cosmico e civile",
            "Dimostra come la rappresentazione teatrale nell'Atene di Pericle non fosse mero spettacolo estetico ma liturgia civica di risanamento delle ferite della polis e rigenerazione del nomos.",
            ['Teatro', 'Atene', 'Spettacolo', 'Catarsi', 'Polis'],
            ['Liturgia civica catartica', 'Risanamento delle lacerazioni sociali', 'Teatro come presidio democratico', 'Purificazione della coscienza collettiva', 'Eudaimonia repubblicana']
        ),
        (
            "Il silenzio dell'Eroe nella tragedia eschilea: la solitudine di Prometeo",
            "Analizza la celebre tecnica drammaturgica di Eschilo: il lungo silenzio attonito dell'eroe sulla scena prima di prorompere nella lamentazione cosmica rivolta all'Etere sacro.",
            ['Silenzio', 'Eschilo', 'Prometeo', 'Parlare', 'Scena'],
            ['Silenzio tragico inaugurale', 'Sospensione attonita della parola', "Lamento cosmico all'Etere", 'Solitudine maestosa del titano', "Drammaturgia dell'indicibile"]
        ),
        (
            "La dialettica dell'invidia degli dèi (Phthonos theon) in Erodoto",
            "Analizza attraverso le Storie l'assioma tragico della storiografia greca: la divinità abbatte sistematicamente ciò che si innalza troppo in altezza, punendo l'eccesso di felicità umana.",
            ['Erodoto', 'Invidia degli dèi', 'Caduta', 'Creso', 'Troppa fortuna'],
            ['Phthonos theon erodoteo', 'Fragilità della prosperità terrena', 'Caduta ineluttabile dei potenti', "Solone e l'ammonimento a Creso", 'Nemesi cosmica']
        ),
        (
            "L'aporia dell'Edipo a Colono: la trasfigurazione del reietto in salvatore",
            'Nel dramma finale di Sofocle, il vecchio Edipo cieco, lebbroso e bandito da tutti diventa, accogliendo la propria morte sacra, il custode benevolo e protettore perpetuo di Atene.',
            ['Edipo a Colono', 'Cieco', 'Tomba', 'Atene', 'Mostro'],
            ['Trasfigurazione del pharmakos', 'Santità sacrificale del reietto', 'Sepoltura segreta protettiva', 'Grazia tragica sofoclea', 'Superamento della colpa']
        ),
        (
            'Il sacrificio cosmico nella cosmogonia orfica: Dioniso Zagreo',
            "Ripercorri il mito misterico orfico: il fanciullo divino smembrato dai Titani le cui ceneri, fulminate da Zeus, generano l'umanità, divisa perennemente tra scintilla celeste e corpo titanico.",
            ['Dioniso', 'Titani', 'Smembrato', 'Orfismo', 'Ceneri'],
            ['Smembrimento di Dioniso Zagreo', 'Scintilla divina e fardello titanico', 'Misteriosofia orfica soteriologica', "Palingenesi dell'anima incarnata", "Lacerazione ontologica dell'umano"]
        ),
        (
            "L'apologia della virtù disperata nel De Rerum Natura di Lucrezio",
            "Commenta il poema cosmico: liberare l'uomo dal terrore degli dèi e dell'aldilà attraverso la consapevolezza materialista atomica, contemplando il cosmo con animo sereno.",
            ['Lucrezio', 'Atomi', 'Paura degli dèi', 'Morte', 'Poema'],
            ['Atarassia materialista lucreziana', 'Dissoluzione del terrore religioso', 'Epos atomistico universale', 'Serenità del saggio epicureo', "Luce contro l'oscurità del mito"]
        ),
        (
            "La parresìa di Cassandra e l'epistemologia della follia profetica",
            "Analizza l'Agamennone di Eschilo: Cassandra che vede dettagliatamente l'omicidio imminente e la propria fine, condannata dal dio a non essere creduta perché rifiutò il suo abbraccio.",
            ['Cassandra', 'Agamennone', 'Vedere il futuro', 'Pazza', 'Apollo'],
            ['Follia mantica apollinea', "Tragedia dell'enunciazione inascoltata", 'Visione del massacro domestico', 'Parresìa profetica fatale', 'Purezza della vittima']
        ),
        (
            "L'enigma del ritorno: il Nostos come compimento e lacerazione",
            'Dimostra come il ritorno a casa (nostos) non sia mai una restaurazione indolore del passato, ma un riconoscimento traumatico: il ritorno a Itaca avviene nel travestimento e nella cenere.',
            ['Nostos', 'Ritorno', 'Casa', 'Itaca', 'Ritrovare tutto'],
            ['Nostos omerico traumatico', 'Irreversibilità del tempo trascorso', 'Riconoscimento ferito', 'Lacerazione del ritorno', "Pellegrinaggio perenne dell'essere"]
        ),
        (
            "La de-costruzione della titanomachia in Esiodo e l'ordine del Diritto (Dike)",
            "Attraverso Le opere e i giorni, illustra il passaggio cruciale dal trionfo della forza violenta bruta all'epifania di Dike, la figlia di Zeus che protegge gli umili dalle fauci dei potenti.",
            ['Esiodo', 'Dike', 'Giustizia', 'Lupo e sparviero', 'Zeus'],
            ['Epifania di Dike esiodea', 'Primato del diritto sulla violenza', "Favola dello sparviero e dell'usignolo", "Lavoro nobilitante dell'uomo", "Trionfo dell'equità cosmica"]
        ),
        (
            "L'archetipo dell'Inno omerico a Demetra e il mistero eleusino",
            "La discesa di Persefone nell'Ade e il lutto cosmico della madre terra: la nascita dei misteri di Eleusi dove l'iniziato vince il terrore della morte contemplando la spiga di grano recisa.",
            ['Demetra', 'Persefone', 'Eleusi', 'Grano', 'Misteri'],
            ['Misteri eleusini salvifici', 'Ierofania della spiga recisa', 'Riconciliazione col ciclo cosmico', "Superamento dell'angoscia mortale", 'Inno a Demetra sacro']
        ),
        (
            "La parodia del sacro e la satira lucianea degli dèi dell'Olimpo",
            "Nei Dialoghi degli dèi di Luciano di Samosata, l'Olimpo viene demistificato: divinità vanitose, litigiose e impotenti che riflettono in farsa le miserie della corte imperiale romana.",
            ['Luciano', 'Dèi', 'Ridere', 'Olimpo', 'Presa in giro'],
            ['Satira dissacrante lucianea', "Demistificazione dell'Olimpo", 'Ironia ellenistica liberatoria', 'Tramonto delle mitologie arcaiche', 'Disincanto razionalista']
        ),
        (
            "L'archetipo dell'eroe solare e la sua caduta: il mito di Fetonte",
            "Fetonte che pretende di guidare il carro infuocato del padre Apollo, bruciando la terra e precipitando nell'Eridano. L'epitaffio sublime: 'Cadde, ma dopo aver osato grandi cose'.",
            ['Fetonte', 'Carro del sole', 'Bruciare', 'Cadere', 'Fiume'],
            ['Magnis tamen excidit ausis', "Caduta dell'audacia solare", 'Hybris giovanile gloriosa', 'Eridano funerario', 'Sublime del fallimento']
        ),
        (
            "L'apologia della memoria poetica contro l'amnesia del Lete",
            "Nelle lamine d'oro orfiche ritrovate nelle tombe greche, l'anima rifiuta di bere all'acqua dell'oblio (Lete) per abbeverarsi alla fredda sorgente della Memoria (Mnemosyne).",
            ['Lete', 'Oblio', 'Bere', 'Mnemosyne', 'Memoria'],
            ['Sorgente di Mnemosyne', "Rifiuto dell'amnesia del Lete", 'Lamine auree orfiche', 'Salvezza della consapevolezza', "Resurrezione perenne dell'anima"]
        ),
        (
            "La lacerazione di Aiace e la solitudine dell'onore arcaico",
            "Analizza il monologo dell'inganno e il suicidio di Aiace sulla riva del mare: quando il mondo delle virtù nobili viene soppiantato dalla politica cinica dei sofisti, l'eroe sceglie l'abisso.",
            ['Aiace', 'Suicidio', 'Spada', 'Mondo cambiato', 'Onore'],
            ['Frattura tra epos e politica', 'Rifiuto del compromesso sofistico', 'Solitudine tragica assoluta', 'Consacrazione della spada nemica', "Morte sull'elsa della fedeltà"]
        ),
        (
            "Il canto dell'Oratore Cosmico: il Logos che abbraccia il Mito",
            'Dimostra con maestria oratoria che la filosofia senza mito è intelletto sterile, ma il mito senza filosofia è cecità irrazionale. La parola suprema unisce narrazione e verità.',
            ['Mito', 'Filosofia', 'Logos', 'Ragione', 'Favola'],
            ['Sintesi suprema di Mythos e Logos', 'Fecondità della narrazione simbolica', "Rigore dell'argomentazione noetica", "Magistero dell'Oratore Cosmico", 'Compiutezza della voce']
        ),
        (
            "L'apoteosi dell'anima eroica nel Somnium Scipionis ciceroniano",
            "Scipione Emiliano incontra l'avo Africano nella Via Lattea: la rivelazione della ricompensa immortale per chi serve la patria terrena con giustizia e virtù.",
            ['Scipione', 'Cicerone', 'Via Lattea', 'Stelle', 'Patria'],
            ['Somnium Scipionis ciceroniano', 'Cosmologia stoica astrale', 'Immortalità dei difensori della patria', 'Piccolezza della gloria terrena', 'Armonia delle sfere celesti']
        ),
        (
            "L'Inno all'Eternità del Verbo Epico: il Congedo Supremo dell'Oratore",
            "Chiudi il magistero dell'Epica Classica: le fiamme hanno arso Troia, l'erba copre Micene, ma la parola dell'Oratore continua a far tremare la terra e risplendere gli dèi.",
            ['Fine', 'Troia', 'Cenere', 'Dèi', 'Voce'],
            ['Eternità del Verbo oratorio', 'Trionfo della voce immortale', "Apoteosi dell'epos classico", "Luce perenne dell'ideale", 'Congedo supremo solenne']
        ),
    ],
}
