# Mazzo: avventura
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            'Il volo in mongolfiera sopra i tetti',
            "Sei a bordo di un grande pallone colorato che si alza nel cielo all'alba. Descrivi le case che diventano piccole come giocattoli sotto di te.",
            ['Mongolfiera', 'Volare', 'Pallone', 'Cielo', 'Piccole'],
            ['Cesto di vimini', 'Brezza', 'Alba', 'Orizzonte', 'Panorama']
        ),
        (
            'La notte in tenda sotto le stelle',
            'Hai montato la tua tenda verde nel prato vicino al bosco. Racconta la magia di addormentarsi ascoltando il canto dei grilli e guardando le stelle.',
            ['Tenda', 'Bosco', 'Dormire', 'Notte', 'Paura'],
            ['Sacco a pelo', 'Grilli', 'Costellazioni', 'Lucciole', 'Avventura']
        ),
        (
            'La scalata della collina dei papaveri',
            'Cammini con lo zainetto sulle spalle per raggiungere la croce di legno in cima alla collina. Spiega la soddisfazione di ammirare la vallata fiorita.',
            ['Collina', 'Zaino', 'Salire', 'Fatica', 'Fiori'],
            ['Papaveri', 'Vetta', 'Respiro', 'Vallata', 'Conquista']
        ),
        (
            "Il naufragio sull'isola delle noci di cocco",
            'Sei approdato su una spiaggia di sabbia bianca dorata con alte palme. Trova una noce di cocco per dissetarti dopo la tempesta marina.',
            ['Isola', 'Naufragio', 'Sabbia', 'Cocco', 'Palma'],
            ['Spiaggia', 'Onde', 'Dissetarsi', 'Rifugio', 'Sopravvivenza']
        ),
        (
            'La zattera di tronchi sul ruscello',
            'Hai legato quattro rami robusti con una corda per far galleggiare una foglia e un soldatino. Descrivi il viaggio del piccolo battello tra i sassi.',
            ['Zattera', 'Tronchi', 'Fiume', 'Corda', 'Acqua'],
            ['Corrente', 'Navigazione', 'Galleggiare', 'Rapide', 'Ruscello']
        ),
        (
            'La mappa del tesoro disegnata col carbone',
            'Trovi un vecchio foglio bruciacchiato con una bussola e venti passi verso la grande quercia. Raduna gli amici per la ricerca del forziere.',
            ['Mappa', 'Tesoro', 'Passi', 'Albero', 'Cercare'],
            ['Bussola', 'Forziere', 'Punti cardinali', 'Esplorazione', 'Segreto']
        ),
        (
            "L'esplorazione della grotta misteriosa",
            "Accendi la torcia ed entri nella caverna di roccia fresca: gocce d'acqua cadono dalle stalattiti come perle lucenti. Guarda le impronte sul fango.",
            ['Grotta', 'Buio', 'Torcia', 'Roccia', 'Paura'],
            ['Stalattiti', 'Gocce', 'Eco', 'Fascio di luce', 'Meraviglia']
        ),
        (
            'Il ponte tibetano sospeso sul torrente',
            "Metti i piedi sulle assi oscillanti tenendoti forte alle funi d'acciaio. Fai coraggio al tuo amico spiegando che guardare avanti scaccia le vertigini.",
            ['Ponte', 'Cadere', 'Funi', 'Acqua sotto', 'Paura'],
            ['Equilibrio', 'Coraggio', 'Passo sicuro', 'Fiume', 'Traguardo']
        ),
        (
            'La traversata del deserto di sabbia dorata',
            "Sei in groppa a un dromedario che cammina dondolando tra le dune calde del deserto. Descrivi il miraggio di un'oasi con palme e acqua fresca.",
            ['Deserto', 'Sabbia', 'Cammello', 'Caldo', 'Sete'],
            ['Duna', 'Oasi', 'Carovana', 'Vento caldo', 'Miraggio']
        ),
        (
            'La canoa sul lago trasparente',
            'Pagaia silenziosamente sulle acque calme del lago alpino specchiandoti nelle montagne innevate. Guarda i pesci argentati nuotare sul fondo.',
            ['Canoa', 'Pagaia', 'Lago', 'Barca', 'Acqua'],
            ["Specchio d'acqua", 'Montagne', 'Scivolare', 'Silenzio', 'Pescetti']
        ),
        (
            'La scoperta delle impronte di dinosauro',
            "Camminando lungo una parete di roccia trovi l'orma gigante di un triceratopo impressa nella pietra secoli fa. Chiama tutti meravigliato.",
            ['Dinosauro', 'Impronta', 'Pietra', 'Grande', 'Mostro'],
            ['Orma fossile', 'Preistoria', 'Roccia antica', 'Scienziato', 'Scoperta']
        ),
        (
            'Il segnale di fumo sulla collina',
            "Sei un esploratore che fa segnali di fumo con una coperta per comunicare con il campo base dall'altra parte della vallata.",
            ['Fumo', 'Fuoco', 'Coperta', 'Segnale', 'Campo'],
            ['Comunicazione', 'Messaggio', 'Campobase', 'Vallata', 'Saluto']
        ),
        (
            "Il nido dell'aquila sulla parete rocciosa",
            'Punti il binocolo verso la cengia della montagna e vedi due aquilotti che aspettano il ritorno della madre. Descrivi il battito delle ali maestre.',
            ['Aquila', 'Nido', 'Montagna', 'Vedere', 'Piccoli'],
            ['Binocolo', 'Cengia rocciosa', 'Volo fiero', 'Ali spiegate', 'Natura selvaggia']
        ),
        (
            'Il rifugio di rami nel bosco fitto',
            'Costruisci una capanna di fronde e corteccia per ripararti da un acquazzone improvviso. Invita i compagni a dividere lo spazio accogliente.',
            ['Capanna', 'Rami', 'Pioggia', 'Bosco', 'Costruire'],
            ['Rifugio', 'Fronde', 'Profumo di pino', 'Asciutto', 'Tana']
        ),
        (
            'La bussola che punta sempre a Nord',
            "Tieni sul palmo della mano una bussola d'ottone e guarda l'ago magnetico che oscilla finché non trova il Nord. Spiega come non perdersi mai.",
            ['Bussola', 'Nord', 'Ago', 'Perdersi', 'Mano'],
            ['Magnete', 'Orientamento', 'Punti cardinali', 'Guida', 'Strada sicura']
        ),
        (
            'Il richiamo del gufo nella notte alpina',
            'Seduto attorno al fuoco del bivacco, imita il verso del gufo reale ascoltando la risposta che rimbalza tra le cime degli abeti.',
            ['Gufo', 'Verso', 'Fuoco', 'Notte', 'Paura'],
            ['Bivacco', 'Eco dei boschi', 'Richiamo', 'Abeti', 'Magia notturna']
        ),
        (
            'Il sentiero delle cascate fragorose',
            "Cammini dietro la cortina d'acqua di una cascata scrosciante, sentendo gli spruzzi freschi bagnarti le guance e ridere con gli amici.",
            ['Cascata', 'Acqua', 'Bagnato', 'Rumore', 'Cadere'],
            ['Spruzzi', "Arcobaleno d'acqua", 'Roccia umida', 'Frastuono', 'Freschezza']
        ),
        (
            'Il vecchio diario di bordo trovato nella cabina',
            'Apri un quaderno ingiallito con la copertina di cuoio trovato in un relitto veliero. Leggi la prima pagina sul vento di tempesta.',
            ['Diario', 'Nave', 'Vecchio', 'Leggere', 'Capitano'],
            ['Pagine ingiallite', 'Inchiostro di china', 'Rotta oceanica', 'Memoria marinara', 'Relitto']
        ),
        (
            'La slitta trainata dai cani sulla neve',
            'Sei alla guida di una muta di husky che corre veloce sulla distesa di ghiaccio artico. Incita i cani con richiami dolci e fieri.',
            ['Slitta', 'Cani', 'Neve', 'Freddo', 'Correre'],
            ['Husky', 'Banchisa', 'Corsa fiera', 'Ghiaccio', 'Vento polare']
        ),
        (
            'Il manifesto dei piccoli esploratori del mondo',
            'Concludi il modulo: esplorare non significa andare per forza sulla Luna, ma guardare ogni albero, ogni sentiero e ogni compagno con occhi curiosi.',
            ['Luna', 'Viaggio', 'Lontano', 'Grandi', 'Fine'],
            ['Sguardo curioso', 'Meraviglia quotidiana', "Spirito d'avventura", 'Cuore aperto', 'Scoperta perenne']
        ),
    ],
    "a2": [
        (
            'La spedizione nella giungla alla ricerca della città perduta',
            'Sei a capo di un gruppo di giovani archeologi con machete e zaini pesanti. Fai strada tra le liane verso le rovine maya nascoste dalla vegetazione.',
            ['Giungla', 'Maya', 'Rovine', 'Verde', 'Machete'],
            ['Città perduta', 'Liane', 'Fascino archeologico', 'Vegetazione impenetrabile', 'Piramidi']
        ),
        (
            "L'attraversamento dello stretto di Magellano",
            "Sei al timone della Victoria nel 1520 tra fiordi gelidi e scogli affioranti. Sprona l'equipaggio spiegando che oltre quel labirinto si apre il Mare del Sud.",
            ['Magellano', 'Stretto', 'Nave', 'Freddo', 'Oceano'],
            ['Passaggio marittimo', 'Fiordi scoscesi', 'Oceano Pacifico', 'Costanza marinara', 'Circumnavigazione']
        ),
        (
            "L'ascesa del vulcano attivo nella notte",
            'Cammini sul sentiero di cenere nera dello Stromboli mentre la bocca del cratere lancia zampilli di lava incandescente contro il cielo buio.',
            ['Vulcano', 'Lava', 'Cenere', 'Fuoco', 'Stromboli'],
            ['Cratere ardente', 'Sciara del fuoco', 'Zampilli incandescenti', 'Lapilli', 'Sublime naturale']
        ),
        (
            'La traversata a piedi del deserto del Sahara',
            "Con la carovana tuareg affronti la tempesta di sabbia (Ghibli) avvolgendo il velo blu intorno al viso. Descrivi la tenacia dell'uomo di fronte all'infinito.",
            ['Sahara', 'Sabbia', 'Vento', 'Tuareg', 'Sete'],
            ['Tempesta di sabbia', 'Tagelmust blu', 'Immensità desertica', 'Resistenza fiera', 'Carovana millenaria']
        ),
        (
            "L'immersione tra i coralli della Grande Barriera",
            "Con maschera e bombole d'ossigeno scendi negli abissi australiani tra anemoni, pesci pagliaccio e mante giganti che volano sott'acqua.",
            ['Sub', 'Pesci', 'Coralli', 'Bombole', 'Australia'],
            ['Barriera corallina', 'Manta gigante', 'Abisso colorato', 'Respiro sottomarino', 'Santuario marino']
        ),
        (
            'Il treno transiberiano attraverso le foreste di betulle',
            "Dal finestrino della carrozza vedi sfilare per giorni l'infinita taiga russa innevata e le acque profonde del lago Baikal ghiacciato.",
            ['Treno', 'Russia', 'Freddo', 'Finestrino', 'Neve'],
            ['Transiberiana', 'Taiga sconfinata', 'Lago Baikal', "Rotaie d'acciaio", 'Viaggio continentale']
        ),
        (
            'Il salvataggio con la liana sul burrone profondo',
            'Un compagno di escursione è scivolato su una sporgenza di roccia. Trova il modo di lanciare una fune assicurandoti a un tronco solido per trarlo in salvo.',
            ['Cadere', 'Burrone', 'Fune', 'Salvare', 'Tirare'],
            ['Ancoraggio sicuro', 'Pronto intervento', 'Solidarietà montana', 'Nervo saldo', 'Salvataggio riuscito']
        ),
        (
            "L'incontro con una tribù nomade dell'Amazzonia",
            'Entri in contatto con un popolo indigeno che non ha mai visto il telefono né le automobili. Comunica con sguardi, sorrisi e donando sale e semi.',
            ['Indigeni', 'Tribù', 'Amazzonia', 'Strani', 'Telefono'],
            ['Incontro fraterno', 'Linguaggio del sorriso', 'Ponte culturale', 'Rispetto ancestrale', 'Ospitalità della foresta']
        ),
        (
            'La navigazione notturna guidata dalla Stella Polare',
            "Il GPS di bordo si è scaricato e le luci della costa sono lontane. Insegna al mozzo a individuare l'Orsa Minore per mantenere la rotta verso casa.",
            ['Stella Polare', 'GPS scarico', 'Navigare', 'Notte', 'Mare'],
            ['Orsa Minore', 'Orientamento astronomico', 'Rotta celeste', 'Bussola naturale', 'Navigazione antica']
        ),
        (
            'La discesa delle rapide del fiume Colorado col gommone',
            'Nel maestoso Grand Canyon, affronti le acque impetuose del fiume pagaiando a ritmo cadenzato per evitare i massi giganti e i gorghi.',
            ['Rafting', 'Grand Canyon', 'Fiume', 'Pagaiare', 'Cadere'],
            ['Rapide tumultuose', 'Gole scoscese', "Coordinazione d'equipaggio", 'Fiume Colorado', 'Ebbrezza fluviale']
        ),
        (
            "L'esplorazione del castello medievale abbandonato",
            'Salendo la scala a chiocciola della torre diroccata, scopri un archivio di vecchie mappe e balestre arrugginite affacciato sulle colline nebbiose.',
            ['Castello', 'Torre', 'Scale', 'Fantasmi', 'Vecchio'],
            ['Scala a chiocciola', 'Fascino medievale', 'Feritoia', 'Archivio diroccato', 'Paesaggio nebbioso']
        ),
        (
            'Il volo in aliante senza motore sulle Alpi',
            'Sfrutti le correnti termiche ascendenti per volare in cerchio insieme ai falchi sfiorando le pareti di roccia del Monte Rosa nel silenzio puro.',
            ['Aliante', 'Volare', 'Motore', 'Vento', 'Alpi'],
            ['Corrente termica ascensionale', 'Volo a vela', "Silenzio dell'aria", 'Prospettiva aerea', 'Planata sublime']
        ),
        (
            'La ricerca dei fossili nel canyon pietroso',
            'Col martello da geologo e lo scalpello stacchi una lastra di scisto scoprendo una conchiglia ammonite a spirale intatta dopo cento milioni di anni.',
            ['Fossile', 'Sasso', 'Martello', 'Rompere', 'Conchiglia'],
            ['Ammonite a spirale', 'Lastra di scisto', 'Tempo geologico', 'Pazienza dello scavo', 'Meraviglia litica']
        ),
        (
            'La traversata della steppa mongola a cavallo',
            'Cavalchi con i nomadi delle yurte tra pascoli infiniti sotto il grande cielo blu della Mongolia, dividendo il tè caldo al latte di giumenta.',
            ['Mongolia', 'Cavallo', 'Tenda', 'Correre', 'Prato'],
            ['Yurta tradizionale', 'Steppa sconfinata', 'Cavalcatura fiera', 'Ospitalità nomade', 'Orizzonte infinito']
        ),
        (
            "L'avventura polare: dormire nell'igloo di blocchi di ghiaccio",
            "Costruisci con la sega da neve un rifugio a cupola spiegando come la neve compatta isoli dal vento gelido a meno trenta gradi all'esterno.",
            ['Igloo', 'Ghiaccio', 'Freddo', 'Polo', 'Neve'],
            ['Isolamento termico', 'Cupola di neve', 'Inuit', 'Rifugio artico', 'Calore interno']
        ),
        (
            "L'esplorazione della città sotterranea di Derinkuyu",
            'In Cappadocia scendi per otto piani scavati nel tufo vulcanico tra pozzi di ventilazione, porte di macina circolari e stalle nascoste.',
            ['Derinkuyu', 'Sotterraneo', 'Scavare', 'Cappadocia', 'Buio'],
            ['Città ipogea', 'Tufo vulcanico', 'Porta a mola', 'Rifugio cristiano', 'Architettura rupestre']
        ),
        (
            'Il viaggio in bicicletta lungo il Danubio',
            "Dalle sorgenti nella Foresta Nera fino al Mar Nero pedalando per tremila chilometri attraverso dieci paesi e capitali storiche dell'Europa.",
            ['Bici', 'Danubio', 'Fiume', 'Pedalare', 'Europa'],
            ['Ciclovia fluviale', 'Foresta Nera', 'Fiume transnazionale', 'Viaggio lento', 'Incontro di popoli']
        ),
        (
            'La traversata aerea della Manica di Louis Blériot (1909)',
            'A bordo del fragile monoplano di legno e tela senza bussola né galleggianti, decolli da Calais atterrando sui prati verdi di Dover.',
            ['Blériot', 'Aereo', 'Manica', 'Inghilterra', 'Francia'],
            ['Monoplano storico', 'Volo sulla Manica', 'Falesie bianche di Dover', 'Coraggio pionieristico', "Conquista dell'aria"]
        ),
        (
            "L'incontro con le balene giganti nel mare d'Islanda",
            'Dalla prua del battello di legno vedi emergere la schiena lucida di una megattera che soffia una nuvola di vapore prima di immergersi con la coda.',
            ['Balena', 'Mare', 'Islanda', 'Pesce grande', 'Barca'],
            ['Megattera oceanica', 'Soffio di vapore', 'Coda a farfalla', 'Incontro maestoso', "Respiro dell'abisso"]
        ),
        (
            "Il codice d'onore dell'esploratore moderno",
            'Concludi il modulo: un vero viaggiatore non lascia tracce del suo passaggio se non le orme delle scarpe, e non porta via nulla se non ricordi e amicizia.',
            ['Turista', 'Portare via', 'Sporcare', 'Foto', 'Fine'],
            ['Impronta ecologica minima', 'Rispetto dei luoghi sacri', 'Viaggio consapevole', 'Custodia del mondo', 'Spirito di fratellanza']
        ),
    ],
    "b1": [
        (
            'La spedizione Endurance di Ernest Shackleton in Antartide (1914)',
            "La nave stritolata dai ghiacci del Mare di Weddell costringe l'equipaggio a mesi di sopravvivenza sulla banchisa. Guida i tuoi marinai verso la salvezza senza perdere un solo uomo.",
            ['Shackleton', 'Endurance', 'Ghiaccio', 'Naufragio', 'Freddo'],
            ['Leadership carismatica', 'Banchisa polare', "Isola dell'Elefante", 'Scialuppa James Caird', 'Salvezza miracolosa']
        ),
        (
            'La tragica sfida per il Polo Sud: Amundsen versus Scott (1911)',
            "Metti a confronto la pianificazione meticolosa del norvegese con gli sci e gli husky e il drammatico fallimento dell'inglese Robert Falcon Scott morto nella tenda ghiacciata.",
            ['Amundsen', 'Scott', 'Polo Sud', 'Cani', 'Morire'],
            ['Pianificazione logistica', 'Dramma della tenda', 'Ultimo diario di Scott', 'Conquista del Polo', 'Eroismo disperato']
        ),
        (
            'La discesa nella Fossa delle Marianne del batiscafo Trieste (1960)',
            "Jacques Piccard e Don Walsh scendono a quasi undicimila metri di profondità nell'abisso oceanico sfidando una pressione titanica che piega l'acciaio.",
            ['Fossa delle Marianne', 'Piccard', 'Abisso', 'Profondo', 'Sottomarino'],
            ['Batiscafo Trieste', 'Pressione idrostatica titanica', 'Abisso Challenger', 'Pesce piatto sul fondo', 'Frontiera oceanica']
        ),
        (
            'Il viaggio solitario di Thor Heyerdahl sul Kon-Tiki (1947)',
            "Attraversare cinquemila miglia dell'Oceano Pacifico su una zattera di tronchi di balsa per dimostrare che gli indigeni del Sudamerica potevano colonizzare la Polinesia.",
            ['Kon-Tiki', 'Heyerdahl', 'Zattera', 'Pacifico', 'Tronchi'],
            ['Navigazione transoceanica', 'Balsa e canapa', 'Archeologia sperimentale', 'Correnti marine', 'Audacia scientifica']
        ),
        (
            "L'ascesa del K2 della spedizione italiana del 1954: Lacedelli e Compagnoni",
            "Sulla seconda montagna più alta e pericolosa della terra, analizza l'eroico bivacco all'addiaccio a ottomila metri di Walter Bonatti che consentì la vittoria finale.",
            ['K2', 'Bonatti', 'Compagnoni', 'Montagna', 'Ghiaccio'],
            ['Bivacco a ottomila metri', 'Sacrificio di Bonatti', 'Vetta del K2', 'Zona della morte', 'Epopea alpinistica']
        ),
        (
            'La circumnavigazione in solitaria di Joshua Slocum sullo Spray (1895)',
            'Il primo uomo a fare il giro del globo da solo a vela su una vecchia barca per ostriche ricostruita con le sue mani senza radio né radar.',
            ['Slocum', 'Spray', 'Giro del mondo', 'Solo', 'Vela'],
            ['Circumnavigazione solitaria', 'Barca in legno riparata', 'Navigazione astronomica pura', 'Autonomia marina', 'Pioniere della vela']
        ),
        (
            "L'odissea nello spazio profondo della missione Apollo 13 (1970)",
            "'Houston, abbiamo un problema'. Dopo l'esplosione del serbatoio di ossigeno a trecentomila chilometri dalla terra, l'ingegno trasforma il modulo lunare in scialuppa salvifica.",
            ['Apollo 13', 'Houston', 'Esplosione', 'Spazio', 'Luna'],
            ['Houston abbiamo un problema', 'Modulo lunare Aquarius', "Adattamento d'emergenza", 'Ingegneria di sopravvivenza', 'Rientro atmosferico sicuro']
        ),
        (
            "L'avventura di David Livingstone e l'incontro con Stanley in Africa",
            "Nel cuore inesplorato dell'Africa equatoriale alla ricerca delle sorgenti del Nilo: l'epico incontro sul lago Tanganica: 'Il dottor Livingstone, suppongo?'.",
            ['Livingstone', 'Stanley', 'Africa', 'Nilo', 'Giungla'],
            ['Esplorazione equatoriale', 'Cascate Vittoria', 'Dr. Livingstone I presume', "Mappatura dell'ignoto", 'Febbri tropicali']
        ),
        (
            'Il naufragio e la solitudine operosa di Robinson Crusoe',
            "Analizza il capolavoro di Daniel Defoe: l'uomo moderno che naufragato su un'isola deserta ricostruisce con tenacia, ragione e fede l'intera civiltà dal nulla.",
            ['Robinson', 'Venerdì', 'Isola deserta', 'Defoe', 'Naufragio'],
            ['Homo economicus solitario', 'Ricostruzione della civiltà', 'Tenacia razionale', 'Incontro con Venerdì', 'Sopravvivenza e riscatto']
        ),
        (
            'La traversata delle Alpi di Annibale con gli elefanti (218 a.C.)',
            "Il generale cartaginese che sfida le nevi perenni, le frane e le tribù ostili portando l'esercito e i colossi d'Africa a minacciare Roma nel suo cuore.",
            ['Annibale', 'Elefanti', 'Alpi', 'Cartagine', 'Guerra'],
            ['Valico alpino audace', 'Guerra annibalica', 'Colossi nella bufera', 'Strategia eversiva', 'Terrore di Roma']
        ),
        (
            "L'esplorazione del fiume Congo ne Il cuore di tenebra di Joseph Conrad",
            'Il viaggio a bordo del battello a vapore risalendo il fiume serpente verso la stazione interna di Kurtz: la discesa geografica che si trasforma in discesa negli abissi morali.',
            ['Conrad', 'Kurtz', 'Congo', 'Fiume', 'Nero'],
            ['Discesa geografica e morale', 'Cuore di tenebra conradiano', 'Orrore imperialista svelato', 'Battello fluviale cieco', 'Giungla primordiale']
        ),
        (
            "L'ascesa all'Everest senza ossigeno di Reinhold Messner e Peter Habeler (1978)",
            'Dimostrare alla comunità scientifica che il corpo umano può salire sul tetto del mondo a 8848 metri con la sola forza dei propri polmoni e della mente.',
            ['Messner', 'Everest', 'Ossigeno', 'Ottomila', 'Freddo'],
            ['Stile alpino puro', 'Senza ossigeno supplementare', 'Limite fisiologico estremo', 'Tetto del mondo', "Etica dell'alpinismo"]
        ),
        (
            'La rotta dei ghiacci del passaggio a Nord-Ovest di Roald Amundsen',
            "A bordo della piccola Gjøa con soli sei compagni, naviga per tre anni tra i ghiacci dell'Artico canadese scoprendo il passaggio tra Atlantico e Pacifico.",
            ['Passaggio a Nord-Ovest', 'Amundsen', 'Ghiaccio', 'Tre anni', 'Canada'],
            ['Sloop Gjøa', 'Passaggio a Nord-Ovest', 'Apprendimento dagli Inuit', 'Migrazione del Polo Magnetico', 'Tenacia esplorativa']
        ),
        (
            'Il viaggio naturalistico di Charles Darwin sul brigantino Beagle (1831)',
            "Cinque anni intorno al mondo raccogliendo fossili in Patagonia e fringuelli alle Galápagos: l'esperienza di viaggio che genererà la teoria dell'evoluzione.",
            ['Darwin', 'Beagle', 'Galapagos', 'Fringuelli', 'Evoluzione'],
            ['Viaggio del Beagle', 'Biodiversità delle Galápagos', 'Fossili patagonici', 'Origine delle specie', 'Rivoluzione biologica']
        ),
        (
            "L'epopea spaziale di Jurij Gagarin: il primo uomo in orbita (1961)",
            "A bordo della Vostok 1 pronuncia l'immortale 'Pojechali!' (Andiamo!). Centootto minuti attorno alla Terra contemplando la fragile bellezza azzurra del pianeta.",
            ['Gagarin', 'Vostok', 'Russo', 'Spazio', 'Terra'],
            ['Pojechali storico', 'Primo volo orbitale', 'Pianeta azzurro fragile', 'Guerra fredda spaziale', 'Frontiera cosmica']
        ),
        (
            "La traversata a piedi dell'Australia di Burke e Wills (1860)",
            "Dal sud al golfo di Carpentaria a nord attraverso il deserto rosso e desolato dell'Outback: una spedizione titanica segnata dalla sete e dalla tragicità finale.",
            ['Burke e Wills', 'Australia', 'Outback', 'Deserto', 'Morire'],
            ["Traversata dell'Outback", 'Spedizione continentale fatale', 'Deserto rosso australiano', 'Incomprensione degli aborigeni', 'Tragedia di Cooper Creek']
        ),
        (
            "La rotta dell'oro del Klondike e la febbre dello Yukon (1897)",
            "Migliaia di cercatori scalano il Chilkoot Pass nella bufera di neve con cento chili di provviste per setacciare le acque ghiacciate dei fiumi dell'Alaska.",
            ['Klondike', "Cercatori d'oro", 'Alaska', 'Yukon', 'Chilkoot'],
            ["Febbre dell'oro del Klondike", 'Chilkoot Pass nella bufera', 'Fatica e disillusione', 'Racconti di Jack London', 'Frontiera selvaggia']
        ),
        (
            'La discesa in kayak delle gole del fiume Yarlung Tsangpo in Tibet',
            "L'Everest dei fiumi: la spedizione che affronta le rapide più violente del mondo incassate tra le vette dell'Himalaya a quattromila metri di quota.",
            ['Kayak', 'Tibet', 'Fiume', 'Rapide', 'Himalaya'],
            ['Gola dello Yarlung Tsangpo', 'Fiume più estremo del globo', 'Forza idraulica titanica', 'Abisso himalayano', 'Impresa fluviale']
        ),
        (
            'La sopravvivenza nella giungla amazzonica di Juliane Koepcke (1971)',
            "Precipita da tremila metri con il sedile dell'aereo disintegrato nella tempesta: da sola, diciassettenne ferita, segue un ruscello per undici giorni fino alla salvezza.",
            ['Aereo precipitato', 'Giungla', 'Ragazza', 'Salvarsi', 'Sola'],
            ['Caduta miracolosa', 'Sopravvivenza nella foresta', "Seguire il corso d'acqua", 'Lezione biologica paterna', 'Resilienza indomita']
        ),
        (
            "Il manifesto dell'Uomo Itinerante: viaggiare per rinascere",
            "Pronuncia un'orazione che celebri il viaggio non come fuga turistica dai problemi, ma come rito di passaggio dove ci si spoglia delle certezze per scoprire chi siamo.",
            ['Turismo', 'Fuga', 'Valigia', 'Tornare', 'Fine'],
            ['Homo viator ontologico', 'Rito di passaggio iniziatico', 'Spoliazione delle certezze', 'Incontro trasformativo', "Compiutezza dell'itineranza"]
        ),
    ],
    "b2": [
        (
            "L'ontologia del limite umano e l'ebbrezza dell'Ulissismo",
            "Analizza il contrasto tra il modello omerico (il ritorno rassicurante all'ordine domestico di Itaca) e il modello dantesco (la sete inestinguibile di oltrepassare le Colonne d'Ercole).",
            ['Ulisse', 'Dante', 'Omero', 'Itaca', "Colonne d'Ercole"],
            ['Folle volo dantesco', 'Hybris e canoscenza', "Tensione verso l'ignoto", 'Ritorno versus oltrepassamento', 'Tragicità del confine']
        ),
        (
            "La poetica del viaggio romantico: dal Grand Tour all'esplorazione solitaria",
            "Come il viaggio dell'aristocrazia settecentesca volto a studiare le rovine classiche si trasformi con Byron e Shelley nell'immersione sublime e malinconica nella natura tempestosa.",
            ['Grand Tour', 'Byron', 'Shelley', 'Rovine', 'Viaggio romantico'],
            ['Sublime romantico', 'Inquietudine byroniana (Wanderlust)', "Natura come specchio dell'anima", 'Rovine e malinconia storica', 'Pellegrinaggio interiore']
        ),
        (
            "L'etica dell'alpinismo moderno e la conquista dell'inutile",
            "Riprendi il celebre titolo di Lionel Terray 'I conquistatori dell'inutile': rischiare la vita per scalare una parete di ghiaccio verticale senza profitto materiale né gloria pratica.",
            ['Terray', 'Alpinismo', 'Inutile', 'Morire', 'Montagna'],
            ["Conquista dell'inutile", "Gratuità dell'impresa estrema", 'Ascetismo della parete', "Sfida all'inaccessibile", 'Dignità della pura passione']
        ),
        (
            'La decostruzione della cartografia coloniale e la terra incognita',
            "Analizza come le mappe europee con la dicitura 'Hic sunt leones' non registrassero uno spazio vuoto, ma cancellassero deliberatamente le civiltà indigene per legittimare la conquista imperiale.",
            ['Mappa', 'Leoni', 'Terra incognita', 'Indigeni', 'Conquista'],
            ['Cartografia coloniale egemonica', 'Invenzione della terra nullius', 'Cancellazione delle sovranità native', "Geografia dell'asservimento", 'Decolonizzazione delle mappe']
        ),
        (
            'Il nomadismo filosofico di Bruce Chatwin: Le vie dei canti',
            "Attraverso i percorsi cromatici degli aborigeni australiani, dimostra come il cammino a piedi sia la vera condizione naturale dell'uomo, creata per cantare e custodire la terra.",
            ['Chatwin', 'Vie dei canti', 'Australia', 'Aborigeni', 'Camminare'],
            ['Nomadismo esistenziale chatwiniano', 'Vie dei canti (Songlines)', "Cantare il mondo all'esistenza", 'Stanzialità come malattia nevrotica', 'Pellegrinaggio sacro']
        ),
        (
            "La conquista dello spazio come nuova frontiera e l'effetto panoramica (Overview Effect)",
            'La testimonianza degli astronauti che vedono la Terra dallo spazio: una sfera minuscola e fragile priva di confini nazionali che induce un risveglio etico e cosmico immediato.',
            ['Spazio', 'Overview Effect', 'Terra vista da fuori', 'Confini', 'Astronauti'],
            ['Overview Effect trascendente', 'Fragilità della biosfera azzurra', 'Dissoluzione dei confini politici', 'Coscienza planetaria globale', 'Sguardo cosmico']
        ),
        (
            "La solitudine dell'oceano e la filosofia marina di Bernard Moitessier",
            "In testa alla Golden Globe Race intorno al mondo senza scalo nel 1968, decide di non tagliare il traguardo per vincere il premio ma di continuare a navigare verso Tahiti per salvare l'anima.",
            ['Moitessier', 'Regata', 'Premio', 'Soldi', 'Barca a vela'],
            ['Rifiuto della gloria commerciale', 'Un lungo cammino pacifico', "Fusione con l'oceano infinito", 'Libertà marittima pura', "Salvezza dell'anima"]
        ),
        (
            "L'esplorazione del Polo Nord e la deriva della Fram di Fridtjof Nansen",
            'Progettare una nave col fondo tondo per farsi intrappolare volontariamente nella banchisa polare e derivare con le correnti artiche verso il polo per tre anni.',
            ['Nansen', 'Fram', 'Ghiaccio', 'Deriva', 'Polo Nord'],
            ['Nave Fram indistruttibile', 'Deriva transpolare congetturale', 'Ingegneria navale artica', 'Esplorazione scientifica pacifica', 'Premio Nobel per la pace']
        ),
        (
            'Il fascino del disastro e la tragica spedizione Franklin (1845)',
            "La scomparsa della HMS Erebus e Terror nel ghiaccio del passaggio a Nord-Ovest: come l'arroganza dell'impero tecnologico britannico soccombette al freddo e al cannibalismo.",
            ['Franklin', 'Erebus', 'Terror', 'Scomparsi', 'Cannibalismo'],
            ['Hubris imperiale tecnologica', 'Tragedia polare frankliniana', 'Ghiaccio tombale perenne', "Decadimento dell'ordine militare", 'Mistero artico disvelato']
        ),
        (
            "La camminata come atto rivoluzionario e l'elogio dei piedi di Henry David Thoreau",
            'Nel saggio Camminare (Walking), difende il camminatore come cavaliere della libertà selvatica (Wildness) che abbandona il villaggio borghese per entrare nella foresta.',
            ['Thoreau', 'Camminare', 'Foresta', 'Piedi', 'Paese'],
            ['Saggio Walking thoreauiano', 'Spiritualità del cammino libero', 'Riconnessione con la Wildness', 'Diserzione dalla routine sociale', 'Pellegrinaggio nel selvatico']
        ),
        (
            'Il viaggio come fuga e disillusione ne Il viaggio di Baudelaire',
            "I Fiori del Male si chiudono con l'amara constatazione: 'Un'oasi d'orrore in un deserto di noia!'. La vera avventura estrema rimane tuffarsi nell'abisso della Morte per trovare il nuovo.",
            ['Baudelaire', 'Fiori del Male', 'Noia', 'Viaggiare', 'Morte'],
            ['Ennui e disillusione del viaggio', "Oasi d'orrore in deserto di noia", "Tuffo nell'abisso sconosciuto", 'Morte capitano supremo', 'Poetica della fine']
        ),
        (
            'La navigazione delle piroghe polinesiane e la lettura delle onde',
            "Come i navigatori delle isole del Pacifico abbiano colonizzato migliaia di isole senza strumenti, leggendo le correnti, i riflessi del cielo e il volo degli uccelli all'imbrunire.",
            ['Polinesia', 'Isole', 'Stelle', 'Onde', 'Senza strumenti'],
            ['Navigazione oceanica polinesiana', 'Wayfinding tradizionale indigeno', 'Mappatura delle correnti e delle onde', 'Connessione biotica col mare', 'Sapienza ancestrale']
        ),
        (
            "L'epopea dei cosmonauti sovietici e il costo umano della corsa allo spazio",
            "Analizza la tragedia di Vladimir Komarov sulla Sojuz 1 nel 1967: consapevole che la navicella era difettosa, decolla per non far morire l'amico Gagarin suo sostituto.",
            ['Komarov', 'Sojuz', 'Schianto', 'Gagarin', 'Spazio'],
            ['Sacrificio fraterno di Komarov', 'Corsa allo spazio ideologica', 'Navicella difettosa accettata', 'Martirio del cosmonauta', "Dignità nella bufera d'acciaio"]
        ),
        (
            "Il viaggio di Ibn Battuta: centoventimila chilometri nell'Islam medievale",
            'Dal Marocco alla Cina, da Timbuctù alle Maldive nel Trecento: la testimonianza di una civiltà musulmana colta, cosmopolita e aperta alla diversità culturale.',
            ['Ibn Battuta', 'Islam', 'Viaggio', 'Cina', 'Mondo arabo'],
            ['Rihla (Il viaggio) di Ibn Battuta', 'Cosmopolitismo islamico medievale', 'Diritto ed etica transnazionale', 'Pluralismo culturale arcaico', 'Itineranza infinita']
        ),
        (
            'La discesa nelle viscere della terra: la speleologia estrema di Krubera-Voronya',
            "Scendere a oltre duemila metri di profondità nell'abisso carsico del Caucaso tra cascate sotterranee a zero gradi e sifoni allagati in apnea.",
            ['Voronya', 'Grotta', 'Profondo', 'Fango', 'Apnea'],
            ['Speleologia profonda estrema', 'Abisso Krubera-Voronya', 'Esplorazione ipogea assoluta', 'Isolamento buio perenne', 'Frontiera interna della terra']
        ),
        (
            'Il dilemma morale del turismo di massa e la profanazione dei luoghi sacri',
            "Le code con bombole d'ossigeno sulla cresta sommitale dell'Everest e le tonnellate di rifiuti lasciati nei campi alti: quando l'avventura diventa consumo predatorio.",
            ['Everest', 'Turisti', 'Coda', 'Spazzatura', 'Soldi'],
            ["Mercificazione dell'avventura", 'Over-tourism montano predatorio', 'Profanazione del Sagarmatha sacro', 'Commercio delle cime', 'Necessità del rispetto etico']
        ),
        (
            "La traversata dell'Oceano Atlantico in barca a remi di Alex Bellini",
            "Affrontare mesi di solitudine tra onde di dieci metri con la sola forza delle braccia e della mente: il dialogo interiore con la paura e la fragilità dell'ego.",
            ['Remi', 'Bellini', 'Atlantico', 'Tempesta', 'Solo'],
            ['Traversata oceanica a remi', 'Resilienza psichica estrema', 'Monotonia feconda del gesto', 'Dialogo con la solitudine marina', 'Trascendenza del limite']
        ),
        (
            "L'avventura polare femminile: le pioniere dimenticate dell'Artico",
            "Dalla geologa Louise Boyd che mappò la Groenlandia a Barbara Hillary che raggiunse entrambi i poli a settant'anni: riscatta l'epica femminile dell'esplorazione.",
            ['Donne', 'Artico', 'Poli', 'Uomini solo', 'Esploratrici'],
            ["Pioniere dell'esplorazione polare", 'Rottura del monopolio maschile', 'Scienza geografica femminile', 'Tenacia artica disconosciuta', 'Emancipazione sui ghiacci']
        ),
        (
            'Il mito del buon selvaggio e la spedizione antropologica di Claude Lévi-Strauss',
            "In Tristi tropici, l'addio disincantato all'illusione del viaggio esotico: 'Odio i viaggi e gli esploratori...'. La civiltà occidentale che distrugge tutto ciò che tocca.",
            ['Lévi-Strauss', 'Tristi tropici', 'Odio i viaggi', 'Indios', 'Distruzione'],
            ['Tristi tropici lévi-straussiani', "Disillusione dell'esotismo borghese", 'Critica della devastazione coloniale', 'Etnografia del lutto', 'Melanconia antropologica']
        ),
        (
            "L'arringa dell'Oratore Esploratore: l'avventura del Pensiero Libero",
            "Pronuncia un'orazione solenne: l'esplorazione più vertiginosa, perigliosa e necessaria non è toccare i poli della terra, ma addentrarsi nell'abisso sconosciuto della coscienza e della verità.",
            ['Terre lontane', 'Poli', 'Mondo', 'Viaggiare fuori', 'Fine'],
            ['Esplorazione della coscienza interiore', 'Avventura sublime del pensiero libero', "Magistero dell'Oratore Viaggiatore", 'Conquista della Verità morale', "Fulgore perenne dell'Ignoto"]
        ),
    ],
    "c1": [
        (
            "La geopoetica dello spazio selvaggio contro l'urbanizzazione totale in Kenneth White",
            'Esporrai la teoria della geopoetica: il superamento della separazione occidentale tra mente e paesaggio attraverso una scrittura che registri le linee di forza geofisiche del mondo.',
            ['White', 'Geopoetica', 'Città', 'Natura', 'Scrittura'],
            ['Geopoetica whitiana dello spazio', 'Uscita dalla gabbia urbana', 'Iscrizione del paesaggio nel testo', 'Terra come testo vivente', 'Mistica del cammino boreale']
        ),
        (
            'Il cuore di tenebra di Joseph Conrad: il viaggio geografico come abisso morale',
            "Analizza come il battello di Marlow risalendo il fiume Congo smantelli la maschera civilizzatrice dell'Europa borghese, disvelando l'orrore coloniale e la corruzione del cuore umano.",
            ['Conrad', 'Marlow', 'Kurtz', 'Congo', 'Civiltà'],
            ["L'orrore conradiano testimoniato", 'Decostruzione della missione civilizzatrice', 'Metamorfosi cannibale del colonialismo', 'Ipocrisia filantropica borghese', 'Abisso morale del potere assoluto']
        ),
        (
            "La cartografia dell'ignoto come conquista della conoscenza scientifica moderna",
            "Dall'Atlante di Mercatore alle spedizioni idrografiche dell'Illuminismo: come la misurazione geometrica della sfera terrestre abbia fondato l'episteme della scienza globale.",
            ['Mappe', 'Mercatore', 'Illuminismo', 'Scienza', 'Misurare'],
            ['Epistemologia cartografica moderna', 'Proiezione di Mercatore e distorsione', 'Secolarizzazione dello spazio cosmico', 'Rilievo geometrico planetario', "Conquista dell'orizzonte"]
        ),
        (
            "L'archetipo dell'Ulissismo tra iniziazione sapienziale e trasgressione titanica",
            'Confronta il viaggio omerico come restaurazione faticosa del patto civile col folle volo dantesco inteso come prometeico oltrepassamento dei limiti imposti da Dio alla ragione umana.',
            ['Omero', 'Dante', 'Ulisse', 'Colonne', 'Peccato'],
            ["Tragicità dell'Ulissismo dantesco", "Restaurazione omerica dell'oikos", 'Frattura tra virtute e canoscenza', 'Infrangimento del confine sacro', 'Naufragio della ragione superba']
        ),
        (
            'Il nomadismo ontologico e la decostruzione del concetto di confine territoriale',
            'Attraverso Gilles Deleuze e Félix Guattari (Trattato di nomadologia), illustra come la macchina da guerra nomade destrutturi lo spazio striato e proprietario dello Stato sovrano.',
            ['Deleuze', 'Guattari', 'Nomadi', 'Confini', 'Stato'],
            ['Nomadologia deleuziana sovversiva', 'Spazio liscio versus spazio striato', 'Decostruzione della recinzione statale', 'Linea di fuga libertaria', 'Ontologia del divenire itinerante']
        ),
        (
            "L'enigma della Terra Incognita nelle cosmologie medievali e rinascimentali",
            "Come l'ignoto cartografico medievale (popolato da mostri marini, antipodi e il paradiso terrestre) sia stato secolarizzato dai viaggi di circumnavigazione nel disincanto razionale.",
            ['Paradiso terrestre', 'Mostri marini', 'Medioevo', 'Mappe', 'Antipodi'],
            ['Secolarizzazione dello spazio mitico', "Scomparsa dell'Eden geografico", "Disincanto dell'orizzonte marino", 'Transizione gnoseologica epocale', 'Mappatura della fatticità empirica']
        ),
        (
            'La sublime desolazione artica e la poetica del silenzio in Barry Lopez',
            "Nel capolavoro Sogni artici (Arctic Dreams), indaga come il paesaggio boreale bianco e spoglio imponga all'uomo occidentale una cura reverente e una conversione etica dell'ascolto.",
            ['Lopez', 'Sogni artici', 'Polo', 'Ghiaccio', 'Silenzio'],
            ['Sogni artici di Barry Lopez', "Etica dell'ascolto boreale", 'Cura reverente del paesaggio', 'Sublime orizzonte bianco', 'Riconciliazione col vivente']
        ),
        (
            "L'apologia della solitudine estrema nella letteratura di mare di Joseph Conrad e Jack London",
            "Il confronto solitario dell'uomo contro la tempesta cieca: l'annientamento di ogni vanità sociale di fronte alla furia maestosa e indifferente della natura non addomesticata.",
            ['Mare', 'Tempesta', 'London', 'Conrad', 'Solitudine'],
            ['Indifferenza sovrana della natura', "Annientamento dell'ego sociale", "Confronto disadorno con l'abisso", 'Solidarietà elementare della ciurma', "Tempra morale dell'inerme"]
        ),
        (
            "Il paradosso della frontiera e la scomparsa dell'ignoto nell'era satellitare",
            "Se ogni metro quadrato della terra è scansionato e mappato da satelliti in tempo reale, quale spazio residua per l'autentica avventura della scoperta geografica e spirituale?",
            ['Satelliti', 'Google Earth', 'Tutto visto', 'Niente da scoprire', 'Fine del viaggio'],
            ["Scomparsa dell'ignoto materiale", 'Onnipresenza dello sguardo satellitare', "Rifugio nell'avventura interiore", "Resistenza dell'invisibile", 'Ricerca del senso oltre la mappa']
        ),
        (
            'La navigazione delle anime e la metafora marittima nella Divina Commedia',
            "Dal 'navicella del mio ingegno' del Purgatorio al 'mar che mai non si corse' del Paradiso: Dante trasfigura l'esplorazione geografica in teologia dell'ascensione mistica verso Dio.",
            ['Dante', 'Navicella', 'Paradiso', 'Mare', 'Ingegno'],
            ['Metafora nautica dantesca', 'Navigazione delle acque teologiche', "Pelago dell'Assoluto", 'Ascensione verso la Luce pura', 'Nave poetica salvifica']
        ),
        (
            "L'avventura dell'Altro: l'incontro con le culture altre nelle memorie gesuite",
            'Dai diari di Matteo Ricci a Pechino alle riduzioni dei gesuiti in Paraguay: analizza il dilemma tra assimilazione etnocentrica e autentico dialogo interculturale.',
            ['Matteo Ricci', 'Gesuiti', 'Cina', 'Paraguay', 'Convertire'],
            ["Metodo dell'accomodamento di Ricci", 'Dialogo interculturale precoce', 'Riduzioni gesuitiche comunitarie', 'Etnografia del rispetto religioso', 'Tensione tra fede e civiltà']
        ),
        (
            "L'archetipo dell'Isola che non c'è e l'utopia politica da Moro a Bacone",
            "Da Thomas More (Utopia) a Francis Bacon (La nuova Atlantide): l'isola lontana ed inaccessibile come specchio critico delle ingiustizie sociali e dei regimi europei corrotti.",
            ['Moro', 'Bacone', 'Utopia', 'Isola', 'Nuova Atlantide'],
            ["Topos insulare dell'Utopia", 'Critica radicale delle ingiustizie europee', 'Laboratorio politico immaginario', 'Ingegneria sociale della perfezione', 'Specchio emancipativo']
        ),
        (
            "La fenomenologia dell'orientamento spaziale in Maurice Merleau-Ponty",
            'Come il corpo vissuto (Leib) non sia dentro lo spazio come un oggetto in una scatola, ma sia la sorgente originaria da cui scaturiscono le coordinate di alto, basso, vicino e lontano.',
            ['Merleau-Ponty', 'Corpo', 'Spazio', 'Alto e basso', 'Orientarsi'],
            ['Corpo vissuto fenomenologico (Leib)', "Spazialità primaria d'orientamento", 'Ancoraggio ontologico al mondo', 'Carne dello spazio percorso', 'Orizzonte cinestetico originario']
        ),
        (
            "L'eroismo tragico e l'amnesia del ritorno nel cinema di Werner Herzog",
            "Da Aguirre furore di Dio a Fitzcarraldo: la follia prometeica dell'esploratore europeo che trascina navi sulle montagne o scende fiumi amazzonici divorato dal proprio delirio.",
            ['Herzog', 'Aguirre', 'Fitzcarraldo', 'Nave sulla montagna', 'Follia'],
            ['Delirio visionario herzoghiano', "Aguirre e l'ebbrezza della ribellione", 'Impresa titanica e assurda', 'Sconfitta tragica nella giungla', "Poetica dell'estasi estrema"]
        ),
        (
            "L'esplorazione delle profondità abissali e la vertigine dell'origine della vita",
            'Nelle sorgenti idrotermali degli abissi vulcanici sottomarini (Black smokers), la scienza scopre ecosistemi che prosperano senza la luce del sole, ridefinendo la biosfera cosmica.',
            ['Abissi', 'Fumarole nere', 'Vita senza sole', 'Vulcano sottomarino', 'Scienza'],
            ['Ecosistemi chemiosintetici abissali', 'Black smokers oceanici', 'Origine idrotermale della vita', 'Biosfera chemiolitotrofica', 'Nuovi orizzonti astrobiologici']
        ),
        (
            'La camminata come pratica filosofica di resistenza in Frédéric Gros',
            "Nel saggio Andare a piedi: una filosofia, dimostra come camminare lentamente per giorni liberi il soggetto dalle illusioni dell'identità sociale, riconsegnandolo all'essenziale.",
            ['Gros', 'Camminare a piedi', 'Lentezza', 'Libertà', 'Zaino'],
            ['Filosofia del cammino di Gros', 'Spoliazione delle maschere sociali', 'Semplicità rigeneratrice del passo', 'Sospensione della velocità produttivistica', 'Libertà del vagabondaggio']
        ),
        (
            "L'archetipo del deserto come spazio dell'ascolto e della purificazione monastica",
            'Dai Padri del Deserto ad Antoine de Saint-Exupéry: la spogliazione totale di ogni consolazione materiale come condizione necessaria per udire la voce del Sacro e delle stelle.',
            ['Deserto', 'Padri del deserto', 'Saint-Exupéry', 'Silenzio', 'Stelle'],
            ['Spiritualità eremitica del deserto', 'Sguardo di Saint-Exupéry aviatore', 'Spoliazione ascetica purificatrice', "Risonanza dell'Assoluto nel vuoto", 'Terra degli uomini']
        ),
        (
            "La fine del viaggio e l'apologia dell'abitare stanziale in Martin Heidegger",
            "Commenta il celebre saggio Costruire, abitare, pensare: la grandezza dell'uomo non risiede nell'erranza senza radici, ma nella capacità di custodire e abitare poeticamente la terra.",
            ['Heidegger', 'Abitare', 'Costruire', 'Casa', 'Radici'],
            ['Abitare poetico heideggeriano', 'Custodia del Quadrante cosmico', 'Radicamento contro lo sradicamento', 'Pace contemplativa del luogo', "Ritorno fecondo all'origine"]
        ),
        (
            'La traversata cosmica della sonda Voyager e il Pale Blue Dot',
            'A sei miliardi di chilometri di distanza, la telecamera della sonda immortala la Terra come un minuscolo granello di polvere sospeso in un raggio di sole. Commenta Carl Sagan.',
            ['Voyager', 'Sagan', 'Pale Blue Dot', 'Granello di polvere', 'Spazio'],
            ['Pale Blue Dot saganiano', 'Vertigine della solitudine cosmica', "Monito all'umiltà e alla fratellanza", 'Sonda interstellare eterna', "Messaggio dell'umanità errante"]
        ),
        (
            "L'Orazione per l'Eterno Pellegrino: il Verbo dell'Avventura Suprema",
            "Pronuncia l'arringa conclusiva: l'uomo è per sua natura un viaggiatore della speranza, che naviga tra le tempeste del mondo portando nel petto la bussola incorruttibile della Verità.",
            ['Bussola', 'Viaggiatore', 'Tempesta', 'Mondo', 'Fine'],
            ['Homo viator metafisico', 'Bussola morale incorruttibile', "Trionfo dell'avventura spirituale", "Magistero dell'Oratore Pellegrino", "Luce imperitura dell'Itineranza"]
        ),
    ],
    "c2": [
        (
            "L'ontologia del limite e l'ebbrezza dell'ulissismo dantesco del folle volo",
            "Pronuncia una summa sulla lacerazione metafisica di Ulisse nel canto XXVI dell'Inferno: la condanna teologica del trasgressore che si rovescia nell'apoteosi umanistica dell'ardore gnoseologico assoluto.",
            ['Ulisse', 'Dante', 'Folle volo', 'Inferno', 'Peccato'],
            ["Apoteosi dell'ardore gnoseologico", 'Condanna teologica rovesciata', "Tragicità dell'oltrepassamento del limite", 'Virtute e canoscenza assolute', 'Folle volo metafisico sublime']
        ),
        (
            "La geopoetica dello spazio selvaggio contro l'urbanizzazione totale del mondo",
            "Delinea con rigore speculativo l'urgenza di una riconciliazione cosmica: strappare la terra alla mercificazione cementizia attraverso una poetica che restituisca sacralità al respiro del vento e della pietra.",
            ['Geopoetica', 'Cemento', 'Terra mercificata', 'Pietra', 'Natura'],
            ['Geopoetica cosmica insorta', 'De-mercificazione dello spazio terrestre', 'Risacralizzazione della physis', 'Custodia del respiro selvaggio', 'Inno alla terra incorrotta']
        ),
        (
            "L'esplorazione come metafora della ricerca inesauribile del senso in Paul Celan",
            "Nella prosa del Meridian, analizza il cammino della poesia: una traiettoria topografica che attraversa l'abisso della rovina storica per cercare l'Altro e approdare all'incontrare.",
            ['Celan', 'Meridiano', 'Poesia', 'Abisso', 'Altro'],
            ['Topografia spirituale celaniana', 'Cammino poetico verso il Meridian', "Attraversamento dell'abisso storico", "Incontro etico con l'Alterità", 'Vessillo della speranza ferita']
        ),
        (
            'Il nomadismo filosofico e la decostruzione del concetto di confine territoriale',
            "Sostieni di fronte al consesso supremo l'illegittimità metafisica di ogni recinto statale: la terra appartiene al cammino di chi la abita con rispetto e non alla violenza delle dogane armate.",
            ['Confini', 'Dogane', 'Stato', 'Muri', 'Terra nostra'],
            ['Decostruzione ontologica del confine', 'Illegittimità della recinzione proprietaria', 'Spazio nomade universale condiviso', 'Fratellanza planetaria itinerante', 'Sovranità del cammino libero']
        ),
        (
            "La dialettica dell'ignoto e la vertigine dell'apofatismo spaziale",
            "Dimostra come l'esplorazione scientifica culminante nell'infinito astronomico non cancelli il mistero, ma disveli l'apofatismo del cosmo: più la vista si allarga, più l'essere rivela la sua incommensurabile ineffabilità.",
            ['Spazio profondo', 'Mistero', 'Scienza', 'Stelle', 'Sapere tutto'],
            ['Apofatismo cosmico vertiginoso', 'Ineffabilità della smisuratezza siderale', "Eclissi dell'antropocentrismo calcolante", 'Stupore contemplativo originario', "Mistero perenne dell'infinito"]
        ),
        (
            "L'apologia della notte artica e la fenomenologia del bianco assoluto",
            "Commenta il silenzio della calotta glaciale dove il bianco accecante cancella ogni coordinata prospettica: l'annientamento delle categorie kantiane di spazio e tempo nell'estasi del nulla puro.",
            ['Artico', 'Ghiaccio', 'Bianco', 'Spazio e tempo', 'Silenzio'],
            ['Fenomenologia del bianco assoluto', 'Annientamento delle categorie spaziali', 'Estasi del silenzio polare', 'Nirvana glaciale contemplativo', "Purezza incontaminata dell'origine"]
        ),
        (
            "L'archetipo della navigazione e la metafora dell'esistenza in Hans Blumenberg",
            "Nel saggio Naufragio con spettatore, analizza l'uomo che contempla dalla terraferma il naufragio altrui, dimostrando come nella modernità l'uomo stesso sia divenuto il marinaio sulla nave sbattuta dalle onde.",
            ['Blumenberg', 'Naufragio con spettatore', 'Mare', 'Terraferma', 'Filosofia'],
            ['Paradigma nautico blumenberghiano', 'Naufragio con spettatore de-costruito', 'Immanenza della condizione marittima', 'Vulnerabilità della zattera umana', "Metaforologia dell'esistenza"]
        ),
        (
            "La solitudine sovrana dell'esploratore e il congedo dal consorzio umano",
            "Evoca la figura titanica di chi decide di varcare l'ultima frontiera (la fossa oceanica o lo spazio interstellare), sapendo che nessun messaggio e nessun soccorso potrà mai raggiungerlo.",
            ['Solitudine', 'Soccorso', 'Abisso', 'Lontano', 'Morire solo'],
            ["Solitudine sovrana dell'inerme", "Varcamento dell'orizzonte degli eventi", 'Incomunicabilità sublime', 'Offerta della vita alla conoscenza', 'Eroismo disadorno e puro']
        ),
        (
            "La decostruzione del mito di Eldorado: l'oro come feticcio mortifero del capitale",
            "Smaschera l'illusione sanguinaria dei conquistadores spagnoli: la ricerca della città d'oro che si rovescia nell'eccidio degli innocenti e nella pazzia cannibale nel cuore della selva.",
            ['Eldorado', 'Oro', 'Conquistadores', 'Pazzia', 'Indios'],
            ["Feticismo mortifero dell'Eldorado", 'Allucinazione aurifera predatoria', 'Delirio distruttivo della conquista', 'Condanna morale del genocidio', "Dissoluzione dell'idolo d'oro"]
        ),
        (
            "La rotta verso l'Oriente interiore nel pensiero di Henry Corbin",
            "Distingui l'Oriente geografico dall'Oriente dell'Anima della mistica persiana di Avicenna e Sohrawardi: il pellegrinaggio ascensionale del sapiente verso la Luce aurorale primordiale.",
            ['Oriente', 'Corbin', 'Mistica', 'Avicenna', 'Luce'],
            ["Oriente dell'Anima corbiniano", 'Mondo immaginale (Mundus Imaginalis)', "Pellegrinaggio verso la Luce d'aurora", 'Teosofia mistica itinerante', 'Ascensione angelica interiore']
        ),
        (
            "L'archetipo dell'abisso sottomarino e la vertigine dell'informe in Jules Verne",
            "Nel Venti giorni sotto i mari, analizza il capitano Nemo a bordo del Nautilus: il rifiuto dell'umanità terrena tirannica per fondare negli abissi marini una sovranità anarchica, colta e libera.",
            ['Nemo', 'Nautilus', 'Verne', 'Abissi', 'Umanità cattiva'],
            ['Sovranità abissale di Nemo', 'Mobilis in mobili', "Rifiuto dell'oppressione terrena", 'Santuario oceanico anarchico', 'Sublime scientifico e tragico']
        ),
        (
            'La frattura del tempo lineare nel viaggio quantistico e la relatività einsteiniana',
            "Il paradosso dei gemelli e la dilatazione temporale: l'esploratore che viaggia a velocità prossime a quella della luce torna sulla terra trovando secoli trascorsi e la civiltà estinta.",
            ['Einstein', 'Relatività', 'Gemelli', 'Tempo', 'Velocità della luce'],
            ['Dilatazione temporale einsteiniana', 'Frattura della contemporaneità assoluta', 'Tragicità del disallineamento temporale', 'Pellegrino dei millenni stellari', 'Vertigine della fisica moderna']
        ),
        (
            "L'archetipo della scalata e l'ascesi mistica sul monte Sinai e sul monte Carmelo",
            "Da Mosè a Giovanni della Croce: dimostra come la salita fisica della montagna rocciosa sia in ogni tradizione religiosa l'itinerario iniziatico di purificazione dalle illusioni del mondo.",
            ['Sinai', 'Carmelo', 'Mosè', 'Salita', 'Montagna sacra'],
            ["Itinerario montano dell'ascesi", 'Nube della non-conoscenza', 'Purificazione delle passioni terrene', 'Salita al Monte Carmelo', 'Teofania della vetta sacra']
        ),
        (
            'La desolazione lunare e la riscoperta della sacralità della biosfera',
            'Ripercorri le parole dei dodici uomini che hanno camminato sulla superficie morta della Luna: il silenzio della polvere sterile che fa risaltare con commozione la santità unica della vita sulla Terra.',
            ['Luna', 'Polvere morta', 'Terra viva', 'Astronauti', 'Silenzio'],
            ['Desolazione lunare sterile', 'Epifania della biosfera vivente', 'Santità inestimabile della Terra', "Commozione dell'esploratore astrale", 'Ritorno orante alla Casa comune']
        ),
        (
            "La decostruzione dell'avventura predatoria: dalla conquista alla cura",
            'Pronuncia una svolta epocale del concetto di esplorazione: non più piantare bandiere di possesso e sfruttare risorse, ma farsi custodi reverenti e testimoni disarmati della bellezza del creato.',
            ['Bandiere', 'Conquistare', 'Possesso', 'Sfruttare', 'Miniere'],
            ['Metamorfosi dalla conquista alla cura', 'Rifiuto della bandiera predatoria', 'Testimonianza disarmata della bellezza', "Etica dell'incolumità dei luoghi", 'Custodia fiduciaria universale']
        ),
        (
            "L'itineranza perpetua e l'archetipo dell'Ebreo errante",
            "Analizza la leggenda medievale dell'eroe condannato a camminare perennemente attraverso i secoli senza poter morire: la figura simbolica della condizione umana strappata a ogni patria terrena definitiva.",
            ['Ebreo errante', 'Condanna', 'Camminare sempre', 'Morire', 'Secoli'],
            ["Archetipo dell'erranza universale", 'Immortalità come fardello tragico', "Condizione dell'esule perenne", 'Pellegrinaggio senza meta finale', 'Nostalgia della quiete metafisica']
        ),
        (
            "L'archetipo della foresta pluviale e la comunione simbiotica con l'Origine",
            "Nell'intrico vergine dell'Amazzonia, l'uomo sperimenta la dissoluzione del proprio ego isolato, fondendosi nella respirazione simbiotica e pulsante di milioni di forme viventi interconnesse.",
            ['Foresta', 'Amazzonia', 'Ego', 'Io', 'Natura'],
            ['Simbiosi biotica radicale', "Dissoluzione dell'ego individualista", 'Respiro corale della foresta vergine', 'Comunione con la matrice vitale', 'Trascendenza immanente']
        ),
        (
            "Il silenzio contemplativo dell'esploratore davanti al sublime cosmico",
            "Dimostra come al termine di ogni grande viaggio, le parole dell'uomo cedano il passo al silenzio dell'adorazione: l'anima riconosce la propria divina finitudine di fronte alla maestà dell'Essere.",
            ['Silenzio', "Finita l'avventura", 'Parole', 'Adorazione', 'Grandezza'],
            ['Silenzio oratorio contemplativo', "Finitudine trasfigurata dell'uomo", "Maestà numinosa dell'Essere", 'Pace incondizionata dello sguardo', "Compiutezza dell'itineranza"]
        ),
        (
            "L'Inno all'Universo Inesplorato: l'avventura senza fine dello Spirito",
            "Pronuncia l'orazione conclusiva di Viaggi ed Esplorazioni: gli oceani della terra possono essere solcati e le cime montane scalate, ma l'abisso della sete di verità nell'animo umano rimarrà per sempre infinito.",
            ['Fine', 'Terra finita', 'Tutto esplorato', 'Navi', 'Mondo piccolo'],
            ['Infinità inesausta dello Spirito', "Inno all'Universo Inesplorato", "Trionfo dell'animo pellegrino", "Magistero dell'Oratore delle Vette", 'Eternità della Ricerca e della Luce']
        ),
        (
            "Il Giuramento Solenne dell'Oratore Cosmopolita",
            "Chiudi il corso consacrando la parola dell'oratore come ponte vivente tra tutti i popoli, tutti gli oceani e tutti gli astri del cosmo: una sola terra, una sola voce, un solo destino d'amore e libertà.",
            ['Popoli divisi', 'Guerra', 'Bandiere', 'Nemici', 'Fine'],
            ["Patto supremo dell'Oratore Cosmopolita", 'Unica terra senza confini', "Voce vivente dell'armonia globale", "Destino d'amore e di libertà", 'Consacrazione solenne del Verbo']
        ),
    ],
}
