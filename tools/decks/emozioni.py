# Mazzo: Emozioni, Relazioni & Empatia (emozioni)
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            "Il palloncino volato via",
            "Hai visto volare via nel cielo il palloncino rosso del tuo amico. Spiegagli come fare a non essere triste e inventa dove sta viaggiando.",
            ["Palloncino", "Rosso", "Piangere", "Cielo", "Perso"],
            ["Nuvole", "Viaggio", "Sorriso", "Uccellino", "Abbraccio"]
        ),
        (
            "La paura del temporale",
            "C'è un forte temporale con tuoni e lampi. Racconta alla tua sorellina perché i tuoni sono solo nuvole che giocano a tamburo.",
            ["Tuono", "Lampo", "Paura", "Pioggia", "Buio"],
            ["Musica", "Tamburo", "Coperta", "Luce", "Sicuro"]
        ),
        (
            "Il leone nella scatola",
            "Sei arrabbiatissimo perché un compagno ti ha fatto cadere la torre di costruzioni. Spiega con calma cosa senti dentro la pancia.",
            ["Rabbia", "Torre", "Cadere", "Urlo", "Pugno"],
            ["Respiro", "Fuoco", "Pazienza", "Costruire", "Pace"]
        ),
        (
            "Il cane che scodinzola",
            "Hai incontrato per strada un cagnolino festoso. Descrivi la felicità pura che si prova quando qualcuno ti accoglie con gioia.",
            ["Cane", "Coda", "Felice", "Strada", "Bau"],
            ["Festa", "Zampa", "Affetto", "Salto", "Amicizia"]
        ),
        (
            "Il disegno rovinato per sbaglio",
            "Hai fatto una macchia sul foglio del tuo vicino di banco. Chiedigli scusa spiegando come trasformare la macchia in un mostriciattolo simpatico.",
            ["Macchia", "Scusa", "Foglio", "Sbaglio", "Disegno"],
            ["Mostro", "Fantasia", "Colorare", "Rimedio", "Insieme"]
        ),
        (
            "La giostra troppo alta",
            "I tuoi amici vogliono salire sulla ruota panoramica, ma tu hai le vertigini. Spiega loro che avere un po' di timore è normale.",
            ["Ruota", "Alto", "Paura", "Giro", "Girotondo"],
            ["Coraggio", "Guardare", "Fermarsi", "Aspettare", "Mano"]
        ),
        (
            "Il regalo inaspettato",
            "Un compagno ti ha regalato una conchiglia raccolta al mare. Ringrazialo spiegando perché i piccoli doni scaldano il cuore.",
            ["Regalo", "Conchiglia", "Mare", "Grazie", "Bello"],
            ["Cuore", "Ricordo", "Sorpresa", "Gentile", "Tesoro"]
        ),
        (
            "La timidezza alla festa",
            "Sei arrivato a una festa di compleanno e non conosci nessuno. Racconta come ci si sente a restare vicino alla porta prima di tuffarsi nei giochi.",
            ["Festa", "Porta", "Timido", "Torta", "Tutti"],
            ["Passo", "Saluto", "Musica", "Curiosità", "Giocare"]
        ),
        (
            "Il compagno che non ride mai",
            "C'è un bambino in classe che sembra sempre imbronciato. Prova a fargli una battuta gentile per vedere se spunta un piccolo sorriso.",
            ["Triste", "Ridere", "Bocca", "Solo", "Niente"],
            ["Battuta", "Sole", "Solletico", "Compagnia", "Occhi"]
        ),
        (
            "Il puzzle da finire insieme",
            "Manca un solo pezzo al grande puzzle e siete in due a volerlo incastrare. Trova una soluzione per completarlo felici entrambi.",
            ["Pezzo", "Puzzle", "Mio", "Vincere", "Tavolo"],
            ["Accordo", "Incastro", "Disegno", "Condividere", "Festa"]
        ),
        (
            "Il silenzio della buonanotte",
            "La mamma spegne la luce della cameretta. Descrivi le ombre amiche che si formano sui muri e i sogni dolci che stanno arrivando.",
            ["Luce", "Letto", "Dormire", "Mostri", "Notte"],
            ["Stella", "Sogno", "Coperta", "Ombra", "Tranquillo"]
        ),
        (
            "La prima volta sui pattini",
            "Hai messo i pattini a rotelle e le gambe tremano come budino. Convinciti a fare il primo passo tenendoti alla staccionata.",
            ["Pattini", "Cadere", "Male", "Gambe", "Ghiaccio"],
            ["Equilibrio", "Pista", "Fiducia", "Scivolare", "Vento"]
        ),
        (
            "La merenda condivisa a metà",
            "Il tuo vicino di banco ha dimenticato la brioche a casa. Dividi la tua a metà spiegando perché mangiare insieme è più saporito.",
            ["Merenda", "Fame", "Metà", "Pane", "Dimenticare"],
            ["Gusto", "Dividere", "Dolce", "Generoso", "Bontà"]
        ),
        (
            "Il pianto per la ginocchiata",
            "Sei scivolato nel cortile e ti sei fatto un graffio sul ginocchio. Spiega perché piangere sfoga il dolore e fa passare la bua prima.",
            ["Male", "Sangue", "Ginocchio", "Pianto", "Cerotto"],
            ["Soffio", "Respiro", "Guarire", "Lacrima", "Forza"]
        ),
        (
            "L'abbraccio dopo il litigio",
            "Dopo aver urlato per chi doveva usare i pennarelli, fate la pace. Racconta quanto è bello sentire che l'amicizia è più forte del litigio.",
            ["Pace", "Litigio", "Pennarelli", "Urlo", "Nemico"],
            ["Abbraccio", "Stringere", "Calma", "Ricominciare", "Amico"]
        ),
        (
            "Il bruco che diventa farfalla",
            "Guardi un piccolo bruco sulla foglia. Spiega a un compagno che tutti possiamo cambiare e diventare qualcosa di meraviglioso con pazienza.",
            ["Bruco", "Farfalla", "Foglia", "Ali", "Brutto"],
            ["Attesa", "Bozzolo", "Volo", "Colori", "Meraviglia"]
        ),
        (
            "La paura del buio sotto il letto",
            "Sei andato a guardare con la torcia sotto il letto e c'erano solo pantofole e polvere. Rassicura te stesso con una risata.",
            ["Sotto", "Letto", "Mostro", "Torcia", "Paura"],
            ["Pantofole", "Polvere", "Risata", "Cameretta", "Fantasia"]
        ),
        (
            "Il complimento sincero",
            "Hai notato che una tua compagna ha fatto un disegno bellissimo. Dille cosa ti piace davvero senza vergognarti di farle un complimento.",
            ["Disegno", "Bello", "Brava", "Vergogna", "Colori"],
            ["Particolare", "Luce", "Sincero", "Ammirazione", "Cuore"]
        ),
        (
            "La tristezza di fine vacanze",
            "È l'ultimo giorno di vacanza al mare. Spiega come portare nel cuore il profumo dell'estate anche quando tornerai a scuola.",
            ["Estate", "Mare", "Finita", "Scuola", "Sabbia"],
            ["Ricordo", "Onde", "Zaino", "Scaldare", "Avventura"]
        ),
        (
            "La festa a sorpresa riuscita",
            "Tutti insieme siete sbucati da dietro il divano urlando auguri per il compleanno del maestro. Racconta l'emozione di vedere la sua faccia stupita.",
            ["Sorpresa", "Divano", "Urlo", "Torta", "Compleanno"],
            ["Stupore", "Occhi", "Segreto", "Gioia", "Applauso"]
        )
    ],
    "a2": [
        (
            "Il compagno escluso dal gioco",
            "Durante l'intervallo, un gruppo non vuole far giocare un nuovo compagno. Convinci la squadra che includerlo rende il gioco più divertente.",
            ["Squadra", "Gioco", "Escluso", "Bravura", "Palla"],
            ["Partecipare", "Accogliere", "Regole", "Entusiasmo", "Coinvolgere"]
        ),
        (
            "L'ansia prima della recita",
            "Sei dietro le quinte del teatro scolastico con il cuore a mille. Pronuncia un discorso d'incoraggiamento agli altri attori della classe.",
            ["Palco", "Paura", "Battuta", "Dimenticare", "Pubblico"],
            ["Respiro", "Applauso", "Coraggio", "Squadra", "Emozione"]
        ),
        (
            "La gelosia per il fratellino",
            "È nato un fratellino e tutti parlano solo di lui. Spiega a te stesso e ai genitori come trasformare l'invidia in un ruolo da guida protettiva.",
            ["Fratello", "Piccolo", "Gelosia", "Attenzione", "Mamma"],
            ["Crescita", "Esempio", "Protettore", "Affetto", "Condivisione"]
        ),
        (
            "Chiedere scusa dopo un brutto gesto",
            "Hai offeso un amico durante una partita concitata. Fai un discorso di scuse onesto spiegando che la rabbia del momento non giustifica le parole.",
            ["Scusa", "Partita", "Rabbia", "Offesa", "Amico"],
            ["Riconoscere", "Sbaglio", "Rispetto", "Lealtà", "Rimediare"]
        ),
        (
            "Il mediatore del cortile",
            "Due compagni si stanno strattonando per decidere chi debba battere il calcio d'angolo. Intervieni con parole ferme per ristabilire la calma.",
            ["Pallone", "Calcio", "Litigare", "Picchiare", "Mio"],
            ["Arbitro", "Accordo", "Dialogo", "Fermarsi", "Ragione"]
        ),
        (
            "Il peso di un segreto confidato",
            "Un amico ti ha rivelato un segreto che lo fa soffrire molto. Spiegagli perché confidarsi con un adulto di fiducia non è un tradimento ma un aiuto.",
            ["Segreto", "Spia", "Tradire", "Dire", "Paura"],
            ["Fiducia", "Aiuto", "Sollievo", "Proteggere", "Coraggio"]
        ),
        (
            "La delusione per un brutto voto",
            "Hai studiato tanto ma il compito non è andato come speravi. Trova le parole per non scoraggiarti e ripartire con determinazione.",
            ["Voto", "Studio", "Compito", "Brutto", "Piangere"],
            ["Impegno", "Migliorare", "Determinazione", "Analisi", "Ripartire"]
        ),
        (
            "L'empatia verso chi ha perso",
            "La tua squadra ha vinto la coppa del torneo scolastico. Rivolgiti agli avversari sconfitti con parole di sincera stima sportiva.",
            ["Vincere", "Perdere", "Coppa", "Campioni", "Sconfitta"],
            ["Onore", "Stima", "Avversario", "Impegno", "Sportività"]
        ),
        (
            "La paura di cambiare scuola",
            "Siete in quinta primaria e l'anno prossimo andrete alle medie. Esprimi alla classe le speranze e i timori per il nuovo percorso.",
            ["Medie", "Grandi", "Professori", "Paura", "Scuola"],
            ["Futuro", "Crescita", "Ricordi", "Legame", "Curiosità"]
        ),
        (
            "Il valore della diversità fisica",
            "Un compagno si sente a disagio perché porta un apparecchio vistoso o gli occhiali spessi. Spiegagli perché ogni dettaglio ci rende unici.",
            ["Occhiali", "Apparecchio", "Brutto", "Vergogna", "Ridere"],
            ["Unicità", "Personalità", "Bellezza", "Accettazione", "Stile"]
        ),
        (
            "La noia come momento creativo",
            "Piove a dirotto e non potete uscire né usare i videogiochi. Convinci i tuoi fratelli che la noia è la porta segreta per inventare giochi nuovi.",
            ["Noia", "Piovere", "Schermo", "Niente", "Uscire"],
            ["Fantasia", "Invenzione", "Tempo", "Creatività", "Avventura"]
        ),
        (
            "Difendere un compagno dalle prese in giro",
            "Qualcuno nel corridoio ha preso di mira un bambino più piccolo. Prendi la parola davanti a tutti per fermare i bulli con fermezza.",
            ["Bullo", "Piccolo", "Prendere in giro", "Ridere", "Debole"],
            ["Fermarsi", "Dignità", "Coraggio", "Protezione", "Giustizia"]
        ),
        (
            "La gioia dell'altruismo senza telecamere",
            "Hai aiutato un anziano a portare le borse pesanti senza che nessuno ti vedesse. Descrivi il calore interiore che si prova nel fare del bene.",
            ["Aiutare", "Borse", "Vecchio", "Vedere", "Bravo"],
            ["Gratuito", "Calore", "Gesto", "Coscienza", "Soddisfazione"]
        ),
        (
            "Il silenzio che consola",
            "Un tuo compagno ha perso il suo animaletto del cuore e non vuole parlare. Spiega perché stargli vicino in silenzio vale più di mille parole.",
            ["Morto", "Animale", "Parlare", "Triste", "Consolare"],
            ["Presenza", "Rispetto", "Vicinanza", "Silenzio", "Comprensione"]
        ),
        (
            "La paura di non essere accettati",
            "Sei arrivato in una nuova città e temi di non trovare amici. Spiega a te stesso come rompere il ghiaccio mostrando chi sei veramente.",
            ["Nuovo", "Città", "Amici", "Solo", "Paura"],
            ["Autenticità", "Apertura", "Ascolto", "Incontro", "Speranza"]
        ),
        (
            "Riconoscere il merito dell'avversario",
            "Un tuo compagno ha vinto il concorso di disegno che speravi di vincere tu. Congratulati con lui elogiando la sua tecnica e fantasia.",
            ["Vinto", "Premio", "Rosicare", "Disegno", "Mio"],
            ["Merito", "Congratulazioni", "Talento", "Ispirazione", "Maturità"]
        ),
        (
            "La vergogna di aver mentito",
            "Hai raccontato una bugia per sembrare più coraggioso davanti al gruppo. Confessa la verità spiegando quanto pesava quella maschera.",
            ["Bugia", "Dire", "Finto", "Vergogna", "Gruppo"],
            ["Verità", "Maschera", "Sollievo", "Onestà", "Sincerità"]
        ),
        (
            "L'ascolto quando qualcuno soffre",
            "La tua migliore amica ha gli occhi lucidi durante l'intervallo. Invitala a confidarsi assicurandole che non la giudicherai mai.",
            ["Piangere", "Problema", "Giudicare", "Occhi", "Segreto"],
            ["Ascolto", "Accoglienza", "Spazio", "Fiducia", "Affetto"]
        ),
        (
            "Il coraggio di dire di no al gruppo",
            "I compagni propongono di fare uno scherzo pesante al custode. Spiega al gruppo perché rifiuti di partecipare a quell'azione.",
            ["Scherzo", "Custode", "Gruppo", "Paura", "Insieme"],
            ["Limite", "Rispetto", "Autonomia", "Coscienza", "Fermezza"]
        ),
        (
            "La gratitudine verso chi lavora per noi",
            "È l'ultimo giorno di scuola. Pronuncia un ringraziamento caloroso ai collaboratori scolastici e alla cuoca della mensa a nome della classe.",
            ["Mensa", "Scuola", "Grazie", "Lavoro", "Pulire"],
            ["Gratitudine", "Cura", "Servizio", "Riconoscimento", "Comunità"]
        )
    ],
    "b1": [
        (
            "L'esclusione dal gruppo social",
            "Sei stato rimosso dalla chat di gruppo dopo un malinteso. Spiega ai compagni il peso psicologico dell'isolamento digitale.",
            ["Chat", "Gruppo", "Rimosso", "Telefono", "Messaggi"],
            ["Isolamento", "Confronto", "Chiarimento", "Maturità", "Dignità"]
        ),
        (
            "La paura del giudizio dei pari",
            "Un compagno evita di intervenire in classe per non sembrare il cocco del professore. Incoraggialo a far valere le sue idee senza timore.",
            ["Cocco", "Professore", "Intervento", "Prendere in giro", "Vergogna"],
            ["Autostima", "Partecipazione", "Libertà", "Espressione", "Valore"]
        ),
        (
            "La gestione della rabbia esplosiva",
            "Dopo un alterco in corridoio, proponi alla classe una riflessione sulla differenza tra sentire rabbia e agire con violenza distruttiva.",
            ["Rabbia", "Pugno", "Urlare", "Corridoio", "Calma"],
            ["Autocontrollo", "Decantazione", "Impulso", "Canalizzare", "Consapevolezza"]
        ),
        (
            "La lealtà tra amici e i suoi limiti",
            "Un amico ti chiede di coprire un'assenza ingiustificata o un guaio grave. Spiegagli perché la vera amicizia non richiede complicità nell'errore.",
            ["Coprire", "Bugia", "Amico", "Guaio", "Segreto"],
            ["Responsabilità", "Integrità", "Complicità", "Sincerità", "Crescita"]
        ),
        (
            "L'ansia da prestazione scolastica",
            "Molti studenti vivono la settimana delle verifiche con insonnia e panico. Proponi all'assemblea di classe strategie per ridimensionare il voto.",
            ["Verifica", "Voto", "Panico", "Insonnia", "Bocciare"],
            ["Apprendimento", "Pressione", "Serenità", "Metodo", "Misura"]
        ),
        (
            "La nostalgia delle cose semplici",
            "Crescendo, vi accorgete che i giochi d'infanzia stanno scomparendo. Fai un elogio dell'immaginazione spontanea prima dell'adolescenza.",
            ["Bambino", "Piccolo", "Crescere", "Giocattoli", "Nostalgia"],
            ["Innocenza", "Transizione", "Spontaneità", "Custodire", "Ricordo"]
        ),
        (
            "Il confronto generazionale con i genitori",
            "Parla in veste di mediatore familiare: spiega ai compagni e ai genitori come superare il muro del silenzio e dell'incomprensione reciproca.",
            ["Genitori", "Mamma", "Papà", "Urla", "Telefono"],
            ["Ascolto", "Generazioni", "Prospettiva", "Pazienza", "Comprensione"]
        ),
        (
            "Il coraggio della vulnerabilità",
            "Spesso tra ragazzi ci si mostra invulnerabili e cinici. Dimostra ai tuoi coetanei che mostrare le proprie debolezze è la forma più alta di coraggio.",
            ["Forte", "Debole", "Maschera", "Piangere", "Duro"],
            ["Vulnerabilità", "Autenticità", "Franchezza", "Umanità", "Risonanza"]
        ),
        (
            "La delusione di un'amicizia che finisce",
            "Un legame nato alle elementari si sta sciogliendo col cambio di interessi. Trova le parole per salutare l'amico senza rancore.",
            ["Amicizia", "Fine", "Cambiato", "Rancore", "Separarsi"],
            ["Evoluzione", "Gratitudine", "Strade", "Rispetto", "Consapevolezza"]
        ),
        (
            "Il potere costruttivo del perdono",
            "Dopo un lungo periodo di freddezza per un torto subito, decidi di concedere il perdono. Spiega come perdonare liberi chi lo compie prima ancora di chi lo riceve.",
            ["Torto", "Vendetta", "Perdono", "Scusa", "Rabbia"],
            ["Liberazione", "Rancore", "Serenità", "Riconciliazione", "Maturità"]
        ),
        (
            "L'invidia verso i successi altrui",
            "Un compagno ottiene una selezione importante o vince una gara. Analizza l'invidia che nasce spontanea e mostra come tramutarla in stimolo.",
            ["Invidia", "Gelosia", "Vinto", "Lui", "Fortuna"],
            ["Emulazione", "Ispirazione", "Riconoscimento", "Generosità", "Miglioramento"]
        ),
        (
            "La solitudine tra la folla",
            "Anche in mezzo a una classe affollata o su un social pieno di follower ci si può sentire soli. Dai voce a questo sentimento diffuso tra i giovani.",
            ["Solo", "Gente", "Follower", "Folla", "Triste"],
            ["Autenticità", "Connessione", "Profondità", "Superficiale", "Presenza"]
        ),
        (
            "La tolleranza alla frustrazione",
            "Non tutto va come pianificato nei progetti scolastici. Argomenta sull'importanza di accettare l'imprevisto come occasione di maturazione.",
            ["Sbaglio", "Piano", "Arrabbiarsi", "Fallimento", "Pazienza"],
            ["Resilienza", "Adattamento", "Ostacolo", "Maturazione", "Prospettiva"]
        ),
        (
            "Il rispetto del confine personale",
            "Qualcuno insiste per toccare i tuoi oggetti o fare battute sul tuo corpo. Esprimi il diritto inviolabile di ciascuno a porre confini chiari.",
            ["Corpo", "Toccarsi", "Scherzo", "Oggetti", "Basta"],
            ["Inviolabilità", "Confine", "Dignità", "Spazio", "Autodeterminazione"]
        ),
        (
            "L'entusiasmo contagioso",
            "Devi presentare un'idea per un progetto extracurricolare. Parla con tale passione ed energia positiva da trascinare l'intero consiglio di classe.",
            ["Progetto", "Bello", "Fare", "Idea", "Votare"],
            ["Entusiasmo", "Coinvolgimento", "Visione", "Condivisione", "Passione"]
        ),
        (
            "La gestione del lutto e della perdita",
            "La classe è colpita dalla perdita di un docente amato o di un familiare di un compagno. Pronuncia un discorso che offra conforto e dignità al dolore.",
            ["Morte", "Triste", "Piangere", "Andato via", "Finito"],
            ["Eredità", "Memoria", "Commiato", "Solidarietà", "Impronta"]
        ),
        (
            "La gratitudine per gli insegnanti severi",
            "Molti criticano il docente più esigente. Dimostra ai compagni che il rigore metodologico e l'onestà valutativa sono la forma più seria di rispetto.",
            ["Severo", "Prof", "Cattivo", "Note", "Compiti"],
            ["Rigore", "Esigenza", "Formativo", "Riconoscimento", "Crescita"]
        ),
        (
            "Il superamento del conformismo",
            "Tutti indossano le stesse scarpe o ascoltano gli stessi brani per non sentirsi diversi. Difendi il valore anticonformista dell'originalità.",
            ["Moda", "Tutti", "Vestiti", "Uguali", "Comprare"],
            ["Identità", "Omologazione", "Singolarità", "Coraggio", "Autonomia"]
        ),
        (
            "La mediazione nei litigi di famiglia",
            "Spiega come un figlio adolescente possa portare una ventata di lucidità e dialogo sereno quando le tensioni in casa salgono alle stelle.",
            ["Casa", "Genitori", "Urlare", "Famiglia", "Tensione"],
            ["Ponte", "Disinnescare", "Prospettiva", "Serenità", "Dialogo"]
        ),
        (
            "La fiducia riposta negli altri",
            "Un compagno a cui avevi affidato una responsabilità ha commesso un errore. Spiega perché rinnovargli la fiducia è la scelta più saggia e umana.",
            ["Fiducia", "Errore", "Sbagliato", "Affidare", "Bocciato"],
            ["Seconda opportunità", "Crescita", "Responsabilizzare", "Stima", "Umanità"]
        )
    ],
    "b2": [
        (
            "L'analfabetismo emotivo contemporaneo",
            "Analizza la tendenza giovanile a mascherare ogni fragilità dietro emoji e sarcasmo. Sostieni l'urgenza di un'educazione sentimentale strutturata.",
            ["Emoji", "Sarcasmo", "Sentimentale", "Fragilità", "Social"],
            ["Lessico affettivo", "Consapevolezza", "Educazione emotiva", "Spessore relazionale", "Autenticità"]
        ),
        (
            "L'empatia selettiva e le bolle mediatiche",
            "Siamo pronti a commuoverci per una storia virale e indifferenti verso chi soffre fuori dalla porta. Denuncia le distorsioni dell'empatia algoritmica.",
            ["Like", "Virale", "Pietà", "Schermo", "Dimenticare"],
            ["Spettacolarizzazione", "Empatia selettiva", "Indifferenza sistemica", "Solidarietà autentica", "Prossimità"]
        ),
        (
            "La cultura della cancellazione relazionale (Ghosting)",
            "Interrompere improvvisamente ogni comunicazione è diventata una prassi comune. Dimostra come il silenzio vile ferisca più di un confronto aspro.",
            ["Ghosting", "Bloccare", "Sparire", "Messaggi", "Finita"],
            ["Viltà relazionale", "Confronto doveroso", "Dignità dell'altro", "Responsabilità affettiva", "Chiusura"]
        ),
        (
            "La trappola del perfezionismo sociale",
            "I giovani sono schiacciati dalla narrazione del successo precoce e della performance impeccabile. Difendi il diritto al fallimento come tappa cognitiva.",
            ["Successo", "Perfetto", "Instagram", "Fallire", "Migliore"],
            ["Dittatura della performance", "Elogio dell'errore", "Accettazione", "Umanità fallibile", "Autonomia"]
        ),
        (
            "L'invidia sociale e la vetrina del benessere",
            "I profili online mostrano vite apparentemente perfette generando risentimento diffuso. Invita i coetanei a decostruire l'illusione della felicità esibita.",
            ["Vetrina", "Foto", "Invidia", "Vacanze", "Felici"],
            ["Finzione narrativa", "Risentimento sociale", "Misura interiore", "Decostruzione", "Sobrietà"]
        ),
        (
            "La solitudine dell'iperconnessione",
            "Migliaia di contatti digitali e zero conversazioni intime. Descrivi il paradosso contemporaneo di una solitudine affollata e rumorosa.",
            ["Contatti", "Amici", "Wifi", "Soli", "Internet"],
            ["Isolamento iperconnesso", "Alienazione digitale", "Relazione incarnata", "Presenza reale", "Ascolto"]
        ),
        (
            "L'ascolto attivo come atto rivoluzionario",
            "In una società in cui tutti urlano per sopraffare la voce altrui, dimostra come l'ascolto paziente e disarmato costituisca la più alta virtù civica.",
            ["Parlare", "Urlare", "Ascoltare", "Opinione", "Zitto"],
            ["Sospensione del giudizio", "Disponibilità etica", "Rivoluzione dialogica", "Accoglienza", "Profondità"]
        ),
        (
            "La gestione del rancore e della vendetta",
            "Il desiderio di rivalsa consuma le energie vitali di chi lo cova. Illustra come l'elaborazione del torto sia l'unica via per l'emancipazione morale.",
            ["Vendetta", "Rancore", "Farsela pagare", "Odio", "Nemico"],
            ["Logoramento", "Emancipazione", "Superamento", "Lucidità", "Pace interiore"]
        ),
        (
            "L'autonomia affettiva contro la dipendenza",
            "Spesso le relazioni giovanili scambiano il possesso geloso per amore autentico. Chiarisci la distinzione tra legame fondato sulla libertà e attaccamento morboso.",
            ["Gelosia", "Mio", "Possesso", "Amore", "Lasciare"],
            ["Autonomia reciproca", "Dipendenza affettiva", "Rispetto dell'alterità", "Libertà condivisa", "Maturità"]
        ),
        (
            "La responsabilità delle parole nell'odio verbale",
            "Gli insulti diffusi nei commenti web vengono minimizzati come semplici battute. Dimostra la violenza performativa del linguaggio ostile.",
            ["Parole", "Insulti", "Scherzo", "Commenti", "Hater"],
            ["Violenza simbolica", "Atto performativo", "Responsabilità etica", "Ferita invisibile", "Rispetto civico"]
        ),
        (
            "La fedeltà a se stessi nelle pressioni di gruppo",
            "Il branco impone riti di conformità per accettare i singoli membri. Esalta il coraggio individuale di chi rifiuta di uniformarsi pur di appartenere.",
            ["Branco", "Gruppo", "Fumare", "Accettare", "Pressione"],
            ["Integrità morale", "Dissenso coscienzioso", "Autenticità", "Fermezza interiore", "Resistenza"]
        ),
        (
            "La compassione verso la sofferenza invisibile",
            "Ognuno combatte una battaglia personale di cui gli altri non sanno nulla. Sostieni il principio della gentilezza preventiva verso ogni persona.",
            ["Battaglia", "Gente", "Gentile", "Sorriso", "Dentro"],
            ["Gentilezza incondizionata", "Sofferenza celata", "Sguardo fraterno", "Delicatezza", "Umanità comune"]
        ),
        (
            "L'elaborazione del rifiuto sentimentale",
            "Ricevere un no da chi si ama può destabilizzare profondamente l'autostima. Spiega come accogliere il rifiuto con dignità e rispetto per l'altro.",
            ["Rifiuto", "No", "Lasciato", "Amare", "Arrabbiato"],
            ["Accettazione matura", "Sovranità dell'altro", "Dignità personale", "Rielaborazione", "Crescita"]
        ),
        (
            "Il valore etico della gratitudine quotidiana",
            "Diamo per scontato il benessere, l'affetto familiare e le opportunità ricevute. Fai un'orazione sull'esercizio quotidiano della riconoscenza.",
            ["Grazie", "Scontato", "Dovere", "Casa", "Tutto"],
            ["Riconoscenza civica", "Debito d'affetto", "Consapevolezza", "Privilegio", "Generosità"]
        ),
        (
            "La gelosia come specchio dell'insicurezza personale",
            "Chi vive nella costante paura del tradimento proietta le proprie paure. Invita a guardarsi dentro per guarire la radice dell'insicurezza.",
            ["Gelosia", "Tradire", "Messaggi", "Controllare", "Paura"],
            ["Insicurezza ontologica", "Proiezione nevrotica", "Autoconsapevolezza", "Fiducia di fondo", "Serenità"]
        ),
        (
            "Il riscatto morale dopo un grave errore",
            "Chi ha sbagliato non deve rimanere marchiato per sempre dal suo passato. Difendi il principio della riabilitazione personale ed esistenziale.",
            ["Sbaglio", "Marchio", "Passato", "Colpa", "Perdonare"],
            ["Rinascita morale", "Diritto all'emancipazione", "Riparazione operosa", "Fiducia sistemica", "Misericordia"]
        ),
        (
            "La bellezza del legame intergenerazionale",
            "Il distacco tra anziani e adolescenti impoverisce entrambe le età della vita. Promuovi patti di cooperazione e ascolto tra nonni e nipoti.",
            ["Nonni", "Vecchi", "Ragazzi", "Storie", "Dimenticare"],
            ["Alleanza generazionale", "Patrimonio memoriale", "Sapienza esperienziale", "Cura reciproca", "Continuità"]
        ),
        (
            "Il coraggio di chiedere scusa pubblicamente",
            "Ammettere i propri sbagli in pubblico viene percepito come debolezza dai leader politici e sociali. Ribalta la tesi dimostrando che è forza morale.",
            ["Scusa", "Debole", "Politica", "Errore", "Faccia"],
            ["Onestà intellettuale", "Esemplarità civica", "Umiltà del potere", "Trasparenza", "Rettitudine"]
        ),
        (
            "L'amicizia come presidio contro l'omologazione",
            "I veri amici sanno dirti le verità sgradevoli che nessun adulatore oserebbe pronunciare. Celebra la parresìa all'interno delle relazioni autentiche.",
            ["Amico", "Dire", "Verità", "Bugiardo", "Piacere"],
            ["Franchezza affettuosa", "Parresìa", "Presidio critico", "Lealtà disinteressata", "Custodia morale"]
        ),
        (
            "La speranza operosa contro la rassegnazione",
            "Il cinismo e il disincanto sono il rifugio comodo di chi ha smesso di lottare. Pronuncia un'arringa appassionata a favore dell'impegno emotivo fiducioso.",
            ["Cinico", "Niente cambia", "Mondo brutto", "Rassegnarsi", "Sperare"],
            ["Speranza operosa", "Fiducia trasformatrice", "Impegno ostinato", "Entusiasmo civico", "Orizzonte"]
        )
    ],
    "c1": [
        (
            "L'etica aristotelica delle passioni e il giusto mezzo",
            "Esporrai di fronte a un consesso accademico la teoria della moderazione delle passioni (mesotes), confutando sia l'apatia stoica sia lo scatenamento incontrollato.",
            ["Passioni", "Giusto", "Medio", "Rabbia", "Tranquillo"],
            ["Mesotes aristotelica", "Canalizzazione virtuosa", "Temperanza", "Equilibrio razionale", "Eudaimonia"]
        ),
        (
            "L'analisi sartriana dello sguardo dell'Altro e la vergogna",
            "Analizza la fenomenologia della vergogna come rivelazione originaria dell'oggettivazione dell'io sotto lo sguardo alienante dell'Altro.",
            ["Vergogna", "Occhi", "Guardare", "Sartre", "Giudicare"],
            ["Sguardo oggettivante", "Alterità perturbante", "Intersoggettività", "Coscienza vergognosa", "Cosificazione"]
        ),
        (
            "La retorica del risentimento nella sfera pubblica",
            "Decostruisci il meccanismo psicologico e politico descritto da Nietzsche e Scheler con cui l'invidia impotente si tramuta in veleno sistemico.",
            ["Risentimento", "Invidia", "Nietzsche", "Odio", "Deboli"],
            ["Ressentiment scheleriano", "Avvelenamento civile", "Spirito di vendetta", "Trasvalutazione reattiva", "Vulnerabilità"]
        ),
        (
            "L'amore liquido e la mercificazione dei sentimenti in Bauman",
            "Pronuncia una critica filosofica della fragilità dei legami umani contemporanei ridotti a beni di consumo intercambiabili e revocabili.",
            ["Liquido", "Bauman", "Amore", "Consumo", "Cambiare"],
            ["Precarizzazione affettiva", "Mercificazione relazionale", "Revocabilità del patto", "Individualismo difensivo", "Solidità ontologica"]
        ),
        (
            "La compassione schopenhaueriana come squarcio del Velo di Maya",
            "Dimostra come la Mitleid (compassione) sia l'unica reale forma di trascendenza del principium individuationis e della cieca volontà universale.",
            ["Compassione", "Dolore", "Schopenhauer", "Mondo", "Soffrire"],
            ["Principium individuationis", "Velo di Maya", "Mitleid universale", "Solidarietà metafisica", "Trascendenza"]
        ),
        (
            "L'angoscia esistenziale kierkegaardiana come vertigine della libertà",
            "Distingui l'angoscia pura dalla comune paura psicologica, interpretandola come la vertigine dell'io posto di fronte all'infinita possibilità del proprio destino.",
            ["Paura", "Angoscia", "Kierkegaard", "Libero", "Scelta"],
            ["Vertigine del possibile", "Scacco esistenziale", "Aut aut categorico", "Singolarità davanti all'Assoluto", "Trepidazione"]
        ),
        (
            "La decostruzione levinasiana dell'egologia attraverso il Volto",
            "Sostieni il primato etico dell'accoglienza dell'Altro prima di ogni affermazione ontologica dell'Io, commentando l'imperativo tu non ucciderai.",
            ["Volto", "Altro", "Levinas", "Io", "Uccidere"],
            ["Epifania del Volto", "Asimmetria etica", "Responsabilità primigenia", "Incondizionatezza del debito", "Comandamento originario"]
        ),
        (
            "Il lutto e la melanconia nell'architettura psichica freudiana",
            "Illustra la distinzione clinica e speculativa tra il doloroso ma fecondo lavoro del lutto e la fissazione narcisistica e autodistruttiva della melanconia.",
            ["Lutto", "Tristezza", "Freud", "Morto", "Perdita"],
            ["Decantazione della perdita", "Fissazione melanconica", "Introiezione dell'oggetto", "Economia pulsionale", "Restituzione alla vita"]
        ),
        (
            "L'intelligenza emotiva come presupposto della democrazia deliberativa",
            "Confuta l'illusione di una razionalità politica asettica: senza educazione alla risonanza empatica la democrazia degenera in tecnocrazia o populismo.",
            ["Politica", "Democrazia", "Ragione", "Popolo", "Tecnici"],
            ["Risonanza empatica", "Deliberazione partecipata", "Civitas affettiva", "Maturità democratica", "Presidio umanistico"]
        ),
        (
            "La catarsi aristotelica: terrore e pietà nella tragedia classica",
            "Spiega come l'esperienza estetica del dramma operi una purificazione profonda delle pulsioni di pietà (eleos) e timore (phobos) nel cittadino.",
            ["Teatro", "Paura", "Piangere", "Catarsi", "Tragedia"],
            ["Eleos e Phobos", "Purificazione catartica", "Pedagogia della pietà", "Ecosistema tragico", "Sublime morale"]
        ),
        (
            "L'odio online come anestesia della presenza corporea",
            "Argomenta sulla dematerializzazione del corpo nel digitale come causa scatenante della disinibizione aggressiva e della de-umanizzazione dell'interlocutore.",
            ["Hater", "Corpo", "Schermo", "Tastiera", "Violenza"],
            ["Smaterializzazione della presenza", "Disinibizione tossica", "De-umanizzazione", "Alterità incarnata", "Cura dialogica"]
        ),
        (
            "L'attesa come dimensione ontologica contro l'istantaneità neoliberale",
            "Difendi il valore pedagogico ed esistenziale dell'attesa, del silenzio e dell'incompiutezza in un'epoca dominata dal consumo in tempo reale.",
            ["Aspettare", "Subito", "Fretta", "Tempo", "Tempo reale"],
            ["Dimensione kairologica", "Pazienza ermeneutica", "Elogio dell'incompiuto", "Custodia del tempo", "Maturazione lenta"]
        ),
        (
            "Il perdono come atto sovrano oltre la logica dello scambio",
            "In accordo con la riflessione di Vladimir Jankélévitch e Jacques Derrida, indaga l'aporia del perdonare ciò che resta eticamente imperdonabile.",
            ["Perdono", "Colpa", "Scambio", "Derrida", "Vendetta"],
            ["Aporia del perdono", "Gratuità assoluta", "Incommensurabilità del torto", "Dono incondizionato", "Sovranità etica"]
        ),
        (
            "La nostalgia come forza critica o come regresso reazionario",
            "Distingui tra la nostalgia riparatrice, che inventa miti dorati per giustificare il revanscismo politico, e la nostalgia riflessiva che interroga le promesse non mantenute della storia.",
            ["Nostalgia", "Passato", "Una volta", "Bello", "Ricordo"],
            ["Nostalgia riflessiva", "Regresso mitologico", "Promessa inappagata", "Critica del presente", "Tensione utopica"]
        ),
        (
            "La simpatia morale in Adam Smith e David Hume",
            "Esporrai la teoria illuminista dei sentimenti morali: come lo spettatore imparziale dentro di noi genera il consenso sociale e la giustizia comunitaria.",
            ["Simpatia", "Smith", "Hume", "Morale", "Sentimenti"],
            ["Spettatore imparziale", "Risonanza simpatetica", "Armonia morale", "Coesione civile", "Sentimento di giustizia"]
        ),
        (
            "La gelosia come patologia del possesso metafisico in Proust",
            "Analizza attraverso la figura di Swann la pretesa prometeica e disperata di possedere l'essere e il tempo dell'Altro attraverso il sospetto continuo.",
            ["Gelosia", "Proust", "Swann", "Amore", "Spiare"],
            ["Feticismo del possesso", "Spazio temporale incomunicabile", "Ermeneutica del sospetto", "Disillusione amorosa", "Tempo perduto"]
        ),
        (
            "La cura (Sorge) come struttura ontologica fondamentale in Heidegger",
            "Mostra come l'essere-nel-mondo umano non sia prima una sostanza che poi prova emozioni, ma sia originariamente e intimamente costituito dalla Cura.",
            ["Cura", "Heidegger", "Uomo", "Pensare", "Mondo"],
            ["Sorge heideggeriana", "Dasein e gettatezza", "Essere-nel-mondo", "Orizzonte di precarietà", "Autenticità esistenziale"]
        ),
        (
            "La banalità del male e l'eclissi dell'immaginazione morale in Arendt",
            "Dimostra come l'incapacità di pensare dal punto di vista altrui e la totale assenza di dialogo interiore siano il terreno fertile per i più efferati crimini burocratici.",
            ["Arendt", "Male", "Burocrazia", "Pensare", "Mostro"],
            ["Banalità del male", "Incapacità di giudizio", "Eclissi dell'empatia", "Dialogo interiore", "Responsabilità personale"]
        ),
        (
            "La solidarietà organica di Durkheim versus la frammentazione anomica",
            "Rifletti sulla crisi dei legami sociali di fronte all'individualismo estremo, delineando le basi per una rinnovata coscienza collettiva affettiva.",
            ["Durkheim", "Società", "Insieme", "Soli", "Regole"],
            ["Solidarietà organica", "Anomia sociale", "Coesione relazionale", "Coscienza collettiva", "Tessuto comunitario"]
        ),
        (
            "L'elogio della timidezza come riserva di profondità ermeneutica",
            "Rovescia la condanna moderna dell'esitazione: la timidezza come difesa del pudore, della contemplazione e del rispetto reverente per l'inconoscibile.",
            ["Timido", "Parlare", "Sicuro", "Vergogna", "Debole"],
            ["Pudore ermeneutico", "Riserva contemplativa", "Rifiuto della sfrontatezza", "Attesa feconda", "Venerazione"]
        )
    ],
    "c2": [
        (
            "Pathos, Ethos e Logos: la sinfonia triadica dell'Oratore Supremo",
            "Pronuncia un'orazione magistrale sulla necessità di armonizzare la passione travolgente con la statura morale e l'argomentazione rigorosa.",
            ["Pathos", "Ethos", "Logos", "Discorso", "Parlare"],
            ["Sintesi triadica", "Risonanza catartica", "Integrità oratoria", "Fervore argomentativo", "Magistero dialettico"]
        ),
        (
            "L'aporia dell'Altro assoluto e l'ospitalità incondizionata",
            "Delinea l'imperativo metafisico di un'accoglienza che non chieda documenti, nome né reciprocità, sfidando i confini convenzionali del diritto.",
            ["Accogliere", "Straniero", "Legge", "Casa", "Chiedere"],
            ["Ospitalità incondizionata", "Aporia derridiana", "Eteronomia radicale", "Sovranità disarmata", "Apertura messianica"]
        ),
        (
            "La sublimazione nietzscheana delle pulsioni dionisiache",
            "Sostieni di fronte al senato filosofico che la grandezza culturale non risiede nell'estirpazione delle passioni ma nella loro trasfigurazione estetica e tragica.",
            ["Dioniso", "Nietzsche", "Passioni", "Male", "Tragedia"],
            ["Dionisiaco trasfigurato", "Volontà di potenza creatrice", "Sublimazione plastica", "Amor fati", "Affermazione gioiosa"]
        ),
        (
            "L'abisso della crudeltà disinteressata e l'enigma del male radicale",
            "Interroga il mistero della distruzione inflitta unicamente per il godimento della devastazione, confutando ogni riduzionismo economico o sociologico.",
            ["Male", "Cattivo", "Interesse", "Soldi", "Spiegare"],
            ["Male radicale kantiano", "Pulsione di morte freudiana", "Godimento perverso", "Incommensurabilità abissale", "Vigile discernimento"]
        ),
        (
            "La parresìa foucaultiana: il coraggio del discorso veritiero e letale",
            "Analizza la parresìa come atto oratorio in cui chi dice la verità accetta deliberatamente il rischio della propria vita di fronte al tiranno.",
            ["Foucault", "Verità", "Parlare", "Paura", "Morte"],
            ["Patto parresiastico", "Veridizione tragica", "Rischio mortale", "Franchezza insorgente", "Esemplarità sovrana"]
        ),
        (
            "L'estetica della disperazione e la rivolta nell'assurdo camusiano",
            "Dimostra come la consapevolezza lucida dell'assurdità dell'esistenza non conduca alla rinuncia bensì all'ardente rivolta morale e solidale.",
            ["Assurdo", "Camus", "Suicidio", "Niente", "Disperazione"],
            ["Rivolta esistenziale", "Fedeltà alla terra", "Solidarietà degli sconfitti", "Lucidità insorta", "Nostalgia di unità"]
        ),
        (
            "La de-sostanzializzazione del sé nella mistica dell'ascolto",
            "Pronuncia una summa sulla vacuità dell'Ego assertivo: solo svuotando l'animo da ogni pretesa identitaria si diventa cassa di risonanza del mondo.",
            ["Io", "Vuoto", "Mente", "Tacere", "Nome"],
            ["Kenosi oratoria", "Vacuità identitaria", "Cassa di risonanza", "Accoglienza pura", "Trascendenza immanente"]
        ),
        (
            "L'angoscia come orizzonte di disvelamento dell'Essere",
            "Ripercorri il movimento heideggeriano in cui il crollo di ogni rassicurazione ontica apre la radura (Lichtung) alla meraviglia che l'ente sia e non sia piuttosto il nulla.",
            ["Angoscia", "Nulla", "Essere", "Paura", "Niente"],
            ["Lichtung originaria", "Disvelamento ontologico", "Sospensione d'ogni senso", "Meraviglia abissale", "Richiamo della coscienza"]
        ),
        (
            "L'intraducibilità del dolore e i limiti della compassione politica",
            "Metti in guardia dall'oratoria populista che strumentalizza il lutto collettivo, riaffermando la sacralità indicibile e non convertibile del trauma singolare.",
            ["Dolore", "Lutto", "Politica", "Strumentalizzare", "Piangere"],
            ["Intraducibilità traumatica", "Sacralità del silenzio", "Violazione retorica", "Pudore civile", "Inviolabilità singolare"]
        ),
        (
            "L'eroismo della tenerezza nella notte della violenza planetaria",
            "Formula un manifesto per gli oratori del futuro: la delicatezza e la cura dei deboli come unica reale resistenza alla fascinazione della potenza bruta.",
            ["Forte", "Guerra", "Armi", "Bontà", "Vincere"],
            ["Radicalità della cura", "Sovversione della tenerezza", "Resistenza disarmata", "Custodia dell'inerme", "Luce imperitura"]
        ),
        (
            "La dialettica della colpa e della redenzione in Dostoevskij",
            "Attraverso l'epopea dei Fratelli Karamazov, dimostra che ciascuno di noi è colpevole di tutto e per tutti di fronte all'infinita misericordia universale.",
            ["Colpa", "Delitto", "Karamazov", "Castigo", "Tutti"],
            ["Corresponsabilità universale", "Grazia incondizionata", "Misericordia abissale", "Redenzione operosa", "Rigenerazione spirituale"]
        ),
        (
            "L'ambivalenza sacrale dell'odio e del sacro in René Girard",
            "Analizza la convergenza di tutte le tensioni comunitarie sul capro espiatorio e il miracolo effimero della riconciliazione fondata sul sangue innocente.",
            ["Capro", "Espiatorio", "Girard", "Sacro", "Uccidere"],
            ["Violenza mimetica", "Meccanismo vittimario", "Catarsi espiatoria", "Demistificazione evangelica", "Crisi sacrificiale"]
        ),
        (
            "Il tramonto dell'eudaimonia nell'orizzonte dell'efficienza algoritmica",
            "Denuncia l'inganno della felicità ridotta a benessere biologico e produttività misurabile, ripristinando la tragicità irrinunciabile della libertà umana.",
            ["Felice", "App", "Benessere", "Algoritmo", "Efficienza"],
            ["Riduzionismo funzionale", "Tragicità della libertà", "Eudaimonia classica", "Incommensurabilità umana", "Rivolta del senso"]
        ),
        (
            "La follia amorosa platonea nel Fedro come forma suprema di conoscenza",
            "Argomenta sulla mania divina dell'eros non come deviazione irrazionale ma come impennata alata dell'anima verso la contemplazione dell'Iperuranio.",
            ["Platone", "Amore", "Pazzo", "Ali", "Sapere"],
            ["Mania divina", "Trascendenza erotica", "Slancio alato", "Contemplazione del Bello", "Memoria originaria"]
        ),
        (
            "La solitudine sovrana dell'oratore davanti alla folla ostile",
            "Evoca l'archetipo dell'apostolo o del tribuno che, abbandonato da tutti, trova nella coerenza del proprio Verbo la forza di non piegare la testa.",
            ["Folla", "Solitario", "Urla", "Pietre", "Paura"],
            ["Fermezza impassibile", "Parola incorruttibile", "Dignità testimoniale", "Solitudine eroica", "Primato del Logos"]
        ),
        (
            "L'inoperosità di Agamben: il riposo del senso e la disattivazione del potere",
            "Sviluppa la teoria della potenza di non fare come massima forma di resistenza etica contro l'obbligo totalizzante dell'attivismo capitalistico.",
            ["Agamben", "Fare", "Lavoro", "Fermarsi", "Potere"],
            ["Inoperosità messianica", "Potenza del non", "Disattivazione del dispositivo", "Riposo originario", "Compiutezza"]
        ),
        (
            "Il silenzio contemplativo come vertice dell'eloquenza",
            "Dimostra come la massima oratoria non risieda nell'inondazione di sillabe ma nella capacità di generare quel silenzio reverente in cui l'uditorio incontra l'Assoluto.",
            ["Silenzio", "Parole", "Parlare tanto", "Voce", "Rumore"],
            ["Eloquenza apofatica", "Aura del silenzio", "Sospensione sacrale", "Riverbero metafisico", "Verità ineffabile"]
        ),
        (
            "La ferita insanabile come sorgente della poesia e del pensiero",
            "Rifletti sulla testimonianza di Paul Celan: solo attraversando la frattura e la rovina della catastrofe la parola si fa autenticamente profetica e redentrice.",
            ["Poesia", "Celan", "Dolore", "Frattura", "Rovinata"],
            ["Ferita inaugurale", "Parola testimoniale", "Breviloquio tragico", "Custodia della frattura", "Luce scaturita"]
        ),
        (
            "L'antagonismo agonistico di Chantal Mouffe contro il consenso pacificante",
            "Difendi la necessità democratica del conflitto passionale regolato (agonismo) contro la finzione tecnocratica e anestetizzante del consenso post-politico.",
            ["Conflitto", "Litigio", "D'accordo", "Politica", "Pace finta"],
            ["Passione agonistica", "Polarizzazione democratica", "Rifiuto dell'anestesia", "Tensione feconda", "Civiltà del dissenso"]
        ),
        (
            "L'inno all'Umanità: il congedo magistrale dell'Oratore",
            "Pronuncia il discorso supremo che consacra la voce umana come ponte tra la polvere delle origini e l'infinito anelito di giustizia e verità.",
            ["Uomo", "Voce", "Mondo", "Morte", "Fine"],
            ["Apoteosi umanistica", "Soffio immortale", "Invocazione cosmica", "Veste di luce", "Pellegrinaggio infinito"]
        )
    ]
}
