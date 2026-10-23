# Mazzo: Digitale, IA & Futuro (digitale)
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            "Il robot che riordina i giochi",
            "Immagina di costruire un piccolo robot di cartone che ti aiuta a raccogliere i pennarelli caduti. Spiega come funziona con parole semplici.",
            ["Robot", "Cartone", "Pennarelli", "Batterie", "Disordine"],
            ["Aiutante", "Sensore", "Rotelle", "Invenzione", "Scatola"]
        ),
        (
            "Il tablet spento per andare al parco",
            "I tuoi compagni guardano un cartone animato sullo schermo. Convincli a spegnere tutto per correre fuori a giocare a nascondino.",
            ["Tablet", "Schermo", "Cartone", "Spento", "Video"],
            ["Parco", "Corsa", "Sole", "Nascondino", "Aria aperta"]
        ),
        (
            "La password segreta del castello",
            "Hai inventato un codice segreto per entrare nella casetta sull'albero. Spiega perché le parole d'ordine vanno tenute al sicuro e non dette a sconosciuti.",
            ["Password", "Codice", "Segreto", "Albero", "Sconosciuti"],
            ["Custodia", "Sicurezza", "Parola magica", "Porta", "Fiducia"]
        ),
        (
            "Il messaggio gentile per la nonna",
            "Mandi un audio vocale alla nonna lontana col telefono della mamma. Raccontale con tanto affetto cosa hai fatto a scuola oggi.",
            ["Audio", "Telefono", "Nonna", "Messaggio", "Scuola"],
            ["Voce", "Affetto", "Saluto", "Racconto", "Bacio"]
        ),
        (
            "Il disegno fatto col dito sullo schermo",
            "Hai usato un'applicazione per colorare col dito. Spiega la differenza tra toccare un vetro liscio e sentire il profumo dei veri pennarelli.",
            ["Schermo", "Dito", "App", "Vetro", "Pennarelli"],
            ["Profumo", "Carta", "Materia", "Tratto", "Mano"]
        ),
        (
            "Il cane robot che abbaia finto",
            "Hai visto un cagnolino meccanico che scodinzola a pile. Spiega perché un cucciolo vero in carne e ossa ha bisogno di amore e non si spegne con un tasto.",
            ["Cane", "Robot", "Pile", "Tasto", "Abbaiare"],
            ["Cuore", "Cura", "Coccole", "Pappa", "Animale vero"]
        ),
        (
            "Il computer che non capisce gli scherzi",
            "Hai provato a fare il solletico al computer ma non ride. Spiega ai compagni perché le macchine non hanno sentimenti né simpatia.",
            ["Computer", "Ridere", "Solletico", "Macchina", "Freddo"],
            ["Sentimento", "Emozione", "Umano", "Battuta", "Calore"]
        ),
        (
            "Il videogioco a tempo",
            "Suona la sveglia che dice che è finita la mezz'ora di gioco. Spiega perché rispettare il timer evita di stancare gli occhi e fa bene alla mente.",
            ["Videogioco", "Timer", "Sveglia", "Basta", "Occhi"],
            ["Misura", "Riposo", "Equilibrio", "Passeggiata", "Serenità"]
        ),
        (
            "La foto ricordo di classe",
            "La maestra scatta una foto ricordo dell'ultimo giorno. Spiega perché una bella foto serve a ricordare i sorrisi di oggi anche quando sarete grandi.",
            ["Foto", "Macchina", "Sorriso", "Classe", "Click"],
            ["Memoria", "Ricordo", "Custodire", "Amici", "Tempo"]
        ),
        (
            "La lente magica degli scienziati",
            "Usi un microscopio digitale per guardare la buccia di una mela. Descrivi la meraviglia dei particolari invisibili ad occhio nudo.",
            ["Mela", "Lente", "Grande", "Vedere", "Scienza"],
            ["Ingrandimento", "Meraviglia", "Dettaglio", "Natura", "Scoperta"]
        ),
        (
            "Il trenino che segue i binari colorati",
            "Hai un trenino giocattolo che segue le strisce disegnate sul pavimento. Spiega come fa la lucina a capire dove curvare.",
            ["Treno", "Luce", "Binari", "Curva", "Giocattolo"],
            ["Sensore", "Colore", "Direzione", "Movimento", "Strada"]
        ),
        (
            "Non parlare con chi non conosci online",
            "Mentre giochi a un gioco online appare un messaggio di uno sconosciuto. Spiega perché non bisogna mai rivelare il proprio nome o indirizzo di casa.",
            ["Gioco", "Sconosciuto", "Nome", "Casa", "Scrivere"],
            ["Prudenza", "Protezione", "Genitori", "Avviso", "Sicurezza"]
        ),
        (
            "La sveglia che canta come un gallo",
            "Hai impostato una suoneria divertente sul comodino. Spiega come la tecnologia possa aiutarci a svegliarci con allegria al mattino.",
            ["Sveglia", "Gallo", "Suono", "Mattino", "Dormire"],
            ["Musica", "Sorriso", "Energia", "Inizio giornata", "Allegria"]
        ),
        (
            "Il libro di carta sfogliato insieme",
            "Qualcuno vuole leggere una fiaba solo sullo schermo. Dimostragli la magia di girare le pagine di carta illustrate seduti sul tappeto.",
            ["Libro", "Carta", "Schermo", "Pagina", "Fiaba"],
            ["Tappeto", "Illustrazione", "Sfogliare", "Magia", "Profumo"]
        ),
        (
            "La biblioteca sul pulmino volante",
            "Immagina un pulmino del futuro che porta libri e tablet volando da un paese all'altro. Racconta la sua prima fermata nella tua scuola.",
            ["Volare", "Pulmino", "Libri", "Scuola", "Futuro"],
            ["Biblioteca", "Ali", "Conoscenza", "Viaggio", "Festa"]
        ),
        (
            "Il tasto magico della gentilezza",
            "Se ci fosse un tasto sulla tastiera per mandare un sorriso a chi è triste, come lo disegneresti e quando lo useresti?",
            ["Tasto", "Tastiera", "Disegnare", "Sorriso", "Triste"],
            ["Simbolo", "Gentilezza", "Conforto", "Invenzione", "Amicizia"]
        ),
        (
            "La pianta che chiede l'acqua con un bip",
            "Hai messo un piccolo sensore nel vaso del geranio che suona quando la terra è secca. Spiega come aiutare la pianta a bere in tempo.",
            ["Pianta", "Acqua", "Vaso", "Suono", "Bip"],
            ["Terra", "Cura", "Segnale", "Foglia", "Vita"]
        ),
        (
            "La musica ascoltata insieme",
            "Invece di ascoltare la musica con le cuffiette isolati, colleghi la cassa per ballare tutti insieme in cerchio.",
            ["Cuffie", "Musica", "Cassa", "Ballo", "Solo"],
            ["Cerchio", "Condivisione", "Festa", "Ritmo", "Compagnia"]
        ),
        (
            "Il semaforo intelligente del corridoio",
            "Costruisci un semaforo che diventa verde solo quando tutti camminano piano senza correre verso la mensa.",
            ["Semaforo", "Verde", "Rosso", "Correre", "Mensa"],
            ["Calma", "Passo", "Ordine", "Segnale", "Sicurezza"]
        ),
        (
            "Il disegno del robot del futuro",
            "Disegna e racconta il tuo robot preferito: non deve fare guerre, ma piantare fiori e raccogliere la plastica nei prati.",
            ["Robot", "Guerra", "Plastica", "Fiori", "Disegno"],
            ["Custode", "Terra", "Prato", "Ecologia", "Speranza"]
        )
    ],
    "a2": [
        (
            "La ricerca su internet: distinguere il vero dal falso",
            "State preparando una ricerca scolastica sugli animali preistorici. Spiega ai compagni perché non tutto quello che si trova online è attendibile.",
            ["Google", "Internet", "Copiare", "Vero", "Falso"],
            ["Fonte attendibile", "Verifica", "Enciclopedia", "Ricerca critica", "Confronto"]
        ),
        (
            "L'impronta digitale: quello che pubblichi resta",
            "Un compagno vuole pubblicare una foto buffa ma ridicola di un altro. Mettilo in guardia: le immagini sul web non si cancellano facilmente.",
            ["Foto", "Postare", "Ridere", "Cancellare", "Web"],
            ["Impronta digitale", "Permanenza", "Rispetto dell'immagine", "Conseguenze", "Privacy"]
        ),
        (
            "Il tempo perso davanti ai video brevi",
            "Ti accorgi di aver passato due ore a scorrere video da quindici secondi senza imparare nulla. Trova argomenti per riprendere il controllo del tuo tempo.",
            ["Video", "Scorrere", "TikTok", "Tempo", "Ore"],
            ["Attenzione", "Concentrazione", "Scelta consapevole", "Creatività attiva", "Passività"]
        ),
        (
            "L'intelligenza artificiale che scrive le fiabe",
            "Hai fatto generare una storia a un programma di intelligenza artificiale. Spiega cosa manca rispetto a una storia nata dal cuore e dall'esperienza umana.",
            ["IA", "Computer", "Storia", "Scrivere", "Cuore"],
            ["Esperienza vissuta", "Sensibilità", "Creatività umana", "Anima", "Immaginazione"]
        ),
        (
            "Il netiquette nei gruppi scolastici",
            "Nel gruppo dei compiti qualcuno usa parole sgarbate o manda decine di adesivi inutili. Proponi un decalogo di buona educazione digitale.",
            ["Gruppo", "Adesivi", "Sticker", "Insulti", "Scrivere"],
            ["Netiquette", "Rispetto reciproco", "Pertinenza", "Educazione digitale", "Moderazione"]
        ),
        (
            "I videogiochi e le trappole degli acquisti in app",
            "Un gioco gratuito ti chiede soldi veri per comprare un costume o una spada virtuale. Metti in guardia i compagni sulle tecniche che spingono a spendere.",
            ["Soldi", "Comprare", "Skin", "Gioco", "Gratis"],
            ["Acquisti in-app", "Manipolazione commerciale", "Valore reale", "Fascino virtuale", "Consapevolezza"]
        ),
        (
            "L'amicizia reale versus i follower virtuali",
            "Un ragazzo si vanta di avere mille contatti ma non ha nessuno con cui fare un giro in bici. Spiega la differenza tra numero e legame autentico.",
            ["Follower", "Mille", "Contatti", "Bici", "Vantarsi"],
            ["Amicizia incarnata", "Presenza fisica", "Qualità del legame", "Superficialità", "Fiducia vera"]
        ),
        (
            "Il cyberbullismo: come rompere la catena",
            "In una chat circola un video per prendere in giro una compagna. Fai un discorso chiaro: chi condivide o ride è complice dell'offesa.",
            ["Video", "Ridere", "Inoltrare", "Presa in giro", "Chat"],
            ["Cyberbullismo", "Complicità silenziosa", "Catena da spezzare", "Dignità della vittima", "Segnalazione"]
        ),
        (
            "La programmazione a blocchi come linguaggio del futuro",
            "Hai imparato a programmare un piccolo videogioco con Scratch. Spiega ai genitori perché imparare il pensiero computazionale apre la mente.",
            ["Scratch", "Blocchi", "Computer", "Gioco", "Difficile"],
            ["Pensiero computazionale", "Logica creativa", "Risoluzione di problemi", "Linguaggio moderno", "Autonomia"]
        ),
        (
            "La luce blu e il sonno della notte",
            "I tuoi compagni si addormentano guardando il cellulare sotto le coperte. Illustra scientificamente perché la luce dello schermo disturba il riposo.",
            ["Cellulare", "Letto", "Dormire", "Luce blu", "Occhi"],
            ["Melatonina", "Ciclo del sonno", "Salute biologica", "Disconnessione notturna", "Riposo profondo"]
        ),
        (
            "L'accessibilità digitale per chi non vede o non sente",
            "Mostra come le tecnologie vocali e i sottotitoli automatici permettano alle persone con disabilità di partecipare a pieno titolo alla vita sociale.",
            ["Cieco", "Sordo", "Computer", "Difficile", "Aiutare"],
            ["Accessibilità digitale", "Inclusione tecnologica", "Sintesi vocale", "Pari opportunità", "Autonomia per tutti"]
        ),
        (
            "Le truffe online e le finte vincite (Phishing)",
            "Ti è arrivato un messaggio che promette uno smartphone gratis cliccando su un link. Spiega ai compagni come riconoscere le trappole del web.",
            ["Vinto", "Telefono", "Cliccare", "Link", "Gratis"],
            ["Phishing", "Truffa telematica", "Dati sensibili", "Diffidenza critica", "Sicurezza informatica"]
        ),
        (
            "Il valore dei dati personali: niente è gratis sul web",
            "Spiega perché molte piattaforme non fanno pagare un abbonamento: il vero prezzo che paghiamo sono le nostre informazioni e la nostra attenzione.",
            ["Gratis", "Social", "Soldi", "Iscriversi", "Pagare"],
            ["Monetizzazione dei dati", "Economia dell'attenzione", "Profilazione", "Trasparenza", "Merce invisibile"]
        ),
        (
            "I droni per salvare le foreste",
            "Racconta come piccoli aeromobili teleguidati vengano usati dai guardaparco per avvistare incendi e piantare semi nei boschi inaccessibili.",
            ["Drone", "Volare", "Incendio", "Guardia", "Telecomando"],
            ["Monitoraggio ambientale", "Riforestazione tecnologica", "Prevenzione rapida", "Custodia del territorio", "Innovazione verde"]
        ),
        (
            "La realtà virtuale per esplorare la storia",
            "Indossi un visore e ti ritrovi a camminare tra le strade dell'antica Roma. Descrivi l'esperienza immersiva e come può arricchire lo studio.",
            ["Visore", "Occhiali", "Roma", "Vedere", "Finto"],
            ["Realtà immersiva", "Ricostruzione storica", "Apprendimento esperienziale", "Viaggio virtuale", "Coinvolgimento"]
        ),
        (
            "Il riciclo dei rifiuti elettronici (RAEE)",
            "I vecchi telefoni e caricabatterie finiscono spesso nel cassetto o nel cassonetto. Spiega perché recuperare i metalli rari è vitale per la Terra.",
            ["Telefono vecchio", "Cassetto", "Buttare", "Spazzatura", "Cavi"],
            ["Rifiuti elettronici", "Terre rare", "Riciclo tecnologico", "Economia circolare", "Sostenibilità mineraria"]
        ),
        (
            "Le bufale scientifiche che corrono veloci",
            "Gira voce online che mangiare una certa bacca guarisca da tutte le malattie. Invita i coetanei a fidarsi della scienza sperimentale e dei medici.",
            ["Bufala", "Guarire", "Bacca", "Miracolo", "Leggere"],
            ["Metodo scientifico", "Disinformazione", "Verifica delle prove", "Consenso medico", "Senso critico"]
        ),
        (
            "La password robusta e l'autenticazione a due fattori",
            "Insegna ai tuoi compagni la regola per creare parole d'ordine forti, combinando lettere, numeri e simboli per proteggere la propria identità.",
            ["Password", "1234", "Nome del cane", "Facile", "Entrare"],
            ["Complessità alfanumerica", "Sicurezza degli account", "Furto d'identità", "Protezione crittografica", "Consapevolezza informatica"]
        ),
        (
            "Il computer quantistico spiegato con semplicità",
            "Prova a raccontare alla classe cosa sono i qubit e come le macchine del futuro potranno risolvere calcoli impossibili in pochi secondi.",
            ["Computer", "Veloce", "Calcoli", "Bit", "Futuro"],
            ["Meccanica quantistica", "Qubit e sovrapposizione", "Potenza computazionale", "Frontiera scientifica", "Elaborazione parallela"]
        ),
        (
            "Il patto tra uomo e macchina: chi guida chi?",
            "Concludi il laboratorio di informatica con una domanda etica: la tecnologia deve restare uno strumento al servizio dell'uomo o dobbiamo diventarne schiavi?",
            ["Schiavi", "Macchine", "Comandare", "Tecnologia", "Uomo"],
            ["Primato umano", "Strumento consapevole", "Sovranità decisionale", "Guida etica", "Futuro responsabile"]
        )
    ],
    "b1": [
        (
            "La dittatura dei like e l'autostima adolescenziale",
            "I coetanei misurano il proprio valore personale dal numero di reazioni ricevute sotto un post. Dimostra la tossicità di questo meccanismo di approvazione.",
            ["Like", "Cuoricini", "Bello", "Social", "Triste se pochi"],
            ["Validazione esterna", "Dipendenza dopaminergica", "Autostima intrinseca", "Mercificazione dell'ego", "Autonomia emotiva"]
        ),
        (
            "I Deepfake e la dissoluzione della testimonianza visiva",
            "I video generati dall'intelligenza artificiale possono far dire a chiunque cose mai pronunciate. Analizza il pericolo per la convivenza democratica.",
            ["Video finto", "Faccia", "Dire bugie", "IA", "Credere"],
            ["Deepfake", "Veridicità probatoria", "Manipolazione dell'opinione", "Disinformazione sintetica", "Educazione ai media"]
        ),
        (
            "La bolla informativa (Echo Chamber) e la polarizzazione",
            "Gli algoritmi ci mostrano solo contenuti affini a ciò che già pensiamo. Spiega perché uscire dalla propria echo chamber è indispensabile per pensare liberi.",
            ["Bolla", "Algoritmo", "Sempre ragione", "Amici uguali", "Internet"],
            ["Echo chamber", "Polarizzazione ideologica", "Bias di conferma", "Pluralismo critico", "Spazio di confronto"]
        ),
        (
            "Il cyberbullismo come reato penale",
            "Illustra la legge 71 del 2017 a tutela dei minori: denigrare, diffamare o rubare l'identità online non è una bravata ma un crimine perseguibile.",
            ["Scherzo", "Prendere in giro", "Polizia", "Legge", "Minori"],
            ["Legge 71/2017", "Reato telematico", "Diffamazione aggravata", "Responsabilità penale", "Tutela dell'integrità"]
        ),
        (
            "L'impatto ambientale invisibile dei Data Center",
            "Inviare una mail, salvare file sul cloud o generare un'immagine consuma litri d'acqua ed energia elettrica. Svela il costo ecologico del web.",
            ["Cloud", "Invisibile", "Internet", "Computer", "Inquinare"],
            ["Data center", "Consumo energetico", "Impronta carbonica del digitale", "Raffreddamento idrico", "Sostenibilità computazionale"]
        ),
        (
            "I software Open Source e la conoscenza libera",
            "Presenta la filosofia di Linux e Wikipedia: condividere liberamente il codice sorgente e il sapere è un atto di libertà contro i monopoli privati.",
            ["Linux", "Wikipedia", "Codice", "Gratis", "Compagnie"],
            ["Open source", "Conoscenza condivisa", "Beni comuni digitali", "Democratizzazione del sapere", "Solidarietà comunitaria"]
        ),
        (
            "La privacy dei minori e lo 'Sharenting'",
            "Genitori che pubblicano foto e dettagli intimi dei figli fin dalla nascita senza il loro consenso. Difendi il diritto del minore a non essere esposto in vetrina.",
            ["Genitori", "Foto neonato", "Postare", "Facebook", "Bambini"],
            ["Sharenting compulsivo", "Consenso informato", "Diritto alla riservatezza", "Esposizione non richiesta", "Identità digitale precoce"]
        ),
        (
            "Il FOMO (Fear of Missing Out) e l'ansia da notifica",
            "La paura costante di essere esclusi da ciò che accade sui social genera stress e insonnia continua. Proponi una strategia di disintossicazione digitale.",
            ["FOMO", "Notifiche", "Controllare sempre", "Perdere qualcosa", "Telefono"],
            ["Fear of missing out", "Iperstimolazione sensoriale", "Detox digitale", "Pace mentale", "Presenza nel reale"]
        ),
        (
            "L'uso dell'IA nei compiti scolastici: aiuto o pigrizia cognitiva?",
            "Farsi scrivere il saggio da ChatGPT risparmia tempo ma atrofizza la capacità critica. Discuti come usare l'IA come tutor e non come stampella.",
            ["ChatGPT", "Compiti", "Copiare", "Scrivere", "Professore"],
            ["Atrofia cognitiva", "Strumento dialettico", "Pensiero critico autonomo", "Paternità dell'opera", "Apprendimento consapevole"]
        ),
        (
            "I lavoratori invisibili dell'algoritmo (Ghost Workers)",
            "Dietro i motori di IA ci sono milioni di lavoratori sottopagati nel terzo mondo che etichettano immagini violente per moderare i contenuti. Denuncialo.",
            ["Persone", "Guardare foto", "Poveri", "Schiavi", "IA"],
            ["Lavoro grigio digitale", "Etichettatura dei dati", "Esternalizzazione dello sfruttamento", "Trauma psicologico", "Giustizia lavorativa tecnologica"]
        ),
        (
            "La sorveglianza biometrica negli spazi pubblici",
            "Telecamere a riconoscimento facciale nelle stazioni e nelle piazze. Argomenta contro la trasformazione delle città in panopticon di controllo costante.",
            ["Telecamere", "Faccia", "Stazione", "Sicurezza", "Polizia"],
            ["Riconoscimento facciale", "Panopticon digitale", "Compressione della libertà", "Spazio pubblico libero", "Sorveglianza predittiva"]
        ),
        (
            "Il gaming patologico e i meccanismi di gratificazione istantanea",
            "Le loot box e i pass battaglia utilizzano gli stessi schemi psicologici delle slot machine. Chiedi regolamentazioni severe per tutelare i minorenni.",
            ["Videogiochi", "Loot box", "Soldi", "Vincere", "Giocare sempre"],
            ["Gratificazione istantanea", "Ludopatia giovanile", "Design persuasivo", "Protezione dei minori", "Regolamentazione etica"]
        ),
        (
            "La pirateria digitale e il rispetto del diritto d'autore",
            "Scaricare musica, film e libri senza pagare toglie sostentamento agli artisti e ai creativi indipendenti. Sostieni il valore della retribuzione culturale.",
            ["Scaricare", "Torrent", "Film gratis", "Artisti", "Soldi"],
            ["Diritto d'autore", "Sostenibilità culturale", "Retribuzione creativa", "Industria intellettuale", "Legalità digitale"]
        ),
        (
            "Il divario digitale (Digital Divide) e le disuguaglianze sociali",
            "Chi non ha una connessione veloce o un computer recente a casa rischia l'esclusione formativa e civile. Chiedi internet pubblico come diritto universale.",
            ["Wifi", "Computer vecchio", "Poveri", "Scuola", "Internet"],
            ["Digital divide", "Disuguaglianza strutturale", "Connettività universale", "Emancipazione civica", "Infrastruttura democratica"]
        ),
        (
            "L'obsolescenza programmata dei dispositivi elettronici",
            "Smartphone progettati per rallentare dopo due anni o resi impossibili da riparare. Difendi il diritto alla riparabilità universale contro lo spreco.",
            ["Telefono rotto", "Rallenta", "Batteria", "Comprare nuovo", "Riparare"],
            ["Obsolescenza programmata", "Diritto alla riparazione", "Economia dello spreco", "Monopoli industriali", "Tutela del consumatore"]
        ),
        (
            "Il riconoscimento dei bot nelle conversazioni online",
            "Migliaia di profili falsi automatizzati diffondono propaganda e fomentano litigi sui social. Chiedi che ogni bot sia chiaramente etichettato per legge.",
            ["Bot", "Profili falsi", "Twitter", "Propaganda", "Utente"],
            ["Automatizzazione della disinformazione", "Identità sintetica", "Trasparenza algoritmica", "Inquinamento del dibattito", "Verifica dell'utente"]
        ),
        (
            "La memoria digitale versus la bellezza di dimenticare",
            "Nel web ogni nostro errore giovanile rimane indicizzato per decenni. Spiega perché l'essere umano ha bisogno del diritto biologico all'oblio per rinascere.",
            ["Ricordare", "Post vecchio", "Cancellare", "Internet", "Errore"],
            ["Diritto all'oblio", "Plasticità biografica", "Redenzione umana", "Eternità digitale", "Spazio di crescita"]
        ),
        (
            "L'accessibilità web per l'autonomia delle persone anziane",
            "Interfacce complicate e burocrazia digitale escludono milioni di nonni dai servizi essenziali. Proponi un design empatico e sportelli fisici di supporto.",
            ["Anziani", "Spid", "Nonno", "Complicato", "Computer"],
            ["Alfabetizzazione digitale inclusiva", "Design empatico", "Inclusione generazionale", "Sportello di prossimità", "Semplificazione delle interfacce"]
        ),
        (
            "L'esplorazione spaziale robotica versus le missioni umane",
            "Le sonde spaziali come Voyager e i rover su Marte raccolgono dati preziosi senza rischiare vite umane. Sostieni la priorità della ricerca scientifica automatizzata.",
            ["Marte", "Rover", "Astronauti", "Spazio", "Morire"],
            ["Esplorazione robotica", "Incolumità umana", "Efficienza scientifica", "Frontiera astronomica", "Sonde interstellari"]
        ),
        (
            "Il manifesto per un'umanità tecnologica e cosciente",
            "Pronuncia un discorso che inviti la tua generazione a non essere consumatori passivi di codici scritti da altri, ma architetti consapevoli del proprio avvenire.",
            ["Usare il telefono", "Passivi", "Futuro", "Ragazzi", "Consumare"],
            ["Architettura consapevole", "Protagonismo digitale", "Umanesimo tecnologico", "Guida etica", "Libertà creativa"]
        )
    ],
    "b2": [
        (
            "Il Capitalismo della Sorveglianza di Shoshana Zuboff",
            "Analizza la mercificazione dell'esperienza umana convertita in dati comportamentali predittivi e venduta nei mercati dei futuri comportamentali.",
            ["Zuboff", "Dati", "Google", "Facebook", "Sorveglianza"],
            ["Surveillance capitalism", "Surplus comportamentale", "Mercato predittivo", "Espropriazione dell'esperienza", "Sovranità individuale"]
        ),
        (
            "La scatola nera (Black Box) dell'IA e l'opacità decisionale",
            "Quando gli algoritmi neurali decidono su mutui, assunzioni o sentenze penali, nessuno sa spiegare il perché. Esigi il diritto alla spiegabilità algoritmica.",
            ["Black box", "Algoritmo", "Decisione", "Spiegare", "Computer"],
            ["Opacità neurale", "Diritto alla spiegabilità", "Giustizia algoritmica", "Trasparenza epistemica", "Responsabilità umana"]
        ),
        (
            "L'allineamento dell'Intelligenza Artificiale ai valori umani (AI Alignment)",
            "Come garantire che modelli superintelligenti perseguano obiettivi compatibili con la sopravvivenza e la dignità umana senza interpretazioni letterali catastrofiche?",
            ["Superintelligenza", "Terminator", "Valori", "Uccidere tutti", "IA"],
            ["AI alignment problem", "Valori condivisi", "Controllo teleologico", "Convergenza strumentale", "Sicurezza esistenziale"]
        ),
        (
            "Le armi autonome letali (Lethal Autonomous Weapons)",
            "Droni programmati per individuare ed eliminare bersagli umani senza alcun intervento o giudizio morale da parte dell'operatore. Chiedine la messa al bando totale.",
            ["Droni killer", "Guerra", "Uccidere", "Soldati", "Pulsante"],
            ["Armi autonome letali", "De-umanizzazione del conflitto", "Bandiera morale", "Diritto internazionale umanitario", "Supervisione umana significativa"]
        ),
        (
            "La proprietà intellettuale nell'era dei modelli generativi",
            "Milioni di testi e opere d'arte umane sono stati raschiati dal web senza compenso per addestrare modelli commerciali. Difendi il lavoro dell'ingegno umano.",
            ["Copyright", "Copiare", "Disegni", "Scrittori", "Addestramento"],
            ["Scraping indiscriminato", "Fair use distorto", "Proprietà intellettuale", "Retribuzione autoriale", "Tutela dell'ingegno"]
        ),
        (
            "La polarizzazione algoritmica e la minaccia alla democrazia",
            "Le piattaforme massimizzano il tempo di permanenza premiando i contenuti che scatenano indignazione e rabbia. Denuncia il veleno iniettato nel corpo sociale.",
            ["Rabbia", "Indignazione", "Condividere", "Litigare", "Piattaforme"],
            ["Ottimizzazione del coinvolgimento", "Ingegneria della polarizzazione", "Veleno democratico", "Frenesia reattiva", "Architettura etica"]
        ),
        (
            "Il transumanesimo e il miraggio del potenziamento cognitivo",
            "Interfacce neurali dirette cervello-computer e manipolazione genetica per superare i limiti biologici. Metti in guardia dalla nascita di caste biologiche separate.",
            ["Chip nel cervello", "Superuomini", "Potenziamento", "Biologia", "Macchine"],
            ["Transumanesimo tecnocratico", "Caste genetiche", "Integrità biologica", "Hubris prometeica", "Giustizia antropologica"]
        ),
        (
            "La solitudine affettiva e i chatbot relazionali",
            "Sempre più individui instaurano legami intimi con avatar empatici artificiali. Analizza il rischio di atrofia relazionale verso gli esseri umani reali e imperfetti.",
            ["Fidanzata virtuale", "Robot", "Chatbot", "Amore", "Soli"],
            ["Simulazione affettiva", "Atrofia relazionale", "Conforto surrogato", "Rifiuto della vulnerabilità", "Relazione incarnata"]
        ),
        (
            "Il riconoscimento delle emozioni: invasione della sfera interiore",
            "Software che analizzano micro-espressioni facciali e tono di voce durante colloqui di lavoro per giudicare l'affidabilità. Denuncia la nuova fisiognomica algoritmica.",
            ["Faccia", "Telecamera", "Emozioni", "Lavoro", "Bocciato"],
            ["Fisiognomica digitale", "Invasione dell'interiorità", "Determinismo biometrico", "Pseudoscienza computazionale", "Dignità della persona"]
        ),
        (
            "La sovranità digitale europea versus i monopoli della Silicon Valley",
            "L'infrastruttura tecnologica del continente dipende totalmente da poche multinazionali statunitensi e cinesi. Difendi l'urgenza di un'autonomia strategica europea.",
            ["Silicon Valley", "Big Tech", "Monopolio", "Europa", "Dipendere"],
            ["Sovranità tecnologica", "Infrastruttura strategica", "Regolamentazione antitrust", "AI Act europeo", "Autonomia geopolitica"]
        ),
        (
            "La manipolazione elettorale e il micro-targeting psicometrico",
            "Dallo scandalo Cambridge Analytica all'uso di messaggi personalizzati per orientare il voto degli indecisi. Mostra la vulnerabilità del processo democratico.",
            ["Cambridge Analytica", "Voto", "Elezioni", "Messaggi mirati", "Profilo"],
            ["Micro-targeting psicometrico", "Manipolazione dell'elettorato", "Vulnerabilità cognitiva", "Trasparenza democratica", "Integrità elettorale"]
        ),
        (
            "L'automazione industriale e la redistribuzione del dividendo tecnologico",
            "Se i robot rimpiazzeranno milioni di professioni intellettuali e manuali, argomenta a favore di una tassazione sui robot per finanziare un reddito universale.",
            ["Robot", "Lavoro perso", "Tasse sui robot", "Disoccupazione", "Fabbriche"],
            ["Disoccupazione tecnologica", "Dividendo della produttività", "Reddito di base universale", "Riforma della previdenza", "Giustizia distributiva"]
        ),
        (
            "Il metaverso e la fuga dal mondo fisico",
            "Miliardi investiti per creare universi virtuali tridimensionali mentre il pianeta reale brucia. Critica la fuga nichilista nella simulazione sintetica.",
            ["Metaverso", "Realtà virtuale", "Avatar", "Fuga", "Mondo vero"],
            ["Nichilismo immersivo", "Alienazione dalla physis", "Fuga dal reale", "Mercificazione spaziale", "Custodia del mondo condiviso"]
        ),
        (
            "La censura delle piattaforme private e lo spazio pubblico",
            "Quando un amministratore delegato di un social network può spegnere l'account di un capo di Stato o di un dissidente, chi controlla l'agorà moderna?",
            ["Bannare", "Account cancellato", "Proprietario del social", "Zittire", "Twitter"],
            ["Privatizzazione dell'agorà", "Monopolio dell'enunciazione", "Garanzie giurisdizionali", "Bene comune comunicativo", "Neutralità della rete"]
        ),
        (
            "Il debito cognitivo delle nuove generazioni",
            "Delegare la memoria, il calcolo e l'orientamento spaziale agli smartphone sta alterando la corteccia cerebrale. Sostieni la riscoperta dell'autonomia mnemonica.",
            ["Memoria", "Smartphone", "Cervello", "Calcolare", "Dimenticare"],
            ["Debito cognitivo", "Plasticità neurale regressiva", "Autonomia mnemonica", "Esternalizzazione della mente", "Esercizio critico"]
        ),
        (
            "L'etica del biohacking e dell'editing genetico CRISPR",
            "La possibilità economica di selezionare tratti fisici e cognitivi per i propri figli rischia di trasformare l'umanità in una società a caste biologiche.",
            ["CRISPR", "Genetica", "Bambini su misura", "DNA", "Malattie"],
            ["Eugenetica neoliberale", "Editing germinale", "Caste biologiche", "Inviolabilità della casualità", "Bioetica democratica"]
        ),
        (
            "I bias algoritmici nella giustizia predittiva",
            "Software di valutazione del rischio di recidiva carceraria assegnano punteggi peggiori alle minoranze etniche. Dimostra come l'IA replichi i pregiudizi storici.",
            ["Razzismo", "Carcere", "Algoritmo", "Neri", "Giudici"],
            ["Bias di addestramento", "Discriminazione sistematica", "Giustizia predittiva fallace", "Riproduzione dell'ingiustizia", "Supervisione etica"]
        ),
        (
            "L'archeologia digitale e la conservazione della memoria storica",
            "Formati di file proprietari che diventano illeggibili dopo pochi anni minacciano di cancellare la memoria del nostro secolo. Difendi i formati aperti.",
            ["Floppy disk", "File non si apre", "Perdere tutto", "Foto vecchie", "Formati"],
            ["Preservazione digitale", "Standard aperti", "Amnesia documentale", "Archivistica contemporanea", "Memoria perenne"]
        ),
        (
            "La neutralità della rete come principio costituzionale",
            "I provider non devono poter rallentare determinati siti per favorire partner commerciali a pagamento. Difendi la rete aperta e indifferente ai contenuti.",
            ["Net neutrality", "Internet veloce per chi paga", "Bloccare siti", "Provider", "Connessione"],
            ["Neutralità della rete", "Non discriminazione del traffico", "Parità di accesso", "Infrastruttura democratica", "Libertà telematica"]
        ),
        (
            "Il manifesto per l'Umanesimo Digitale",
            "Pronuncia un discorso programmatico: la tecnica deve essere sottomessa alla dignità della persona umana, e non l'uomo ridotto a ingranaggio del codice.",
            ["Tecnologia", "Uomo", "Comandare", "Schiavo", "Futuro"],
            ["Umanesimo digitale", "Primato assiologico dell'umano", "Tecnocrazia decostruita", "Emancipazione tecnologica", "Futuro responsabile"]
        )
    ],
    "c1": [
        (
            "La stanza cinese di John Searle e la critica all'IA forte",
            "Esporrai la confutazione del test di Turing: la mera manipolazione sintattica di simboli formali non implica alcuna reale comprensione semantica né coscienza intenzionale.",
            ["Searle", "Stanza cinese", "Turing", "Capire", "Simboli"],
            ["Sintassi vs Semantica", "Intenzionalità originaria", "Confutazione dell'IA forte", "Manipolazione simbolica", "Coscienza incarnata"]
        ),
        (
            "L'ontologia dell'informazione e la filosofia di Luciano Floridi",
            "Illustra la transizione verso l'Infosfera e l'inforg: come la riconcettualizzazione dell'essere in termini informazionali stia ridefinendo la condizione umana.",
            ["Floridi", "Infosfera", "Dati", "Inforg", "Internet"],
            ["Filosofia dell'informazione", "Onlife e infosfera", "Soggettività come inforg", "Ecologia dell'iperstoria", "Riconcettualizzazione ontologica"]
        ),
        (
            "Il panopticon digitale e la sorveglianza diffusa in Byung-Chul Han",
            "Analizza la psicopolitica neoliberale: a differenza della sorveglianza orwelliana fondata sulla costrizione, oggi ci sorvegliamo volontariamente attraverso l'esibizione.",
            ["Byung-Chul Han", "Panopticon", "Sorveglianza", "Trasparenza", "Volontari"],
            ["Psicopolitica digitale", "Auto-sfruttamento volontario", "Dittatura della trasparenza", "Società della stanchezza", "Dispositivo immateriale"]
        ),
        (
            "L'interfaccia neurale e il problema dell'identità personale in Derek Parfit",
            "Se i ricordi e i processi cerebrali possono essere caricati (mind uploading) o sincronizzati su supporti sintetici, quale nozione di io continuo permane?",
            ["Cervello", "Mind uploading", "Io", "Ricordi", "Macchina"],
            ["Identità personale", "Continuità psicologica", "Decostruzione dell'Io sostanziale", "Sdoppiamento ontologico", "Parfitismo computazionale"]
        ),
        (
            "L'etica del machine learning e la responsabilità senza soggetto",
            "Chi è responsabile moralmente e giuridicamente per il danno cagionato da una rete neurale ad auto-apprendimento il cui operato è imprevedibile ai programmatori stessi?",
            ["Responsabile", "Colpa", "Programmatore", "Incidente", "Algoritmo"],
            ["Agency adespota", "Lacuna di responsabilità", "Autonomia decisionale non-umana", "Imputabilità causale", "Nuovi paradigmi di imputazione"]
        ),
        (
            "La singolarità tecnologica e l'ipotesi dell'esplosione di intelligenza",
            "Valuta criticamente l'orizzonte di I.J. Good e Vernor Vinge: il momento in cui una macchina superintelligente progetterà macchine ancora superiori escludendo l'uomo.",
            ["Singolarità", "Superintelligenza", "Fine dell'uomo", "Veloce", "Futuro"],
            ["Esplosione di intelligenza", "Orizzonte degli eventi cognitivo", "Limite antropologico", "Teleologia transumana", "Imprevedibilità radicale"]
        ),
        (
            "Il simulacro e la simulazione in Jean Baudrillard",
            "Dimostra come l'iperreale abbia soppiantato il reale: viviamo in una mappa che genera il territorio, dove il codice precede e determina i fatti.",
            ["Baudrillard", "Simulazione", "Vero e falso", "Mappa", "Televisione"],
            ["Precessione dei simulacri", "Iperrealtà simulata", "Dissoluzione del referente", "Trasparenza del male", "Codice autopoietico"]
        ),
        (
            "L'antropotecnica e le regole per il parco umano in Peter Sloterdijk",
            "Ripercorri la polemica sulla fine dell'umanesimo letterario come strumento di addomesticamento e la comparsa delle biotecnologie di selezione intenzionale.",
            ["Sloterdijk", "Parco umano", "Addomesticare", "Umanesimo", "Biotecnologie"],
            ["Antropotecnica", "Fine dell'umanesimo classico", "Addomesticamento biologico", "Autoproduzione dell'umano", "Post-umanismo filosofico"]
        ),
        (
            "Il cyberfemminismo e il Manifesto Cyborg di Donna Haraway",
            "Illustra la potenza sovversiva del cyborg come figura ibrida che demolisce le dicotomie patriarcali tradizionali tra natura/cultura, umano/animale, maschio/femmina.",
            ["Haraway", "Cyborg", "Donne", "Natura", "Macchine"],
            ["Manifesto cyborg", "Sovversione delle dicotomie", "Identità spuria", "Rifiuto dell'essenzialismo", "Epistemologia femminista"]
        ),
        (
            "L'illusione del libero arbitrio di fronte alla previsione neuro-algoritmica",
            "Se modelli matematici possono prevedere con largo anticipo le scelte di consumo e di voto prima che siano coscienti, quale spazio residua per l'autonomia etica?",
            ["Libero arbitrio", "Prevedere", "Decidere", "Scienza", "Cervello"],
            ["Determinismo predittivo", "Precessione inconscia della scelta", "Illusione volizionale", "Autonomia etica resistente", "Spazio deliberativo"]
        ),
        (
            "L'epistemologia dei Big Data e la fine della teoria scientifica",
            "Confuta la tesi provocatoria di Chris Anderson: l'enorme massa di correlazioni statistiche automatizzate rende obsoleti i modelli causali e le ipotesi teoriche.",
            ["Big Data", "Teoria", "Scienza", "Correlazione", "Dati"],
            ["Fine della teoria", "Correlazione vs causalità", "Epistemologia computazionale", "Empirismo cieco", "Necessità del senso ipotetico"]
        ),
        (
            "L'archeologia dei media e la genealogia tecnica di Friedrich Kittler",
            "Illustra la celebre tesi di Kittler: i media determinano la nostra situazione. L'architettura del canale trasmissivo plasma la struttura del pensiero umano.",
            ["Kittler", "Media", "Computer", "Pensare", "Canale"],
            ["Determinismo materiale mediale", "Archeologia dei sistemi di trascrizione", "Struttura tecnica del logos", "Substrato materiale", "Genealogia del codice"]
        ),
        (
            "Il paradosso della trasparenza e la perdita del mistero",
            "Difendi la necessità ermeneutica dell'ombra, del segreto e dell'inespresso contro la pretesa positivista della quantificazione totale dell'esistenza.",
            ["Tutto trasparente", "Numeri", "Segreto", "Sapere tutto", "Schermo"],
            ["Resistenza dell'incommensurabile", "Elogio dell'opacità", "Sfera del segreto", "Positivismo quantificatore", "Mistero ontologico"]
        ),
        (
            "La proprietà dei commons digitali e il Copyleft",
            "Approfondisci la dottrina giuridica di Richard Stallman e Lawrence Lessig: il copyright rovesciato (copyleft) come strumento per preservare la libertà perenne dell'opera.",
            ["Stallman", "Copyleft", "Codice libero", "Diritti", "Licenza"],
            ["Copyleft universale", "Libertà di rimediazione", "Creative commons", "Beni comuni intangibili", "Rovesciamento del copyright"]
        ),
        (
            "La tecnocrazia e il tramonto della decisione politica in Habermas",
            "Come la razionalità strumentale teleologica sostituisce la deliberazione etica sui fini, riducendo la politica alla mera ottimizzazione funzionale dei mezzi.",
            ["Tecnici", "Habermas", "Politica", "Scelte", "Governo"],
            ["Ragione strumentale vs comunicativa", "Colonizzazione del mondo della vita", "Depoliticizzazione tecnocratica", "Subordinazione dei fini", "Etica del discorso"]
        ),
        (
            "La derealizzazione della guerra nei conflitti iperspettrali",
            "Attraverso la riflessione di Paul Virilio, analizza la velocità logistica e la visione satellitare che trasformano il campo di battaglia in un videogioco asettico per gli operatori.",
            ["Virilio", "Guerra", "Videogioco", "Schermi", "Bombardare"],
            ["Derealizzazione cinetica", "Guerra iperspettrale", "Asepsi omicida", "Velocità logistica", "Perdita del testimone oculare"]
        ),
        (
            "La fenomenologia dell'avatar e la corporeità disincarnata",
            "Cosa accade alla percezione sensoriale quando il soggetto si proietta in un corpo poligonale virtuale? Un'indagine merleau-pontyana della carne digitale.",
            ["Merleau-Ponty", "Avatar", "Corpo", "Carne", "Videogiochi"],
            ["Schema corporeo esteso", "Carne del mondo digitale", "Disincarnazione spuria", "Propriocezione virtuale", "Alterità poligonale"]
        ),
        (
            "La mercificazione dell'attenzione e la distrazione come merce",
            "Commenta la formula di Herbert Simon: la ricchezza di informazioni crea la povertà di attenzione. L'attenzione come risorsa scarsa contesa dalle multinazionali.",
            ["Attenzione", "Simon", "Notizie", "Mente", "Pubblicità"],
            ["Economia dell'attenzione", "Scarsità cognitiva", "Ingegneria della distrazione", "Appropriazione psichica", "Presidio meditativo"]
        ),
        (
            "La cittadinanza algoritmica e il Social Credit System",
            "Decostruisci il modello di quantificazione del comportamento civile applicato in regimi autoritari: il punteggio sociale come fine della libertà morale interiore.",
            ["Punteggio sociale", "Cina", "Buoni cittadini", "Premi e punizioni", "Telecamere"],
            ["Social credit scoring", "Quantificazione della virtù", "Omologazione comportamentale", "Totalitarismo digitale", "Morte della coscienza libera"]
        ),
        (
            "L'apologia dell'errore umano nell'era del calcolo perfetto",
            "Pronuncia un'orazione sull'errore, sulla deviazione imprevista e sull'esitazione poetica come scintilla originaria di ogni autentica scoperta e umanità.",
            ["Sbaglio", "Perfezione", "Calcolo", "Computer", "Infallibile"],
            ["Fecondità dell'errore", "Scarto imprevisto", "Serendipità ontologica", "Resistenza alla perfezione", "Scintilla creativa"]
        )
    ],
    "c2": [
        (
            "La questione della tecnica (Die Frage nach der Technik) in Heidegger",
            "Dimostra come l'essenza della tecnica moderna non sia affatto tecnica, ma sia il Ge-stell: l'imposizione che disvela la natura unicamente come fondo a disposizione (Bestand).",
            ["Heidegger", "Tecnica", "Macchine", "Natura", "Sfruttare"],
            ["Essenza della tecnica", "Ge-stell impositivo", "Bestand e fondo di riserva", "Disvelamento calcolante", "Pericolo supremo e salvezza"]
        ),
        (
            "L'obsolescenza dell'uomo e la vergogna prometeica in Günther Anders",
            "Pronuncia una summa sulla vergogna prometeica: il sentimento di inferiorità e imperfezione che l'essere umano prova di fronte alla precisione delle proprie macchine.",
            ["Anders", "Vergogna", "Macchine perfette", "Prometeo", "Uomo debole"],
            ["Vergogna prometeica", "Dislivello prometeico", "Obsolescenza dell'umano", "Cecità di fronte all'apocalisse", "Inadeguatezza dell'immaginazione"]
        ),
        (
            "L'archetipo del Golem e il destino demiurgico dell'Uomo",
            "Ripercorri la leggenda cabalistica di Praga: quando l'uomo scrive Verità (Emet) sulla fronte della materia inerte, rischia di esserne travolto se dimentica la Morte (Met).",
            ["Golem", "Praga", "Fango", "Robot", "Mostro"],
            ["Hybris demiurgica", "Scrittura animatrice", "Emet e Met cabalistico", "Creatura che sovrasta il creatore", "Responsabilità teurgica"]
        ),
        (
            "La decostruzione del concetto di intelligenza: Logos versus Calcolo",
            "Sostieni di fronte al consesso supremo che il calcolo combinatorio algoritmico, per quanto smisurato, non coincide in alcun modo con l'intuizione del Logos che coglie il senso dell'Essere.",
            ["Intelligenza", "Computer", "Pensare", "Calcolare", "Cervello"],
            ["Primato del Logos", "Riduzionismo computazionale", "Intuizione noetica", "Incommensurabilità del senso", "Abisso ermeneutico"]
        ),
        (
            "L'aporia della mente sintetica e la negazione dell'Altro cosmico",
            "Se un'intelligenza artificiale non muore, non prova dolore né finitudine biologica, può mai accedere all'etica della cura o rimarrà un solipsismo sterile?",
            ["Morte", "Dolore", "Macchina", "Etica", "Soffrire"],
            ["Finitudine ontologica", "Condizione di vulnerabilità", "Impossibilità dell'etica artificiale", "Solipsismo sintetico", "Custodia del limite"]
        ),
        (
            "L'algocrazia sovrana e il tramonto dello Stato costituzionale",
            "Delinea la profezia dell'ordinamento giuridico autopoietico automatizzato: la sostituzione della sentenza giurisdizionale con l'esecuzione istantanea del codice.",
            ["Giudice", "Codice", "Legge", "Automatico", "Tribunale"],
            ["Sovranità algocratica", "Esecuzione automatizzata", "Eclissi dell'ermeneutica giudiziaria", "Morte del contraddittorio", "Dittatura del codice"]
        ),
        (
            "La perdita dell'aura nell'epoca della riproducibilità generativa",
            "Rivisita Walter Benjamin: se l'opera d'arte nell'era industriale perdeva l'hic et nunc, cosa accade quando l'immagine viene generata a comando da una matrice algoritmica senza autore?",
            ["Benjamin", "Aura", "Arte", "IA", "Quadro"],
            ["Dissoluzione dell'hic et nunc", "Generazione adespota", "Eclissi dell'autore", "Aura irriproducibile", "Spettralità estetica"]
        ),
        (
            "L'apocalisse dell'attenzione e la fine della meditazione profonda",
            "Pronuncia un'orazione funebre per la capacità dell'uomo moderno di sostenere il pensiero lungo, l'argomentazione complessa e il silenzio mistico contemplativo.",
            ["Fretta", "Pensare piano", "Silenzio", "Attenzione", "Rumore"],
            ["Pensiero profondo", "Ecologia dell'attenzione", "Sospensione contemplativa", "Distruzione dell'interiorità", "Resistenza spirituale"]
        ),
        (
            "Il mito di Frankenstein rivisitato: la tragedia del rifiuto parentale",
            "Analizza il capolavoro di Mary Shelley: la vera colpa del dottor Frankenstein non fu la creazione della vita, ma l'abbandono vile della creatura orfana di senso.",
            ["Frankenstein", "Mostro", "Scienziato", "Creare la vita", "Paura"],
            ["Responsabilità genitoriale demiurgica", "Orfanezza della creatura", "Tragedia dell'abbandono", "Hybris e vigliaccheria", "Richiesta d'amore negata"]
        ),
        (
            "La colonizzazione del tempo vissuto nell'architettura dell'iperconnessione",
            "Dimostra come la tecnologia contemporanea abbia soppresso il Kairos (il momento opportuno) a favore del Chronos quantificato e monetizzato al millisecondo.",
            ["Tempo", "Orologio", "Notifiche", "Fretta", "Vivere"],
            ["Monetizzazione kairologica", "Sincronizzazione forzata", "Spazio interiore violato", "Ripristino del tempo sacro", "Frenesia estrattiva"]
        ),
        (
            "La neutralità assiologica della tecnica come finzione ideologica",
            "Confuta definitivamente il luogo comune per cui la tecnologia è solo uno strumento neutro che dipende dall'uso che se ne fa: la tecnica è già un progetto ontologico.",
            ["Strumento neutro", "Uso buono o cattivo", "Tecnica", "Dipende dall'uomo", "Macchina"],
            ["Progetto ontologico intrinseco", "Non-neutralità del dispositivo", "Pre-formattazione del mondo", "Struttura trascendentale", "Superamento dell'illusione strumentale"]
        ),
        (
            "L'erosione dell'Habus Corpus: dall'individuo al dividuo numerico",
            "Evoca Gilles Deleuze e la società del controllo: l'essere umano cessa di essere persona singola indivisibile (in-dividuo) per frammentarsi in dividui di dati tracciabili.",
            ["Deleuze", "Società del controllo", "Persone", "Dati", "Numero"],
            ["Società del controllo deleuziana", "Frammentazione in dividui", "Cifratura del soggetto", "Habeas Data", "Resistenza ontologica"]
        ),
        (
            "L'enigma del Test di Turing invertito: quando l'uomo deve provare di essere umano",
            "Rifletti sull'assurdità del Captcha: l'essere umano costretto a dimostrare a un server di non essere un robot selezionando semafori e passaggi pedonali.",
            ["Captcha", "Non sono un robot", "Semafori", "Dimostrare", "Computer"],
            ["Inversione kafkiana", "Sottomissione all'arbitro sintetico", "Umanità sotto scrutinio", "Dover provare la vita", "Ironia cibernetica"]
        ),
        (
            "La parresìa del programmatore ribelle e l'etica dell'hacking",
            "Delinea la figura dell'hacker etico che viola il codice proprietario non per profitto ma per disvelare al mondo le violazioni dei diritti civili celate negli algoritmi.",
            ["Hacker", "Pirati", "Computer", "Soldi", "Rubare"],
            ["Etica hacker originaria", "Parresìa cibernetica", "Disvelamento del codice", "Trasparenza insorgente", "Ribellione all'algocrazia"]
        ),
        (
            "La morte dell'esperienza incarnata nella pornografia digitale",
            "Analizza la scomparsa dell'incontro reale, della trepidazione dell'attesa e dell'odore dell'Altro nell'inondazione di stimoli visivi sintetici iper-accessibili.",
            ["Pornografia", "Sesso", "Schermi", "Corpi", "Incontri"],
            ["Disincarnazione del desiderio", "Spettacolo dell'intimità", "Atrofia della vicinanza", "Scomparsa dell'incontro", "Eros desacralizzato"]
        ),
        (
            "L'immortalità digitale come estrema aberrazione narcisistica",
            "Critica i progetti di clonazione mnemonica che promettono avatar conversazionali perpetui dei defunti: il rifiuto del lutto e la profanazione della morte.",
            ["Vivere per sempre", "Clonare voce", "Morti", "Avatar", "Dimenticare"],
            ["Profanazione del lutto", "Narcisismo immortale", "Negazione della finitudine", "Spettralità commerciale", "Rispetto dell'assenza"]
        ),
        (
            "L'oratore profetico contro l'anestesia cibernetica",
            "In un mondo in cui ogni parola è sintetizzata e ripulita da prompt linguistici prefabbricati, evoca la potenza devastatrice e sacra della voce umana viva.",
            ["Prompt", "Testo generato", "Parlare bene", "Perfetto", "Voce"],
            ["Voce incarnata vivente", "Rottura del codice prefabbricato", "Fervore profetico", "Parola non replicabile", "Potenza testimoniale"]
        ),
        (
            "Il patto di Faust nell'era della telematica universale",
            "Rivisita Goethe: abbiamo venduto la nostra anima, il nostro silenzio e la nostra libertà deliberativa in cambio della comodità e dell'onnipresenza immediata.",
            ["Faust", "Mefistofele", "Anima", "Comodo", "Diavolo"],
            ["Patto faustiano cibernetico", "Comodità alienante", "Espropriazione dell'anima", "Fascino demoniaco della velocità", "Riscatto morale"]
        ),
        (
            "L'apologia della notte: difendere l'oscurità dalla luce dei display",
            "Fai un'elegia filosofica del buio, delle stelle e del silenzio notturno come spazio primigenio dove il pensiero filosofico e la poesia possono ancora nascere.",
            ["Luce", "Display", "Notte", "Stelle", "Buio"],
            ["Sacralità della notte", "Silenzio siderale", "Difesa dell'oscurità", "Respiro cosmico", "Rifugio dell'anima"]
        ),
        (
            "L'inno all'Umano Incalcolabile: il giuramento dell'Oratore",
            "Pronuncia l'orazione conclusiva: gli algoritmi possono calcolare tutto tranne il sussulto del cuore, l'atto d'amore gratuito e la libertà insorgente dello spirito.",
            ["Algoritmo", "Tutto calcolato", "Cuore", "Amore", "Fine"],
            ["Incalcolabilità dello spirito", "Gratuità dell'amore", "Sussulto originario", "Trionfo della coscienza", "Magistero perenne"]
        )
    ]
}
