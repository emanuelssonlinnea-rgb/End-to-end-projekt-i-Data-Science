# Kompetenstrender inom svensk IT - en NLP-analys av jobbannonser 2025-2026

![alt text](<data/graphs/Vanligast kompetenser wordcloud.png>)


## Projektbeskrivning
I det här projektet tillämpar vi NLP-metoder för att extrahera hard skills ur svenska jobbannonser.


## Snabb start
Clona repot:  
`git clone https://github.com/emanuelssonlinnea-rgb/End-to-end-projekt-i-Data-Science.git`  

Skapa och aktivera env:  
`cd End-to-end-projekt-i-Data-Science`    
`python -m venv .venv`  
`.venv\Scripts\Activate` (Windows PowerShell)  

Installera beroenden:  
`pip install -e .`  


## Miljö  
Python 3.13.7  
Paket: NumPy, Pandas, Jupyter, Matplotlib, Spacy (se `pyproject.toml`)  


## Projektstruktur
```text
End-to-end-projekt-i-Data-Science/
├── data/
│   ├── ads_clean.json
│   ├── ads_skills.json
│   ├── annoterad_test_data.json
│   ├── skills_2511.json
│   ├── test_set_labelstudio.json
│   └── train_set.json
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_test_set_extraction.ipynb
│   ├── 04_baseline.ipynb    
│   ├── 05_entity_ruler.ipynb  
│   ├── 06_evaluation.ipynb
│   ├── 07_full_dataset_analysis.ipynb            
│   └── 08_demo.ipynb
├── src/
│   ├── evaluation_utils.py
│   ├── get_job_ads.py
│   ├── get_skills.py
│   ├── models.py
│   └── skill_rules.py
├── project_limitations.md
└── README.md
```

## Data

Projektet kombinerar två dataset från Arbetsförmedlingen: en samling **opublicerade jobbannonser** och en **taxonomi över kompetenser**.  
Båda är begränsade till en yrkesgrupp, **SSYK 2511** (Systemanalytiker och IT-arkitekter m.fl.). I Arbetsförmedlingens taxonomi har varje yrkesgrupp ett concept-ID, och ID:t för 2511 är **UXKZ_3zZ_ipB**.

### Historiska jobbannonser
- **Källa:** JobTech Historical API (Arbetsförmedlingen / Platsbanken), `https://historical.api.jobtechdev.se/search`, licens CC0.
- **Omfattning:** historiska annonser i yrkesgrupp SSYK 2511 (*Systemanalytiker och IT-arkitekter m.fl.*), filtrerade på serversidan med `occupation-group=UXKZ_3zZ_ipB`.
- **Period:** 2025-01-01 till 2026-08-31.
- **Hämtning:** `src/get_job_ads.py` frågar efter en månad i taget och bläddrar igenom resultaten 100 annonser åt gången. Resultatet beskärs till de fält som är relevanta för vårt projekt.
- **Hämtad:** 2026-10-09
- **Begränsningar:** datan omfattar inte annonser som är publicerade just nu, och dubbletter finns kvar.

### Kompetenstaxonomi
- **Källa:** Arbetsförmedlingens öppna data, dataset *SSYK nivå fyra med relationer till kompetensbegrepp och yrkesbenämningar* (https://data.arbetsformedlingen.se/taxonomy/version/31/query/skills-with-related-skill-headlines-and-ssyk-level-4-groups), licens CC0.
- **Innehåll:** SSYK nivå 4-grupper, var och en med relaterade kompetenser (`related`) och yrkesbenämningar (`narrower`).
- **Urval:** vi behåller endast gruppen med concept-ID `UXKZ_3zZ_ipB` (SSYK 2511), samma ID som annonserna har i `occupation_group.concept_id`.
- **Hämtning:** `<src/get_skills.py>`, sparad som `data/skills_2511.json`.
- **Hämtad:** 2026-10-05.
- **Observera:** taxonomin uppdateras månadsvis. Vid hämtningstillfället var den senaste versionen 31.

## Definition av skill/kompetenser

I detta projekt definieras en kompetens/skill som en konkret kunskap, teknik, metod, verktyg, programvara, plattform eller annan teknisk kompetens som en person kan behöva behärska för att utföra ett arbete inom IT.
Vi använder Arbetsförmedlingens taxonomi som en referens men inte facit. Fokus ligger dock på det som kallas "hard skills" då vi inte kommer att inkludera "soft skills" som exempelvis kommunikation, noggranhet, etc. 

**Inkluderat i definitionen**
Tekniska kompetenser inom 14 kategorier i taxonomin, bland annat datorspråk, ramverk, operativsystem, nätverk och certifikat.

**Exkluderas ur definitionen**
Arbetsansvar, arbetstitlar, generella aktiviteter, soft skills och år av erfarenhet.

## Reproducerbarhet
**Rådatan finns inte i repot.** De råa jobbannonserna är inte incheckade eftersom de potentiellt innehåller personuppgifter. `src/get_job_ads.py` och `src/get_skills.py` hämtar dem från Arbetsförmedlingens API:er, så att köra dem ger dig en ny ögonblicksbild, inte den data vi arbetade med.

**Notebook 3 (uppdelning i tränings- och testdata) är fryst.** Testdatan annoterades för hand, och varje senare notebook bygger på exakt den uppdelningen. Om uppdelningen körs om på ny data skulle den ge andra tränings- och testmängder, och de manuella annoteringarna skulle inte längre stämma med datan. Därför är uppdelningen sparad på disk och incheckad i repot, och notebookarna efter den läser från dessa sparade filer i stället för från rådatan. Cellen som sparar dem är bortkommenterad som standard; avkommentera den bara om du medvetet vill skapa en ny uppdelning.

För att **reproducera våra resultat**, kör följande notebooks i ordning:
- 04_baseline.ipynb
- 05_entity_ruler.ipynb
- 06_evaluation.ipynb
- 07_full_dataset_analysis.ipynb

För att **tillämpa metoden på ny data**, kör hela pipelinen med början i de två skripten från projektets rotkatalog.
```python
python src/get_job_ads.py
python src/get_skills.py
```
Du får då en ny uppdelning och behöver annotera en ny testmängd.