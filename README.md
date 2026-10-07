## Project description  

## Data
This project combines two datasets from Arbetsförmedlingen: a collection of **unpublished job ads** and a **taxonomy of skills**.  
Both are restricted to one occupation group, **SSYK 2511** (Systemanalytiker och IT-arkitekter m.fl.). In Arbetsförmedlingen's taxonomy every occupation group has a concept ID, and the ID for 2511 is **UXKZ_3zZ_ipB**.

### Hitorical job ads
- **Source:** JobTech Historical API (Arbetsförmedlingen / Platsbanken), `https://historical.api.jobtechdev.se/search`, license CC0.
- **Scope:** historical ads in occupation group SSYK 2511. (*Systemanalytiker och IT-arkitekter m.fl.*), filtered on the server with `occupation-group=UXKZ_3zZ_ipB`.
- **Period:** 2025-01-01 to 2026-08-31.
- **Retrieval:** `src/get_job_ads.py` queries one month at a time and pages through results 100 ads at a time. The result is trimmed to the fields relevant for our project.
- **Retrieved on:** 2026-10-07
- **Limits:** the data does not account for currently pubblished ads and duplicates remain.

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