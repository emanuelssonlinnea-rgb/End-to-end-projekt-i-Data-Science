# Avvägningar och begränsningar

För att genomföra projektet har vissa avvägningar och avgränsningar behövt vidtas, både gällande metodval och källdatan, som i slutändan påverkar hur resultatet av vår analys bör tolkas. Nedan följer en genomgång av de mest betydande besluten som tagits.

## Data och urval
### Platsbanken som källa
Datan i projektet kommer från Arbetsförmedlingens jobbdatabas Platsbanken. Eftersom studien fokuserar på historiska jobbannonser från 2025 och 2026 hämtades datan från Arbetsförmedlingens Historical Job Ads API. API:et innehåller jobbannonser som inte längre är aktiva i Platsbanken.

Vi har inte kunnat kontrollera hur stor andel av alla tjänster som annonseras i Platsbanken. Annonser som bara publiceras hos rekryteringsföretag, på sociala medier eller genom nätverk saknas. Resultaten beskriver därför Platsbankens annonser, och vi drar inga slutsatser om hela arbetsmarknaden.

### Tidsperiod
Vi hämtade annonser som publicerats från 1 januari 2025 till 31 augusti 2026. Historical Job Ads API innehåller bara annonser som inte längre är aktiva, och projektet genomfördes i september och oktober 2026. De senaste månaderna är därför sannolikt underrepresenterade, och de annonser som finns med kan vara ett skevt urval mot annonser som togs bort snabbt. För att jämförelsen mellan åren ska bli rättvis jämför vi bara samma månader, januari till augusti, i 2025 och 2026.

### Yrkesgrupp, SSYK 2511
Projektets ursprungliga mål var att undersöka vilka kompetenser som efterfrågas inom IT på den svenska arbetsmarknaden. På grund av projektets omfattning valde vi att avgränsa analysen till SSYK-gruppen 2511, Systemanalytiker och IT-arkitekter m.fl. Gruppen omfattar bland annat yrken som Data Scientist, IT-arkitekt, kravanalytiker, systemanalytiker, systemarkitekt och verksamhetskonsult inom IT.

Avgränsningen minskar datamängden och gör det möjligt att genomföra en mer fokuserad analys inom projektets tidsram. Samtidigt innebär den att resultaten inte kan generaliseras till hela IT- och datasektorn. Resultaten bör i stället tolkas som en analys av kompetensefterfrågan inom den valda yrkesgruppen.

### Språk
Platsbanken har annonser på både svenska och engelska. Eftersom spaCy använder olika språkpaket och projektets tid var begränsad analyserade vi bara svenska annonser. Språket avgjordes med hjälp av langdetect, och 36 % av annonserna uteslöts. Det kan ge en skev bild av företag som annonserar på engelska, till exempel internationella bolag och konsultföretag.

### Exkludering av "mjuka kompetenser"
För analysen valde vi att ta bort mjuka kompetenser, exempelvis serviceinriktning och stresstålighet, på grund av mjuka kompetenser är svåra att definiera entydigt och matcha med regler. Det hade dock också varit intressant att undersöka hur inkluderingen av dessa kompetenser hade påverkat resultatet och om den hade gett en bredare bild av arbetsgivarnas förväntningar.

## Metod
### Baseline med strängmatchning och kompetenstaxonomi
Som baseline använded strängmatchning mot kompetenser från Arbetsförmedlingens kompetenstaxonomi. Även taxonomin har avgränsats till kompetenser som är relaterade till SSYK 2511 för att motsvara den valda gruppen av jobbannonser. Denna avgränsning minskar antalet kompetenser som behöver matchas och gör bearbetningen mer hanterbar. En konsekvens är dock att kompetenser som förekommer i annonserna men som i Arbetsförmedlingens taxonomi främst är kopplade till andra yrkesgrupper kan missas.

Strängmatchning har dessutom en begränsning i metoden eftersom den huvudsakligen identifierar kompetenser som uttrycks på samma eller liknande sätt som i taxonomin. Förkortningar, synonymer, alternativa stavningar och kompetenser som saknas i taxonomin riskerar därför att inte identifieras.

### spaCy och EntityRuler
spaCy är ett verktyg för att analysera text, och EntityRuler är den del som markerar ord och fraser utifrån regler vi själva skriver. Metoden fungerar bra när det som ska hittas är en känd och avgränsad lista, när stavningen är ganska stabil och när det är viktigt att kunna förklara varför något räknades. Den fungerar sämre när det som ska hittas är obegränsat eller förändras snabbt, när samma ord kan betyda olika saker och när sammanhanget avgör om något är relevant. Metoden hittar det som står i reglerna, men den förstår inte texten.

I vårt projekt passar metoden väl för frågan hur ofta kända kompetenser nämns i jobbannonser. Vi har en tydlig lista från Arbetsförmedlingens taxonomi att utgå från och EntityRuler passar bra för egenskrivna regler, snarare än att träna en egen modell för kompetenser. Dessutom ville vi kunna se exakt vilken regel som låg bakom varje träff, så att fel går att hitta och rätta. Metoden passar sämre för frågan vilka kompetenser arbetsgivare faktiskt kräver. Ett omnämnande är inte samma sak som ett krav, nya tekniker syns först när vi lägger till dem, och ord som kan betyda flera saker kräver särskilda regler. Resultatet ska därför läsas som en bild av de kompetenser som vår lista kan fånga, och inte som en fullständig bild av arbetsmarknaden.

### Utformning av regler
Hur strikt en regel är avgör vad den hittar och vad den missar. En regel som ignorerar stora och små bokstäver fångar fler varianter av samma ord, men träffar också vanliga ord som råkar se likadana ut. En regel som kräver exakt stavning skyddar mot sådana felträffar, men missar kompetensen när den skrivs på ett oväntat sätt. Synonymer och förkortningar fångas bara om någon har kommit på dem i förväg. Det går därför inte att få både alla träffar och inga felträffar, och varje regel är ett val mellan de två.

Vi delade in kompetenserna i tre nivåer efter hur lätt de är att förväxla med något annat. Långa och tydliga namn, som Docker eller Systemarkitektur, matchas oavsett stora och små bokstäver, eftersom risken för förväxling är liten. Korta eller tvetydiga ord, som R, SAS och Julia, matchas bara med exakt stavning, eftersom de annars också träffar vanliga ord och egennamn. Kompetenser som skrivs på flera sätt, som Amazon Web Services och AWS, samlas under ett gemensamt namn, och varje variant får sin egen regel för skiftläge. Indelningen minskar felträffarna men kostar träffar: en kompetens som skrivs på ett sätt vi inte förutsett, eller med fel skiftläge, syns inte i resultatet. Det är en av orsakerna till att en del kompetenser (116 av 290) i vår lista aldrig matchade.

## Utvärdering
### Facit och annotering
För att kunna mäta hur bra vår metod var på att hitta rätt, tog vi fram ett facit genom att manuellt annotera ett urval av 192 jobbannonser, fördelade jämnt utifrån månad och annonslängd. Som utgångspunkt definierade vi en kompetens som en en konkret teknisk kunskap eller ett verktyg som behövs för ett IT arbete. Med denna definition och fokus på hårda kompetenser genomfördes annoteringen i Label Studio.

För att minska variationen mellan olika annotatörers bedömningar utfördes annoteringen av en enda person. Det eliminerade dock inte risken för subjektiva tolkningar eller att vissa kompetenser missades, exempelvis på grund av hur de formulerades i annonserna eller hur de tolkades av annotatören. Arbetet visade även att annoteringens kvalitet var beroende av annotatörens förståelse för de kompetenser som förekom i annonserna. Facitets tillförlitlighet begränsas därmed av både annotatörens kunskap och de bedömningar som gjordes under processen.

Dessa begränsningar innebär att facit kan ha varit ofullständigt, vilket i sin tur kan ha påverkat metodernas uppmätta precision och recall. Exempelvis kan en kompetens som identifierades korrekt av en automatisk metod ha bedömts som en falsk positiv träff om den saknades i den manuella annoteringen. På längre sikt är manuell annotering dessutom tidskrävande och svår att skala upp till större datamängder.

### Mått och jämförelse
Vi jämförde två metoder mot facit: en baseline som matchar taxonomins kompetenser, och EntityRuler med våra egna regler. Reglerna skrevs före utvärderingen.

EntityRuler letar också efter kompetenser som vi lagt till själva, och dem kan baseline inte hitta. För att jämförelsen skulle bli rättvis mätte vi baseline mot två versioner av facit: en med enbart taxonomikompetenser och en med alla annoterade kompetenser. EntityRuler mättes mot facit med alla annoterade kompetenser.

Facit finns bara för de 192 annonserna i urvalet, så recall på övriga annonser är okänd. Våra kontroller av enskilda kompetenser gjordes dessutom på små stickprov. Resultaten visar därför hur metoderna står sig mot vårt facit, och de ska inte läsas som exakta värden för hela arbetsmarknaden.