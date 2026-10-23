# Mazzo: mistero
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            'La gomma magica scomparsa',
            "La tua gomma per cancellare a forma di tartaruga è sparita dall'astuccio. Spiega ai compagni come seguire le tracce sul banco per ritrovarla.",
            ['Gomma', 'Tartaruga', 'Astuccio', 'Rubata', 'Persa'],
            ['Indizio', 'Traccia', 'Cercare', 'Banco', 'Ritrovamento']
        ),
        (
            'Le impronte di fango sul pavimento',
            'Ci sono piccole impronte di zampette umide che vanno dalla porta alla ciotola del latte. Dimostra chi è il colpevole con allegria.',
            ['Impronte', 'Fango', 'Cane', 'Gatto', 'Sporco'],
            ['Zampina', 'Segugio', 'Indagine', 'Pista', 'Latte']
        ),
        (
            'Il baule polveroso nella soffitta',
            'Sei salito in soffitta e trovi un vecchio baule di legno con una chiave arrugginita. Descrivi il mistero di ciò che potrebbe esserci dentro.',
            ['Baule', 'Soffitta', 'Chiave', 'Polvere', 'Paura'],
            ['Mistero', 'Tesoro', 'Coperchio', 'Ricordo', 'Sorpresa']
        ),
        (
            'Lo strano rumore dietro la tenda',
            'Senti un fruscio misterioso dietro la tenda della cameretta. Trova il coraggio di avvicinarti piano per scoprire che è solo una folata di vento.',
            ['Tenda', 'Rumore', 'Mostro', 'Paura', 'Notte'],
            ['Fruscio', 'Spiffero', 'Vento', 'Finestra', 'Sollievo']
        ),
        (
            'La scatola di latta sepolta in giardino',
            'Scavando sotto il cespuglio trovi una scatoletta di biscotti sepolta chissà quando. Racconta la caccia al tesoro ai tuoi amici.',
            ['Scatola', 'Terra', 'Scavare', 'Giardino', 'Vecchia'],
            ['Caccia al tesoro', 'Segreto', 'Messaggio', 'Scoperta', 'Mistero']
        ),
        (
            'La lettera senza francobollo',
            'Trovi una busta gialla infilata sotto la porta con un disegno misterioso. Prova a decifrare chi ha mandato questo messaggio segreto.',
            ['Busta', 'Lettera', 'Postino', 'Disegno', 'Porta'],
            ['Mittente', 'Indovinello', 'Codice', 'Messaggio', 'Curiosità']
        ),
        (
            'Il cappello a cilindro del mago',
            'Il nonno ha tirato fuori un cilindro nero da prestigiatore. Spiega dove sono finiti i fazzoletti colorati che sembravano scomparsi nel nulla.',
            ['Cappello', 'Mago', 'Fazzoletto', 'Trucco', 'Sparito'],
            ['Prestigiatore', 'Illusione', 'Magia', 'Fondo falso', 'Stupore']
        ),
        (
            'La chiave misteriosa senza serratura',
            'Hai trovato una chiavetta di bronzo in un cassetto ma non apre nessuna porta della casa. Inventa quale scrigno segreto potrebbe aprire.',
            ['Chiave', 'Porta', 'Serratura', 'Bronzo', 'Cassetto'],
            ['Scrigno', 'Segreto', 'Mistero', 'Mappa', 'Avventura']
        ),
        (
            "L'ombra misteriosa sul muro della camera",
            "La luce del lampione crea l'ombra di un gigante con le corna. Dimostra ridendo che è solo l'ombra della tua pianta grassa.",
            ['Ombra', 'Gigante', 'Muro', 'Lampione', 'Paura'],
            ['Pianta', 'Illusione', 'Luce', 'Forma', 'Risata']
        ),
        (
            "Il messaggio scritto con l'inchiostro simpatico",
            'Un foglio bianco sembra vuoto, ma scaldandolo vicino alla lampada appaiono scritte magiche fatte col limone. Svela il segreto.',
            ['Limone', 'Inchiostro', 'Foglio', 'Bianco', 'Scaldare'],
            ['Invisibile', 'Segreto', 'Rivelazione', 'Calore', 'Messaggio cifrato']
        ),
        (
            'Il mistero delle ciabatte volanti',
            'Ogni mattina trovi una pantofola in cucina e una sotto il tavolo del soggiorno. Metti sotto accusa il cagnolino birbone.',
            ['Ciabatta', 'Cane', 'Cucina', 'Tavolo', 'Scomparsa'],
            ['Colpevole', 'Zampa', 'Monello', 'Nascondiglio', 'Indizio']
        ),
        (
            "L'orologio a pendolo che batte tredici colpi",
            "L'antico orologio del corridoio ha suonato tredici rintocchi a mezzogiorno. Spiega ai fratellini perché non bisogna aver paura dei vecchi ingranaggi.",
            ['Orologio', 'Tredici', 'Pendolo', 'Paura', 'Fantasma'],
            ['Ingranaggio', 'Molla', 'Rintocco', 'Antico', 'Spiegazione']
        ),
        (
            'Il libro con le pagine incollate',
            'Hai trovato una fiaba dove due pagine sono unite da un sigillo di cera rossa. Chiediti quale segreto sia custodito tra quelle righe.',
            ['Libro', 'Cera', 'Rosso', 'Pagine', 'Leggere'],
            ['Sigillo', 'Mistero', 'Custodia', 'Incantesimo', 'Rivelazione']
        ),
        (
            'La mappa disegnata sul fazzoletto',
            "Un disegno a penna su un fazzoletto mostra tre alberi e una grande X. Guida i compagni nell'esplorazione del giardino della scuola.",
            ['Mappa', 'Fazzoletto', 'X', 'Alberi', 'Tesoro'],
            ['Bussola', 'Passi', 'Segnavia', 'Esplorazione', 'Indizio']
        ),
        (
            'Il gatto nero dagli occhi lucenti',
            'Un gattino nero attraversa la strada e ti fissa con due occhi come lanterne. Spiega perché le superstizioni sui gatti neri sono solo sciocchezze.',
            ['Gatto nero', 'Sfortuna', 'Superstizione', 'Occhi', 'Strada'],
            ['Lanterne', 'Fusa', 'Affetto', 'Mistero', 'Morbido']
        ),
        (
            'Il quadro che sembra seguirti con gli occhi',
            "Nel corridoio c'è il ritratto di un vecchio capitano di mare. Spiega la tecnica prospettica per cui il suo sguardo sembra muoversi.",
            ['Quadro', 'Occhi', 'Guardare', 'Capitano', 'Paura'],
            ['Prospettiva', 'Sguardo', 'Dipinto', 'Illusione ottica', 'Tecnica']
        ),
        (
            'La scia argentata sul sentiero',
            "Trovi una traccia brillante e viscida sulle foglie dell'orto. Guida i compagni a scoprire che l'architetto del mistero è una lumachina.",
            ['Bava', 'Lumaca', 'Traccia', 'Argento', 'Viscido'],
            ['Scia luminosa', 'Guscio', 'Sentiero', 'Piccolo investigatore', 'Natura']
        ),
        (
            'La soffitta proibita e il vecchio carillon',
            "Senti una musichetta dolce e metallica provenire dal piano di sopra. Sali le scale per svelare l'antico carillon a manovella.",
            ['Carillon', 'Musica', 'Soffitta', 'Scale', 'Suonare'],
            ['Manovella', 'Melodia', 'Ballettrice', 'Ricordo', 'Incanto']
        ),
        (
            'La scomparsa delle briciole sul davanzale',
            'Avevi lasciato tre pezzetti di biscotto per gli uccellini e sono spariti senza rumore. Identifica il passerotto mattiniero come autore del furto.',
            ['Briciole', 'Sparite', 'Uccellino', 'Finestra', 'Mangiare'],
            ['Passerotto', 'Volo', 'Ladro piumato', 'Banchetto', 'Sorpresa']
        ),
        (
            'Il taccuino segreto del piccolo detective',
            'Mostra alla classe il tuo quadernetto degli indizi dove annoti impronte, orari e dettagli curiosi per risolvere i misteri della scuola.',
            ['Detective', 'Taccuino', 'Scrivere', 'Lente', 'Indagare'],
            ['Taccuino investigativo', 'Osservazione', 'Deduzione', 'Dettaglio', 'Curiosità']
        ),
    ],
    "a2": [
        (
            'Il furto del trofeo della scuola',
            "La coppa d'argento del torneo di basket è scomparsa dalla bacheca chiusa a chiave. Analizza la scena del crimine e formula la prima ipotesi investigativa.",
            ['Coppa', 'Bacheca', 'Rubata', 'Chiave', 'Ladro'],
            ['Scena del crimine', 'Rilievi', 'Assenza di scasso', 'Ipotesi investigativa', 'Movente']
        ),
        (
            'Il messaggio in codice cifrato di Cesare',
            "Hai intercettato un biglietto dove ogni lettera è spostata di tre posizioni nell'alfabeto. Spiega alla squadra come decifrare il codice segreto.",
            ['Codice', 'Cesare', 'Lettere', 'Biglietto', 'Difficile'],
            ['Cifrario di Cesare', 'Decodifica', 'Sostituzione alfabetica', 'Crittografia', 'Messaggio segreto']
        ),
        (
            "L'alibi dell'ora di ginnastica",
            "Durante l'intervallo qualcuno ha dipinto una maschera buffa sulla foto del preside. Ricostruisci gli alibi dei compagni presenti in palestra.",
            ['Preside', 'Foto', 'Vernice', 'Palestra', 'Alibi'],
            ["Verifica dell'alibi", 'Interrogatorio', 'Cronologia dei fatti', 'Testimonianza', 'Sospettato']
        ),
        (
            'La polvere bianca sulla maniglia: rilievo delle impronte',
            "Usi polvere di grafite e nastro adesivo per rilevare un'impronta digitale sulla porta del laboratorio. Spiega il procedimento scientifico.",
            ['Impronta', 'Dita', 'Maniglia', 'Polvere', 'Nastro'],
            ['Dattiloscopia', 'Rilievo scientifico', 'Polvere di grafite', 'Archi e anelli', 'Identificazione']
        ),
        (
            "Il mistero dell'orologio fermo alle 15:42",
            "Tutti gli orologi della scuola hanno segnato l'orario esatto tranne quello dell'aula magna, bloccato alle 15:42. Collega il fermo al blackout elettrico.",
            ['Orologio', 'Fermo', '15:42', 'Aula magna', 'Luce'],
            ['Anomalia temporale', 'Sbalzo di tensione', 'Circuito elettrico', "Fissazione dell'ora", 'Indizio cronologico']
        ),
        (
            'La caccia al tesoro nella biblioteca antica',
            'Seguendo una serie di indovinelli nascosti tra le pagine dei classici, guida la squadra alla scoperta del manoscritto dimenticato.',
            ['Biblioteca', 'Libri', 'Indovinello', 'Tesoro', 'Cercare'],
            ['Catalogazione', 'Enigma letterario', 'Scaffale polveroso', 'Pista di carta', 'Rivelazione']
        ),
        (
            'Il falso indizio lasciato per depistare',
            'Trovi una sciarpa rossa vicino al vetro rotto, ma appartiene a un compagno che oggi era assente. Smaschera il tentativo di depistaggio.',
            ['Sciarpa', 'Assente', 'Vetro', 'Colpa sua', 'Falso'],
            ['Depistaggio deliberato', 'Falsa pista', 'Contraddizione logica', 'Incastro', 'Lucidità deduttiva']
        ),
        (
            'Il testamento misterioso del vecchio marinaio',
            "Un vecchio capitano ha lasciato una lettera con coordinate nautiche indecifrabili. Usa la carta nautica per scoprire l'isola indicata.",
            ['Marinaio', 'Mappa', 'Coordinate', 'Isola', 'Mare'],
            ['Carta nautica', 'Latitudine e longitudine', 'Rotte perdute', 'Mistero marittimo', 'Tracciamento']
        ),
        (
            'La porta segreta dietro la libreria',
            "Tirando un finto volume di enciclopedia, una parete della villa d'epoca ruota rivelando un passaggio segreto. Descrivi l'emozione della scoperta.",
            ['Porta segreta', 'Libreria', 'Muro', 'Passaggio', 'Libro finto'],
            ['Passaggio segreto', 'Meccanismo a scomparsa', "Architettura d'altri tempi", 'Oscurità', "Brivido dell'ignoto"]
        ),
        (
            'Il mistero del diario dalle pagine strappate',
            'Hai recuperato un vecchio diario del 1944 dove mancano proprio le pagine del giorno della liberazione. Ricostruisci il mistero usando la calligrafia.',
            ['Diario', 'Pagine strappate', '1944', 'Guerra', 'Mancano'],
            ['Lacuna documentale', 'Ricostruzione indiziaria', 'Solco della penna', 'Luce radente', 'Testimonianza storica']
        ),
        (
            'Il rumore di passi nella soffitta disabitata',
            "Tutti giurano che la vecchia casa in fondo alla via sia vuota da trent'anni, eppure si sentono passi lenti sul tetto. Organizza una ricognizione diurna.",
            ['Fantasma', 'Passi', 'Casa vecchia', 'Paura', 'Notte'],
            ['Sopralluogo diurno', 'Razionalità investigativa', 'Asi di legno scricchiolanti', 'Presenza clandestina', 'Mistero svelato']
        ),
        (
            'Il furto dei microfilm al museo scientifico',
            'Durante la notte sono sparite le pellicole con i progetti del primo motore solare. Analizza le registrazioni delle telecamere di sicurezza.',
            ['Microfilm', 'Museo', 'Telecamere', 'Notte', 'Rubare'],
            ['Registrazione a circuito chiuso', 'Punto cieco', 'Fuga pianificata', 'Furto su commissione', 'Analisi dei fotogrammi']
        ),
        (
            'La falsa confessione per proteggere un fratello',
            "Un compagno si dichiara colpevole del graffio sulla fiancata dell'auto del bidello. Dimostra con le prove orarie che sta mentendo per coprire il fratello.",
            ['Confessare', 'Coprire', 'Fratello', 'Fiancata', 'Auto'],
            ['Falsa confessione', 'Incongruenza temporale', 'Lealtà fraterna fuorviata', 'Discolpa provata', 'Giustizia oggettiva']
        ),
        (
            'Il segreto del quadro con la firma cancellata',
            "Sotto la crosta di un anonimo dipinto di paesaggio comprato al mercatino, spunta una seconda firma celebre. Spiega l'indagine ai compagni.",
            ['Mercatino', 'Quadro', 'Firma', 'Cancellata', 'Soldi'],
            ['Dipinto sottostante', 'Restauro conservativo', 'Raggi ultravioletti', 'Capolavoro celato', 'Attribuzione artistica']
        ),
        (
            "L'enigma del messaggio nella bottiglia al lago",
            "Una bottiglietta di vetro verde portata dalle onde contiene un messaggio d'aiuto datato dieci anni prima. Avvia l'indagine storica sul lago.",
            ['Bottiglia', 'Lago', 'Aiuto', 'Messaggio', 'Dieci anni'],
            ['Naufragio dimenticato', 'Archivio comunale', 'Indagine a ritroso', 'Mistero lacustre', 'Risoluzione tardiva']
        ),
        (
            'La scatola nera del modellino aereo precipitato',
            'Un drone radiocomandato si è schiantato nel cortile della scuola con la scheda dati intatta. Estrai le informazioni per risalire al pilota.',
            ['Drone', 'Precipitato', 'Scheda', 'Pilota', 'Cortile'],
            ['Telemetria di volo', 'Coordinate GPS', 'Decollo tracciato', 'Scatola nera miniaturizzata', 'Identificazione del pilota']
        ),
        (
            'Il mistero del codice Morse dalla finestra di fronte',
            'Di notte una finestra della casa di fronte emette lampi di luce lunghi e brevi. Trascrivi il messaggio Morse scoprendo una richiesta di soccorso.',
            ['Morse', 'Luce', 'Finestra', 'Lampi', 'Notte'],
            ['Codice Morse', 'Segnale luminoso', 'Intermittenza ritmica', 'Decifrazione urgente', "Chiamata d'emergenza"]
        ),
        (
            "L'inganno del sosia nella sfilata in maschera",
            'Qualcuno ha commesso una marachella durante la festa di Carnevale indossando la maschera identica a quella del capoclasse. Trova il dettaglio distintivo.',
            ['Maschera', 'Carnevale', 'Uguale', 'Sosia', 'Colpa'],
            ['Particolare imperfetto', 'Postura corporea', 'Dettaglio calzature', 'Smascheramento', 'Identità reale']
        ),
        (
            'Il mistero della pianta che fiorisce solo a mezzanotte',
            "Nel giardino botanico c'è un cactus raro che apre i suoi petali profumati solo per un'ora nella notte buia. Invita i compagni a documentare l'evento.",
            ['Cactus', 'Fiore', 'Mezzanotte', 'Buio', 'Notte'],
            ['Fioritura notturna', 'Profumo effimero', 'Impollinazione crepuscolare', 'Meraviglia biologica', 'Veglia scientifica']
        ),
        (
            'Il manifesto del giovane investigatore: logica contro superstizione',
            "Concludi il modulo investigativo: non esistono fantasmi né mostri, ma solo fatti complessi che attendono la luce della logica e dell'osservazione.",
            ['Fantasmi', 'Mostri', 'Magia', 'Paura', 'Mistero risolto'],
            ['Metodo deduttivo', 'Trionfo della razionalità', 'Osservazione meticolosa', 'Rifiuto della superstizione', "Luce dell'indagine"]
        ),
    ],
    "b1": [
        (
            "L'enigma della camera chiusa dall'interno (Locked Room)",
            "Il furto del diamante è avvenuto in uno studio con finestre sbarrate e porta chiusa a chiave dall'interno. Decostruisci il trucco meccanico.",
            ['Camera chiusa', 'Chiave dentro', 'Diamante', 'Impossibile', 'Finestre'],
            ['Locked-room mystery', 'Illusione meccanica', 'Corda e chiavistello', 'Deduzione holmesiana', 'Inganno prospettico']
        ),
        (
            "L'analisi forense delle tracce ematiche e del DNA",
            "Spiega alla corte scolastica come il principio di Locard ('ogni contatto lascia una traccia') e l'estrazione genetica colleghino il sospettato alla scena.",
            ['Sangue', 'DNA', 'Locard', 'Tracce', 'Colpevole'],
            ['Principio di Locard', 'Profilazione genetica', 'Biologia forense', 'Repertazione incontrovertibile', 'Prova scientifica']
        ),
        (
            "Il depistaggio e l'inquinamento della scena del crimine",
            "Un'indagine per sabotaggio dei computer della scuola rischia di fallire perché decine di studenti hanno calpestato i cavi e toccato le tastiere.",
            ['Computer', 'Cavi', 'Toccare', 'Tutti entrati', 'Rovinato'],
            ['Inquinamento probatorio', 'Cordone di sicurezza', 'Repertazione forense', 'Integrità della catena di custodia', 'Rigore metodologico']
        ),
        (
            "L'interrogatorio dei testimoni e l'illusione della memoria",
            'Tre testimoni oculari descrivono il fuggitivo con tre giacche di colore diverso. Dimostra la fallibilità dei ricordi sotto shock emotivo.',
            ['Testimoni', 'Giacca', 'Ricordare', 'Sicuro', 'Colori diversi'],
            ['Fallibilità testimoniale', 'Effetto arma (Weapon focus)', 'Distorsione cognitiva', 'Ricostruzione mnestica', 'Interrogatorio cognitivo']
        ),
        (
            'La crittografia asimmetrica e il messaggio dei partigiani',
            'Ripercorri come le staffette partigiane usassero messaggi cifrati basati su doppie chiavi letterarie per coordinare le azioni senza farsi intercettare.',
            ['Partigiani', 'Cifrato', 'Chiave', 'Messaggio', 'Spie'],
            ['Crittografia di resistenza', 'Cifrario a griglia', 'Staffetta clandestina', 'Sicurezza della trasmissione', 'Segretezza vitale']
        ),
        (
            "Il caso dell'alibi fabbricato col ritardo del treno",
            "Un sospettato esibisce un biglietto ferroviario timbrato all'ora esatta del delitto. Dimostra come abbia sfruttato il tabellone dei ritardi per ingannare gli inquirenti.",
            ['Biglietto', 'Treno', 'Orario', 'Alibi perfetto', 'Stazione'],
            ['Alibi artificioso', 'Cronologia disallineata', "Manipolazione dell'orario", 'Sfasamento temporale', 'Incastro logico']
        ),
        (
            'La balistica forense e il confronto dei proiettili',
            "Descrivi l'esame microscopico delle rigature impresse dalla canna dell'arma sul bossolo recuperato: l'impronta balistica unica e irrepetibile.",
            ['Pistola', 'Proiettile', 'Bossolo', 'Microscopio', 'Sparare'],
            ['Balistica comparativa', 'Rigatura della canna', 'Micro-striature identificative', 'Comparatore ottico', "Tracciamento dell'arma"]
        ),
        (
            "Il furto del quadro al museo: la sostituzione con la copia d'autore",
            "La tela di Caravaggio è rimasta sulla parete, ma un restauratore attento scopre che si tratta di una copia magistrale recente. Avvia la caccia all'originale.",
            ['Caravaggio', 'Falso', 'Museo', 'Copia', 'Pareti'],
            ['Sostituzione fraudolenta', 'Pigmenti anacronistici', 'Riflettografia infrarossa', 'Ricettazione internazionale', "Recupero dell'originale"]
        ),
        (
            'La grafologia giudiziaria e la perizia calligrafica',
            'Analizza la lettera minatoria anonima: pressione del tratto, inclinazione degli assi e legature dimostrano che la scrittura è stata artificiosamente alterata.',
            ['Lettera', 'Scrittura', 'Falsa', 'Calligrafia', 'Anonima'],
            ['Perizia calligrafica', 'Dinamica del tratto grafico', 'Disconoscimento della firma', 'Gesti fuggitivi', 'Scienza grafologica']
        ),
        (
            'Il delitto senza movente apparente e la psicologia investigativa',
            "Quando una serie di furti non ha alcun tornaconto economico, illustra come l'analisi del comportamento (profiling) guidi gli investigatori verso la verità.",
            ['Rubare', 'Senza motivo', 'Pazzo', 'Psicologo', 'Soldi'],
            ['Criminal profiling', 'Firma comportamentale', 'Movente psicologico', 'Modus operandi', 'Coazione a ripetere']
        ),
        (
            "L'enigma del veleno inodore e la tossicologia moderna",
            'Un antico sovrano è morto nel sonno senza segni di violenza. Spiega come la spettrometria di massa isoli minuscole tracce di alcaloidi tossici nei tessuti.',
            ['Veleno', 'Morto nel sonno', 'Spettrometro', 'Bere', 'Tossico'],
            ['Tossicologia forense', 'Spettrometria di massa', 'Alcaloidi letali', 'Tossicocinetica', 'Identificazione chimica']
        ),
        (
            'Il testimone reticente e il ricatto mascherato',
            "Un testimone chiave ritratta improvvisamente la sua versione giurata. Dimostra di fronte alla commissione d'inchiesta che sta subendo un ricatto economico.",
            ['Ritirare', 'Paura', 'Bugia', 'Soldi', 'Testimone'],
            ['Reticenza indotta', 'Vulnerabilità al ricatto', 'Tutela dei testimoni', 'Contraddizione documentata', 'Verità protetta']
        ),
        (
            "Il caso del cold case riaperto dopo trent'anni",
            "Un delitto irrisolto del 1995 trova finalmente soluzione grazie alle nuove tecnologie di estrazione del DNA mitocondriale da un capello d'archivio.",
            ["Trent'anni", 'Capello', 'Vecchio caso', 'Assassino', 'DNA'],
            ['Cold case riaperto', 'DNA mitocondriale', 'Archivio giudiziario', 'Giustizia tardiva', 'Infallibilità della traccia']
        ),
        (
            "La trappola investigativa dell'esca controllata",
            "Per incastrare una banda di ladri di biciclette d'epoca, la polizia installa un localizzatore GPS all'interno del telaio di una bici esca.",
            ['Esca', 'GPS', 'Bicicletta', 'Ladri', 'Trappola'],
            ['Operazione sotto copertura', 'Dispositivo civetta', 'Tracciamento in tempo reale', 'Flagranza di reato', 'Smantellamento della rete']
        ),
        (
            "L'enigma del messaggio speculare leonardesco",
            'Un documento segreto è redatto a caratteri rovesciati leggibili solo allo specchio. Spiega la genialità protettiva della scrittura speculare.',
            ['Specchio', 'Leonardo', 'Rovesciato', 'Leggere', 'Segreto'],
            ['Scrittura speculare', 'Protezione crittografica rinascimentale', 'Riflessione ottica', 'Decrittazione immediata', 'Ingegno archivistico']
        ),
        (
            'La manipolazione dei registri digitali (Log tampering)',
            'Il pirata informatico ha cancellato i propri accessi al server della scuola, dimenticando il backup orario salvato sul server secondario.',
            ['Hacker', 'Log', 'Cancellare', 'Server', 'Accesso'],
            ['Log tampering', 'Traccia forense digitale', 'Backup ridondante', 'Impronta temporale', 'Inviolabilità del timestamp']
        ),
        (
            "Il depistaggio dell'incendio doloso per coprire il furto",
            "Le fiamme hanno distrutto l'ufficio contabile. Dimostra con l'analisi degli acceleranti chimici che l'incendio è stato appiccato dopo la sottrazione dei libri mastri.",
            ['Incendio', 'Fuoco', 'Benzina', 'Bruciato', 'Ufficio'],
            ['Accelerante chimico', 'Punto di innesco', 'Copertura del reato', 'Idrocarburi combusti', 'Doppio crimine']
        ),
        (
            "Il riconoscimento vocale e l'analisi fonetica forense",
            "Una telefonata minatoria è giunta alla redazione del giornale. Gli specialisti confrontano lo spettrogramma delle frequenze vocali con la voce dell'indagato.",
            ['Voce', 'Telefono', 'Spettro', 'Parlare', 'Registrazione'],
            ['Fonetica forense', 'Spettrogramma acustico', 'Formanti vocali', 'Confronto biometrico', "Attribuzione dell'enunciato"]
        ),
        (
            'Il caso della nave fantasma Mary Celeste',
            "Ritrovata alla deriva nel 1872 con vele spiegate, carico intatto e scialuppa scomparsa senza alcun equipaggio. Formula un'arringa logica sulle cause probabili.",
            ['Mary Celeste', 'Nave fantasma', 'Equipaggio sparito', 'Mostro marino', 'Deriva'],
            ['Enigma della Mary Celeste', "Abbandono d'emergenza", 'Vapori di alcol combusti', 'Psicosi da naufragio', 'Deduzione marittima']
        ),
        (
            "L'orazione di chiusura del Pubblico Ministero: oltre ogni ragionevole dubbio",
            'Pronuncia una requisitoria impeccabile: quando tutti gli indizi convergono univocamente e concordemente, il dubbio cede il passo alla certezza morale della giustizia.',
            ['Indizi', 'Condanna', 'Dubbio', 'Prigione', 'Colpevole'],
            ['Oltre ogni ragionevole dubbio', 'Gravità, precisione e concordanza', 'Requisitoria forense', 'Certezza morale probatoria', 'Trionfo della giustizia']
        ),
    ],
    "b2": [
        (
            "L'epistemologia indiziaria di Carlo Ginzburg: Spie, radici di un paradigma",
            'Analizza il paradigma indiziario comune a cacciatori primitivi, medici come Freud e Morelli, e detective come Sherlock Holmes: il dettaglio marginale che svela la totalità.',
            ['Ginzburg', 'Holmes', 'Freud', 'Dettaglio', 'Segni'],
            ['Paradigma indiziario', 'Sapere congetturale', 'Dettaglio marginale rivelatore', 'Semiologia forense', 'Decifrazione dei sintomi']
        ),
        (
            'La presunzione di innocenza versus la gogna mediatica',
            "I processi penali celebrati nei talk show televisivi condannano gli indagati prima dell'udienza preliminare. Difendi la segretezza istruttoria e la dignità civile.",
            ['Televisione', 'Gogna', 'Condannato subito', 'Giornalisti', 'Audience'],
            ['Processo mediatico distorcente', "Presunzione costituzionale d'innocenza", 'Segreto istruttorio', 'Cannibalismo mediatico', 'Verità processuale protetta']
        ),
        (
            "Il delitto della camera chiusa e l'illusione ottica di Gaston Leroux",
            "Nel mistero della camera gialla, l'attacco è avvenuto in sogno mentre la ferita fisica era preesistente. Decostruisci la trappola psicologica del testimone.",
            ['Camera gialla', 'Leroux', 'Sogno', 'Ferita', 'Attacco'],
            ['Trappola psicologica', 'Disallineamento causale', 'Falso nesso temporale', 'Risoluzione brillante', 'Ermeneutica del delitto']
        ),
        (
            "L'antropologia criminale di Cesare Lombroso e la sua decostruzione",
            "Critica le teorie ottocentesche sull'atavismo e la conformazione cranica del delinquente nato: dimostra la pericolosità delle pseudoscienze deterministe.",
            ['Lombroso', 'Cranio', 'Delinquente nato', 'Faccia da ladro', 'Fisiognomica'],
            ['Determinismo biologico fallace', 'Pseudoscienza lombrosiana', 'Atavismo criminale decostruito', 'Fattori socio-economici', 'Dignità della rieducazione']
        ),
        (
            'La prova regina: limiti e vulnerabilità del test del DNA',
            'Un profilo genetico compatibile non equivale a colpevolezza automatica: contaminazione accidentale dei reperti e transfer secondario di cellule epiteliali.',
            ['DNA', 'Sicuro al cento per cento', 'Carcere', 'Sangue', 'Colpevole'],
            ['Transfer secondario di DNA', 'Contaminazione crociata da laboratorio', 'Statistica probabilistica Bayesiana', 'Fallacia del pubblico ministero', 'Relatività della prova']
        ),
        (
            'La decostruzione del metodo deduttivo in Edgar Allan Poe',
            "Analizza I delitti della Rue Morgue: Dupin risolve l'enigma non accumulando dati, ma identificandosi psicologicamente con l'intelletto dell'avversario.",
            ['Poe', 'Dupin', 'Rue Morgue', 'Scimmia', 'Deduzione'],
            ['Metodo analitico poiano', 'Identificazione psicologica colpevole', "Risoluzione dell'apparentemente insolubile", 'Oltre la routine poliziesca', 'Logica pura']
        ),
        (
            "L'inganno del narratore inattendibile ne L'assassinio di Roger Ackroyd",
            "Nel capolavoro di Agatha Christie, il colpevole coincide con la voce narrante in prima persona che registra l'indagine. Svela il trucco metaletterario.",
            ['Christie', 'Ackroyd', 'Io narratore', 'Colpevole', 'Sorpresa'],
            ['Narratore inattendibile', 'Artificio diegetico', 'Omissione calcolata', 'Ribaltamento delle convenzioni', 'Maestria del giallo']
        ),
        (
            'Il depistaggio di Stato nei crimini di matrice politica',
            "Dalla strage di Piazza Fontana alla scomparsa di documenti top-secret: come apparati deviati costruiscono false piste per impedire l'accertamento storico.",
            ['Piazza Fontana', 'Servizi segreti', 'Bomba', 'Pista anarchica', 'Depistaggio'],
            ['Servizi segreti deviati', 'Ragion di Stato criminale', 'Falsa pista eversiva', 'Occultamento della verità', 'Dovere della memoria democratica']
        ),
        (
            "L'enigma del serial killer e la caccia all'uomo geografica",
            "L'algoritmo di profilazione geografica di Kim Rossmo: calcolare il centroide di residenza del predatore attraverso la distribuzione spaziale dei crimini.",
            ['Serial killer', "Caccia all'uomo", 'Mappa', 'Dove abita', 'Crimini'],
            ['Profilazione geografica di Rossmo', 'Centroide di residenza', 'Buffer zone protetta', 'Pattern seriale territoriale', 'Criminologia analitica']
        ),
        (
            'La testimonianza infantile nei casi di abuso e il protocollo di Carta di Noto',
            "Spiega la delicatezza estrema dell'ascolto protetto del minore: domande suggestive possono impiantare falsi ricordi devastanti distruggendo vite innocenti.",
            ['Bambini', 'Suggestione', 'Abuso', 'Interrogatorio', 'Falsi ricordi'],
            ['Carta di Noto', 'Ascolto protetto del minore', 'Memorie impiantate', 'Domande suggestive vietate', 'Psicologia giuridica minorile']
        ),
        (
            "L'errore giudiziario e l'aporia del caso Enzo Tortora",
            'Un celebre presentatore televisivo arrestato sulla base delle accuse infamanti e concordate di pentiti di camorra screditati. Ricorda il martirio civile.',
            ['Tortora', 'Pentiti', 'Cocaina', 'Camorra', 'Arresto in diretta'],
            ['Martirio giudiziario di Tortora', 'Inattendibilità delle chiamate in correità', 'Fascino mediatico della colpevolezza', 'Riforma della responsabilità dei magistrati', 'Memoria riparatrice']
        ),
        (
            'Il paradosso della scatola nera nelle catastrofi aeree',
            "Come la sincronizzazione del Flight Data Recorder e del Cockpit Voice Recorder consenta di ricostruire l'interazione uomo-macchina prima dell'impatto fatale.",
            ['Aereo caduto', 'Scatola nera', 'Piloti', 'Registrazione', 'Schianto'],
            ['Flight Data Recorder', 'Cockpit Voice Recorder', 'Fattore umano e automazione', 'Inchiesta aeronautica internazionale', 'Prevenzione dei disastri']
        ),
        (
            "La balistica terminale e la traiettoria dei proiettili nell'attentato di Dallas",
            "La controversia della Magic Bullet nell'assassinio di John Fitzgerald Kennedy: analizza criticamente le conclusioni della Commissione Warren.",
            ['Kennedy', 'Dallas', 'Magic bullet', 'Oswald', 'Cecchino'],
            ['Commissione Warren', 'Traiettoria della pallottola unica', 'Rilevazione tridimensionale forense', 'Dubbio cospirativo', 'Declassificazione degli archivi']
        ),
        (
            "L'indagine finanziaria antimafia di Giovanni Falcone: Segui i soldi",
            'Seguire il flusso delle transazioni bancarie internazionali per smascherare il riciclaggio dei proventi del narcotraffico prima che arrivino alle holding pulite.',
            ['Falcone', 'Soldi', 'Banche', 'Riciclaggio', 'Mafia'],
            ['Metodo investigativo Falcone', 'Follow the money', 'Tracciabilità finanziaria globale', 'Misure di prevenzione patrimoniale', 'Colletto bianco mafioso']
        ),
        (
            "L'antropologia forense e l'identificazione dei resti nei massacri di massa",
            'Il lavoro degli scienziati forensi nelle fosse comuni di Srebrenica o dei desaparecidos argentini: restituire un nome e una dignità alle ossa violate.',
            ['Ossa', 'Fosse comuni', 'Srebrenica', 'Desaparecidos', 'Scheletro'],
            ['Antropologia forense transnazionale', "Restituzione dell'identità", 'Osteologia comparata', 'Crimini di guerra puniti', 'Dignità della sepoltura']
        ),
        (
            'La psicologia del delitto passionale e la decostruzione del raptus',
            "Dimostra in tribunale che il femminicidio non è mai frutto di un temporaneo raptus d'amore, ma l'epilogo prevedibile di una dinamica possessiva e patriarcale.",
            ['Raptus', 'Gelosia', 'Tanto amore', 'Follia del momento', 'Uccisa'],
            ['Falsa narrazione del raptus', 'Escalation possessiva patriarcale', 'Femminicidio premeditato', 'Struttura del dominio maschile', 'Rigore probatorio']
        ),
        (
            'Il giallo deduttivo versus il noir esistenziale',
            "Confronta il giallo classico all'inglese (dove l'ordine borghese viene ripristinato) con il noir americano di Chandler (dove la società stessa è marcia e corrotta).",
            ['Giallo', 'Noir', 'Inghilterra', 'America', 'Poliziotto'],
            ['Giallo a enigma (Whodunit)', 'Hard-boiled e noir sociale', 'Disillusione chandleriana', 'Società corrotta', 'Sguardo etico disarmato']
        ),
        (
            "La perizia psichiatrica e l'incapacità di intendere e di volere",
            "Analizza l'Articolo 88 del codice penale: come distinguere la follia clinica che abolisce la colpevolezza morale dalla lucida perversione criminale imputabile.",
            ['Pazzo', 'Capire', 'Articolo 88', 'Manicomio', 'Colpa'],
            ['Vizio totale di mente', "Capacità d'intendere e di volere", 'Perizia psichiatrica forense', 'Imputabilità penale', 'Pericolosità sociale']
        ),
        (
            "La grafologia e l'accertamento dei testamenti olografi falsi",
            "Un anziano milionario lascia tutti i beni al badante dell'ultimo mese. Dimostra con la perizia grafica che la mano dell'anziano è stata guidata con la forza.",
            ['Testamento', 'Eredità', 'Badante', 'Firma falsa', 'Mano guidata'],
            ['Testamento olografo apocrifo', 'Mano guidata o forzata', 'Spontaneità del tracciato grafico', 'Tremolio senile vs imitativo', 'Tutela degli eredi legittimi']
        ),
        (
            "L'orazione per l'Innocente Condannato: il dovere della Revisione",
            "Pronuncia un'arringa solenne per la riapertura del processo: finché un solo innocente marcisce in carcere, la giustizia repubblicana è sconfitta.",
            ['Innocente in carcere', 'Revisione', 'Giudici hanno sbagliato', 'Riaprire il processo', 'Libertà'],
            ['Revisione straordinaria del processo', "Riparazione dell'errore giudiziario", 'Inviolabilità della libertà personale', 'Fermezza garantista', 'Trionfo della verità sostanziale']
        ),
    ],
    "c1": [
        (
            "L'aporia dell'indagine ne Il nome della rosa di Umberto Eco",
            "Guglielmo da Baskerville scopre la serie di delitti nell'abbazia benedettina seguendo lo schema dell'Apocalisse, per poi scoprire che lo schema era solo una coincidenza casuale.",
            ['Eco', 'Guglielmo da Baskerville', 'Nome della rosa', 'Apocalisse', 'Monastero'],
            ['Schema apocalittico fasullo', 'Congettura causale arbitraria', 'Nominalismo filosofico', 'Labirinto abbaziale', "Scacco dell'ordine razionale"]
        ),
        (
            'Il giallo metafisico di Jorge Luis Borges: La morte e la bussola',
            'Erik Lönnrot crede di risolvere una serie di omicidi cabalistici tracciando un rombo perfetto sulla mappa, ma la perfetta geometria logica è la trappola predisposta dal suo nemico.',
            ['Borges', 'Lönnrot', 'Bussola', 'Rombo', 'Trappola'],
            ['Giallo metafisico borgesiano', 'Simmetria geometrica fatale', 'Deduzione come labirinto', 'Cabala e misticismo numerico', "Ironia dell'intelletto"]
        ),
        (
            "La decostruzione del crimine ne L'avversario di Emmanuel Carrère",
            "Jean-Claude Romand ha finto per diciotto anni di essere medico all'OMS prima di sterminare la famiglia. Come narrare l'abisso della menzogna totale senza giustificarla?",
            ['Carrère', 'Romand', 'Bugiardo', 'Finto medico', 'Uccidere la famiglia'],
            ['Abisso della finzione biografica', 'De-sostanzializzazione del sé', "Vuoto ontologico dell'impostura", 'Sguardo letterario non assolutorio', 'Menzogna totalizzante']
        ),
        (
            'La verità testimoniale tra sofistica e decostruzione giudiziaria',
            "Metti a confronto la Gorgiana orazione di Elena con la riflessione di Jacques Derrida: fino a che punto l'eloquenza dell'avvocato istituisce la verità anziché rivelarla?",
            ['Gorgia', 'Derrida', 'Avvocato', 'Verità', 'Discorso convince'],
            ['Retorica sofistica istituente', 'Performanza della verità legale', "Apologia dell'inganno persuasivo", 'Decostruzione forense', 'Limiti della rappresentazione']
        ),
        (
            "L'apologia di Socrate e il paradosso dell'accusa di empietà",
            'Analizza il processo del 399 a.C.: come Meleto e Anito utilizzarono il sospetto di corruzione giovanile per colpire la libertà di pensiero del maestro.',
            ['Socrate', 'Processo', 'Atene', 'Corrompere i giovani', 'Cicuta'],
            ["Accusa d'empietà (Asebeia)", 'Parresìa socratica estrema', 'Discorso apologico integrale', 'Vittoria morale della vittima', 'Condanna politica']
        ),
        (
            "Il caso Dreyfus e il J'accuse di Émile Zola",
            "Nel 1898 uno scrittore sfida lo Stato maggiore dell'esercito francese denunciando l'antisemitismo e il complotto militare contro un ufficiale innocente.",
            ['Dreyfus', 'Zola', "J'accuse", 'Esercito', 'Antisemitismo'],
            ["J'accuse zoliano", 'Affaire Dreyfus fondativo', 'Intellettuale impegnato moderno', 'Complotto militare antisemita', 'Trionfo della verità repubblicana']
        ),
        (
            "L'interrogatorio inquisitorio nel Manuale dei confessori e nell'Inquisizione",
            "Ripercorri il Malleus Maleficarum: la costruzione rituale della colpa dove la negazione dell'imputato viene considerata prova diabolica di ostinazione eretica.",
            ['Inquisizione', 'Streghe', 'Tormentare', 'Confessare il diavolo', 'Malleus'],
            ["Procedura inquisitoria d'eccezione", 'Tortura confessionale istituzionalizzata', 'Circolo ermeneutico satanico', 'Colpa presunta perversa', 'Demistificazione illuminista']
        ),
        (
            'Il delitto imperfetto ne Delitto e castigo di Fëdor Dostoevskij',
            "L'uccisione della vecchia usuraia da parte di Raskol'nikov: il fallimento della teoria dell'uomo straordinario napoleonico di fronte alla coscienza morale.",
            ['Raskolnikov', 'Delitto e castigo', 'Usuraia', 'Napoleone', 'Ascia'],
            ["Teoria dell'uomo straordinario", 'Lacerazione psicologica post-delictum', 'Porfirij Petrovič e il duello dialettico', 'Espiazione redentrice', 'Trionfo della legge interiore']
        ),
        (
            "La semiosi investigativa di Charles Sanders Peirce: l'abduzione pura",
            "Spiega la terza via della logica oltre deduzione e induzione: l'abduzione come scommessa intuitiva geniale che formula un'ipotesi esplicativa dell'anomalia.",
            ['Peirce', 'Abduzione', 'Deduzione', 'Induzione', 'Ipotesi'],
            ['Inferenza abduttiva peirceana', 'Scommessa esplicativa audace', 'Logica della scoperta scientifica', "Trattamento dell'anomalia empirica", 'Plausibilità euristica']
        ),
        (
            "Il processo kafkiano e l'imperscrutabilità della colpa",
            "Josef K. viene arrestato una mattina senza aver fatto nulla di male. Dimostra l'orrore metafisico di una macchina burocratico-giudiziaria senza volto né fine.",
            ['Kafka', 'Processo', 'Josef K', 'Arresto', 'Legge segreta'],
            ['Angoscia kafkiana burocratica', "Imperscrutabilità dell'accusa", 'Alienazione giudiziaria totale', 'Parabola Davanti alla Legge', 'Colpa ontologica inestinguibile']
        ),
        (
            "L'archetipo dell'enigma della Sfinge e il destino di Edipo",
            "La decifrazione dell'enigma dell'uomo come compimento e inizio della tragedia: colui che risolve tutti gli enigmi del mondo è cieco davanti all'enigma di se stesso.",
            ['Sfinge', 'Edipo', 'Enigma', 'Piedi', 'Cieco'],
            ['Enigma della Sfinge tebana', "Cecità dell'intelletto auto-referenziale", 'Destino tragico della conoscenza', 'Tiresia e la visione interiore', 'Scacco della ragione investigatrice']
        ),
        (
            "La finzione probatoria e l'invenzione della stregoneria in Salem",
            'Analizza i processi di Salem del 1692: la spectral evidence (visioni dei testimoni) come base probatoria legale per mandare al patibolo decine di innocenti.',
            ['Salem', 'Streghe', 'Visioni', 'Impaccare', 'Processi'],
            ['Spectral evidence allucinatoria', 'Isteria collettiva puritana', 'Paranoide proiezione comunitaria', 'Fallimento del garantismo probatorio', 'Memoria critica americana']
        ),
        (
            'Il segreto di Stato e la ragion di Stato in Machiavelli e Botero',
            "Fino a che punto l'investigatore o il magistrato può spingersi quando la sicurezza della comunità politica esige che determinate verità rimangano nell'ombra?",
            ['Machiavelli', 'Botero', 'Ragion di Stato', 'Segreto', 'Sovrano'],
            ['Ragion di Stato moderna', 'Arcana imperii', 'Bilanciamento tra verità e ordine', 'Patto fiduciario repubblicano', 'Diritto alla trasparenza']
        ),
        (
            "L'analisi transazionale e la menzogna patologica (Pseudologia fantastica)",
            "Distingui la comune bugia difensiva dalla pseudologia fantastica: la costruzione compulsiva di universi biografici alternativi a cui l'autore stesso finisce per credere.",
            ['Bugiardo patologico', 'Menzogna', 'Fantasia', 'Credere alle proprie bugie', 'Psicopatico'],
            ['Pseudologia fantastica clinica', 'Mitomania compulsiva', "Disintegrazione dell'identità reale", 'Ermeneutica del discorso mitomane', 'Accertamento peritale']
        ),
        (
            'Il dubbio sistematico di René Descartes come indagine metafisica',
            "Il filosofo che mette sotto interrogatorio la totalità del sensibile ipotizzando un genio maligno ingannatore per trovare l'unica verità indubitabile: Cogito, ergo sum.",
            ['Cartesio', 'Dubbio', 'Genio maligno', 'Cogito', 'Tutto finto'],
            ['Dubbio metodico e iperbolico', 'Ipotesi del genio maligno', 'Punto archimedeo della certezza', 'Fondazione metafisica del soggetto', 'Trionfo della coscienza']
        ),
        (
            'La falsificazione delle prove e la teoria dei giochi nelle confessioni',
            "Analizza il dilemma del prigioniero applicato alle strategie d'accusa: come gli inquirenti manipolano le informazioni per indurre i complici ad accusarsi reciprocamente.",
            ['Prigioniero', 'Dilemma', 'Confessare entrambi', 'Teoria dei giochi', 'Tradire il compagno'],
            ['Dilemma del prigioniero', 'Teoria dei giochi strategica', 'Asimmetria informativa processuale', 'Equilibrio di Nash difensivo', "Etica dell'interrogatorio"]
        ),
        (
            "L'archetipo dell'investigatore cieco: Tiresia versus Creonte",
            "Evoca la figura del veggente cieco Tiresia che, privo della vista biologica, possiede la vista divina della verità che smaschera l'arroganza dell'investigatore sovrano.",
            ['Tiresia', 'Cieco', 'Edipo', 'Vedere la verità', 'Dèi'],
            ['Chiaroveggenza tragica interiore', 'Cecità biologica vs noetica', 'Smascheramento della cecità del potere', 'Parola profetica inascoltata', 'Trascendenza del vero']
        ),
        (
            'La manipolazione della memoria storica nei regimi totalitari',
            "Rivisita 1984 di George Orwell: il Ministero della Verità dove i documenti d'archivio vengono riscritti ogni giorno per cancellare l'esistenza degli sgraditi (Unpersons).",
            ['Orwell', '1984', 'Cancellare la storia', 'Ministero della Verità', 'Buchi della memoria'],
            ['Riscrizione retroattiva del passato', "Cancellazione dell'evidenza documentale", 'Totalitarismo epistemologico orwelliano', "Custodia dell'archivio storico", 'Resistenza memoriale']
        ),
        (
            "Il paradosso del testimone perfetto: l'onniscienza tragica",
            "Argomenta sulla solitudine dell'unico testimone che sa tutta la verità ma è impossibilitato a provarla legalmente in aula: il dramma della verità senza prova.",
            ['Sapere tutto', 'Nessuna prova', 'Giudice', 'Tribunale', 'Verità muta'],
            ['Tragicità del testimone inascoltato', 'Frattura tra sapere e provare', 'Impotenza della verità pura', 'Dignità della testimonianza solitaria', "Giustizia dell'avvenire"]
        ),
        (
            "L'Orazione per la Verità Incorruttibile: il Verbum Investigativo",
            "Pronuncia una requisitoria solenne: la verità può essere nascosta, sepolta, calunniata o differita, ma prima o poi riemergerà dall'ombra perché l'Essere rifiuta il nulla.",
            ['Verità riemerge', 'Bugiardi', 'Luce', 'Fine', 'Menzogna sconfitta'],
            ['Trionfo ineluttabile della Verità', 'Rifiuto ontologico della menzogna', "Magistero dell'Oratore-Detective", 'Luce imperitura della Ragione', 'Consacrazione del Vero']
        ),
    ],
    "c2": [
        (
            "L'aporia dell'indagine pura: l'osservatore che altera il sistema",
            "Dimostra con il principio d'indeterminazione di Heisenberg e la psicoanalisi lacaniana che nessun investigatore può osservare la scena del delitto senza diventarne parte integrante e alterarla.",
            ['Heisenberg', 'Osservatore', 'Scena del crimine', 'Lacan', 'Neutro'],
            ['Indeterminazione heisenberghiana', "Contaminazione dell'osservatore", 'Sguardo desiderante lacaniano', 'Impossibilità della purezza neutrale', 'Complesso investigativo']
        ),
        (
            'Il delitto come una delle belle arti secondo Thomas De Quincey',
            'Ripercorri la vertiginosa ironia del saggio del 1827: quando il delitto cessa di essere valutato con la pietà morale per diventare oggetto di puro godimento estetico formale.',
            ['De Quincey', 'Belle arti', 'Uccidere per arte', 'Estetica', 'Orrore bello'],
            ['Estetizzazione del delitto', 'Sublime orrore dequinceyano', "Sospensione ironica dell'etica", 'Compiutezza formale della scena', 'Critica della morale borghese']
        ),
        (
            "L'enigma del tempo e l'irreversibilità del danno in Vladimir Jankélévitch",
            "Indaga l'essenza ontologica del crimine: non è solo la perdita di un bene, ma l'irreversibilità temporale che impedisce per sempre che ciò che è accaduto non sia accaduto.",
            ['Tempo', 'Irreversibile', 'Jankélévitch', 'Tornare indietro', 'Cancellare'],
            ['Irreversibilità temporale del torto', "Fatticità inestirpabile dell'accaduto", 'Inconsolabilità del danno', 'Ontologia del passato', 'Impossibilità della cancellazione']
        ),
        (
            'La confessione come sacramento e dispositivo di potere in Michel Foucault',
            "Nel primo volume della Storia della sessualità, decostruisci l'obbligo secolare dell'Occidente di estrarre la verità attraverso la confessione estorta e verbalizzata.",
            ['Foucault', 'Confessione', 'Potere', 'Prete', 'Dire la verità'],
            ['Dispositivo confessionale foucaultiano', 'Volontà di sapere e asservimento', 'Produzione disciplinare della verità', "Istituzionalizzazione dell'intimo", 'Potere pastorale moderno']
        ),
        (
            "L'abisso della colpa metafisica e il silenzio di Amleto",
            "Analizza il dramma shakespeariano: l'apparizione dello spettro del padre apre un'indagine che paralizza la volontà dell'eroe di fronte alla marcescenza totale della corte danese.",
            ['Amleto', 'Spettro', 'Vendetta', 'Danimarca marcia', 'Dubbio'],
            ['Esitazione tragica amletica', 'Spettro e dovere testimoniale', 'Marcescenza ontologica del regno', 'Il resto è silenzio', 'Paralisi della ragione indagatrice']
        ),
        (
            'Il giallo metafisico di Friedrich Dürrenmatt: La promessa',
            "Sottotitolato 'Requiem per il romanzo giallo', l'opera demolisce la fede nell'onnipotenza del metodo deduttivo: il detective ha ragione su tutto, ma il caso viene deciso dal puro caso cieco.",
            ['Dürrenmatt', 'Promessa', 'Detective impazzito', 'Caso fortuito', 'Giallo finito'],
            ['Requiem per il romanzo giallo', 'Scacco della presunzione deduttiva', 'Intrusione del caso cieco (Zufall)', 'Fallimento del trionfo logico', "Tragicità dell'investigatore sconfitto"]
        ),
        (
            "La decostruzione della prova testimoniale: il processo a Giovanna d'Arco",
            "Analizza gli atti originali del processo di Rouen del 1431: come i teologi inglesi manipolarono le risposte mistiche della Pulzella per trasformare l'eroismo in eresia diabolica.",
            ["Giovanna d'Arco", 'Processo', 'Rouen', 'Streghe', 'Voci divine'],
            ['Manipolazione teologico-giudiziaria', 'Parresìa mistica di Giovanna', 'Trappola inquisitoria formalizzata', 'Martirio del candore', 'Riabilitazione postuma']
        ),
        (
            "L'archetipo dell'enigma insolubile e la teologia negativa",
            "Dimostra come la massima indagine filosofica conduca necessariamente all'apofatismo: la verità ultima di Dio e dell'Essere non può essere catturata da sillogismi ma solo sfiorata per silenzio.",
            ['Teologia negativa', 'Dio inconoscibile', 'Silenzio', 'Sillogismo', 'Sapere tutto'],
            ['Apofatismo ontologico', 'Docta ignorantia cusiana', 'Ineffabilità del Fondamento', "Eclissi dell'intelletto calcolante", 'Mistero primigenio inaccessibile']
        ),
        (
            "Il delitto e il castigo dell'innocente: l'archetipo biblico di Giobbe",
            'Di fronte alla perdita totale di famiglia e salute, Giobbe rifiuta le spiegazioni consolatorie e moraliste dei tre amici, pretendendo un contraddittorio diretto a viso aperto con Dio.',
            ['Giobbe', 'Colpa', 'Perché a me', 'Dio', 'Amici consolatori'],
            ['Protesta innocente di Giobbe', 'Rifiuto della teodicea consolatoria', "Contraddittorio con l'Altissimo", 'Mistero del dolore immotivato', 'Teofania della tempesta']
        ),
        (
            'La genealogia del sospetto in Paul Ricoeur: Marx, Nietzsche, Freud',
            "Analizza i tre maestri del sospetto che hanno demolito l'illusione cartesiana della trasparenza della coscienza, svelando le matrici nascoste: economia, risentimento e inconscio.",
            ['Ricoeur', 'Maestri del sospetto', 'Marx', 'Nietzsche', 'Freud'],
            ['Scuola del sospetto', 'Demistificazione delle false coscienze', 'Ermeneutica della decifrazione', 'Oltre la trasparenza del Cogito', 'Disvelamento genealogico']
        ),
        (
            "L'enigma del cigno nero e l'epistemologia dell'imprevisto in Nassim Taleb",
            "Dimostra la fragilità di ogni modello predittivo basato sulla statistica del passato: l'evento raro, ad alto impatto e retrospettivamente razionalizzato che scombina tutte le indagini.",
            ['Cigno nero', 'Taleb', 'Imprevisto', 'Statistica', 'Tutti cigni bianchi'],
            ['Evento Cigno Nero (Black Swan)', 'Fragilità epistemica predittiva', "Cecità all'asimmetria causale", 'Razionalizzazione retroattiva', 'Antifragilità investigativa']
        ),
        (
            "L'inquisizione contemporanea e il processo a Galileo Galilei",
            "Ripercorri l'abiura del 1633: il conflitto titanico tra l'evidenza empirica delle osservazioni telescopiche e l'autorità dogmatica del principio di autorità aristotelico.",
            ['Galileo', 'Abiura', 'Telescopio', 'Terra gira', 'Inquisizione'],
            ['Conflitto epistemologico epocale', 'Osservazione telescopica eversiva', "Rifiuto dell'Ipse Dixit", 'Eppur si muove', 'Nascita del metodo sperimentale']
        ),
        (
            'La decostruzione del concetto di confessione sincera: la tortura bianca',
            "Nel totalitarismo moderno, la privazione del sonno e l'isolamento sensoriale inducono l'imputato a confessare qualsiasi mostruosità pur di far cessare il tormento interiore.",
            ['Tortura bianca', 'Sonno', 'Isolamento', 'Confessare tutto', 'Polizia'],
            ['Tortura bianca asettica', 'Annientamento psichico del soggetto', 'Auto-accusa delirante indotta', 'Orrore della coercizione invisibile', "Tutela dell'integrità umana"]
        ),
        (
            "Il giallo ontologico di Thomas Pynchon: L'incanto del lotto 49",
            "Edipa Maas si ritrova sulle tracce del sistema postale clandestino Tristero: l'indagine conduce a un bivio tragico tra complotto cosmico reale e paranoia psicotica personale.",
            ['Pynchon', 'Lotto 49', 'Tristero', 'Complotto', 'Paranoia'],
            ['Paranoia ermeneutica pynchoniana', 'Tristero e ordine clandestino', 'Entropia informativa incontenibile', 'Insolubilità del complotto', "Vertigine dell'apofenia"]
        ),
        (
            "L'archetipo dell'alibi impossibile: la simultaneità quantistica",
            "Dalla meccanica quantistica alla riflessione filosofica: il fenomeno dell'entanglement dove due particelle separate da anni luce comunicano istantaneamente, sfidando lo spazio euclideo.",
            ['Quantistica', 'Due posti insieme', 'Entanglement', 'Fisica', 'Impossibile'],
            ['Entanglement quantistico', "Non-località dell'evento fisico", 'Superamento dello spazio newtoniano', 'Simultaneità non causale', 'Vertigine della materia']
        ),
        (
            "L'apologia della notte dell'intelletto e la Docta Ignorantia",
            'Ripercorri Nicola Cusano: il vertice della conoscenza umana non è la presunzione di aver risolto tutti i misteri del cosmo, ma la consapevolezza luminosa della propria ignoranza.',
            ['Cusano', 'Docta ignorantia', 'Sapere tutto', 'Ignoranza', 'Limite'],
            ['Docta ignorantia cusiana', 'Coincidentia oppositorum', 'Riconoscimento del limite intellettuale', 'Pace contemplativa', 'Umiltà del vero sapiente']
        ),
        (
            "L'enigma del suicidio di Seneca: l'investigatore che giudica se stesso",
            "Costretto da Nerone a togliersi la vita, il filosofo stoico trasforma la propria morte in un'orazione vivente di libertà, accusando il tiranno con la serenità del proprio sangue.",
            ['Seneca', 'Nerone', 'Suicidio', 'Vene tagliate', 'Tiranno'],
            ['Morte esemplare senecana', 'Libertà stoica suprema', "Atto d'accusa contro la tirannide", "Tranquillità dell'animo serena", 'Eternità della virtù']
        ),
        (
            'La parresìa del testimone solitario contro il complotto di Stato',
            'Evoca la figura storica di chi, consapevole che rivelare la verità sul complotto dei potenti significherà la propria condanna a morte, sceglie comunque di parlare.',
            ['Complotto', 'Tacere', 'Morte se parlo', 'Coraggio', 'Segreto di Stato'],
            ['Parresìa testimoniale mortale', 'Incorruttibilità della verità', 'Martirio del testimone solitario', 'Frattura del silenzio imposto', 'Eredità immortale']
        ),
        (
            "La decostruzione del mito dell'indagine perfetta: il resto è enigma",
            'Dimostra con saggezza conclusiva che per ogni mistero risolto dalla scienza e dalla logica, si aprono dieci nuovi abissi di meraviglia e interrogativi più profondi.',
            ['Fine', 'Tutto spiegato', 'Nessun mistero', 'Scienza risolve', 'Chiudere il caso'],
            ["Fecondità dell'enigma inesauribile", 'Abisso della meraviglia cosmica', 'Apertura perenne della domanda', "Respiro dell'infinito", "Magistero dell'indagine perenne"]
        ),
        (
            "L'Inno alla Luce della Verità: il Giuramento Supremo dell'Oratore-Giudice",
            "Pronuncia l'orazione che congeda il modulo del Mistero: non ci sarà oscurità tanto densa, né segreto tanto profondo che la parola della Verità non possa illuminare e redimere.",
            ['Luce', 'Buio', 'Mistero', 'Verità', 'Fine'],
            ['Fiat Lux ermeneutico', 'Redenzione della Verità celata', 'Schiacciamento della tenebra', "Magistero dell'Oratore Supremo", 'Eternità della Giustizia']
        ),
    ],
}
