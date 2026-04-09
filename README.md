# End-to-End ETL Pipeline Project

A production-style end-to-end ETL pipeline built using Python, PySpark, Databricks, Supabase PostgreSQL, and Apache Airflow to extract, transform, validate, and automate GitHub repository analytics.

---

## Project Overview

This project demonstrates a complete real-world ETL workflow:

- Extracts GitHub repository data using GitHub REST API
- Validates and cleans incoming data using Pydantic
- Loads structured data into PostgreSQL / SQLite
- Applies PySpark transformations for analytics
- Implements Bronze → Silver → Gold medallion architecture
- Automates nightly pipeline execution with Apache Airflow
- Produces analytics-ready gold tables for reporting

---

## Architecture

### End-to-End Pipeline Flow

GitHub REST API  
→ Python Extractor  
→ Pydantic Validation  
→ SQLAlchemy Loader  
→ Supabase PostgreSQL / SQLite  
→ PySpark Transformer  
→ Bronze Layer  
→ Silver Layer  
→ Gold Layer  
→ Analytics Outputs

---

## Medallion Architecture

### Bronze Layer
Raw GitHub repository data:
- github_repos
- github_repos_raw

### Silver Layer
Cleaned and enriched transformed data:
- Null language handling
- fork_ratio calculation
- star_tier classification
- repo_age_days enrichment

### Gold Layer
Analytics-ready outputs:
- lang_stats_gold
- top_repos_gold

---

## Technologies Used

### Languages
- Python 3.13
- SQL

### Frameworks / Tools
- PySpark
- Apache Spark
- Databricks
- Apache Airflow 3
- SQLAlchemy
- Pydantic
- Supabase PostgreSQL
- SQLite

### Libraries
- requests
- tenacity
- psycopg2
- python-dotenv

---

## Key Features

### Data Extraction
- GitHub REST API integration
- Pagination handling (1000+ records)
- Retry logic with exponential backoff
- Rate limiting support

### Data Validation
- Strong schema enforcement with Pydantic
- Type coercion and error handling
- Malformed row skipping

### Data Loading
- Batch upsert logic
- Idempotent pipeline design
- PostgreSQL + SQLite support

### Data Transformation
- PySpark distributed processing
- Window functions
- Aggregations
- Ranking logic

### Orchestration
- Apache Airflow DAG scheduling
- Nightly automated execution
- Retry handling on failure

---

## Project Structure

```bash
ETL-Pipeline-project/
│
├── connector.py
├── extractor.py
├── transformer.py
├── loader.py
├── state.py
├── quality_checks.py
├── spark_transformer.py
├── analytics.py
├── export_to_csv.py
├── check_data.py
│
├── airflow/
│   └── dags/
│       └── github_etl_dag.py
│
├── spark_output/
├── .env
├── requirements.txt
└── README.md
