# Mazzo: Diritti, Legalità & Costituzione (diritti)
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            "La fila per la fontanella",
            "C'è una lunga fila di bambini assetati dopo la corsa. Spiega perché aspettare il proprio turno senza spingere fa bene a tutti.",
            ["Fila", "Spingere", "Acqua", "Sete", "Primo"],
            ["Turno", "Pazienza", "Rispetto", "Ordine", "Bere"]
        ),
        (
            "Il compagno senza merenda",
            "Un bambino ha dimenticato lo zainetto con la merenda sul pulmino. Convinci la classe che condividere un pezzetto a testa è un diritto e un dovere.",
            ["Merenda", "Fame", "Dimenticare", "Mangiare", "Mio"],
            ["Dividere", "Insieme", "Compagno", "Dono", "Sorriso"]
        ),
        (
            "Il pallone che appartiene a tutti",
            "Il pallone nuovo della scuola è stato preso da un solo gruppo. Ricorda a tutti che i giochi del cortile sono di tutti gli alunni.",
            ["Pallone", "Solo noi", "Prendere", "Mio", "Calcio"],
            ["Condivisione", "Tutti", "Cortile", "Regola", "Insieme"]
        ),
        (
            "Ascoltare chi parla piano",
            "Una compagna molto timida sta provando a dire la sua opinione a voce bassa. Invita la classe a fare silenzio per ascoltarla con cura.",
            ["Silenzio", "Zitti", "Urlare", "Voce", "Bassa"],
            ["Ascolto", "Attenzione", "Opinione", "Rispettare", "Pazienza"]
        ),
        (
            "La promessa mantenuta",
            "Hai promesso a un amico di prestargli i colori a matita il giorno dopo. Spiegagli perché mantenere le promesse crea fiducia vera.",
            ["Promessa", "Colori", "Domani", "Dimenticato", "Matite"],
            ["Parola data", "Fiducia", "Lealtà", "Patto", "Amicizia"]
        ),
        (
            "Rispettare chi ha una lingua diversa",
            "È arrivato un nuovo compagno che parla una lingua diversa dalla tua. Spiega come accoglierlo con i gesti e imparare le sue parole.",
            ["Lingua", "Straniero", "Capire", "Parlare", "Strano"],
            ["Accoglienza", "Gesto", "Imparare", "Ponte", "Sorriso"]
        ),
        (
            "Rimettere in ordine i giochi",
            "Finita l'ora di ricreazione la classe è sottosopra. Spiega perché riordinare insieme è una regola che aiuta tutti a ritrovare le cose.",
            ["Disordine", "Tavolo", "Mettere a posto", "Lavoro", "Stanco"],
            ["Collaborazione", "Cura", "Spazio comune", "Ordine", "Squadra"]
        ),
        (
            "Il rispetto del sonno altrui",
            "Durante il riposino o la lettura silenziosa, qualcuno fa rumore. Invitalo dolcemente a rispettare la tranquillità di chi si riposa.",
            ["Rumore", "Fastidio", "Urlare", "Dormire", "Zitto"],
            ["Tranquillità", "Delicatezza", "Silenzio", "Pace", "Cura"]
        ),
        (
            "Il diritto di dire la verità",
            "È caduto un barattolo di colla. Spiega perché ammettere che è stato un incidente è molto meglio che dare la colpa a un altro.",
            ["Colla", "Colpa", "Bugia", "Caduto", "Nascondere"],
            ["Verità", "Coraggio", "Onestà", "Incidente", "Fiducia"]
        ),
        (
            "Nessuno può essere picchiato",
            "Due compagni alzano le mani per un disaccordo. Fermali ricordando che le mani servono per costruire e disegnare, non per fare male.",
            ["Mani", "Picchiare", "Pugno", "Male", "Arrabbiato"],
            ["Carezza", "Dialogo", "Costruire", "Fermarsi", "Accordo"]
        ),
        (
            "Il diritto di sbagliare disegno",
            "Un compagno piange perché ha sbagliato a colorare fuori dai bordi. Rassicuralo sul fatto che tutti abbiamo il diritto di sbagliare e riprovare.",
            ["Sbaglio", "Bordo", "Brutto", "Piangere", "Gomma"],
            ["Tentativo", "Imparare", "Pazienza", "Unicità", "Ricominciare"]
        ),
        (
            "Il nome proprio di ciascuno",
            "Qualcuno chiama un compagno con un nomignolo sgradevole. Ricorda a tutti che ciascuno ha un nome bello che va rispettato.",
            ["Nome", "Nomignolo", "Ridere", "Offesa", "Chiamare"],
            ["Identità", "Rispetto", "Dignità", "Persona", "Chiamata"]
        ),
        (
            "La cura del cortile della scuola",
            "Qualcuno ha gettato le cartacce per terra invece che nel cestino. Convinci i compagni che la scuola pulita è un bene di tutti.",
            ["Carta", "Buttare", "Terra", "Cestino", "Sporco"],
            ["Ambiente", "Pulizia", "Comune", "Responsabilità", "Bello"]
        ),
        (
            "Il diritto di fare domande",
            "Non hai capito la spiegazione del maestro. Trova il coraggio di alzare la mano e ricordare che fare domande è il modo più bello di imparare.",
            ["Capito", "Maestro", "Vergogna", "Mano", "Domanda"],
            ["Curiosità", "Chiarimento", "Sapere", "Dubbio", "Crescita"]
        ),
        (
            "Il diritto di giocare in pace",
            "Un gruppo di bambini corre all'impazzata travolgendo chi stava disegnando col gessetto. Chiedi loro di fare spazio a ogni gioco con prudenza.",
            ["Correre", "Cadere", "Travolgere", "Spazio", "Gessetto"],
            ["Attenzione", "Prudenza", "Convivenza", "Gioco libero", "Armonia"]
        ),
        (
            "La merenda equa",
            "C'è una scatola di biscotti per la festa. Spiega come fare a distribuirli in parti esattamente uguali per non lasciare nessuno senza.",
            ["Biscotti", "Più a me", "Prendere", "Scatola", "Festa"],
            ["Uguaglianza", "Equità", "Distribuzione", "Condivisione", "Giustizia"]
        ),
        (
            "Rispettare gli animali della scuola",
            "C'è un uccellino ferito nel giardino della scuola. Spiega ai compagni perché anche gli animali hanno diritto a essere protetti e non disturbati.",
            ["Uccello", "Nido", "Prendere", "Sasso", "Volare"],
            ["Protezione", "Cura", "Vita", "Creatura", "Rispetto"]
        ),
        (
            "La pace dopo la ricreazione",
            "Suona la campanella e c'è ancora agitazione. Fai un piccolo annuncio per invitare tutti a rientrare sereni e pronti ad ascoltare.",
            ["Campana", "Correre", "Urlare", "Fine", "Rientro"],
            ["Serenità", "Ascolto", "Pausa", "Ripresa", "Accordo"]
        ),
        (
            "Il prestito dei libri della biblioteca",
            "Prendi in prestito il libro di favole della classe. Prometti di custodirlo con cura perché dopo di te lo leggeranno altri bambini.",
            ["Libro", "Pagina", "Strappare", "Mio", "Biblioteca"],
            ["Custodia", "Prestito", "Lettura", "Futuro", "Rispetto"]
        ),
        (
            "Il diritto di essere tristi senza essere presi in giro",
            "Un bambino è in disparte con gli occhi lucidi. Ricorda alla classe che tutti abbiamo il diritto di avere una giornata storta senza giudizi.",
            ["Piangere", "Triste", "Ridere", "Prendere in giro", "Cos'hai"],
            ["Accoglienza", "Spazio", "Delicatezza", "Silenzio", "Comprensione"]
        )
    ],
    "a2": [
        (
            "La carta dei diritti della classe",
            "Siete incaricati di redigere il regolamento condiviso della classe. Presenta tre articoli fondamentali che garantiscano pari voce e rispetto reciproco.",
            ["Regole", "Divieto", "Punizione", "Scuola", "Maestra"],
            ["Costituzione", "Pari dignità", "Partecipazione", "Accordo", "Cittadinanza"]
        ),
        (
            "Il diritto all'istruzione per tutti i bambini",
            "Racconta la storia di bambini che nel mondo non possono andare a scuola perché costretti a lavorare. Spiega perché la scuola è un diritto fondamentale.",
            ["Lavoro", "Poveri", "Bambini", "Fabbrica", "Scuola"],
            ["Istruzione", "Emancipazione", "Futuro", "Diritti inviolabili", "Convenzione ONU"]
        ),
        (
            "L'elezione del capoclasse democratico",
            "Presenta la tua candidatura a capoclasse spiegando che il rappresentante non è un capo che comanda, ma un portavoce che serve la comunità.",
            ["Votatemi", "Capo", "Comandare", "Prometto", "Migliore"],
            ["Portavoce", "Servizio", "Rappresentanza", "Ascolto", "Trasparenza"]
        ),
        (
            "Il dovere civico di pagare il biglietto del bus",
            "Un compagno si vanta di viaggiare sui mezzi pubblici senza pagare. Dimostragli che il trasporto pubblico funziona solo grazie al contributo di ciascuno.",
            ["Biglietto", "Furbizia", "Controllore", "Multa", "Soldi"],
            ["Bene comune", "Senso civico", "Contributo", "Legalità", "Servizio pubblico"]
        ),
        (
            "La libertà di espressione e il rispetto altrui",
            "Qualcuno offende un compagno e si giustifica dicendo che in democrazia si può dire ciò che si vuole. Chiarisci il limite della libertà d'espressione.",
            ["Libertà", "Dire tutto", "Offendere", "Democrazia", "Parola"],
            ["Limite", "Dignità della persona", "Rispetto", "Responsabilità", "Confine"]
        ),
        (
            "La parità di genere nei giochi e nello sport",
            "Alcuni ragazzi dicono che il calcio è solo per maschi e la danza solo per femmine. Dimostra con argomenti chiari l'assurdità degli stereotipi di genere.",
            ["Maschi", "Femmine", "Calcio", "Danza", "Gioco"],
            ["Uguaglianza", "Passione", "Stereotipo", "Pari opportunità", "Talento"]
        ),
        (
            "La difesa dei beni monumentali del quartiere",
            "Hanno imbrattato con una bomboletta una statua o un muro storico. Parla al consiglio comunale dei ragazzi per chiedere rispetto per l'arte comune.",
            ["Muro", "Scrivere", "Vernice", "Statua", "Polizia"],
            ["Patrimonio comune", "Bellezza", "Storia", "Rispetto civico", "Tutela"]
        ),
        (
            "Il valore del voto segreto",
            "Si sta votando per scegliere la meta della gita scolastica. Spiega perché il voto segreto è una conquista democratica che tutela la libertà di coscienza.",
            ["Votare", "Foglio", "Gita", "Guardare", "Vincere"],
            ["Segretezza", "Libertà di coscienza", "Scelta autonoma", "Democrazia", "Espressione"]
        ),
        (
            "La presunzione di innocenza prima del verdetto",
            "È scomparso un temperino prezioso e tutti accusano subito il compagno più disordinato. Difendilo ricordando che nessuno è colpevole senza prove certe.",
            ["Ladro", "Rubato", "Lui", "Certo", "Punire"],
            ["Presunzione di innocenza", "Prove", "Giustizia", "Accusa infondata", "Equità"]
        ),
        (
            "Il diritto alla privacy del diario personale",
            "Qualcuno ha aperto e letto ad alta voce una pagina del diario segreto di una compagna. Denuncia l'invasione indebita della sfera intima personale.",
            ["Diario", "Leggere", "Segreto", "Ridere", "Vergogna"],
            ["Sfera privata", "Intimità", "Rispetto", "Inviolabilità", "Confidenziale"]
        ),
        (
            "Il riciclo come dovere verso la collettività",
            "Presenta alla scuola un piano per la raccolta differenziata spiegando che gettare correttamente i rifiuti è un atto di rispetto verso i vicini e l'ambiente.",
            ["Spazzatura", "Cassonetto", "Plastica", "Buttare", "Puzza"],
            ["Raccolta differenziata", "Sostenibilità", "Dovere civico", "Riciclo", "Comunità"]
        ),
        (
            "Il dovere di soccorso verso chi cade",
            "Un bambino è caduto dalle scale e molti tirano dritto per non perdere la campanella. Fai un appello al dovere immediato di solidarietà e primo soccorso.",
            ["Scale", "Campanella", "Tardi", "Cadere", "Correre"],
            ["Soccorso", "Solidarietà", "Priorità umana", "Intervento", "Cura"]
        ),
        (
            "Il valore delle tasse spiegato a un bambino",
            "Spiega in modo semplice ed efficace a un coetaneo a cosa servono le imposte: costruire ospedali, asfaltare strade e pagare gli insegnanti.",
            ["Tasse", "Soldi", "Stato", "Pagare", "Governo"],
            ["Servizi essenziali", "Ospedali", "Bene pubblico", "Solidarietà sociale", "Contributo equo"]
        ),
        (
            "Il divieto di farsi giustizia da soli",
            "Dopo un calcio ricevuto in campo, un compagno vuole vendicarsi a fine partita. Convinci il giocatore che la vendetta personale distrugge ogni convivenza civile.",
            ["Vendetta", "Rivalersi", "Picchiare", "Arbitro", "Farsela pagare"],
            ["Regole condivise", "Rinuncia alla violenza", "Giustizia terza", "Civilizzazione", "Pace"]
        ),
        (
            "Il diritto al riposo e al tempo libero",
            "Commenta l'Articolo 31 della Convenzione dei Diritti dell'Infanzia: ogni bambino ha diritto al riposo, al tempo libero, al gioco e alle attività culturali.",
            ["Compiti", "Studiare sempre", "Stanco", "Dovere", "Lavoro"],
            ["Diritto al gioco", "Tempo libero", "Sviluppo armonico", "Creatività", "Benessere infantile"]
        ),
        (
            "Il contrasto al lavoro minorile nel mondo",
            "Illustra in un'assemblea di classe la piaga del lavoro minorile nelle piantagioni di cacao e nelle miniere, chiedendo un consumo critico ed etico.",
            ["Bambini", "Lavoro", "Fatica", "Soldi", "Comprare"],
            ["Sfruttamento minorile", "Consumo critico", "Commercio equo", "Dignità universale", "Solidarietà"]
        ),
        (
            "L'importanza dei cartelli stradali",
            "Spiega ai bambini più piccoli perché le strisce pedonali e il semaforo non sono un fastidio, ma scudi che salvano vite ogni giorno.",
            ["Semaforo", "Rosso", "Macchine", "Attraversare", "Fretta"],
            ["Sicurezza stradale", "Incolumità", "Rispetto delle regole", "Prudenza", "Patto civico"]
        ),
        (
            "La solidarietà con le famiglie in difficoltà",
            "Proponi un mercatino di solidarietà per sostenere le famiglie del quartiere che attraversano momenti difficili.",
            ["Poveri", "Soldi", "Comprare", "Vendita", "Roba usata"],
            ["Solidarietà circolare", "Mutuo aiuto", "Comunità coesa", "Dignità", "Sostegno reciproco"]
        ),
        (
            "Il rispetto del lavoro dei rappresentanti della legge",
            "Incontra un vigile urbano o un carabiniere venuto a scuola. Esprimi a nome degli studenti il ringraziamento per chi tutela la nostra sicurezza quotidiana.",
            ["Poliziotto", "Multa", "Sirena", "Pistola", "Arrestare"],
            ["Tutela dei cittadini", "Servizio pubblico", "Legalità democratica", "Sicurezza comune", "Riconoscenza"]
        ),
        (
            "La Costituzione come bussola di tutti i giorni",
            "Concludi la settimana dell'educazione civica mostrando come la nostra Costituzione non sia un vecchio testo di biblioteca ma una guida viva per stare insieme.",
            ["Libro vecchio", "Leggi", "Politici", "Scuola", "Studio"],
            ["Bussola democratica", "Patto fondativo", "Cittadinanza attiva", "Valori condivisi", "Futuro comune"]
        )
    ],
    "b1": [
        (
            "L'Articolo 3 della Costituzione: l'uguaglianza sostanziale",
            "Illustra la rivoluzione del secondo comma dell'Articolo 3: è compito della Repubblica rimuovere gli ostacoli economici e sociali che limitano la libertà.",
            ["Articolo 3", "Uguali", "Poveri", "Ostacoli", "Stato"],
            ["Uguaglianza sostanziale", "Riparazione sociale", "Pari dignità", "Pieno sviluppo", "Repubblica attiva"]
        ),
        (
            "La libertà di stampa e la lotta alla censura",
            "Commenta l'Articolo 21 della Costituzione: difendi il diritto dei giornalisti a informare la pubblica opinione senza temere intimidazioni o censure.",
            ["Giornale", "Articolo 21", "Censura", "Scrivere", "Zittire"],
            ["Libertà di stampa", "Opinione pubblica", "Trasparenza del potere", "Informazione indipendente", "Presidio democratico"]
        ),
        (
            "La nascita della Costituzione italiana dalla Resistenza",
            "Ricostruisci come dalle macerie del fascismo e della guerra nacque il patto costituzionale antifascista tra forze politiche diverse unite dalla libertà.",
            ["Guerra", "Fascismo", "Partigiani", "Macerie", "Pace"],
            ["Resistenza fondativa", "Patto costituente", "Rinascita democratica", "Antifascismo", "Memoria civile"]
        ),
        (
            "Il diritto alla salute come interesse della collettività",
            "Analizza l'Articolo 32: la salute non è solo un diritto fondamentale dell'individuo, ma una responsabilità condivisa e un bene collettivo.",
            ["Ospedale", "Malato", "Dottore", "Curare", "Medicine"],
            ["Diritto alla salute", "Sanità pubblica universale", "Bene collettivo", "Prevenzione solidale", "Tutela degli indigenti"]
        ),
        (
            "Il principio della separazione dei poteri",
            "Spiega perché nella democrazia moderna legislativo, esecutivo e giudiziario devono restare indipendenti per impedire ogni tirannia.",
            ["Potere", "Governo", "Giudici", "Parlamento", "Tiranno"],
            ["Separazione montesquieuiana", "Pesi e contrappesi", "Stato di diritto", "Indipendenza della magistratura", "Garanzie costituzionali"]
        ),
        (
            "La presunzione di non colpevolezza e il processo equo",
            "Affronta il fenomeno del processo mediatico: difendi il principio per cui un imputato non è colpevole sino alla condanna definitiva.",
            ["Colpevole", "Televisione", "Giornali", "Prigione", "Condannato"],
            ["Presunzione d'innocenza", "Giusto processo", "Garanzie difensive", "Giustizia terrena", "Dignità dell'imputato"]
        ),
        (
            "Il dovere di voto e la crisi della partecipazione",
            "Davanti a dati record sull'astensionismo giovanile, esorta i futuri elettori a non rinunciare all'arma più potente conquistata col sangue: il voto.",
            ["Scheda", "Elezioni", "Politici tutti uguali", "Astenersi", "Non andare"],
            ["Dovere civico", "Sovranità popolare", "Partecipazione democratica", "Conquista storica", "Futuro politico"]
        ),
        (
            "L'educazione alla legalità contro le mafie",
            "Ricorda le figure di Giovanni Falcone e Paolo Borsellino: spiega perché la mafia si sconfigge prima di tutto nelle aule scolastiche e con la cultura.",
            ["Falcone", "Borsellino", "Bomba", "Mafia", "Polizia"],
            ["Cultura della legalità", "Senso dello Stato", "Resistenza civile", "Memoria operosa", "Dignità contro il pizzo"]
        ),
        (
            "Il ripudio della guerra nell'Articolo 11",
            "L'Italia ripudia la guerra come strumento di offesa alla libertà degli altri popoli e come mezzo di risoluzione delle controversie internazionali. Commentalo.",
            ["Guerra", "Armi", "Pace", "Combattere", "Soldati"],
            ["Ripudio categorico", "Risoluzione diplomatica", "Organizzazioni internazionali", "Giustizia globale", "Diritto umanitario"]
        ),
        (
            "I doveri inderogabili di solidarietà politica ed economica",
            "Illustra l'Articolo 2: la Repubblica riconosce i diritti inviolabili dell'uomo e richiede l'adempimento dei doveri di solidarietà politica, economica e sociale.",
            ["Diritti miei", "Doveri", "Solidarietà", "Articolo 2", "Stato"],
            ["Inderogabilità del dovere", "Solidarietà sociale", "Inviolabilità della persona", "Corresponsabilità", "Cittadinanza matura"]
        ),
        (
            "Il lavoro come fondamento della Repubblica (Art. 1)",
            "L'Italia è una Repubblica democratica, fondata sul lavoro. Dimostra perché i costituenti scelsero il lavoro e non il censo o il privilegio nobiliare.",
            ["Lavoro", "Repubblica", "Soldi", "Articolo 1", "Costituzione"],
            ["Dignità del lavoro", "Emancipazione sociale", "Contributo civico", "Superamento del privilegio", "Fondamento democratico"]
        ),
        (
            "Il diritto di asilo e la protezione internazionale",
            "Esamina l'Articolo 10 comma 3: lo straniero al quale sia impedito nel suo paese l'effettivo esercizio delle libertà democratiche ha diritto d'asilo.",
            ["Profughi", "Barconi", "Confini", "Stranieri", "Rimpatriare"],
            ["Diritto d'asilo", "Protezione costituzionale", "Libertà negate", "Umanità transnazionale", "Dovere di accoglienza"]
        ),
        (
            "La tutela dell'ambiente nella Costituzione rinnovata",
            "Nel 2022 la Repubblica ha introdotto nell'Articolo 9 la tutela dell'ambiente, della biodiversità e degli ecosistemi anche nell'interesse delle future generazioni.",
            ["Ambiente", "Articolo 9", "Animali", "Generazioni future", "Inquinamento"],
            ["Riforma costituzionale", "Tutela della biodiversità", "Giustizia intergenerazionale", "Sviluppo sostenibile", "Presidio ecologico"]
        ),
        (
            "La laicità dello Stato e la libertà di culto",
            "Spiega come la laicità repubblicana non sia ostilità verso le religioni, ma garanzia che ogni persona possa professare liberamente la propria fede o nessuna fede.",
            ["Religione", "Prete", "Chiesa", "Credere", "Laico"],
            ["Laicità inclusiva", "Libertà di culto", "Pari dignità confessionale", "Neutralità dello Stato", "Pluralismo spirituale"]
        ),
        (
            "Il contrasto al caporalato e allo sfruttamento lavorativo",
            "Denuncia le condizioni disumane dei braccianti agricoli nei campi e invoca l'applicazione rigorosa delle leggi a tutela della sicurezza e della retribuzione minima.",
            ["Campi", "Pomodori", "Paga da fame", "Caporalato", "Padrone"],
            ["Sfruttamento lavorativo", "Dignità salariale", "Contrattazione collettiva", "Legalità nei campi", "Tutela sindacale"]
        ),
        (
            "Il valore civico della raccolta differenziata e della cura urbana",
            "Dimostra come il decoro urbano e la gestione ecologica dei beni comuni siano indicatori diretti del grado di democrazia e civiltà di una comunità.",
            ["Spazzatura", "Città sporca", "Strada", "Multe", "Vigili"],
            ["Beni comuni urbani", "Senso civico", "Coesione territoriale", "Spazio condiviso", "Cura collettiva"]
        ),
        (
            "La funzione rieducativa della pena (Art. 27)",
            "Le pene non possono consistere in trattamenti contrari al senso di umanità e devono tendere alla rieducazione del condannato. Difendi questo principio cardine.",
            ["Carcere", "Buttare la chiave", "Punire", "Gattabuia", "Cella"],
            ["Rieducazione sociale", "Senso di umanità", "Riforma carceraria", "Dignità intangibile", "Giustizia riparativa"]
        ),
        (
            "Il diritto alla privacy nell'era degli smartphone a scuola",
            "Regolamentare l'uso dei dispositivi mobili a scuola non è autoritarismo ma difesa dell'attenzione, della socialità dal vivo e della privacy reciproca.",
            ["Cellulare", "Vietato", "Professore", "Messaggiare", "Ritiro"],
            ["Tutela dei dati personali", "Comunità di apprendimento", "Socialità autentica", "Presidio educativo", "Autodisciplina"]
        ),
        (
            "La tutela del paesaggio e del patrimonio storico-artistico",
            "Illustra l'Articolo 9: la Repubblica promuove lo sviluppo della cultura e la ricerca scientifica, e tutela il paesaggio e il patrimonio storico della Nazione.",
            ["Quadri", "Museo", "Paesaggio", "Monumenti", "Turismo"],
            ["Patrimonio storico-artistico", "Identità culturale", "Tutela costituzionale", "Ricerca scientifica", "Memoria collettiva"]
        ),
        (
            "La cittadinanza e i diritti dei figli di stranieri nati in Italia",
            "Argomenta a favore di una riforma della legge sulla cittadinanza per riconoscere come concittadini a pieno titolo i giovani cresciuti e scolarizzati in Italia.",
            ["Ius soli", "Stranieri", "Passaporto", "Permesso di soggiorno", "Italiani veri"],
            ["Inclusione repubblicana", "Ius scholae", "Appartenenza civica", "Omogeneità generazionale", "Diritti civici"]
        )
    ],
    "b2": [
        (
            "La disobbedienza civile da Thoreau a Martin Luther King",
            "Delinea la legittimità morale e politica della disobbedienza civile: quando una legge viola apertamente i diritti umani, l'obiezione di coscienza è un dovere.",
            ["Legge", "Disobbedire", "Arresto", "King", "Thoreau"],
            ["Obiezione di coscienza", "Disobbedienza civile", "Legge ingiusta", "Resistenza nonviolenta", "Diritto naturale"]
        ),
        (
            "Il bilanciamento tra sicurezza nazionale e libertà individuali",
            "Nell'era del terrorismo e della cyber-guerra, molti governi comprimono i diritti fondamentali. Difendi l'inviolabilità dell'habeas corpus contro la ragion di Stato.",
            ["Sicurezza", "Telecamere", "Terroristi", "Controllo", "Polizia"],
            ["Habeas corpus", "Ragion di Stato", "Bilanciamento costituzionale", "Stato di diritto", "Diritti inalienabili"]
        ),
        (
            "La crisi della rappresentanza e il populismo anti-istituzionale",
            "Analizza la sfiducia crescente verso i parlamenti e la fascinazione per l'uomo forte. Riafferma la complessità insostituibile della mediazione democratica.",
            ["Parlamento", "Cast", "Uomo forte", "Popolo contro i politici", "Voto inutile"],
            ["Mediazione democratica", "Crisi di rappresentanza", "Corpi intermedi", "Degenerazione populista", "Complessità istituzionale"]
        ),
        (
            "Il whistleblowing: tradimento dell'azienda o presidio civico?",
            "Difendi i dipendenti che denunciano illeciti ambientali o corruzione all'interno della propria organizzazione, confutando l'accusa infamante di spionaggio.",
            ["Spia", "Traditore", "Azienda", "Segreto d'ufficio", "Denunciare"],
            ["Whistleblower", "Trasparenza civica", "Prevalenza dell'interesse pubblico", "Etica del coraggio", "Tutela legale"]
        ),
        (
            "La progressività fiscale e la giustizia distributiva (Art. 53)",
            "Tutti sono tenuti a concorrere alle spese pubbliche in ragione della loro capacità contributiva. Il sistema tributario è informato a criteri di progressività.",
            ["Tasse", "Flat tax", "Soldi", "Ricchi", "Stato ladro"],
            ["Progressività tributaria", "Capacità contributiva", "Patto ridistributivo", "Giustizia fiscale", "Stato sociale"]
        ),
        (
            "Il diritto all'oblio versus il diritto all'informazione",
            "Analizza il conflitto tra la permanenza a tempo indeterminato delle notizie giudiziarie sui motori di ricerca e il diritto del cittadino a rifarsi una vita.",
            ["Google", "Internet", "Notizie vecchie", "Cancellare", "Vergogna"],
            ["Diritto all'oblio", "Memoria digitale perenne", "Diritto di cronaca", "Riabilitazione sociale", "Autodeterminazione informativa"]
        ),
        (
            "La regolamentazione del fine vita e l'autodeterminazione terapeutica",
            "Argomenta sulla libertà della persona di rifiutare trattamenti sanitari sproporzionati e di decidere dignitosamente sul proprio fine vita in conformità all'Art. 32.",
            ["Eutanasia", "Morire", "Ospedale", "Macchine", "Dolore"],
            ["Autodeterminazione terapeutica", "Consenso informato", "Accanimento clinico", "Dignità del morire", "Biotestamento"]
        ),
        (
            "Il lavoro agile e il diritto alla disconnessione",
            "La pervasività dei dispositivi digitali ha cancellato il confine tra orario di lavoro e vita privata. Sostieni la necessità normativa del diritto alla disconnessione.",
            ["Smart working", "Mail", "Notte", "Rispondere", "Capo"],
            ["Diritto alla disconnessione", "Tempo di vita", "Sfruttamento cognitivo", "Confine del lavoro", "Salute mentale lavorativa"]
        ),
        (
            "Il sovraffollamento carcerario come violazione dei diritti umani",
            "Di fronte alle condanne inflitte all'Italia dalla Corte EDU per le condizioni disumane delle carceri, proponi un piano di depenalizzazione e misure alternative.",
            ["Celle piene", "Prigione", "Buttare la chiave", "Delinquenti", "Polizia penitenziaria"],
            ["Corte europea dei diritti dell'uomo", "Misure alternative", "Decenza detentiva", "Umanizzazione della pena", "Costituzionalità"]
        ),
        (
            "L'ingerenza umanitaria e la sovranità degli Stati",
            "È lecito che la comunità internazionale intervenga militarmente all'interno di uno Stato per fermare massacri civili o violazioni sistematiche dei diritti?",
            ["Guerra", "Intervento", "Confini", "Dittatore", "ONU"],
            ["Responsabilità di proteggere", "Sovranità statale", "Ingerenza umanitaria", "Diritto cosmopolitico", "Multilateralismo"]
        ),
        (
            "La tutela dei dati biometrici e il riconoscimento facciale",
            "L'installazione di telecamere biometriche nei centri urbani minaccia la libertà di assembramento e la privacy. Chiedi una moratoria sull'uso dell'IA repressiva.",
            ["Telecamere", "Faccia", "Polizia", "Strada", "Riconoscere"],
            ["Dati biometrici", "Sorveglianza di massa", "Libertà di manifestazione", "Profilazione algoritmica", "Garante della privacy"]
        ),
        (
            "Il finanziamento pubblico dei partiti contro la corruzione oligarchica",
            "L'abolizione totale dei rimborsi elettorali rischia di consegnare la politica ai grandi donatori privati. Riapri il dibattito sulla trasparenza dei fondi democratici.",
            ["Partiti ladri", "Soldi pubblici", "Elezioni", "Privati", "Campagna"],
            ["Pluralismo democratico", "Trasparenza elettorale", "Cattura oligarchica", "Pari condizioni di competizione", "Finanziamento trasparente"]
        ),
        (
            "La tutela delle minoranze linguistiche (Art. 6)",
            "La Repubblica tutela con apposite norme le minoranze linguistiche. Celebra la ricchezza polifonica dell'Italia contro ogni nazionalismo monolitico.",
            ["Dialetto", "Italiano solo", "Lingua", "Minoranze", "Parlare bene"],
            ["Pluralismo linguistico", "Patrimonio intangibile", "Tutela costituzionale", "Convivenza pacifica", "Valorizzazione territoriale"]
        ),
        (
            "L'indipendenza della Corte Costituzionale come custode supremo",
            "Illustra il ruolo dei quindici giudici della Consulta: annullare le leggi approvate dal parlamento se in contrasto con i principi supremi della Carta.",
            ["Giudici", "Consulta", "Bocciare leggi", "Costituzione", "Parlamento"],
            ["Corte Costituzionale", "Sindacato di legittimità", "Rigidità costituzionale", "Garanzia democratica", "Argine antimaggioritario"]
        ),
        (
            "La giustizia riparativa contro la sola retribuzione penale",
            "Spiega l'orizzonte introdotto dalla riforma penale: l'incontro mediato tra vittima e autore del reato per ricostruire il legame sociale infranto.",
            ["Punire", "Carcere", "Occhio per occhio", "Vittima", "Condanna"],
            ["Giustizia riparativa", "Mediazione penale", "Riparazione del legame", "Riconoscimento del danno", "Riconciliazione comunitaria"]
        ),
        (
            "Il dovere di soccorso in mare nel diritto internazionale marittimo",
            "La Convenzione di Amburgo e la Convenzione SAR impongono a ogni capitano di trarre in salvo chiunque sia in pericolo di naufragio. Difendi la legge del mare.",
            ["Migranti", "Barconi", "ONG", "Porti chiusi", "Naufraghi"],
            ["Diritto marittimo internazionale", "Convenzione SAR", "Obbligo di soccorso", "Place of safety", "Incondizionatezza del salvataggio"]
        ),
        (
            "Il contrasto all'evasione fiscale come dovere patriottico",
            "L'evasione sottrae oltre ottanta miliardi all'anno alla scuola e alla sanità pubblica. Dimostra come evadere sia un tradimento della comunità nazionale.",
            ["Furbi", "Scontrino", "Nero", "Tasse troppe", "Stato"],
            ["Fedeltà fiscale", "Patriottismo civico", "Evasione sistemica", "Servizi universali", "Equità redistributiva"]
        ),
        (
            "Il diritto all'aborto e la tutela della salute riproduttiva",
            "Analizza la legge 194 e la sua difesa della dignità e dell'autonomia della donna di fronte alle sfide dei tassi elevati di obiezione di coscienza.",
            ["Aborto", "194", "Medici obiettori", "Donne", "Scelta"],
            ["Autodeterminazione femminile", "Salute riproduttiva", "Accesso alle cure", "Legge 194", "Dignità della persona"]
        ),
        (
            "La cittadinanza digitale e il contrasto all'odio telematico",
            "Proponi all'assemblea scolastica un codice etico di istituto per l'uso dei canali social, fondato sulla responsabilità penale e morale delle parole online.",
            ["Post", "Insulti", "Profilo falso", "Hater", "Scuola"],
            ["Cittadinanza digitale", "Identità telematica", "Responsabilità giuridica", "Decoro civile online", "Netiquette normativa"]
        ),
        (
            "Il futuro del regionalismo: autonomia differenziata o unità nazionale?",
            "Dibatti sul dilemma costituzionale tra la valorizzazione delle autonomie locali (Art. 5) e la salvaguardia dell'uguaglianza dei livelli essenziali di prestazione (LEP).",
            ["Regioni", "Nord e Sud", "Soldi", "Autonomia", "Stato"],
            ["Unità indivisibile", "Livelli essenziali delle prestazioni", "Autonomia differenziata", "Perequazione solidale", "Patto costituzionale"]
        )
    ],
    "c1": [
        (
            "L'apologia kantiana della pace perpetua e il diritto cosmopolitico",
            "Esporrai la visione di Immanuel Kant sull'istituzione di una federazione mondiale di popoli liberi (Foedus Amphictyonicum) fondata sul diritto d'ospitalità.",
            ["Kant", "Pace", "Guerra", "Mondo", "Nazioni"],
            ["Diritto cosmopolitico", "Federazione di repubbliche", "Pace perpetua", "Ospitalità universale", "Imperativo giuridico razionale"]
        ),
        (
            "La dottrina pura del diritto di Hans Kelsen e la Grundnorm",
            "Illustra la teoria normativista del diritto: l'ordinamento come piramide gerarchica (Stufenbau) la cui validità poggia sulla norma fondamentale presupposta.",
            ["Kelsen", "Leggi", "Giusto", "Morale", "Validità"],
            ["Grundnorm trascendentale", "Stufenbau piramidale", "Dottrina pura del diritto", "Nomodinamica formale", "Positivismo giuridico"]
        ),
        (
            "Il costituzionalismo liberale contro la tirannia della maggioranza",
            "Analizza attraverso Alexis de Tocqueville e John Stuart Mill la necessità democratica dei contropoteri e delle garanzie a tutela delle minoranze dissenzienti.",
            ["Maggioranza", "Tutti d'accordo", "Tocqueville", "Mill", "Vincere le elezioni"],
            ["Tirannia della maggioranza", "Argine antimaggioritario", "Pluralismo liberale", "Diritti inviolabili delle minoranze", "Garanzie sostanziali"]
        ),
        (
            "La giustizia come equità nella teoria di John Rawls",
            "Illustra l'esperimento mentale del velo di ignoranza e i due principi di giustizia: la massima libertà per ciascuno e il principio di differenza a favore dei più svantaggiati.",
            ["Rawls", "Giustizia", "Velo", "Ignoranza", "Ricchezza"],
            ["Velo d'ignoranza", "Posizione originaria", "Principio di differenza", "Equità distributiva", "Liberalismo egualitario"]
        ),
        (
            "Il dilemma habermasiano tra fatti e norme nella democrazia discorsiva",
            "Dimostra come la legittimità delle leggi nello Stato contemporaneo discenda unicamente dalla procedura discorsiva aperta a tutti i consociati giuridici.",
            ["Habermas", "Legge", "Discorso", "Democrazia", "Comunicare"],
            ["Democrazia discorsiva", "Fatti e norme", "Agire comunicativo", "Sfera pubblica deliberativa", "Legittimazione procedurale"]
        ),
        (
            "La sovranità statale e lo stato di eccezione in Carl Schmitt",
            "Decostruisci la tesi di Schmitt: Sovrano è chi decide sullo stato di eccezione. Difendi la resistenza dell'ordinamento costituzionale contro la decisione arbitraria.",
            ["Schmitt", "Sovrano", "Eccezione", "Dittatura", "Costituzione"],
            ["Decisionismo politico", "Stato d'eccezione", "Sospensione della norma", "Sostanzialismo autoritario", "Stato di diritto legalitario"]
        ),
        (
            "L'universalismo dei diritti umani di fronte al relativismo culturale",
            "Affronta il dilemma epistemologico ed etico: i diritti umani sono una maschera dell'imperialismo occidentale o un'autentica istanza di emancipazione per ogni essere umano?",
            ["Occidente", "Imperialismo", "Cultura nostra", "Diritti", "Relativo"],
            ["Universalismo transculturale", "Inviolabilità ontologica", "Critica post-coloniale", "Emancipazione condivisa", "Dialogo interculturale"]
        ),
        (
            "La biopolitica e l'Habeas Corpus nell'era del biosorveglianza",
            "Seguendo la riflessione di Michel Foucault e Giorgio Agamben, indaga come il controllo dei corpi biologici sia diventato il centro nevralgico della governance moderna.",
            ["Foucault", "Agamben", "Corpi", "Controllo", "Salute"],
            ["Dispositivo biopolitico", "Nuda vita e homo sacer", "Governance securitaria", "Anatomopolitica del potere", "Compressione dell'Habeas Corpus"]
        ),
        (
            "La formula di Radbruch: il diritto sovralegale contro la legge ingiusta",
            "Esporrai la celebre formula giuridica del 1946: quando la legge positiva è intollerabilmente ingiusta, essa deve cedere di fronte alla giustizia sostanziale.",
            ["Radbruch", "Legge fascista", "Giustizia", "Ubbidire", "Tribunale"],
            ["Formula di Radbruch", "Diritto intollerabilmente ingiusto", "Torto legale", "Rinascita del giusnaturalismo", "Validità materiale"]
        ),
        (
            "Il principio di responsabilità verso le generazioni future in Hans Jonas",
            "Sostieni la costituzionalizzazione del dovere ecologico: le future generazioni hanno un diritto reale a ereditare una biosfera vivibile e intatta.",
            ["Jonas", "Futuro", "Generazioni", "Natura", "Responsabilità"],
            ["Imperativo dell'esistenza futura", "Euristica della paura", "Dovere asimmetrico", "Titolarità giuridica dei posteri", "Ecologia costituzionale"]
        ),
        (
            "L'istituzionalismo giuridico di Santi Romano contro lo statalismo puro",
            "Illustra la teoria per cui il diritto non nasce dalla sanzione statale ma dall'organizzazione sociale spontanea (Ubi societas, ibi ius).",
            ["Santi Romano", "Stato", "Leggi", "Società", "Tribunali"],
            ["Ordinamento come istituzione", "Pluralità degli ordinamenti", "Ubi societas ibi ius", "Spontaneità nomopoietica", "Superamento del monismo"]
        ),
        (
            "La dignità umana come principio supremo non negoziabile (Art. 1 Grundgesetz)",
            "Analizza il dettato costituzionale tedesco dell'inviolabilità della dignità (Menschenwürde) come barriera invalicabile anche contro esigenze di sicurezza estrema.",
            ["Dignità", "Germania", "Inviolabile", "Tortura", "Salvare persone"],
            ["Menschenwürde kantiana", "Divieto di strumentalizzazione", "Barriera assiologica", "Intoccabilità della persona", "Diritto fondamentale assoluto"]
        ),
        (
            "La giustizia transizionale e i processi di riconciliazione",
            "Esamina l'esperienza delle Commissioni per la Verità e la Riconciliazione in Sudafrica: come pacificare un paese senza rinunciare alla verità storica.",
            ["Sudafrica", "Mandela", "Processi", "Verità", "Perdono"],
            ["Giustizia transizionale", "Ubuntu costituzionale", "Accertamento testimoniale", "Riconciliazione civile", "Oltre la vendetta penale"]
        ),
        (
            "L'aporia dell'internazionalismo socialista e l'autodeterminazione dei popoli",
            "Ripercorri il dibattito tra Lenin e Wilson sull'autodeterminazione: tra principio di emancipazione antimperialista e frammentazione etno-nazionalista.",
            ["Lenin", "Wilson", "Nazioni", "Autodeterminazione", "Confini"],
            ["Autodeterminazione dei popoli", "Principio di nazionalità", "Internazionalismo internazionalista", "Frammentazione balcanica", "Sovranità decolonizzata"]
        ),
        (
            "La tutela costituzionale del lavoro precario e dell'autonomia economica",
            "Interpreta l'Articolo 36 alla luce della gig economy: il diritto a una retribuzione proporzionata e in ogni caso sufficiente ad assicurare un'esistenza libera e dignitosa.",
            ["Rider", "Paga", "Articolo 36", "Minimo", "Lavoro"],
            ["Salario dignitoso", "Sussistenza autonoma", "Integrazione costituzionale", "Protezione del lavoro intermittente", "Giustizia contrattuale"]
        ),
        (
            "La decostruzione derridiana della sovranità e della pena di morte",
            "Riprendi i seminari di Jacques Derrida: la sovranità statale come diritto di vita e di morte, e l'abolizione universale del patibolo come compimento della civiltà.",
            ["Derrida", "Pena di morte", "Stato", "Boia", "Uccidere"],
            ["Decostruzione del diritto sovrano", "Teologia politica della pena capitale", "Incondizionatezza del vivente", "Compiutezza abolizionista", "Sovranità decostruita"]
        ),
        (
            "Il costituzionalismo globale e la Corte Penale Internazionale",
            "Valuta la giurisdizione dell'Aja sui crimini contro l'umanità: una promessa di fine dell'impunità per i dittatori o una giustizia selettiva dei vincitori?",
            ["Aja", "Tribunale", "Guerra", "Dittatori", "Condanna"],
            ["Giurisdizione universale", "Statuto di Roma", "Crimini contro l'umanità", "Ineffettività sanzionatoria", "Cosmopolitismo giudiziario"]
        ),
        (
            "L'autonomia della scienza e i limiti etici della ricerca biotecnologica",
            "Discuti l'Articolo 33 (L'arte e la scienza sono libere): qual è il limite costituzionale di fronte all'ingegneria genetica germinale e al potenziamento umano?",
            ["Scienza", "Clonazione", "Articolo 33", "Esperimenti", "Divieto"],
            ["Libertà della ricerca", "Integrità del genoma umano", "Bioetica costituzionale", "Principio di precauzione", "Custodia dell'umano"]
        ),
        (
            "L'Hate Speech e la dottrina statunitense del First Amendment",
            "Metti a confronto il modello europeo di limitazione dell'odio verbale con il modello americano della marketplace of ideas che protegge anche i discorsi ripugnanti.",
            ["First Amendment", "America", "Odio", "Libertà assoluta", "Parole"],
            ["Marketplace of ideas", "Dignità vs libertà d'espressione", "Limiti all'istigazione", "Clear and present danger", "Modello europeo militante"]
        ),
        (
            "L'eredità morale di Piero Calamandrei e il discorso ai giovani",
            "Ricrea l'appello pronunciato nel 1955 agli studenti milanesi: La Costituzione non è una macchina che va avanti da sola... ci dovete mettere la vostra voce e la vostra volontà.",
            ["Calamandrei", "Discorso", "Macchina", "Studenti", "1955"],
            ["Costituzione viva", "Sangue dei martiri", "Impegno testimoniale", "Militanza democratica", "Combustibile civile"]
        )
    ],
    "c2": [
        (
            "L'orazione per la Civitas Cosmopolita e il Tramonto del Leviatano",
            "Pronuncia un'orazione solenne che teorizzi il superamento dello Stato-Nazione sovrano verso un'architettura giuridica federale planetaria.",
            ["Stato", "Leviatano", "Mondo", "Confini", "Potere"],
            ["Metamorfosi cosmopolitica", "Eclissi della sovranità vestfaliana", "Nomos della Terra", "Costituzionalismo planetario", "Fratellanza universale"]
        ),
        (
            "L'archetipo dell'Antigone: il conflitto irriducibile tra Nomos e Themis",
            "Sviscera la tragedia sofoclea nell'aula magna dell'Istituto di Diritto Comparato: il decreto positivo di Creonte contro le leggi non scritte e immutabili degli dèi.",
            ["Antigone", "Creonte", "Sepoltura", "Fratello", "Decreto"],
            ["Themis primigenia", "Nomos secolare", "Aporia giusnaturalistica", "Tragicità del comando", "Legge non scritta"]
        ),
        (
            "La genesi violenta del diritto nel saggio di Walter Benjamin",
            "Decostruisci la distinzione tra la violenza che pone il diritto (rechtsetzend) e la violenza che lo conserva (rechtserhaltend), evocando la violenza pura o divina.",
            ["Benjamin", "Violenza", "Diritto", "Polizia", "Conservare"],
            ["Violenza istituente", "Violenza conservatrice", "Violenza pura o divina", "Critica della forza legale", "Messianismo redentore"]
        ),
        (
            "L'illusione democratica nella società dell'informazione e l'algocrazia",
            "Sostieni la tesi che l'automazione algoritmica dei processi deliberativi costituisca la fine sostanziale dell'autonomia deliberativa del cittadino.",
            ["Algoritmo", "Computer", "Voto", "Democrazia", "Decidere"],
            ["Deriva algocratica", "Eclissi dell'autonomia deliberativa", "Spazio pubblico automatizzato", "Asservimento cognitivo", "Sovranità del Logos"]
        ),
        (
            "Il processo a Socrate: la fedeltà alle Leggi della Polis fino alla cicuta",
            "Rivivi il Critone platonico: pronuncia il discorso delle Leggi di Atene a Socrate carcerato, spiegando perché distruggere la sentenza ingiusta distruggerebbe la polis stessa.",
            ["Socrate", "Cicuta", "Fuga", "Atene", "Morte"],
            ["Fedeltà alle Leggi", "Patto pedagogico originario", "Sacralità della Polis", "Ingiustizia subita vs agita", "Coerenza filosofica suprema"]
        ),
        (
            "La teologia politica e la secolarizzazione dei concetti giuridici",
            "Ripercorri l'assioma di Carl Schmitt: tutti i concetti più pregnanti della moderna dottrina dello Stato sono concetti teologici secolarizzati.",
            ["Schmitt", "Dio", "Miracolo", "Stato", "Religione"],
            ["Teologia politica secolarizzata", "Stato d'eccezione come miracolo", "Onnipotenza del legislatore", "Genealogia concettuale", "Sovranità demiurgica"]
        ),
        (
            "L'ordinamento internazionale come diritto primitivo e la sua metamorfosi",
            "Analizza la debolezza strutturale del diritto internazionale privo di monopolio della forza centralizzata, e delinea le condizioni per la sua maturazione vincolante.",
            ["Guerra", "Poliziotto del mondo", "Tribunale", "Trattati", "Forza"],
            ["Ordinamento adespota", "Monopolio della coercizione legittima", "Evoluzione nomopoietica", "Trascendenza dello ius ad bellum", "Pace kantiana"]
        ),
        (
            "L'uguaglianza delle capacità in Amartya Sen e Martha Nussbaum",
            "Difendi l'approccio delle capacità (Capabilities Approach) come fondamento per ridefinire i diritti costituzionali oltre la mera dotazione monetaria di beni primari.",
            ["Sen", "Nussbaum", "Soldi", "Diritti", "Povertà"],
            ["Capabilities approach", "Fioritura umana", "Uguaglianza sostanziale delle opportunità", "Funzionamenti essenziali", "Dignità capacitiva"]
        ),
        (
            "Il principio del nemico nel diritto penale dell'eccezione",
            "Confuta la dottrina del Feindstrafrecht di Günther Jakobs: negare le garanzie penali a terroristi o criminali significa trasformare lo Stato in un mostro liberticida.",
            ["Jakobs", "Nemico", "Terroristi", "Diritti a loro no", "Guerra"],
            ["Feindstrafrecht liberticida", "Inviolabilità dello status di cittadino", "Barriera garantista", "Universalità delle garanzie", "Dignità anche per il colpevole"]
        ),
        (
            "La democrazia costituzionale come limite insuperabile al potere costituente",
            "Argomenta contro ogni dottrina plebiscitaria: persino l'unanimità del popolo sovrano non ha il potere giuridico né morale di sopprimere i diritti inviolabili dell'uomo.",
            ["Popolo sovrano", "Tutti vogliono", "Cancellare diritti", "Votazione", "Referendum"],
            ["Limiti materiali della revisione", "Nucleo duro intangibile", "Democrazia sostanziale", "Argine assiologico", "Inviolabilità dell'umano"]
        ),
        (
            "La secolarizzazione del sacro e l'inviolabilità del corpo civile",
            "Esamina come il corpo umano, svincolato dalla sanzione religiosa tradizionale, sia diventato il nuovo tempio laico dei diritti costituzionali contemporanei.",
            ["Corpo", "Sacro", "Religione", "Dio", "Uomo"],
            ["Inviolabilità corporale laica", "Tempio costituzionale", "Autodeterminazione ontologica", "Rispetto dell'integrità", "Santità laica del vivente"]
        ),
        (
            "L'epistemologia giudiziaria e la verità processuale",
            "Delinea la distanza invalicabile tra la verità storica assoluta e la verità processuale costruita nel contraddittorio delle parti secondo le regole di prova.",
            ["Verità", "Processo", "Prove", "Giudice", "Sapere tutto"],
            ["Verità processuale formale", "Regole di esclusione probatoria", "Epistemologia giudiziaria", "Contraddittorio dialettico", "Incertezza ontologica"]
        ),
        (
            "Il diritto alla città e la riappropriazione dello spazio pubblico",
            "Sviluppa la teoria di Henri Lefebvre e David Harvey: il diritto alla città non come mera fruizione di servizi, ma come potere collettivo di trasformare l'ambiente urbano.",
            ["Città", "Case", "Sindaco", "Spazio", "Vivere"],
            ["Diritto alla città", "Riappropriazione collettiva", "Spazio pubblico sottratto alla speculazione", "Ecologia democratica urbana", "Cittadinanza partecipata"]
        ),
        (
            "La giustizia tra le specie: il costituzionalismo oltre l'umano",
            "Formula un'arringa per l'estensione della soggettività giuridica agli animali non umani e agli ecosistemi complessi (fiumi, foreste, barriere coralline).",
            ["Animali", "Diritti umani solo", "Fiume", "Uomo al centro", "Natura"],
            ["Soggettività giuridica non-umana", "Biocentrismo costituzionale", "Diritti della Natura", "Superamento dell'antropocentrismo", "Comunità biotica"]
        ),
        (
            "Il tradimento dei chierici di Julien Benda e l'indipendenza dell'intellettuale",
            "Riafferma il dovere sacro dell'uomo di pensiero di servire la giustizia e la verità universale, rifiutando ogni asservimento agli interessi di fazione o di Stato.",
            ["Intellettuali", "Benda", "Politica", "Partito", "Servire"],
            ["Tradimento dei chierici", "Custodia della verità universale", "Indipendenza intellettuale", "Rifiuto del cinismo pratico", "Testimonianza etica"]
        ),
        (
            "L'immunità parlamentare e la ratio di tutela dell'organo sovrano",
            "Distingui l'insindacabilità delle opinioni espresse e l'immunità processuale dal volgare privilegio di casta, ricostruendone la funzione di difesa contro vendette giudiziarie.",
            ["Privilegio", "Parlamentari", "Cast", "Polizia", "Processi"],
            ["Insindacabilità parlamentare", "Presidio dell'organo sovrano", "Ratio costituzionale", "Libertà del mandato", "Difesa dal potere giudiziario"]
        ),
        (
            "Il costituzionalismo dei beni comuni: acqua, aria e conoscenza aperta",
            "Elabora la categoria giuridica dei beni comuni (common goods) come terza via fondamentale tra la proprietà privata mercantilistica e la proprietà statale burocratica.",
            ["Beni comuni", "Privato", "Stato", "Acqua", "Proprietà"],
            ["Beni comuni primari", "Demanio collettivo dell'umanità", "Inappropriabilità essenziale", "Custodia fiduciaria", "Accesso universale"]
        ),
        (
            "La parresìa nella Repubblica romana: l'orazione di Cicerone pro Roscio Amerino",
            "Evoca il debutto oratorio del giovane Cicerone che sfida il tiranno Silla difendendo un innocente ingiustamente accusato di parricidio da potenti corrotti.",
            ["Cicerone", "Silla", "Paura", "Difesa", "Tribunale"],
            ["Oratoria della parresìa", "Sfida alla tirannide", "Incorruttibilità forense", "Coraggio della giovinezza", "Primato della giustizia"]
        ),
        (
            "Il ripensamento della proprietà privata in una prospettiva sociale",
            "Commenta l'Articolo 42 della Costituzione: la proprietà privata è riconosciuta e garantita dalla legge, che ne determina i modi di acquisto e i limiti allo scopo di assicurarne la funzione sociale.",
            ["Proprietà privata", "Mio", "Articolo 42", "Esproprio", "Padroni"],
            ["Funzione sociale della proprietà", "Limite all'egoismo proprietario", "Destinazione universale dei beni", "Solidarismo costituzionale", "Equità sociale"]
        ),
        (
            "L'appello alla Giustizia Vivente: il giuramento dell'Oratore Giusto",
            "Chiudi il percorso con un'invocazione epica: la legge senza giustizia è oppressione, ma la giustizia senza parola è muta. Siate la voce viva di chi non ha diritti.",
            ["Legge", "Giustizia", "Voce", "Parlare", "Fine"],
            ["Verbum iustitiae", "Voce degli inermi", "Magistero repubblicano", "Giuramento solenne", "Trionfo della civiltà"]
        )
    ]
}
