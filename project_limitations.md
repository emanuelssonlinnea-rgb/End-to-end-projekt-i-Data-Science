# Projektavgränsningar

För att genomföra projektet har vissa avvägningar och avgränsningar behövt vidtas, både gällande metodval och källdatan, som i slutändan påverkar hur resultatet av vår analys bör tolkas. Nedan följer en genomgång av de mest betydande besluten som tagits.

## Avgränsningar
### Data
Datan i projektet kommer från Arbetsförmedlingens jobbdatabas Platsbanken. Eftersom studien fokuserar på historiska jobbannonser från 2025 och 2026 hämtades datan från Arbetsförmedlingens Historical Job Ads API . API:et innehåller jobbannonser som inte längre är aktiva i Platsbanken.

Projektet omfattar därför inte annonser från andra jobbsajter eller rekryteringsplattformar. Resultaten speglar därmed de jobbannonser som publicerats i Platsbanken och kan inte antas representera samtliga lediga tjänster på den svenska arbetsmarknaden. Men eftersom merparten företag väljer att publicera sina annonser på platsbanken för god spridning så bör ändå annonser från platsbanken ge en relativt bra represenation av lediga tjänster på arbetsmarknaden. 

### Tidsperiod
Studieperioden avgränsades till 1 januari 2025–31 augusti 2026. Projektet genomförs under september och oktober 2026, vilket innebär att vissa annonser som publicerats under 2026 fortfarande kan vara aktiva och därför ännu inte finnas tillgängliga i Historical Job Ads API.

Detta innebär att framför allt de senare månaderna under 2026 kan innehålla färre annonser än motsvarande period 2025. Jämförelser mellan åren behöver därför göras med hänsyn till denna begränsning.

För att göra jämförelser mellan 2025 och 2026 mer rättvisande kan analyser som jämför åren direkt begränsas till samma månader, exempelvis januari–augusti för båda åren.

### Yrkesmässig avgränsning
Projektets ursprungliga mål var att undersöka vilka kompetenser som efterfrågas inom IT på den svenska arbetsmarknaden. På grund av projektets omfattning valde vi att avgränsa analysen till SSYK-gruppen 2511 - Systemanalytiker och IT-arkitekter m.fl. 

Gruppen omfattar bland annat yrken som Data Scientist, IT-arkitekt, kravanalytiker, systemanalytiker, systemarkitekt och verksamhetskonsult inom IT.

Enligt Arbetsförmedlingens Yrkesatlas arbetar dessa roller bland annat med utveckling av IT-system, IT-struktur och teknisk arkitektur samt med att säkerställa att IT-lösningar stödjer verksamhetens behov.

Avgränsningen minskar datamängden och gör det möjligt att genomföra en mer fokuserad analys inom projektets tidsram. Samtidigt innebär den att resultaten inte kan generaliseras till hela IT- och datasektorn. Resultaten bör i stället tolkas som en analys av kompetensefterfrågan inom den valda yrkesgruppen.

### Exkludering av "mjuka kompetenser"
För analysen valde vi godtyckligt att ta bort mjuka kompetenser, exempelvis serviceinriktning och stresstålighet, på grund av intresseområde och tidsbegränsningar i projektet. Det hade dock också varit intressant att undersöka hur inkluderingen av dessa kompetenser hade påverkat resultatet och om den hade gett en bredare bild av arbetsgivarnas förväntningar.

### Språk
På Platsbankens annonserar företag både på svenska och på engelska. På grund av begränsad tid att genomföra projektet och att spaCy använder sig av olika språkpaket för olika språk valde vi att avgränsa oss till att endast analysera annonser skrivna på svenska, således valde vi att helt exkludera annonser skrivna på engelska vid datakvalitetskontrollerna. 

### Baseline och kompetenstaxonomi

Som baseline används strängmatchning mot kompetenser från Arbetsförmedlingens kompetenstaxonomi. Även taxonomin har avgränsats till kompetenser som är relaterade till SSYK 2511 för att motsvara den valda gruppen av jobbannonser.

Denna avgränsning minskar antalet kompetenser som behöver matchas och gör bearbetningen mer hanterbar. En konsekvens är dock att kompetenser som förekommer i annonserna men som i Arbetsförmedlingens taxonomi främst är kopplade till andra yrkesgrupper kan missas.

Strängmatchning har dessutom en metodologisk begränsning eftersom den huvudsakligen identifierar kompetenser som uttrycks på samma eller liknande sätt som i taxonomin. Förkortningar, synonymer, alternativa stavningar och kompetenser som saknas i taxonomin riskerar därför att inte identifieras.

Taxonomin omfattar inte heller nödvändigtvis alla typer av kompetenser som kan förekomma i jobbannonser, exempelvis vissa generella eller sociala kompetenser (soft skills). För att kunna utvärdera denna begränsning kommer ett urval av jobbannonser att annoteras manuellt i Label Studio. Den manuella annoteringen används som ett gold standard mot vilket resultatet från baseline och övriga metoder kan jämföras.

## Modellval
### spaCy och EntityRuler

spaCy är ett verktyg för att analysera text, och EntityRuler är den del som markerar ord och fraser utifrån regler vi själva skriver. Metoden fungerar bra när det som ska hittas är en känd och avgränsad lista, när stavningen är ganska stabil och när det är viktigt att kunna förklara varför något räknades. Den fungerar sämre när det som ska hittas är obegränsat eller förändras snabbt, när samma ord kan betyda olika saker och när sammanhanget avgör om något är relevant. Metoden hittar det som står i reglerna, men den förstår inte texten.

I vårt projekt passar metoden väl för frågan hur ofta kända kompetenser nämns i jobbannonser. Vi har en tydlig lista från Arbetsförmedlingens taxonomi att utgå från och EntityRuler passar bra för egenskrivna regler, snarare än att träna en egen modell för kompetenser. Dessutom ville vi kunna se exakt vilken regel som låg bakom varje träff, så att fel går att hitta och rätta. Den passar sämre för frågan vilka kompetenser arbetsgivare faktiskt kräver. Ett omnämnande är inte samma sak som ett krav, nya tekniker syns först när vi lägger till dem, och ord som kan betyda flera saker kräver särskilda regler. Resultatet ska därför läsas som en bild av de kompetenser som vår lista kan fånga, och inte som en fullständig bild av arbetsmarknaden.

### Utformning av regler

Hur strikt en regel är avgör vad den hittar och vad den missar. En regel som ignorerar stora och små bokstäver fångar fler varianter av samma ord, men träffar också vanliga ord som råkar se likadana ut. En regel som kräver exakt stavning skyddar mot sådana felträffar, men missar kompetensen när den skrivs på ett oväntat sätt. Synonymer och förkortningar fångas bara om någon har kommit på dem i förväg. Det går därför inte att få både alla träffar och inga felträffar, och varje regel är ett val mellan de två.

Vi delade in kompetenserna i tre nivåer efter hur lätt de är att förväxla med något annat. Långa och tydliga namn, som Docker eller Systemarkitektur, matchas oavsett stora och små bokstäver, eftersom risken för förväxling är liten. Korta eller tvetydiga ord, som R, SAS och Julia, matchas bara med exakt stavning, eftersom de annars också träffar vanliga ord och egennamn. Kompetenser som skrivs på flera sätt, som Amazon Web Services och AWS, samlas under ett gemensamt namn, och varje variant får sin egen regel för skiftläge. Indelningen minskar felträffarna men kostar träffar: en kompetens som skrivs på ett sätt vi inte förutsett, eller med fel skiftläge, syns inte i resultatet. Det är en av orsakerna till att en del kompetenser i vår lista aldrig matchade.

### Hur vi mätte resultatet

För att veta hur bra en metod är på att hitta rätt behöver man ta fram ett facit, med tillhörande mått. Precision visar hur stor andel av träffarna som var korrekta, och recall visar hur stor andel av det som fanns att hitta som metoden faktiskt hittade. De drar åt olika håll, eftersom en metod som hittar allt får många felträffar och en som är försiktig missar mycket. F1 slår ihop de två till ett tal. 

Vi tog fram ett facit genom att manuellt annotera ett urval av 192 annonser, fördelade jämnt över månad och annonslängd. Urvalet ger en rättvis bild av olika typer av annonser, men det speglar inte hur annonserna fördelar sig i hela datamaterialet. Vi jämförde två metoder: en baseline som matchar taxonomins kompetenser, och EntityRuler med våra egna regler. Reglerna skrevs före utvärderingen. Eftersom EntityRuler också letar efter kompetenser som vi lagt till, och baseline inte kan hitta dem, mätte vi baseline både mot facit med enbart taxonomikompetenser och mot facit med alla annoterade kompetenser. Recall på annonserna utanför urvalet är okänd, och våra kontroller av enskilda kompetenser byggde på små stickprov. Resultaten visar därför hur metoderna står sig mot vårt facit och ska inte läsas som exakta värden för hela arbetsmarknaden.