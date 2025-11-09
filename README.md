DataSC-Essences — Steam Reviews NLP & Topic Insights

One-stop ML/NLP pipeline that scrapes Steam reviews for top games, embeds text with SentenceTransformers, explores topics (PCA), clusters similar reviews, and explains model behavior with LIME. Built end-to-end in a single notebook for fast iteration and clear storytelling.

⭐ Project scored highest out of 15 in course cohort.

Why this project matters

Shows data collection → NLP embeddings → dimensionality reduction → clustering → explainability in one place.

Uses production-relevant tools (Hugging Face SentenceTransformers, LIME) and a reproducible notebook workflow.

Includes a concrete scraper command and a 12k-row dataset example to make the work tangible. 
GitHub

Project Highlights

Custom web-scraper for Steam reviews with CLI flags and CSV export. 
GitHub

Sentence embeddings using all-MiniLM-L6-v2 (great speed/quality tradeoff). 
GitHub

Topic exploration with PCA (see pca_topics_interpretation.csv). 
GitHub

Explainability via LIME (see lime_review_explanation.html). 
GitHub

Single-notebook pipeline: steam_full_pipeline.ipynb for EDA → embeddings → clustering/visuals. 
GitHub

Repo Structure
DataSC-Essences/
├─ data/                             # (optional) local data store
├─ steam_full_pipeline.ipynb         # end-to-end notebook
├─ pca_topics_interpretation.csv     # PCA topics mapping/output
├─ lime_review_explanation.html      # LIME local explanations (HTML)
├─ image.png / image-1.png / ...     # visuals used in README / notebook
└─ README.md


Refs: notebook, LIME HTML, PCA CSV, and images are in the repo root. 
GitHub
+1

Data Collection (Steam Reviews)

Example scrape command used in this project:

python steam_scraper.py --apps 730 570 578080 --limit 4000 --outfile reviews.csv


This produced ~12,000 review rows (three apps × 4k limit) into reviews.csv. 
GitHub

Tech used in scraper: requests (HTTP), argparse (CLI flags), csv (streaming writes). 
GitHub

Fun edge-case: a review with extremely high “useful” score was actually sarcastic (“2 likes and I’ll uninstall this game”) — highlights why semantic models beat naive heuristics. 
GitHub

Methods

Embeddings

Model: sentence-transformers/all-MiniLM-L6-v2

Why: compact, fast, and strong sentence-level semantics for clustering/search. 
GitHub

Dimensionality Reduction & Topics

PCA for low-dim projections and topic axes; interpretation stored in pca_topics_interpretation.csv. 
GitHub

Clustering / Exploration

Clustering and neighborhood analysis performed in the notebook (steam_full_pipeline.ipynb). 
GitHub

Explainability

LIME to explain local predictions / cluster assignments (HTML artifact in repo). 
GitHub

Quickstart
1) Environment
# Python 3.10+
python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -U pip wheel
pip install sentence-transformers scikit-learn pandas numpy matplotlib tqdm lime

2) Get Data

Use your own reviews.csv or scrape with the provided command above (apps: 730, 570, 578080). 
GitHub

3) Run the Pipeline

Open steam_full_pipeline.ipynb and run all cells to:

Load & clean reviews

Encode text with SentenceTransformers

Reduce dimensionality (PCA) + visualize

Cluster & inspect topics

Generate LIME explanations

Notebook path and artifacts are in the repo root. 
GitHub

Results (at a glance)

Semantic clusters that group similar reviews beyond keywords.

PCA topic axes to interpret dominant themes (e.g., gameplay, performance, community).

LIME explainers to show which phrases drove a sample prediction/cluster placement.
