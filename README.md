---
title: "ANALISIS SENTIMEN ULASAN ANIME GENRE FANTASY DI MYANIMELIST MENGGUNAKAN TEXTBLOB DAN VADER"
author: "Nathanael Putra Ganata, Muhammad Fawwaz Razani, Christhoper Carlos Pangaribuan"
date: "09/05/2025"
---

## Repository Structure

```
📂 myanimelist                # Root project folder
 ├── data/                    # Raw and processed datasets
 │   ├── raw/                 # Scraped raw data
 │   │   ├── top_150_anime_links.csv
 │   │   └── top_150_fantasy_reviews.csv
 │   ├── processed/           # Cleaned and scored data
 │   │   ├── top_150_fantasy_reviews_cleaned.csv
 │   │   └── top_150_fantasy_reviews_sentiment.csv
 │   └── libs/                # NLTK language resources
 │       └── nltk_data/
 │           ├── corpora/
 │           └── sentiment/
 │
 ├── notebooks/              # Jupyter notebooks for each pipeline stage
 │   ├── archive/
 │   │   ├── 00-setup.ipynb
 │   │   ├── 01-preprocessing-sentiment.ipynb
 │   │   ├── 02-sentiment-analysis.ipynb
 │   │   └── 03-pos-ner.ipynb
 │
 ├── scripts/                # Python scripts for scraping
 │   ├── scrap-reviews.py
 │   └── scrap-top-150.py
 │
 ├── venv/                   # Virtual environment (excluded in .gitignore)
 │
 ├── README.md               # Project introduction and documentation
 ├── requirements.txt        # List of required Python packages
 ├── .gitignore              # Files/folders to exclude from git
 └── .python-version         # Python version specification
```

## Introduction

This repository contains the source code, datasets, and analysis results for the project titled **"Analisis Sentimen Ulasan Anime Genre Fantasy di MyAnimeList Menggunakan TextBlob dan VADER"**. This study focuses on extracting and analyzing public sentiment from user reviews of the **150 most popular fantasy anime** on **MyAnimeList**, using Natural Language Processing (NLP) techniques.

The analysis leverages two lexicon-based sentiment models—**TextBlob** and **VADER**—to classify reviews as **positive**, **neutral**, or **negative**, and compare their performance against user recommendations.

Here's the rewritten version of that section, fully aligned with your **anime sentiment analysis** project from the PDF:

### **Research Focus:**

This project aims to **analyze user sentiment** in reviews of the **top 150 fantasy anime titles** on **MyAnimeList** by applying **Natural Language Processing (NLP)** techniques. The focus is on evaluating and comparing two lexicon-based sentiment models—**TextBlob** and **VADER**—to understand how effectively they capture user opinions.

Key components of this project include:

* **Web scraping** of anime titles and user reviews from MyAnimeList
* **Preprocessing review texts** for sentiment analysis (e.g., HTML decoding, contraction expansion, punctuation normalization)
* **Sentiment classification using TextBlob and VADER**, generating polarity and subjectivity scores
* **Evaluation using user recommendations** (Recommended, Mixed Feelings, Not Recommended)
* **Linguistic analysis with POS and NER** to uncover patterns in language structure and named entities mentioned in reviews

The ultimate goal is to **gain insights into audience sentiment**, explore the strengths and weaknesses of each sentiment model, and identify patterns in **how users express preferences toward anime content**, such as characters, stories, and studios.

## Dataset

The dataset consists of **2,403 user reviews** with the following attributes:
- `anime_title`: Title of the anime
- `review`: Raw review text
- `rating`: User's numeric score (1–10)
- `recommendation`: Explicit label from the user (Recommended, Mixed Feelings, Not Recommended)
- `review_sentiment`: Cleaned review for sentiment analysis
- `review_nerpos`: Cleaned review for POS and NER
- `textblob_polarity`, `textblob_subjectivity`, `textblob_label`
- `vader_neg`, `vader_pos`, `vader_neu`, `vader_compound`, `vader_label`

## Methodology

### 1. Data Collection
- Web scraping was used to collect:
  - 150 top-rated fantasy anime titles
  - First-page reviews for each title
- Tools used: `requests`, `BeautifulSoup`, `pandas`

### 2. Data Preprocessing
- Two separate preprocessing pipelines:
  - **For Sentiment Analysis** (TextBlob/VADER): cleaning, lowercasing, removing noise
  - **For POS/NER** (spaCy): structure-preserving, punctuation retained

### 3. Sentiment Analysis
- **TextBlob**:
  - Computes polarity and subjectivity
  - Labels: `positive`, `neutral`, `negative`
- **VADER**:
  - Returns scores: `pos`, `neu`, `neg`, `compound`
  - More responsive to informal and expressive text

### 4. Evaluation & Comparison
- Compared model output to user recommendations
- Accuracy, precision, recall, and F1-score computed
- Visualized using confusion matrices and sentiment distributions

### 5. POS and NER Analysis
- Used `spaCy` to extract:
  - Common POS tags (e.g., NOUN, VERB, ADJ)
  - Named entities like characters, studios, and numeric values

## Key Insights

- **TextBlob** is more conservative, labeling many reviews as neutral, and best suited for general polarity.
- **VADER** is more expressive and accurate in identifying both strong positives and negatives.
- VADER's F1-score for **negative sentiment** outperformed TextBlob significantly.
- Frequent mentions of anime characters and studios were captured via **Named Entity Recognition (NER)**.

## Conclusion

This project demonstrates how lexicon-based NLP methods can effectively capture sentiment trends in user-generated content within niche communities like anime fandoms. By combining sentiment scoring and linguistic entity extraction, we gain richer insights into how audiences engage with and evaluate fantasy anime titles.

## References

All technical implementation and documentation are based on the final project submitted as part of coursework. Full report and datasets are available in this repository. Original code repository:  
📎 [GitHub - nathanaelganata/myanimelist-nlp](https://github.com/nathanaelganata/myanimelist-nlp)