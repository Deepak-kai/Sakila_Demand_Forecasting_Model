import pandas as pd
import mysql.connector
import numpy as np
import os
import platform
from sklearn.ensemble import RandomForestRegressor

# --- 1. Database Configuration ---
DB_CONFIG = {
    "host": "localhost",
    "user": "User_Name", #<---Use your user name of sql
    "password": "Password", # <--- Update this 
    "database": "sakila"
}

# --- 2. The "Clean Root" SQL Query ---
# This structure is the ONLY way to prevent the 11,22 math duplication issue
sql_query = """
SELECT 
    f.film_id AS ID,
    f.title AS MOVIE_TITLE,
    cat.name AS GENRE,
    f.rental_rate AS UNIT_PRICE,
    -- Isolated Subqueries for 100% Mathematical Accuracy
    (SELECT COUNT(r.rental_id) 
     FROM rental r 
     JOIN inventory i ON r.inventory_id = i.inventory_id 
     WHERE i.film_id = f.film_id) AS TOTAL_RENTALS,
     
    (SELECT SUM(p.amount) 
     FROM payment p 
     JOIN rental r2 ON p.rental_id = r2.rental_id 
     JOIN inventory i2 ON r2.inventory_id = i2.inventory_id 
     WHERE i2.film_id = f.film_id) AS TOTAL_REVENUE,
     
    (SELECT COUNT(*) 
     FROM inventory i3 
     WHERE i3.film_id = f.film_id) AS CURRENT_STOCK,
     
    (SELECT COUNT(DISTINCT r3.customer_id) 
     FROM rental r3 
     JOIN inventory i4 ON r3.inventory_id = i4.inventory_id 
     WHERE i4.film_id = f.film_id) AS UNIQUE_CUSTOMERS,
     
    -- Picking the primary store location context
    (SELECT co.country 
     FROM inventory i5
     JOIN store s ON i5.store_id = s.store_id 
     JOIN address ad ON s.address_id = ad.address_id 
     JOIN city ci ON ad.city_id = ci.city_id 
     JOIN country co ON ci.country_id = co.country_id 
     WHERE i5.film_id = f.film_id LIMIT 1) AS REGION
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
ORDER BY f.film_id ASC;
"""

def run_analytics_system():
    try:
        print("Connecting to Sakila Analytics Engine...")
        conn = mysql.connector.connect(**DB_CONFIG)
        df = pd.read_sql(sql_query, conn)
        conn.close()

        # --- 3. Machine Learning (Demand Forecasting) ---
        # Features: Price, Historical Volume, and Customer Reach
        X = df[['UNIT_PRICE', 'TOTAL_RENTALS', 'UNIQUE_CUSTOMERS']].fillna(0)
        y = df['TOTAL_RENTALS'] * 1.25 # Training for a 25% growth target
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        # Apply predictions to the dataframe
        df['PREDICTED_DEMAND'] = np.ceil(model.predict(X)).astype(int)
        df['SAFETY_STOCK_REQ'] = np.ceil(df['PREDICTED_DEMAND'] * 1.3).astype(int)
        
        # --- 4. Supply Chain Intelligence ---
        df['STOCK_GAP'] = df['SAFETY_STOCK_REQ'] - df['CURRENT_STOCK']
        df['INVENTORY_STATUS'] = np.where(df['STOCK_GAP'] > 0, 'URGENT REORDER', 'HEALTHY')

        # --- 5. Professional Excel Dashboard Construction ---
        file_name = "SAKILA_PREDICTIVE_DASHBOARD.xlsx"
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Inventory Analysis')

        workbook  = writer.book
        worksheet = writer.sheets['Inventory Analysis']

        # UI/UX Styles
        header_fmt = workbook.add_format({'bold': True, 'bg_color': '#1F4E78', 'font_color': 'white', 'border': 1})
        money_fmt  = workbook.add_format({'num_format': '$#,##0.00'})
        urgent_fmt = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'bold': True})
        status_fmt = workbook.add_format({'align': 'center'})

        # Apply Header Style
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value.replace('_', ' '), header_fmt)

        # Apply Column Formatting
        worksheet.set_column('D:D', 12, money_fmt) # Unit Price
        worksheet.set_column('F:F', 15, money_fmt) # Total Revenue
        worksheet.set_column('K:K', 18, status_fmt) # Status Column

        # Conditional Formatting: Highlight Reorders in Red
        worksheet.conditional_format('K2:K2000', {
            'type':     'cell',
            'criteria': 'equal to',
            'value':    '"URGENT REORDER"',
            'format':   urgent_fmt
        })

        # Final layout adjustments
        worksheet.set_column('B:B', 35) # Movie Title
        worksheet.set_column('C:C', 15) # Genre
        worksheet.freeze_panes(1, 0)     # Freeze top row

        writer.close()
        print(f"Success! Dashboard saved as {file_name}")

        # --- 6. Auto-Open Function ---
        if platform.system() == 'Windows':
            os.startfile(file_name)
        elif platform.system() == 'Darwin':
            os.system(f'open "{file_name}"')
        else:
            os.system(f'xdg-open "{file_name}"')

    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    run_analytics_system()
