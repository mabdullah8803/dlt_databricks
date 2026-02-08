# Databricks Lakeflow Declarative Pipeline (Delta Live Tables)

This project is a hands-on learning implementation of a **Databricks Lakeflow (Delta Live Tables)** declarative pipeline using the **Bronze–Silver–Gold Medallion Architecture**.

The pipeline processes **customer, product, and sales** data using streaming tables and CDC flows, and produces a business-level aggregated table for analytics.

This project focuses on understanding how Databricks manages data pipelines declaratively and visualizes data lineage using pipeline graphs.

---

## Description

- Raw customer, product, and sales data are ingested into **Bronze streaming tables**
- Data is cleaned and enriched in the **Silver layer** using streaming views and Auto CDC
- **SCD Type 1** logic is applied for incremental updates
- Fact and dimension tables are joined in the **Gold layer**
- A materialized Gold table (`business_sales`) is created for business analytics

---

## Technologies Used

- Databricks Lakeflow
- Delta Live Tables (DLT)
- PySpark
- Apache Spark (Structured Streaming)
- Delta Lake
- Medallion Architecture (Bronze, Silver, Gold)

---

## Key Learnings

- Understanding declarative data pipelines in Databricks
- Working with streaming tables and views
- Implementing CDC using `create_auto_cdc_flow`
- Applying SCD Type 1 for dimension updates
- Visualizing data flow using Databricks pipeline graphs
- Designing analytics-ready Gold tables

---

*This project is part of my ongoing learning journey in Data Engineering using Databricks.*
