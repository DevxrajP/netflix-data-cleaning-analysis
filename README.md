# 🎬 Netflix Data Quality & Analytics

### An End-to-End Data Preparation Project Using Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Data%20Quality-0A7B83)
![Status](https://img.shields.io/badge/Status-Data%20Preparation%20Complete-orange)

A data analytics portfolio project focused on **data inspection, quality assessment, text preparation, and dataset export** using Python and Pandas. The project establishes a reproducible foundation for exploratory data analysis and visualization of Netflix titles.

---

## 📌 Executive Summary

Before data can support reliable business decisions, its structure and quality must be understood. This project applies a structured data-preparation workflow to a Netflix titles dataset, examining missing values, duplicate records, blank fields, categorical values, and text formatting.

The resulting dataset is exported to CSV for subsequent analysis.

| Project Metric | Result |
|---|---:|
| Records inspected | 8,790 |
| Columns inspected | 10 |
| Movies | 6,126 |
| TV Shows | 2,664 |
| Duplicate rows detected | 0 |
| Missing values reported | 0 |
| `Not Given` country entries | 287 |

> **Scope:** This repository currently focuses on data preparation. Exploratory visualizations are planned as a separate project extension.

## 🎯 Business & Analytical Objectives

- Establish an understanding of the dataset's structure and schema.
- Assess data completeness and record duplication.
- Identify blank values and potential text-formatting issues.
- Examine categorical fields such as content type and rating.
- Preserve records when information is unavailable rather than deleting them without justification.
- Produce a CSV output that can be reused in downstream analysis.

## 🧰 Technology Stack

| Technology | Role in the Project |
|---|---|
| Python | Scripting and data-processing logic |
| Pandas | Data loading, validation, transformation, and export |
| Visual Studio Code | Development environment |
| GitHub | Source-code hosting and project documentation |

## 📂 Dataset & Schema

The dataset contains **8,790 rows and 10 columns** describing Netflix titles.

| Column | Description |
|---|---|
| `show_id` | Title identifier |
| `type` | Movie or TV Show |
| `title` | Title name |
| `director` | Director information |
| `country` | Country information |
| `date_added` | Date added to Netflix |
| `release_year` | Original release year |
| `rating` | Content rating |
| `duration` | Runtime or season information |
| `listed_in` | Genre/category labels |

The dataset source and redistribution permissions should be documented before publishing the raw or cleaned CSV files.

## 🔬 Data Quality Methodology

### 1. Structural inspection
- Loaded the CSV using Pandas.
- Reviewed sample records, dimensions, column information, and data types.

### 2. Completeness assessment
- Calculated missing-value counts for each column.
- Checked for empty and whitespace-only strings.

### 3. Duplicate assessment
- Checked whether complete rows were duplicated.
- Applied duplicate removal to the working dataset.

### 4. Categorical and text validation
- Inspected unique values in the `type` and `rating` columns.
- Examined sample country values.
- Checked selected fields for leading and trailing whitespace.
- Applied whitespace trimming to relevant text columns.

### 5. Data preservation
- Preserved `Not Given` country entries because they represent unavailable country information rather than blank strings or Pandas null values.

### 6. Output generation
- Exported the prepared dataset to `netflix_cleaned.csv`.
- Retained the original input file separately in the local working directory.

## 📈 Key Findings

**Content distribution**

| Content Type | Count | Share of Records |
|---|---:|---:|
| Movies | 6,126 | 69.69% |
| TV Shows | 2,664 | 30.31% |
| **Total** | **8,790** | **100%** |

**Data quality observations**

- No missing values were reported by the initial Pandas check.
- No duplicate rows were detected.
- No blank or whitespace-only values were detected by the checks performed.
- No extra spaces were found in the inspected `country`, `type`, and `rating` fields.
- 287 records use `Not Given` for country information.

*These metrics describe the current dataset and the checks implemented in the script; they do not guarantee that every possible data-quality issue has been eliminated.*

## ⚙️ Reproducibility

### Prerequisites
- Python 3.x
- Pandas

### Install the dependency

```bash
py -m pip install pandas
```

### Run the project

Place the input file named `Dataset.csv` in the same local directory as `task1_cleaning.py`.

```bash
py task1_cleaning.py
```

The script generates:

```text
netflix_cleaned.csv
```

### Expected workflow

```text
Input CSV
   ↓
Load and inspect
   ↓
Check completeness and duplicates
   ↓
Prepare text fields
   ↓
Export prepared CSV
```

## 🗂️ Repository Structure

```text
netflix-data-cleaning-analysis/
├── README.md
├── task1_cleaning.py
├── visualizations/       # Planned analysis charts
└── screenshots/          # Project evidence and outputs
```

The input and generated CSV files may remain local until their redistribution permissions have been verified.

## 🚀 Roadmap

- [x] Load and inspect the dataset
- [x] Assess missing values and duplicate rows
- [x] Check blank strings and selected text fields
- [x] Prepare text columns and export a CSV
- [x] Document initial dataset findings
- [ ] Add automated validation tests
- [ ] Analyze titles by release year
- [ ] Compare Movies and TV Shows visually
- [ ] Analyze country-level content distribution
- [ ] Publish verified charts and their interpretations

## ⚠️ Limitations & Considerations

- The current workflow performs basic data-quality checks; deeper semantic validation remains future work.
- A value of `Not Given` is preserved, not treated as a confirmed country.
- No visualization results are claimed until the charts have been generated and checked.
- Reproducibility depends on having the correct input dataset and required library installed.

## 👨‍💻 Author

**Devaraj P**  
Aspiring Data Analyst

**Areas of interest:** Python · Pandas · Data Cleaning · Exploratory Data Analysis · Data Visualization

---

*Created as a learning and portfolio project to demonstrate practical data-preparation skills.*
