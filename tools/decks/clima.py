# Mazzo: clima
# 120 carte uniche calibrate pedagogicamente da A1 a C2 (20 carte per livello)

CARDS = {
    "a1": [
        (
            "L'albero del cortile",
            "Hai notato un grande albero che perde le foglie in autunno. Spiega a un compagno perché gli alberi dormono d'inverno per rifiorire a primavera.",
            ['Albero', 'Foglie', 'Autunno', 'Freddo', 'Morto'],
            ['Riposo', 'Primavera', 'Rami', 'Terra', 'Risveglio']
        ),
        (
            "La goccia d'acqua preziosa",
            "Mentre ti lavi i denti lasci scorrere l'acqua. Spiega a te stesso perché chiudere il rubinetto salva i pesciolini del fiume.",
            ['Rubinetto', 'Acqua', 'Sprecare', 'Denti', 'Lavati'],
            ['Goccia', 'Fiume', 'Cura', 'Dissetare', 'Preziosa']
        ),
        (
            "L'ape sul fiore profumato",
            "Vedi un'ape che si posa su una margherita. Spiega alla tua sorellina perché le api non vanno scacciate ma protette per il miele.",
            ['Ape', 'Puntura', 'Male', 'Scacciare', 'Paura'],
            ['Fiore', 'Polline', 'Miele', 'Giardino', 'Operosa']
        ),
        (
            'La bottiglietta di plastica abbandonata',
            'Trovi una bottiglia vuota vicino allo scivolo del parco. Spiega perché gettarla nel bidone blu rende il mondo più pulito.',
            ['Bottiglia', 'Plastica', 'Buttare', 'Terra', 'Sporco'],
            ['Riciclo', 'Parco', 'Cestino', 'Pulizia', 'Cura']
        ),
        (
            'Il canto degli uccellini al mattino',
            "Ti svegli sentendo gli uccelli cantare sul davanzale. Descrivi l'allegria che porta il risveglio della natura nella tua stanza.",
            ['Uccelli', 'Cantare', 'Finestra', 'Sveglia', 'Rumore'],
            ['Melodia', 'Alba', 'Piume', 'Mattino', 'Serenità']
        ),
        (
            'La passeggiata nel bosco in punta di piedi',
            'Cammini con la classe in un sentiero di montagna. Invita i compagni a fare silenzio per non spaventare gli animali selvatici.',
            ['Bosco', 'Urlare', 'Animali', 'Camminare', 'Paura'],
            ['Silenzio', 'Passo felpato', 'Foglie', 'Natura', 'Rispetto']
        ),
        (
            'La piantina nata dal fagiolo',
            "Hai messo un fagiolo nell'ovatta bagnata ed è spuntata una radice verde. Racconta il miracolo della vita che cresce sul davanzale.",
            ['Fagiolo', 'Ovatta', 'Acqua', 'Pianta', 'Bicchiere'],
            ['Germoglio', 'Radici', 'Luce', 'Crescita', 'Meraviglia']
        ),
        (
            'Il cane infreddolito sotto la pioggia',
            'Un cagnolino trema sotto un portico mentre piove a dirotto. Spiega perché dobbiamo prenderci cura di tutti gli animali senza casa.',
            ['Cane', 'Pioggia', 'Freddo', 'Tremare', 'Bagnato'],
            ['Rifugio', 'Calore', 'Protezione', 'Cuccia', 'Compassione']
        ),
        (
            'La neve soffice sui tetti',
            "È caduta la prima neve dell'anno e la città è tutta bianca. Racconta la sensazione magica di lasciare le prime orme sulla coltre soffice.",
            ['Neve', 'Bianco', 'Freddo', 'Pupazzo', 'Ghiaccio'],
            ['Manto', 'Orme', 'Silenzio', 'Magia', 'Inverno']
        ),
        (
            'Il lombrico che scava la terra',
            "Vedi un lombrico strisciare nell'orto dopo la pioggia. Spiega a chi ha schifo che i lombrichi rendono la terra fertile e soffice.",
            ['Lombrico', 'Schifo', 'Terra', 'Verme', 'Strisciare'],
            ['Orto', 'Fertile', 'Tunnel', 'Aiuto', 'Natura']
        ),
        (
            'La lucciola nella notte estiva',
            "Una lucina verde vola nell'erba alta della sera. Descrivi lo stupore di vedere una stella vivente che illumina il buio del prato.",
            ['Lucciola', 'Luce', 'Buio', 'Notte', 'Prendere'],
            ['Lanterina', 'Magia', 'Volare', 'Prato', 'Stupore']
        ),
        (
            'Il sasso liscio del torrente',
            "Raccogli un ciottolo levigato dall'acqua del ruscello. Spiega come la pazienza dell'acqua abbia trasformato una pietra spigolosa in una gemma liscia.",
            ['Sasso', 'Fiume', 'Acqua', 'Liscio', 'Pietra'],
            ['Pazienza', 'Levigato', 'Corrente', 'Tempo', 'Morbido']
        ),
        (
            "L'arcobaleno dopo la tempesta",
            'Il sole buca i nuvoloni neri e appare un grande arco colorato. Spiega perché la pioggia è necessaria per far risplendere i colori del cielo.',
            ['Arcobaleno', 'Pioggia', 'Sole', 'Colori', 'Cielo'],
            ['Riflesso', 'Tempesta', 'Speranza', 'Nuvole', 'Meraviglia']
        ),
        (
            'La formica che porta la briciola',
            "Guardi una minuscola formica che trascina una briciola tre volte più grande di lei. Fai un elogio della forza e dell'aiuto reciproco nel formicaio.",
            ['Formica', 'Briciola', 'Piccola', 'Pane', 'Lavoro'],
            ['Tenacia', 'Squadra', 'Formicaio', 'Carico', 'Collaborazione']
        ),
        (
            "Il profumo dell'erba tagliata",
            "Il giardiniere ha falciato il prato della scuola. Descrivi il profumo fresco dell'erba che ricorda le corse spensierate dell'estate.",
            ['Erba', 'Tagliare', 'Odore', 'Prato', 'Verde'],
            ['Profumo', 'Freschezza', 'Estate', 'Terra', 'Spensieratezza']
        ),
        (
            'La conchiglia che tiene il rumore del mare',
            "Appoggi una grande conchiglia all'orecchio. Racconta a un amico come sembra di ascoltare le onde che si infrangono sulla spiaggia.",
            ['Conchiglia', 'Orecchio', 'Mare', 'Rumore', 'Spiaggia'],
            ['Onde', 'Sussurro', 'Marea', 'Ricordo', 'Abisso']
        ),
        (
            "L'ombra fresca della grande quercia",
            'In una giornata afosa ti ripari sotto le fronde di un albero secolare. Ringrazia la pianta per il fresco dono del suo riparo.',
            ['Caldo', 'Sole', 'Albero', 'Ombra', 'Sudare'],
            ['Rifugio', 'Fronde', 'Frescura', 'Quercia', 'Ristoro']
        ),
        (
            'Il rispetto per i nidi sugli alberi',
            'Un compagno vuole toccare un nido con le uova celestine. Fermalo spiegando che la mamma uccello potrebbe abbandonare i suoi piccoli.',
            ['Nido', 'Uova', 'Toccare', 'Rami', 'Uccello'],
            ['Protezione', 'Mamma', 'Calore', 'Schiusa', 'Rispetto']
        ),
        (
            "La bicicletta invece dell'auto",
            "Chiedi al papà di andare a scuola in bicicletta anziché in macchina. Spiegagli come pedalare faccia bene al cuore e tenga l'aria pulita.",
            ['Bici', 'Macchina', 'Fretta', 'Pedalare', 'Puzzolente'],
            ['Aria pulita', 'Salute', 'Pedali', 'Vento sul viso', 'Passeggiata']
        ),
        (
            'Il saluto al sole che tramonta',
            'Guardi il sole rosso che scende dietro le montagne. Esprimi la gratitudine per la luce che ha scaldato la giornata e prepara la notte serena.',
            ['Sole', 'Rosso', 'Tramonto', 'Montagna', 'Buio'],
            ['Gratitudine', 'Orizzonte', 'Calore', 'Serenità', 'Riposo']
        ),
    ],
    "a2": [
        (
            'Il termometro del pianeta: la febbre della Terra',
            "Spiega ai tuoi compagni l'effetto serra usando la metafora di una coperta troppo pesante che fa salire la temperatura globale.",
            ['Caldo', 'Terra', 'Gradi', 'Febbre', 'Sole'],
            ['Effetto serra', 'Atmosfera', 'Surriscaldamento', 'Coperta termica', 'Equilibrio']
        ),
        (
            "L'isola di plastica nell'oceano",
            'Racconta il dramma del Pacific Trash Vortex: milioni di tonnellate di rifiuti che soffocano pesci e tartarughe a migliaia di chilometri da noi.',
            ['Plastica', 'Mare', 'Isola', 'Pesci', 'Spazzatura'],
            ['Pacific Trash Vortex', 'Microplastiche', 'Biodiversità marina', 'Soffocamento', 'Responsabilità']
        ),
        (
            "L'orto didattico a scuola: imparare dalla zappa",
            'Presenta il progetto per trasformare un angolo di cortile abbandonato in un orto di pomodori e carote curato dagli alunni.',
            ['Orto', 'Zappa', 'Verdura', 'Fango', 'Sporcarsi'],
            ['Auto-produzione', 'Pazienza stagionale', 'Cura della terra', 'Raccolto comune', 'Nutrimento']
        ),
        (
            "L'estinzione delle api e la catena alimentare",
            "Se le api scomparissero dalla faccia della terra, all'uomo resterebbero quattro anni di vita. Commenta il monito attribuito a Einstein.",
            ['Api', 'Miele', 'Einstein', 'Uccidere', 'Insetti'],
            ['Impollinazione', 'Sicurezza alimentare', 'Catena trofica', 'Ecosistema fragile', 'Custodia']
        ),
        (
            'Lo spreco di cibo nella mensa scolastica',
            'Ogni giorno tonnellate di pane e frutta intatta finiscono nella spazzatura. Proponi un piano per redistribuire le porzioni avanzate.',
            ['Cibo', 'Mensa', 'Buttare', 'Pane', 'Fame'],
            ['Spreco alimentare', 'Porzioni etiche', 'Ridistribuzione', 'Rispetto del nutrimento', 'Beni primari']
        ),
        (
            "Le borracce d'acciaio contro l'usa e getta",
            "Convinci l'istituto scolastico a eliminare le bottigliette di plastica dai distributori automatici regalando una borraccia a ogni studente.",
            ['Bottiglie', 'Plastica', 'Macchinette', 'Borraccia', 'Comprare'],
            ['Riuso permanente', 'Abolizione monouso', 'Impronta ecologica', 'Acqua pubblica', 'Sostenibilità']
        ),
        (
            'La tartaruga salvata dalla rete da pesca',
            'Sei un volontario del centro recupero fauna marina. Racconta il salvataggio di una tartaruga impigliata in una rete fantasma.',
            ['Tartaruga', 'Rete', 'Pescatore', 'Mare', 'Plastica'],
            ['Rete fantasma', 'Pronto soccorso marino', 'Liberazione', 'Fondali', 'Salvataggio']
        ),
        (
            "L'invasione del cemento e la perdita dei prati",
            "Nel tuo quartiere vogliono abbattere un boschetto per costruire un nuovo parcheggio. Difendi l'area verde davanti alla giunta comunale.",
            ['Parcheggio', 'Cemento', 'Alberi', 'Tagliare', 'Macchine'],
            ['Polmone verde', 'Permeabilità del suolo', 'Isola di calore', 'Vivibilità urbana', 'Presidio ecologico']
        ),
        (
            "L'energia invisibile del vento: i parchi eolici",
            'Spiega come il soffio del vento possa girare gigantesche pale bianche per accendere la luce di intere città senza bruciare carbone.',
            ['Vento', 'Pale', 'Luce', 'Carbone', 'Elettricità'],
            ['Energia rinnovabile', 'Parco eolico', 'Transizione pulita', 'Turbina', 'Sostenibilità']
        ),
        (
            'La deforestazione spiegata attraverso la casa degli orango',
            "Mostra come l'acquisto sconsiderato di prodotti con olio di palma non certificato distrugga le foreste pluviali della Malesia.",
            ['Orango', 'Foresta', 'Olio di palma', 'Tagliare', 'Animali'],
            ['Deforestazione', 'Habitat naturale', 'Consumo critico', 'Foresta pluviale', 'Specie minacciate']
        ),
        (
            "La raccolta dell'acqua piovana per i giardini",
            'Proponi di installare cisterne sul tetto della scuola per recuperare la pioggia e innaffiare le aiuole durante i mesi estivi.',
            ['Pioggia', 'Tetto', 'Tubo', 'Innaffiare', 'Acqua'],
            ['Bacino di raccolta', 'Risorsa idrica', 'Irrigazione sostenibile', 'Cisterna', 'Risparmio']
        ),
        (
            'Il silenzio degli orsi polari senza ghiaccio',
            'Descrivi la fatica di una madre orsa che deve nuotare per centinaia di chilometri perché la banchisa polare si scioglie troppo in fretta.',
            ['Orso polare', 'Ghiaccio', 'Nuotare', 'Polo Nord', 'Caldo'],
            ['Banchisa artica', 'Fusione dei ghiacci', 'Rifugiati ecologici', 'Fauna polare', 'Dramma climatico']
        ),
        (
            'Il compostaggio della frazione organica',
            'Dimostra come bucce di mela e fondi di caffè possano trasformarsi in terriccio nero e profumato per i fiori della scuola.',
            ['Bucce', 'Caffè', 'Puzza', 'Spazzatura', 'Marcire'],
            ['Compostaggio naturale', 'Humus fertile', 'Ciclo della materia', 'Decomposizione', 'Nutrimento del suolo']
        ),
        (
            'La mobilità sostenibile: il Pedibus scolastico',
            'Presenta il progetto del pedibus: una carovana di bambini che va a scuola a piedi accompagnata da genitori volontari.',
            ['Macchina', 'Fretta', 'Smog', 'Camminare', 'Accompagnare'],
            ['Pedibus', 'Mobilità dolce', 'Autonomia infantile', 'Aria pulita', 'Socialità urbana']
        ),
        (
            "L'inquinamento luminoso e la scomparsa delle stelle",
            "I lampioni stradali mal progettati illuminano il cielo cancellando la via lattea. Chiedi un'illuminazione rivolta solo verso il basso.",
            ['Lampione', 'Luce', 'Stelle', 'Notte', 'Vedere'],
            ['Inquinamento luminoso', 'Volta celeste', 'Orientamento degli uccelli', 'Efficienza energetica', 'Meraviglia notturna']
        ),
        (
            'Il falò illegale delle campagne e la diossina',
            "Spiega perché bruciare sterpaglie e scarti di plastica nei campi avvelena l'aria che respiriamo e la verdura che mangiamo.",
            ['Bruciare', 'Fumo', 'Campagna', 'Fuoco', 'Puzza'],
            ['Fumi tossici', 'Diossina', "Qualità dell'aria", 'Tossicità agricola', 'Smaltimento corretto']
        ),
        (
            'La moda veloce (Fast Fashion) e i fiumi colorati',
            'Mostra come comprare magliette da tre euro ogni settimana inquini fiumi lontani con tinture chimiche tossiche.',
            ['Maglietta', 'Vestiti', 'Negozio', 'Pochi soldi', 'Comprare'],
            ['Fast fashion', 'Scarichi industriali', 'Sostenibilità tessile', 'Durabilità dei capi', 'Consumo etico']
        ),
        (
            'I parchi nazionali come santuari della vita',
            "Descrivi una visita al Parco Nazionale d'Abruzzo tra camosci e faggi secolari: la natura lasciata libera di prosperare.",
            ['Parco', 'Abruzzo', 'Animali', 'Guardie', 'Gita'],
            ['Santuario ecologico', 'Tutela integrale', 'Ecosistema protetto', 'Fauna appenninica', 'Patrimonio naturale']
        ),
        (
            'La riparazione delle cose rotte contro lo spreco',
            'Organizza un Repair Café nella palestra della scuola dove aggiustare giocattoli, sedie e tostapane invece di buttarli.',
            ['Rotto', 'Buttare', 'Nuovo', 'Aggiustare', 'Comprare'],
            ['Cultura della riparazione', 'Repair café', 'Allungare la vita degli oggetti', "Contrasto all'usa e getta", 'Manualità']
        ),
        (
            'Il patto tra le generazioni per la Terra',
            "Concludi il festival della sostenibilità con un discorso solenne: non abbiamo ereditato la Terra dai nostri padri, l'abbiamo presa in prestito dai nostri figli.",
            ['Nostra', 'Terra', 'Padri', 'Futuro', 'Mondo'],
            ['Prestito generazionale', 'Custodia ecologica', 'Eredità comune', 'Patto climatico', 'Speranza operosa']
        ),
    ],
    "b1": [
        (
            'La fusione dei ghiacciai alpini: il gigante ferito',
            'Dalla Marmolada al Monte Bianco, i ghiacciai millenari arretrano di decine di metri ogni estate. Esponi il referto clinico delle nostre montagne.',
            ['Ghiaccio', 'Montagna', 'Marmolada', 'Caldo', 'Acqua'],
            ['Fusione criosferica', 'Arretramento glaciale', 'Riserva idrica alpina', 'Crisi idrologica', 'Testimone climatico']
        ),
        (
            'La desertificazione delle pianure meridionali',
            "La siccità prolungata e lo sfruttamento intensivo delle falde stanno trasformando intere regioni in paesaggi semidesertici. Lancia l'allarme siccità.",
            ['Siccità', 'Acqua', 'Pozzo', 'Sud', 'Pioggia'],
            ['Desertificazione', 'Stress idrico', 'Erosione dei suoli', 'Salinizzazione delle falde', 'Gestione della risorsa']
        ),
        (
            'I giovani dei Fridays for Future e lo sciopero per il clima',
            'Difendi la legittimità morale degli scioperi scolastici per il clima: quando il futuro è a rischio, la protesta diventa la lezione più importante.',
            ['Sciopero', 'Greta', 'Scuola', 'Cartelli', 'Venerdì'],
            ['Attivismo climatico', 'Giustizia climatica', 'Coscienza generazionale', 'Appello alla scienza', 'Mobilitazione globale']
        ),
        (
            'La sesta estinzione di massa della biodiversità',
            "A differenza delle precedenti cinque estinzioni causate da meteoriti o vulcani, questa è provocata da una singola specie: l'Homo sapiens.",
            ['Animali', 'Morti', 'Estinzione', 'Uomo', 'Dinosauri'],
            ['Antropocene biologico', 'Sesta estinzione', 'Tasso di scomparsa', 'Frammentazione ecologica', 'Integrità ecosistemica']
        ),
        (
            "Il Greenwashing delle multinazionali dell'energia",
            "Spot pubblicitari con foreste verdi e cascate limpide finanziati da colossi del petrolio. Smaschera l'ipocrisia del marketing ecologico di facciata.",
            ['Spot', 'Pubblicità', 'Verde', 'Petrolio', 'Bugie'],
            ['Greenwashing', 'Cosmesi ecologica', 'Impronta fossile', 'Trasparenza aziendale', 'Responsabilità reale']
        ),
        (
            "L'acidificazione degli oceani e la morte dei coralli",
            "L'eccesso di CO2 assorbito dai mari rende l'acqua acida, sciogliendo gli scheletri calcarei delle barriere coralline. Delinea la tragedia sottomarina.",
            ['Coralli', 'Mare', 'Acido', 'Pesci', 'Bianco'],
            ['Acidificazione oceanica', 'Sbiancamento dei coralli', 'Biomineralizzazione', 'Polmone blu del pianeta', 'Catena trofica']
        ),
        (
            "L'impronta idrica invisibile: quanta acqua mangiamo?",
            "Per produrre un chilo di carne bovina servono quindicimila litri d'acqua. Spiega ai compagni il concetto di acqua virtuale incorporata nei consumi.",
            ['Carne', 'Hamburger', 'Litri', 'Acqua', 'Mangiare'],
            ['Acqua virtuale', 'Impronta idrica', 'Zootecnia intensiva', 'Efficienza calorica', 'Dieta sostenibile']
        ),
        (
            "L'economia circolare contro il modello lineare prendi-usa-getta",
            "Illustra il modello economico circolare: scarti che diventano materie prime seconde per azzerare l'estrazione e il rifiuto finale.",
            ['Rifiuti', 'Comprare', 'Buttare', 'Fabbrica', 'Monouso'],
            ['Economia circolare', 'Materia prima seconda', 'Ecodesign', 'Ciclo a cascata', 'Rigenerazione']
        ),
        (
            "La transizione energetica e l'abbandono delle fonti fossili",
            'Carbone, petrolio e gas naturale hanno costruito la modernità ma ne minacciano la sopravvivenza. Difendi il passaggio radicale a sole, vento e geotermia.',
            ['Petrolio', 'Carbone', 'Gas', 'Fumo', 'Centrale'],
            ['Decarbonizzazione', 'Transizione ecologica', 'Fonti fossili', 'Fonti rinnovabili', 'Mix energetico']
        ),
        (
            "L'impatto dei trasporti aerei e la vergogna di volare (Flygskam)",
            'Un singolo volo a lungo raggio produce più emissioni di quante un individuo ne dovrebbe emettere in un anno. Riapri la riflessione sui treni notturni.',
            ['Aereo', 'Volare', 'Treno', 'Biglietto', 'Vacanze'],
            ['Flygskam', 'Intensità carbonica del volo', 'Rete ferroviaria', 'Turismo lento', 'Consapevolezza cinetica']
        ),
        (
            "Il cemento che divora l'Italia: il rapporto ISPRA",
            'Due metri quadrati di suolo naturale sigillati dal cemento ogni secondo in Italia. Denuncia la vulnerabilità al dissesto idrogeologico che ne consegue.',
            ['Cemento', 'Costruire', 'Fango', 'Alluvione', 'Case'],
            ['Consumo di suolo', 'Sigillatura impermeabile', 'Dissesto idrogeologico', 'Rapporto ISPRA', 'Rigenerazione urbana']
        ),
        (
            "L'agricoltura biologica versus l'abuso di pesticidi",
            'I fitofarmaci chimici avvelenano le falde e sterminano gli insetti utili. Sostieni la riconversione agroecologica per la salute dei campi e delle persone.',
            ['Pesticidi', 'Chimica', 'Veleno', 'Mele', 'Campi'],
            ['Agroecologia', 'Coltivazione biologica', 'Sovranità alimentare', 'Fitofarmaci sistemici', 'Salute del microbiota']
        ),
        (
            'La riforestazione urbana per abbattere le isole di calore',
            "Nelle metropolitane d'asfalto le temperature estive superano i quaranta gradi. Proponi la piantumazione di boschi urbani per raffrescare i quartieri.",
            ['Caldo', 'Asfalto', 'Città', 'Alberi', 'Condizionatore'],
            ['Isole di calore urbane', 'Foresta metropolitana', 'Ombreggiamento naturale', 'Evapotraspirazione', 'Resilienza climatica']
        ),
        (
            'Il traffico delle navi da crociera nei centri storici',
            'Giganti galleggianti alti come condomini che navigano a pochi metri dai palazzi storici di Venezia. Chiedi la salvaguardia definitiva delle lagune.',
            ['Crociera', 'Venezia', 'Turisti', 'Giganti', 'Laguna'],
            ['Impatto idrodinamico', 'Ecosistema lagunare', 'Inquinamento da nafta pesante', 'Vulnerabilità monumentale', 'Turismo sostenibile']
        ),
        (
            'La giustizia climatica e i rifugiati ambientali',
            'Popolazioni insulari del Pacifico e contadini del Sahel costretti a fuggire perché la loro terra è sommersa o inaridita. Esigi il loro riconoscimento legale.',
            ['Migranti', 'Mare sale', 'Fuggire', 'Poveri', 'Africa'],
            ['Rifugiati climatici', 'Giustizia ambientale globale', 'Debito ecologico', 'Spostamento forzato', "Diritto d'asilo ecologico"]
        ),
        (
            "L'inquinamento acustico sottomarino e il disorientamento dei cetacei",
            'I sonar militari e i motori navali creano un inferno sonoro negli abissi, spingendo capodogli e balene a spiaggiarsi disorientati. Denuncialo.',
            ['Balene', 'Sonar', 'Spiaggia', 'Rumore', 'Navi'],
            ['Inquinamento acustico sottomarino', 'Bioacustica marina', 'Disorientamento dei cetacei', 'Spiaggiamento di massa', 'Corridoi blu']
        ),
        (
            'La valorizzazione delle comunità energetiche rinnovabili',
            'Cittadini, scuole e piccole imprese che si uniscono per produrre e scambiare energia solare a chilometro zero. Delinea la democrazia energetica.',
            ['Pannelli solari', 'Bolletta', 'Insieme', 'Corrente', 'Tetto'],
            ['Comunità energetica rinnovabile', 'Autoconsumo collettivo', "Democrazia dell'energia", 'Decentralizzazione della rete', 'Solidarietà energetica']
        ),
        (
            'Il contrasto agli incendi boschivi dolosi',
            "Ogni estate migliaia di ettari di macchia mediterranea vengono inceneriti dalla speculazione o dall'incuria. Esigi pene severe e videosorveglianza satellitare.",
            ['Fuoco', 'Bruciare', 'Pompieri', 'Piromani', 'Cenere'],
            ['Incendi boschivi dolosi', 'Speculazione fondiaria', 'Telerilevamento satellitare', 'Perdita di biomassa', 'Ricostituzione forestale']
        ),
        (
            "La tutela delle zone umide e l'accordo di Ramsar",
            'Paludi, acquitrini e torbiere assorbono più carbonio di tutte le foreste della terra e depurano le acque. Difendi questi ecosistemi sottovalutati.',
            ['Palude', 'Fango', 'Zanzare', 'Bonifica', 'Uccelli'],
            ['Zone umide protette', 'Convenzione di Ramsar', 'Pozzi di assorbimento del carbonio', 'Depurazione naturale', 'Avifauna migratoria']
        ),
        (
            'Il giuramento per la Terra dei giovani oratori',
            'Pronuncia una dichiarazione solenne di fedeltà al pianeta: non saremo la generazione che ha guardato altrove mentre la casa comune bruciava.',
            ['Fine', 'Pianeta', 'Promessa', 'Guardare altrove', 'Brucia'],
            ['Custodia della biosfera', 'Giuramento solenne', 'Responsabilità generazionale', 'Casa comune', 'Azione radicale']
        ),
    ],
    "b2": [
        (
            "L'antropocene: l'uomo come forza geologica trainante",
            "Analizza la definizione di Paul Crutzen: l'umanità ha impresso strati di plastica e isotopi radioattivi nella roccia, aprendo una nuova epoca geologica.",
            ['Crutzen', 'Antropocene', 'Geologia', 'Roccia', 'Uomo'],
            ['Forza geologica globale', 'Firma antropica stratigrafica', 'Grande accelerazione', 'Frattura metabolica', 'Epoca geologica']
        ),
        (
            'La tragedia dei beni comuni di Garrett Hardin',
            "Quando una risorsa naturale (pascolo, mare, atmosfera) è ad accesso libero, l'interesse egoistico individuale porta alla rovina collettiva. Confutalo o confermalo.",
            ['Hardin', 'Pascolo', 'Mio', 'Rovina', 'Pecore'],
            ['Tragedy of the commons', 'Libero accesso distruttivo', 'Governance dei beni comuni', 'Elinor Ostrom', 'Regolazione cooperativa']
        ),
        (
            'Il debito ecologico tra Nord e Sud del pianeta',
            "I paesi industrializzati occidentali hanno consumato l'ottanta per cento del carbon budget globale, ma a subire le peggiori catastrofi sono i paesi poveri.",
            ['Poveri', 'Ricchi', 'Colpa', 'Soldi', 'Inquinare'],
            ['Debito ecologico storico', 'Carbon budget planetario', 'Ingiustizia climatica asimmetrica', 'Riparazioni ambientali', 'Loss and Damage fund']
        ),
        (
            'I Tipping Point del sistema climatico globale',
            'Dalla fusione del permafrost siberiano al collasso della circolazione atlantica (AMOC): spiega i punti di non ritorno che rischiano di innescare un effetto domino incontrollabile.',
            ['Punto di non ritorno', 'Domino', 'Permafrost', 'Metano', 'Ghiaccio'],
            ['Punti di non ritorno (Tipping Points)', 'Rilascio del clatrato di metano', "Inversione dell'AMOC", 'Cascata di feedback positivo', 'Instabilità non lineare']
        ),
        (
            "L'illusione del disaccoppiamento (Decoupling) e la crescita verde",
            "È davvero possibile far crescere il PIL all'infinito riducendo l'uso materiale di risorse ed energia? Dibatti i limiti intrinseci della Green Economy.",
            ['PIL', 'Crescere', 'Verde', 'Soldi', 'Economia'],
            ['Disaccoppiamento assoluto vs relativo', 'Limiti termodinamici', 'Post-crescita ecologica', 'Paradosso di Jevons', 'Materialismo bioeconomico']
        ),
        (
            "L'ecocidio come crimine contro l'umanità nel diritto penale",
            "Sostieni l'introduzione dell'ecocidio nello Statuto di Roma: la distruzione sistematica e permanente di un ecosistema deve essere punita dall'Aja.",
            ['Ecocidio', 'Aja', 'Prigione', 'Distruggere la natura', 'Reato'],
            ["Giurisdizione penale sull'ecocidio", 'Crimini contro la biosfera', 'Statuto di Roma integrato', 'Soggettività giuridica degli ecosistemi', 'Deterrenza ecologica']
        ),
        (
            'La cattura e lo stoccaggio del carbonio (CCS): soluzione o alibi?',
            'Le tecnologie di iniezione sotterranea della CO2 vengono promosse dalle compagnie petrolifere per continuare a estrarre idrocarburi. Denunciane i costi e i rischi.',
            ['CCS', 'Catturare CO2', 'Sottoterra', 'Petrolio', 'Soluzione'],
            ['Tecno-ottimismo consolatorio', 'Sequestro geologico incerto', 'Intensità energetica parassita', 'Moratoria fossile', 'Efficienza sistemica']
        ),
        (
            'Il declino della biodiversità agricola e i brevetti sui semi',
            'Quattro multinazionali controllano oltre il sessanta per cento del mercato globale delle sementi brevettate. Difendi i semi antichi e la sovranità contadina.',
            ['Semi', 'Multinazionali', 'Brevetti', 'Contadini', 'Grano'],
            ['Monopolio sementiero', 'Biodiversità agricola', 'Sementi open source', 'Sovranità contadina', 'Vandana Shiva']
        ),
        (
            "Il paradosso dell'idrogeno: verde, blu o grigio?",
            "Distingui l'idrogeno prodotto da elettrolisi alimentata da fonti rinnovabili da quello estratto dal metano con rilascio di carbonio. Fai chiarezza scientifica.",
            ['Idrogeno', 'Colori', 'Auto a idrogeno', 'Pulito', 'Metano'],
            ['Idrogeno verde da elettrolisi', 'Idrogeno grigio e blu', 'Resa termodinamica', 'Vettore energetico', 'Decarbonizzazione industriale']
        ),
        (
            "L'impatto geopolitico delle Terre Rare e del litio",
            'La transizione verde richiede quantità colossali di cobalto, litio e neodimio, aprendo nuove rotte di estrattivismo neo-coloniale in Africa e Sudamerica.',
            ['Litio', 'Batterie', 'Miniere', 'Cina', 'Africa'],
            ['Estrattivismo neo-coloniale', 'Terre rare e geopolitica', 'Corsa ai minerali critici', 'Triangolo del litio', 'Impatto minerario']
        ),
        (
            'La sesta conferenza delle parti (COP): successi o passerella diplomatica?',
            "Analizza le conclusioni dell'ultimo summit ONU sul clima: accordi al ribasso e veti incrociati delle lobby petrolifere. Proponi un multilateralismo vincolante.",
            ['COP', 'Summit', 'Discorsi', 'Accordo', 'Lobby'],
            ['Multilateralismo climatico vincolante', 'Veto dei paesi fossili', 'Dichiarazioni non vincolanti', 'Accordo di Parigi (1.5°C)', 'Mobilitazione dal basso']
        ),
        (
            "L'ingegneria solare e la geoingegneria planetaria",
            'Irrorare solfati nella stratosfera per riflettere i raggi solari o sbiancare le nuvole. Metti in guardia dagli imprevedibili effetti collaterali sui monsoni.',
            ['Riflettere il sole', 'Aerosol', 'Cielo', 'Esperimento', 'Fermare il caldo'],
            ['Solar radiation management', 'Geoingegneria stratosferica', 'Alterazione dei regimi monsonici', 'Azzardo morale planetario', 'Governance globale del clima']
        ),
        (
            'Il consumo critico e il boicottaggio come armi democratiche',
            'Spiega come il portafoglio dei cittadini sia una scheda elettorale permanente: premiare le filiere eque e boicottare i brand predatori cambia i mercati.',
            ['Boicottare', 'Comprare', 'Supermercato', 'Soldi', 'Marchio'],
            ['Consumo critico consapevole', 'Voto con il portafoglio', 'Filiere trasparenti', 'Disinvestimento dai fossili', 'Pressione dal basso']
        ),
        (
            "L'abbandono delle zone interne e il ritorno alla terra",
            "Mentre le megalopoli implodono nel traffico e nell'inquinamento, i borghi montani si spopolano. Delinea un manifesto per la rinascita dell'Appennino.",
            ['Borghi', 'Montagna', 'Case vuote', 'Giovani', 'Città'],
            ['Restanza comunitaria', 'Rigenerazione rurale', 'Presidio territoriale attivo', 'Agricoltura di montagna', "Cura dell'entroterra"]
        ),
        (
            "L'energia nucleare di quarta generazione nel dibattito della transizione",
            'I reattori modulari a fissione avanzata possono garantire energia di base a zero emissioni o costituiscono ancora un rischio inaccettabile di scorie e costi?',
            ['Nucleare', 'Scorie', 'Chernobyl', 'Atomo', 'Uranio'],
            ['Fissione nucleare di IV generazione', 'Reattori modulari (SMR)', 'Proliferazione e scorie millenarie', 'Costi di de-commissioning', 'Carico di base a zero carbonio']
        ),
        (
            'La transizione ecologica giusta (Just Transition)',
            'Non si può chiedere ai lavoratori delle acciaierie o delle centrali a carbone di pagare da soli il prezzo della chiusura. Delinea le garanzie salariali e formative necessarie.',
            ['Operai', 'Chiudere la fabbrica', 'Lavoro perso', 'Inquinamento', 'Taranto'],
            ['Just Transition', 'Riconversione ecologica del lavoro', 'Protezione salariale e riqualificazione', 'Caso ILVA Taranto', 'Giustizia sociale e climatica']
        ),
        (
            'La biofilia di Edward O. Wilson: la nostra affinità innata con il vivente',
            "Illustra la tesi dell'entomologo di Harvard: l'essere umano ha una necessità evolutiva biologica di connettersi con la natura per non ammalarsi nell'anima.",
            ['Wilson', 'Biofilia', 'Amore per la natura', 'Città', 'Malinconia'],
            ['Ipotesi della biofilia', 'Connessione evolutiva innata', 'Architettura biofilica', 'Dissonanza urbana', 'Affinità ancestrale']
        ),
        (
            'Il diritto del mare e la corsa mineraria negli abissi (Deep Sea Mining)',
            'Robot sottomarini pronti a scavare il fondale oceanico profondo per estrarre noduli polimetallici. Chiedi una moratoria globale per difendere gli abissi inesplorati.',
            ['Fondale', 'Robot', 'Scavare', 'Metalli', 'Abissi'],
            ['Deep sea mining', 'Noduli polimetallici', 'Moratoria internazionale', 'Distruzione dei fondali vergini', 'Beni comuni oceanici']
        ),
        (
            "La carne coltivata in laboratorio e il futuro dell'alimentazione",
            'Proteine prodotte da colture cellulari senza macellazione animale e con il novanta per cento in meno di suolo e acqua. Affronta il tabù culturale contro la sostenibilità.',
            ['Carne sintetica', 'Laboratorio', 'Schifo', 'Mucca', 'Tradizione'],
            ['Agricoltura cellulare', 'Carne coltivata', 'Riduzione del consumo di suolo', 'Benessere animale radicale', 'Transizione proteica']
        ),
        (
            "L'appello alla Terra Vivente: il risveglio della coscienza ecologica",
            "Pronuncia un'orazione appassionata che squarci il velo dell'indifferenza: la Terra non ha bisogno dell'uomo, è l'uomo che non può esistere senza la Terra.",
            ['Uomo al centro', 'Natura serve a noi', 'Salvare il mondo', 'Distruzione', 'Fine'],
            ['Autonomia della biosfera', "Riconoscimento dell'interdipendenza", 'Umiltà cosmica', 'Canto della Terra vivente', 'Rinascita ecologica']
        ),
    ],
    "c1": [
        (
            "L'ecologia profonda di Arne Naess e l'egualitarismo biosferico",
            "Esporrai la distinzione tra l'ecologia di superficie antropocentrica e l'ecologia profonda (Deep Ecology) che riconosce valore intrinseco a ogni forma di vita.",
            ['Naess', 'Ecologia profonda', 'Uomo', 'Valore', 'Natura'],
            ['Egualitarismo biosferico', 'Valore intrinseco non strumentale', 'Realizzazione del Sé cosmico', "Decostruzione dell'antropocentrismo", 'Olismo ecologico']
        ),
        (
            "Il principio di responsabilità di Hans Jonas e l'euristica della paura",
            "Dimostra come la mutata natura dell'agire umano, dotato di potere di auto-annientamento tecnologico, esiga una nuova etica orientata alla vulnerabilità del futuro.",
            ['Jonas', 'Futuro', 'Paura', 'Tecnica', 'Responsabilità'],
            ['Euristica della paura', 'Imperativo categorico jonasiano', "Integrità dell'essenza umana", 'Vulnerabilità planetaria', 'Asimmetria temporale']
        ),
        (
            "L'ipotesi Gaia di James Lovelock: la Terra come organismo autoregolato",
            "Illustra il modello geofisiologico: la biosfera, l'atmosfera e gli oceani cooperano ciberneticamente per mantenere costanti le condizioni ottimali per la vita.",
            ['Lovelock', 'Gaia', 'Terra viva', 'Organismo', 'Omeostasi'],
            ['Omeostasi geofisiologica', 'Cibernetica planetaria', 'Ipotesi Gaia lovelockiana', 'Accoppiamento biota-clima', 'Autopoiesi sistemica']
        ),
        (
            "L'antropocentrismo forte versus antropocentrismo debole in Bryan Norton",
            'Analizza il dibattito filosofico: è possibile fondare la salvaguardia ambientale sulla valorizzazione estetica e spirituale umana senza cadere nel biocentrismo assoluto?',
            ['Norton', 'Uomo', 'Estetica', 'Bello', 'Valore'],
            ['Antropocentrismo debole', 'Preferenze ponderate vs istintive', 'Educazione estetica della natura', 'Valore trasformativo', 'Pragmatismo ambientale']
        ),
        (
            "La bioeconomia di Nicholas Georgescu-Roegen e la legge dell'entropia",
            "Dimostra l'incompatibilità radicale tra la crescita economica illimitata e il secondo principio della termodinamica: ogni processo produttivo accelera l'entropia materiale.",
            ['Roegen', 'Entropia', 'Termodinamica', 'Crescita', 'Energia'],
            ['Bioeconomia termodinamica', 'Degradazione entropica irreversibile', 'Fondo versus flusso di risorse', 'Ineluttabilità del limite fisico', 'Decrescita metabolica']
        ),
        (
            "L'eco-marxismo e la frattura metabolica in John Bellamy Foster",
            "Rivisita la critica marxiana del capitale: la rottura irreparabile del ricambio organico (Stoffwechsel) tra uomo e suolo causata dall'urbanizzazione capitalistica.",
            ['Marx', 'Foster', 'Capitale', 'Campagna', 'Città'],
            ['Frattura metabolica del suolo', 'Stoffwechsel organico', 'Accumulazione originaria ecologica', 'Seconda contraddizione del capitale', 'Socialismo ecologico']
        ),
        (
            "L'etica della terra (Land Ethic) di Aldo Leopold",
            "Commenta l'assioma di A Sand County Almanac: Una cosa è giusta quando tende a preservare l'integrità, la stabilità e la bellezza della comunità biotica. È sbagliata altrimenti.",
            ['Leopold', 'Terra', 'Giusto e sbagliato', 'Bellezza', 'Comunità'],
            ['Land Ethic leopoldiana', 'Comunità biotica allargata', 'Da dominatore a membro biotico', 'Piramide ecologica', 'Coscienza ecologica']
        ),
        (
            "L'apologia della wilderness e la wilderness preservation in John Muir",
            "Difendi l'intoccabilità degli spazi selvaggi vergini non per il turismo o l'utilità economica, ma come templi cosmici dove l'essere si rivela nella sua purezza primigenia.",
            ['Muir', 'Wilderness', 'Parchi', 'Bello', 'Turismo'],
            ['Wilderness intatta', 'Spazio sacro primigenio', 'Preservazionismo radicale', 'Non-ingerenza antropica', 'Epifania naturale']
        ),
        (
            "L'ecofemminismo di Carolyn Merchant e la morte della natura",
            'Mostra come la rivoluzione scientifica seicentesca abbia trasformato la Terra da madre vivente e nutriente in macchina inerte da dominare e sfruttare col patriarcato.',
            ['Merchant', 'Donne', 'Madre Terra', 'Scienza', 'Macchina'],
            ['Ecofemminismo filosofico', 'Morte della natura vivente', 'Meccanicismo seicentesco', 'Dominio interconnesso donna-natura', 'Risacralizzazione olistica']
        ),
        (
            "I limiti dello sviluppo del Club di Roma cinquant'anni dopo",
            'Ripercorri il rapporto del MIT del 1972: le simulazioni matematiche sui limiti materiali planetari ignorate per decenni trovano oggi puntuale conferma nei dati climatici.',
            ['Club di Roma', '1972', 'Modelli', 'Limiti', 'Collasso'],
            ['The Limits to Growth', 'Dinamica dei sistemi computazionali', 'Collasso ecologico simulato', 'Cecità politico-economica', 'Validazione retrospettiva']
        ),
        (
            'Il paradosso della scarsità creata e i beni comuni in Vandana Shiva',
            "Come la privatizzazione dell'acqua e l'ingegneria genetica trasformino l'abbondanza naturale condivisa in scarsità artificiale a fini di profitto monopolistico.",
            ['Shiva', 'Acqua', 'Semi', 'Scarsità', 'Comprare'],
            ['Monopolio della vita', 'Scarsità artificiale imposta', 'Enclosure dei beni comuni', 'Biodiversità comunitaria', 'Democrazia della Terra']
        ),
        (
            "L'ingiustizia ambientale e il razzismo ambientale negli Stati Uniti",
            'Analizza come le discariche tossiche e gli inceneritori siano sistematicamente localizzati nei quartieri popolati da minoranze afroamericane e ispaniche.',
            ['Razzismo', 'Neri', 'Discarica', 'Quartiere', 'Veleni'],
            ['Razzismo ambientale sistemico', "Disparità d'esposizione tossica", 'Movimento per la giustizia ambientale', 'Vulnerabilità zonale discriminatoria', 'Equità territoriale']
        ),
        (
            "L'ecologia della liberazione e la teologia della creazione in Papa Francesco",
            "Commenta l'enciclica Laudato si': l'interconnessione indissolubile tra il grido della terra e il grido dei poveri contro la cultura dello scarto.",
            ['Papa', 'Laudato si', 'Chiesa', 'Poveri', 'Pianeta'],
            ['Ecologia integrale', 'Grido della terra e dei poveri', 'Cultura dello scarto', 'Conversione ecologica', 'Casa comune universale']
        ),
        (
            'La resilienza ecologica di Crawford S. Holling versus la stabilità rigida',
            "Distingui l'equilibrio ingegneristico fisso dalla resilienza sistemica: la capacità di un ecosistema di assorbire perturbazioni e mutare senza collassare.",
            ['Resilienza', 'Equilibrio', 'Cambiamento', 'Forte', 'Stabile'],
            ['Resilienza panarchica di Holling', 'Capacità adattativa sistemica', 'Fluttuazioni non lineari', 'Regimi multipli di stabilità', 'Vulnerabilità ecosistemica']
        ),
        (
            "L'antropologia oltre l'umano di Eduardo Kohn: come pensano le foreste",
            "Abbandona il provincialismo ontologico occidentale: esplora il pensiero dei segni e delle semiosi della foresta pluviale attraverso l'etnografia amazzonica.",
            ['Kohn', 'Foresta', 'Pensare', 'Indigeni', 'Segni'],
            ["Antropologia oltre l'umano", 'Semiosi non-umana vivente', 'Provincialismo linguistico', 'Risonanza trans-specifica', 'Cosmologia amazzonica']
        ),
        (
            'Il dilemma della conservazione fortezza (Fortress Conservation)',
            'Discuti la critica post-coloniale alla creazione di parchi nazionali che deportano le popolazioni indigene che avevano custodito quelle terre per millenni.',
            ['Indigeni', 'Cacciare via', 'Parco', 'Custodi', 'Terra'],
            ['Fortress conservation', 'Espulsione indigena ingiusta', 'Custodia ancestrale millenaria', 'Decolonizzazione ecologica', 'Co-gestione territoriale']
        ),
        (
            'La metabolizzazione urbana in David Harvey: la città come natura alterata',
            'Supera la falsa opposizione città/natura: ogni grattacielo e ogni fogna sono pura natura metabolizzata e riorganizzata dal capitale spaziale.',
            ['Harvey', 'Città', 'Natura', 'Cemento', 'Metabolismo'],
            ['Metabolismo socio-ecologico', 'Urbanizzazione della natura', 'Circolazione del capitale spaziale', 'Riconfigurazione geofisica', 'Ecologia politica urbana']
        ),
        (
            "L'etica del ripristino ecologico (Ecological Restoration) e la finzione dell'Eden",
            'È possibile ripristinare un ecosistema originario degradato o ogni ricostruzione umana è solo un giardino botanico artificiale privo di autenticità storica?',
            ['Restauro', 'Ricostruire', 'Naturale', 'Finto', 'Giardino'],
            ['Ripristino ecologico', 'Autenticità ontologica del paesaggio', "Mito dell'Eden incontaminato", 'Intenzionalità riparatrice', 'Successione ecologica guidata']
        ),
        (
            'Il diritto dei fiumi alla personalità giuridica: il caso Whanganui',
            'Commenta la legge neozelandese che ha riconosciuto il fiume Whanganui come entità vivente indivisibile titolare di diritti propri difesi dal popolo Maori.',
            ['Fiume', 'Nuova Zelanda', 'Maori', 'Persona', 'Legge'],
            ['Personalità giuridica fluviale', 'Whanganui Iwi cosmologia', 'Soggettività ecocentrica', 'Giurisprudenza della terra', 'Inseparabilità uomo-fiume']
        ),
        (
            "Il testamento per l'Oratore Ecologico: custode dell'Armonia Cosmica",
            "Pronuncia l'orazione che congeda il corso magistrale: farsi lingua e canto per tutte le specie mute, difendendo la bellezza del cosmo dall'oblio predatorio.",
            ['Voce', 'Muto', 'Difesa', 'Canto', 'Cosmo'],
            ["Voce dell'interezza cosmica", "Avvocato dell'inerme naturale", 'Canto della biodiversità', 'Patto indissolubile', 'Custodia sacrale']
        ),
    ],
    "c2": [
        (
            "L'ontologia della Physis presocratica contro la tecnica planetaria",
            "Delinea il contrasto metafisico originario tra la Physis come schiudersi spontaneo dell'essere in Eraclito ed Empedocle e la sua riduzione a materiale d'impiego tecnico.",
            ['Eraclito', 'Physis', 'Natura', 'Tecnica', 'Sfruttamento'],
            ['Physis autoctona originaria', "Schiudimento dell'essere", 'Poiesis contemplativa', "Profanazione dell'Origine", 'Custodia sacrale presocratica']
        ),
        (
            "L'aporia del Terricidio e la distruzione del legame cosmoteandrico",
            'Esamina il concetto sudamericano di Terricidio: la cancellazione simultanea della natura fisica, delle cosmologie indigene e della presenza spirituale sulla Terra.',
            ['Terricidio', 'Indigeni', 'Distruzione', 'Spirito', 'Mondo'],
            ['Crimine di Terricidio', 'Legame cosmoteandrico', 'Epistemicidio ontologico', 'Distruzione olistica', 'Resistenza ancestrale']
        ),
        (
            "Il sublime naturale kantiano e l'eccedenza smisurata della Natura",
            "Ripercorri la Critica del Giudizio: il sublime dinamico di fronte all'oceano in tempesta che umilia la nostra fragilità fisica esaltando la dignità morale dello spirito.",
            ['Sublime', 'Kant', 'Tempesta', 'Paura', 'Mare'],
            ['Sublime dinamico kantiano', 'Smisuratezza incommensurabile', 'Umiliazione della sensibilità', 'Trascendenza sovrasensibile', 'Dignità morale cosmica']
        ),
        (
            "La dialettica della catastrofe in Walter Benjamin: il freno d'emergenza",
            "Commenta la tesi rivoluzionaria: Marx diceva che le rivoluzioni sono il treno della storia, ma forse sono il tentativo dei passeggeri di tirare il freno d'emergenza.",
            ['Treno', "Freno d'emergenza", 'Marx', 'Benjamin', 'Progresso'],
            ["Freno d'emergenza messianico", 'Interruzione della catastrofe', 'Falsa necessità del progresso', 'Salvezza del vivente', 'Rivoluzione conservatrice']
        ),
        (
            "L'ontologia relazionale e il pluriverso zapatista di Arturo Escobar",
            "Confuta l'ontologia del Mondo Unico globale: difendi il Pluriverso, un mondo dove molti mondi siano possibili e coesistano in interdipendenza simbiotica.",
            ['Escobar', 'Mondo unico', 'Zapatisti', 'Pluriverso', 'Tutti uguali'],
            ['Ontologia relazionale simbiotica', 'Pluriverso cosmologico', 'Oltre il monismo moderno', 'Interdipendenza radicale', 'Eterogeneità ecologica']
        ),
        (
            "La morte della morte nell'era dell'estinzione globale",
            "Filosoficamente, la morte individuale è condizione del rinnovarsi della vita. Cosa accade quando l'estinzione sistemica cancella per sempre la possibilità stessa della nascita futura?",
            ['Morte', 'Estinzione', 'Nascita', 'Specie', 'Fine'],
            ['Morte del ciclo generativo', 'Estinzione come cesura ontologica', 'Perdita del futuro biologico', 'Lutto metafisico planetario', "Silenzio dell'evoluzione"]
        ),
        (
            'Il concetto di Natura naturans in Baruch Spinoza: Deus sive Natura',
            "Dimostra l'identità assoluta di Dio e della Natura: profanare un albero, un fiume o un animale significa letteralmente mutilare la sostanza infinita divina.",
            ['Spinoza', 'Dio', 'Natura', 'Sostanza', 'Albero'],
            ['Deus sive Natura', 'Natura naturans e naturata', 'Sostanza unica infinita', 'Panteismo monistico radicale', 'Amore intellettuale di Dio']
        ),
        (
            'La necropolitica ecologica e i sacrifici territoriali del capitale',
            "Attraverso Achille Mbembe, analizza la creazione di sacrifice zones: territori periferici deliberatamente condannati all'inquinamento letale per consentire il lusso delle metropoli centrali.",
            ['Mbembe', 'Necropolitica', 'Zona di sacrificio', 'Morte', 'Tossico'],
            ['Necropolitica ambientale', 'Sacrifice zones capitalistiche', 'Gestione della mortalità differenziale', 'Asservimento letale dello spazio', 'Imperialismo ecologico']
        ),
        (
            "La frattura del tempo geologico e l'iperoggetto di Timothy Morton",
            'Spiega la categoria di Iperoggetto: entità come il riscaldamento globale o il plutonio, così massivamente distribuite nel tempo e nello spazio da sfuggire alla nostra percezione sensoriale.',
            ['Morton', 'Iperoggetto', 'Plutonio', 'Clima', 'Vedere'],
            ['Iperoggetti distribuiti', 'Viscosità ontologica', "Ritiro dell'oggetto dalla presa", 'Interoggettività profonda', 'Sgomento fenomenologico']
        ),
        (
            "L'archetipo del Diluvio universale e la secolarizzazione dell'Apocalisse",
            "Dalla saga mesopotamica di Gilgamesh alla Genesi: l'archetipo dell'acqua purificatrice che cancella l'arroganza dell'uomo e il terrore moderno di un'apocalisse senza rinascita.",
            ['Diluvio', 'Noè', 'Arca', 'Acqua', 'Fine del mondo'],
            ['Archetipo diluviale primordiale', 'Hybris e catastrofe palingenetica', 'Apocalisse secolarizzata senza redenzione', 'Memoria mitica delle acque', 'Palingenesi cosmica']
        ),
        (
            "Il silenzio di Chernobyl e l'invisibilità del pericolo radiativo",
            'Evoca la zona di alienazione di Chernobyl: una natura che fiorisce rigogliosa e ingannevole mentre atomi invisibili e inodori distruggono il DNA delle cellule.',
            ['Chernobyl', 'Radiazioni', 'Atomo', 'Invisibile', 'Zona morta'],
            ['Invisibilità spettrale radiativa', 'Natura apparentemente incontaminata', 'Mutilazione del genoma', 'Spettralità tecnologica', 'Catastrofe pura']
        ),
        (
            "L'ecologia della mente di Gregory Bateson: il sacro come integrità epistemologica",
            "Dimostra come l'errore epistemologico di separare la mente dal corpo e l'uomo dalla natura generi la follia ecologica. Recupera la sacralità dei pattern che connettono.",
            ['Bateson', 'Mente', 'Sacro', 'Pensare', 'Separare'],
            ['Pattern che connette', 'Ecologia della mente', 'Unità epistemologica mente-natura', "Follia dell'antropocentrismo", 'Rigore sistemico e sacro']
        ),
        (
            'La decostruzione del concetto di Ambiente: oltre la dicotomia soggetto-oggetto',
            "Dimostra con Bruno Latour che la parola 'ambiente' è una trappola concettuale: presuppone che ci sia l'uomo al centro e il mondo intorno come mero sfondo scenografico.",
            ['Latour', 'Ambiente', 'Centro', 'Attorno', 'Uomo'],
            ['Rifiuto del concetto di ambiente', 'Collettivo di umani e non-umani', 'Parlamento delle cose', 'Simmetria ontologica', 'Rete socio-tecnica e naturale']
        ),
        (
            "L'impossibilità del lutto ecologico planetario",
            'Possiamo elaborare il lutto per una persona cara. Ma come può la psiche umana metabolizzare la scomparsa progressiva di ghiacciai, barriere coralline, stagioni e canti di uccelli?',
            ['Lutto', 'Piangere', 'Perdere la natura', 'Ghiacciai', 'Disperazione'],
            ['Solastalgia filosofica', 'Lutto ecologico inconsolabile', 'Melanconia planetaria', 'Trauma della perdita irreversibile', 'Tenacia della testimonianza']
        ),
        (
            'Il nomadismo ontologico e la riconciliazione con la terra aperta',
            "Pronuncia un'orazione sull'abbandono della stanzialità proprietaria e della recinzione fondiaria verso un nomadismo contemplativo che abita la Terra senza possederla.",
            ['Recinto', 'Proprietà', 'Terra mia', 'Muri', 'Fermarsi'],
            ['Abitare poetico laico', 'Nomadismo ontologico', 'Sottrarsi al dominio fondiario', 'Passo leggero sulla Terra', "Compiutezza dell'itineranza"]
        ),
        (
            "L'angoscia della tecnica e il dovere della diserzione produttivistica",
            "Di fronte all'apparato tecno-economico che consuma la biosfera ad accelerazione costante, teorizza il sabotaggio dell'immaginario e la diserzione dalla produzione.",
            ['Disertare', 'Lavoro', 'Fermare le macchine', 'Produzione', 'Sabotare'],
            ['Diserzione produttivistica', "Sabotaggio dell'immaginario capitalista", 'Potenza della sottrazione', 'Resistenza ontologica radicale', 'Inoperosità sacra']
        ),
        (
            'La liturgia del cosmo: il ritorno al sacro senza dogmi',
            "Formula una preghiera cosmica laica: il riconoscimento della sacralità intrinseca di ogni particella di materia, dal respiro della foglia all'esplosione delle supernovae.",
            ['Preghiera', 'Religione', 'Dio', 'Chiesa', 'Fede'],
            ['Ierofania cosmica laica', 'Intrinseca sacralità della materia', 'Stupore contemplativo originario', 'Sinfonia del vivente', 'Mistica immanente']
        ),
        (
            "L'apologia della notte stellata: contro l'antropizzazione della luce",
            "Rifletti sulla notte come orizzonte primordiale dove l'ego umano viene ridotto a polvere cosmica di fronte all'abisso vertiginoso degli anni luce.",
            ['Notte', 'Stelle', 'Luce artificiale', 'Piccoli', 'Cielo'],
            ['Vertigine siderale notturna', "Riduzione cosmica dell'ego", "Rivelazione dell'infinito", 'Commozione astronomica', 'Silenzio degli spazi eterni']
        ),
        (
            "La riconciliazione con il silenzio della roccia e dell'acqua",
            "Pronuncia una meditazione sublime sul tempo geologico profondo (Deep Time): la roccia millenaria che attende, incurante del passaggio frettoloso dell'uomo.",
            ['Roccia', 'Montagna', 'Tempo', 'Uomo passa', 'Pazienza'],
            ['Tempo profondo geologico (Deep Time)', 'Indifferenza sovrana della pietra', 'Lezione della lentezza litica', 'Pace incondizionata della materia', 'Orizzonte abissale']
        ),
        (
            "L'Inno alla Madre Terra: il congedo supremo dell'Oratore Cosmico",
            "Chiudi il magistero ecologico con un'orazione trionfale: la parola dell'uomo ritorna alla sorgente muta da cui è scaturita, piegando il capo in devozione perenne alla Vita.",
            ['Fine', 'Madre Terra', 'Parola', 'Morte', 'Uomo'],
            ['Inno alla Madre Terra', 'Congedo oratorio cosmico', 'Riconciliazione totale', "Silenzio dell'adorazione", 'Vittoria perenne della Vita']
        ),
    ],
}
