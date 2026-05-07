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
* MySQL Server (with the [Sakila sample database](https://dev.mysql.com/doc/sakila/en/) installed)

### Installation Steps
## Setup and Installation

### Prerequisites
* Python 3.8+
* MySQL Server (with the [Sakila sample database](https://dev.mysql.com/doc/sakila/en/) installed)

### Installation Steps

1. **Database Setup:** 
   Ensure MySQL is running and the Sakila database is loaded. Run the provided SQL script to set up necessary views/queries:
   '''bash
   mysql -u root -p < mysql_queries.sql
   
3. **Clone Repository**
   '''bash
   git clone [https://github.com/deepak-kai/sakila_demand_forecasting_model.git](https://github.com/Deepak-kai/Sakila_Demand_Forecasting_Model.git)
cd predictive-inventory-analytics

3.**Environment setup**
   '''bash
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

## Usage

Once your database is running and your virtual environment is activated, you can execute the data pipeline with a single command:
```bash
python generate_dashboard.py
