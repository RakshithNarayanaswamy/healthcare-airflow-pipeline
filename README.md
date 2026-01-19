# Healthcare Streaming Data Engineering & Event-Driven Analytics Pipeline

## From Real-Time Vitals to Risk-Aware Patient Insights Using a Modern Lakehouse Architecture

A full end-to-end streaming data engineering project that ingests, processes, enriches, and analyzes healthcare vitals using **Databricks**, **Medallion Architecture**, **Apache Airflow**, **Apache Kafka**, and **Python analytics libraries**.

---

## Project Overview

This project simulates a real-world **healthcare streaming environment** where patient vitals such as heart rate, SpO₂, blood pressure, and alert signals are continuously ingested and transformed into **analytics-ready datasets**.

The pipeline follows a **Bronze → Silver → Gold Medallion Architecture** implemented on **Databricks**, orchestrated using **Apache Airflow**, and enhanced with **event-driven Kafka notifications** for pipeline completion and alerting.

The objective is to demonstrate how **raw streaming telemetry** can be converted into **actionable patient risk insights**, high-quality analytics tables, and business-facing visualizations.

---

## Business Questions Addressed

### Patient Risk & Severity

- How do vital signals correlate with patient severity levels?
- Which vitals are most associated with critical alerts?
- How can patient risk be summarized at a snapshot level?

### Alert Behavior

- Which patients generate the highest alert volume?
- What alert types occur most frequently?
- Are alerts clustered around certain vital thresholds?

### Data Quality & Reliability

- Are vitals consistently populated in the Gold layer?
- Which attributes show higher null or inconsistency rates?
- How reliable is the analytics layer for downstream use?

---

## Data Sources

### Synthetic Healthcare Data (Synthea)

- Source: Synthea™ Synthetic Patient Generator
- Provider: MITRE Corporation
- Website: https://synthea.mitre.org
- Data Type: Synthetic (HIPAA-safe, non-identifiable healthcare data)

### Description:

Synthea is an open-source synthetic data generator that simulates realistic patient health records. It produces longitudinal healthcare data, including patient demographics, encounters, conditions, observations (vitals), medications, and procedures. The dataset is widely used for healthcare analytics, interoperability testing, and data engineering pipelines without exposing real patient information.

### Key Characteristics:

- Fully synthetic and privacy-safe (no real patient data)
- Longitudinal patient timelines
- Realistic clinical workflows and vitals generation
- Industry-aligned healthcare schema (FHIR-inspired)

---

## Architecture Overview

The pipeline is designed using a **modern lakehouse pattern**:

### Bronze Layer — Raw Streaming Data

- Ingests simulated healthcare vitals as-is
- Preserves raw event fidelity
- No transformations applied

### Silver Layer — Cleansed & Enriched

- Data type normalization and validation
- Severity classification logic
- Statistical enrichment using **Pandas** and **NumPy**
- Alert standardization

### Gold Layer — Analytics Ready

- Patient-level risk snapshots
- Aggregated alert metrics
- Optimized datasets for analytics and reporting
- Quality-validated, low-latency tables
  ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.30.12%E2%80%AFPM.png)

---

## Orchestration & Event-Driven Design

### Apache Airflow

- Orchestrates Databricks notebook execution
- Manages task dependencies across Bronze → Silver → Gold
- Supports scheduled and manual pipeline runs

### Apache Kafka

- Publishes pipeline completion events
- Emits alert-related notifications
- Enables downstream extensibility for monitoring systems

## ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.27.52%E2%80%AFPM.png)

## Analytics & Visualizations

Analytics are performed directly within **Databricks notebooks** using **Pandas, NumPy, and Matplotlib**, demonstrating analytics readiness without external BI tools.

Key analyses include:

- Distribution of vital signals (heart rate, SpO₂)
- Heart rate vs patient severity correlation
- Top patients by alert frequency
- Severity category breakdowns
- Null percentage validation across Gold datasets

---

## Analytical Data Model (Gold Layer)

The Gold layer exposes analytics-friendly structures:

- **Patient Risk Snapshot**
  - Aggregated vitals
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.53.30%E2%80%AFPM.png)
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.53.10%E2%80%AFPM.png)
  - Severity classification
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.52.44%E2%80%AFPM.png)
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.52.33%E2%80%AFPM.png)
  - Statistical summaries
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.51.13%E2%80%AFPM.png)

- **Alert Analytics**
  - Alert frequency by patient
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.52.05%E2%80%AFPM.png)
  - Severity distribution
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.51.56%E2%80%AFPM.png)
  - Threshold breach patterns
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.51.38%E2%80%AFPM.png)

- **Data Quality Metrics**
  - Column-level null percentage check
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.52.23%E2%80%AFPM.png)
  - Completeness validation
    ![image](https://github.com/RakshithNarayanaswamy/healthcare-airflow-pipeline/blob/main/Screenshots/Screenshot%202026-01-19%20at%203.52.55%E2%80%AFPM.png)

---

## Technology Stack

| Category               | Tools                          |
| ---------------------- | ------------------------------ |
| Streaming & Processing | Databricks (PySpark, SQL)      |
| Orchestration          | Apache Airflow                 |
| Event Streaming        | Apache Kafka                   |
| Analytics              | Pandas, NumPy, Matplotlib      |
| Architecture           | Medallion (Bronze–Silver–Gold) |
| Containerization       | Docker                         |
| Version Control        | Git & GitHub                   |

---

## Engineering Highlights

- Designed a Medallion Architecture for scalable streaming analytics
- Implemented event-driven observability using Kafka
- Orchestrated notebook execution using Airflow
- Applied statistical enrichment with Pandas and NumPy
- Enforced analytics-layer data quality validation

---

## Business Value

This project demonstrates how healthcare streaming data can be transformed into:

- Patient-centric risk insights
- Reliable analytics layers for reporting
- Event-driven monitoring and extensibility
- Scalable lakehouse-based healthcare analytics

---

## What This Project Demonstrates

- Real-time data engineering workflows
- Modern Databricks lakehouse design
- Airflow-based orchestration
- Kafka-based event publishing
- Analytics using Python data libraries
- Production-style data quality checks
