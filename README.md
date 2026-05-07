## Predictive Inventory Analytics Engine

An end-to-end data pipeline that connects a MySQL database to a Python-based Machine Learning environment, automatically generating formatted Excel dashboards for supply chain management.

##  Business Value
This project bridges the gap between raw database storage and actionable business intelligence. By integrating a Sakila MySQL database with a predictive model, this system forecasts inventory demand, identifies urgent supply chain gaps, and automatically generates conditionally formatted financial Excel dashboards. It is designed to demonstrate full-stack data pipeline architecture, from optimized database queries to an automated executive reporting UI.

##  System Architecture
1. **MySQL (Data Extraction):** Extracts operational data from the Sakila database using optimized, isolated subqueries to prevent row duplication and ensure strict mathematical accuracy.
2. **Python (Machine Learning & Logic):** Leverages `scikit-learn` (Random Forest Regressor) to anticipate a 25% business growth target based on historical volume, unit pricing, and unique customer reach.
3. **Excel (Automated UI/UX):** Uses `xlsxwriter` to programmatically output a formatted dashboard that flags urgent reorder requirements and calculates stock gaps.

##  Core Features
* **Precision SQL Extraction:** Uses isolated subqueries for exact calculations of total rentals, revenue, and current stock without cross-join errors.
* **Demand Forecasting:** Integrates a Random Forest algorithm to predict future inventory needs based on historical patterns.
* **Supply Chain Logic:** Calculates safety stock (130% of predicted demand) and dynamically assigns 'URGENT REORDER' or 'HEALTHY' inventory statuses.
* **Automated Reporting:** Generates a professional-grade Excel file with pre-applied conditional formatting, frozen panes, and custom column widths.
* **Cross-Platform Execution:** Automatically launches the generated financial report upon completion on Windows, macOS, or Linux.

##  Tech Stack
* **Database:** MySQL (Sakila Database)
* **Language:** Python
* **Machine Learning:** `scikit-learn`
* **Data Processing:** `pandas`, `numpy`
* **Database Connector:** `mysql-connector-python`
* **Reporting Engine:** `xlsxwriter`

##  Setup and Installation

### Prerequisites
* Python 3.8+
* MySQL Server (with the Sakila sample database installed)

### Installation Steps
1.Install Mysql(full) with Sakila database
2.copy paste code in Mysql queries.sql and run the file
3.install vscode(python ide) and install required environment and files to run the code
