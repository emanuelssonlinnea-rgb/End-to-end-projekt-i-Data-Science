## Project description  

## Data
This project combines two datasets from Arbetsförmedlingen: a collection of **unpublished job ads** and a **taxonomy of skills**.  
Both are restricted to one occupation group, **SSYK 2511** (Systemanalytiker och IT-arkitekter m.fl.). In Arbetsförmedlingen's taxonomy every occupation group has a concept ID, and the ID for 2511 is **UXKZ_3zZ_ipB**.

### Hitorical job ads
- **Source:** JobTech Historical API (Arbetsförmedlingen / Platsbanken), `https://historical.api.jobtechdev.se/search`, license CC0.
- **Scope:** historical ads in occupation group SSYK 2511. (*Systemanalytiker och IT-arkitekter m.fl.*), filtered on the server with `occupation-group=UXKZ_3zZ_ipB`.
- **Period:** 2025-01-01 to 2026-09-30.
- **Retrieval:** `src/get_job_ads.py` queries one month at a time and pages through results 100 ads at a time. The result is trimmed to the fields relevant for our project.
- **Retrieved on:** 2026-10-05
- **Limits:** the data does not account for currently pubblished adds and duplicates remain.

### Skills taxonomy
- **Source:** Arbetsförmedlingen open data, dataset *SSYK nivå fyra med relationer till kompetensbegrepp och yrkesbenämningar* (https://data.arbetsformedlingen.se/taxonomy/version/31/query/skills-with-related-skill-headlines-and-ssyk-level-4-groups), license CC0.
- **Content:** SSYK level 4 groups, each with related skills (`related`) and occupation names (`narrower`).
- **Selection:** we keep only the group with concept id `UXKZ_3zZ_ipB` (SSYK 2511), the same id that the ads carry in `occupation_group.concept_id`.
- **Retrieval:** `<src/get_skills.py>`, saved as `data/skills_2511.json`.
- **Retrieved on:** 2026-10-05.
- **Note:** the taxonomy is updated monthly. As of the time of retrieval, the latest version is 31.

### Reproducing the data
Run the two scripts from the project root.

```python
python src/get_job_ads.py
python src/get_skills.py
```

## Quick Start
Clone the repo:  
`git clone https://github.com/emanuelssonlinnea-rgb/End-to-end-projekt-i-Data-Science.git`  

Create and activate a virtual environment:  
`cd End-to-end-projekt-i-Data-Science`    
`python -m venv .venv`  
`.venv\Scripts\Activate` (for Windows PowerShell)  

Install dependencies:  
`python -m pip install -r requirements.txt`  


## Environment  
Python 3.13.7  
Packages: NumPy, Pandas, Jupyter (see `requirements.txt`)  

## Project structure

```text
End-to-end-projekt-i-Data-Science/
├── data/
│   └── skills_2511.json
├── notebooks/  
│   └── 01_exploration.ipynb
├── src/
│   └── get_job_ads.py
│   └── get_skills.py
└── README.md
```

## Avgränsningar
### Data
Datan i projektet kommer från Arbetsförmedlingens jobbdatabas Platsbanken. Eftersom studien fokuserar på historiska jobbannonser från 2025 och 2026 hämtades datan från Arbetsförmedlingens Historical Job Ads API . API:et innehåller jobbannonser som inte längre är aktiva i Platsbanken.

Projektet omfattar därför inte annonser från andra jobbsajter eller rekryteringsplattformar. Resultaten speglar därmed de jobbannonser som publicerats i Platsbanken och kan inte antas representera samtliga lediga tjänster på den svenska arbetsmarknaden.

### Tidsperiod
Studieperioden avgränsades till 1 januari 2025–31 augusti 2026. Projektet genomförs under september och oktober 2026, vilket innebär att vissa annonser som publicerats under 2026 fortfarande kan vara aktiva och därför ännu inte finnas tillgängliga i Historical Job Ads API.

Detta innebär att framför allt de senare månaderna under 2026 kan innehålla färre annonser än motsvarande period 2025. Jämförelser mellan åren behöver därför göras med hänsyn till denna begränsning.

För att göra jämförelser mellan 2025 och 2026 mer rättvisande kan analyser som jämför åren direkt begränsas till samma månader, exempelvis januari–augusti för båda åren.

### Yrkesmässig avgränsning
Projektets ursprungliga mål var att undersöka vilka kompetenser som efterfrågas inom IT på den svenska arbetsmarknaden. På grund av projektets omfattning valde vi att avgränsa analysen till SSYK-gruppen 2511 - Systemanalytiker och IT-arkitekter m.fl. 

Gruppen omfattar bland annat yrken som Data Scientist, IT-arkitekt, kravanalytiker, systemanalytiker, systemarkitekt och verksamhetskonsult inom IT.

Enligt Arbetsförmedlingens Yrkesatlas arbetar dessa roller bland annat med utveckling av IT-system, IT-struktur och teknisk arkitektur samt med att säkerställa att IT-lösningar stödjer verksamhetens behov.

Avgränsningen minskar datamängden och gör det möjligt att genomföra en mer fokuserad analys inom projektets tidsram. Samtidigt innebär den att resultaten inte kan generaliseras till hela IT- och datasektorn. Resultaten bör i stället tolkas som en analys av kompetensefterfrågan inom den valda yrkesgruppen.

### Baseline och kompetenstaxonomi

Som baseline används strängmatchning mot kompetenser från Arbetsförmedlingens kompetenstaxonomi. Även taxonomin har avgränsats till kompetenser som är relaterade till SSYK 2511 för att motsvara den valda gruppen av jobbannonser.

Denna avgränsning minskar antalet kompetenser som behöver matchas och gör bearbetningen mer hanterbar. En konsekvens är dock att kompetenser som förekommer i annonserna men som i Arbetsförmedlingens taxonomi främst är kopplade till andra yrkesgrupper kan missas.

Strängmatchning har dessutom en metodologisk begränsning eftersom den huvudsakligen identifierar kompetenser som uttrycks på samma eller liknande sätt som i taxonomin. Förkortningar, synonymer, alternativa stavningar och kompetenser som saknas i taxonomin riskerar därför att inte identifieras.

Taxonomin omfattar inte heller nödvändigtvis alla typer av kompetenser som kan förekomma i jobbannonser, exempelvis vissa generella eller sociala kompetenser (soft skills). För att kunna utvärdera denna begränsning kommer ett urval av jobbannonser att annoteras manuellt i Label Studio. Den manuella annoteringen används som ett gold standard mot vilket resultatet från baseline och övriga metoder kan jämföras.

### Definitionen av skill/kompetenser

I detta projekt definieras en kompetens/skill som en konkret kunskap, teknik, metod, verktyg, programvara, plattform eller annan teknisk kompetens som en person kan behöva behärska för att utföra ett arbete inom IT.
Vi använder Arbetsförmedlingens taxonomi som en referens men inte facit. Exempelvis inkluderar vi såkallade soft skills som kommunikation, noggranhet och strukturerad som kompetens även om dessa inte inkluderas I Arbetsförmedlingens taxonomi. 

#### Inkluderat I definitionen:
- Allmänna datakunskaper:
- Applikationsplattformar
- Certifikat/licenser
- Datorspråk
- Integrationsplattformar
- Kommunikationsprotokoll
- Kvalitetssystem
- Mobiltelefonsystem
- Nätverk
- Operativsystem
- Programmerings- och systemutvecklingsverktyg
- Ramverk
- Styr- och utvecklingsmodeller
- Soft skills

#### Exkluderas ur definitionen:
- Arbetstitlar
- Arbetsgivare
- Regioner
- Städer
- Datum
- Generella aktiviteter
- År av erfarenhet
- Arbetsansvar