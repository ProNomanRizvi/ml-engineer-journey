"""
File: etl_pipeline.py
Topic: ETL Pipeline Design (Extract, Transform, Analyze, Load)
Description: A structured pipeline to extract data from SQLite, clean it, analyze it, and save it.
"""

import sqlite3
import pandas as pd
import numpy as np
import os

# ==========================================
# Task 1 - Extract
# ==========================================
def extract_data(db_path):
    """
    Extract raw data from the SQL database and return a Pandas DataFrame.
    """
    print("--- Step 1: Extracting Data ---")
    
    # 1. Establish a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # 2. Write the SQL query to select everything from the 'sales' table
    query = "SELECT * FROM sales"
    
    # 3. Use Pandas to run the query and convert it directly into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # 4. It is good practice to close the connection once we have our data
    conn.close()
    
    # 5. Print the raw data to see what we extracted
    print("Raw Data Extracted from Database:")
    print(df.head(10)) # Print top rows to verify data extraction
    print("-" * 40 + "\n")
    
    return df

# ==========================================
# Task 2 - Transform
# ==========================================
def transform_data(df):
    """
    Clean the Pandas DataFrame - strip spaces, standardize text, handle missing values, and remove duplicates.
    """
    print("--- Step 2: Transforming / Cleaning Data ---")
    df_clean = df.copy()

    # 1. Standardize Text (remove extra spaces and make Title Case)
    # This will fix variations like "STATIONERY", "electronics", "mouse"
    df_clean["product_name"] = df_clean["product_name"].str.strip().str.title()
    df_clean["category"] = df_clean["category"].str.strip().str.title()
    
    # 2. Fill missing 'price' with the average price of its specific category
    df_clean["price"] = df_clean["price"].fillna(
        df_clean.groupby("category")["price"].transform("mean")
    )
    
    # 3. Fill missing 'quantity' with 0
    df_clean["quantity"] = df_clean["quantity"].fillna(0)
    
    # 4. Drop Duplicates (Ignoring 'id')
    # Updated 'date' to 'sale_date' to match the actual database schema
    columns_to_check = ["product_name", "category", "price", "quantity", "sale_date"]
    df_clean = df_clean.drop_duplicates(subset=columns_to_check)
    
    print("Data successfully cleaned!")
    print("-" * 40 + "\n")
    
    return df_clean

# ==========================================
# Task 3 - Analyze
# ==========================================
def analyze_data(df):
    """
    Extract numerical insights using NumPy - calculate total revenue, average price, etc.
    """
    print("--- Step 3: Analyzing Data ---")
    
    # 1. Create 'revenue' column (price * quantity)
    df["revenue"] = df["price"] * df["quantity"]
    
    # 2. Calculate insights using NumPy
    total_revenue = np.sum(df["revenue"])
    average_price = np.mean(df["price"])
    highest_revenue = np.max(df["revenue"])
    
    # Print the findings
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Average Price: ${average_price:.2f}")
    print(f"Highest Single Revenue: ${highest_revenue:.2f}")
    print("-" * 40 + "\n")
    
    return df

# ==========================================
# Task 4 - Load
# ==========================================
def load_data(df, output_path):
    """
    Save the final, cleaned DataFrame into a CSV file.
    """
    print("--- Step 4: Loading Data ---")
    
    # Create the output folder automatically if it doesn't exist
    folder_path = os.path.dirname(output_path)
    if folder_path:
        os.makedirs(folder_path, exist_ok=True)
    
    # Save the data without the index column
    df.to_csv(output_path, index=False)
    
    print(f"SUCCESS: Final report saved securely to '{output_path}'")
    print("-" * 40 + "\n")

# ==========================================
# Task 5 - Main Execution Block
# ==========================================
# This is where we actually run the pipeline functions in order
if __name__ == "__main__":
    print("🚀 Starting ETL Pipeline...\n")
    
    # Get the directory where this script is physically located
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Dynamically build the file paths so they work on any machine
    db_file = os.path.join(SCRIPT_DIR, "data", "source.db")
    output_file = os.path.join(SCRIPT_DIR, "data", "output", "final_report.csv")
    
    # Pipeline execution sequence
    try:
        # Step 1: Extract
        raw_dataframe = extract_data(db_file)
        
        # Step 2: Transform
        clean_dataframe = transform_data(raw_dataframe)
        
        # Step 3: Analyze
        analyzed_dataframe = analyze_data(clean_dataframe)
        
        # Step 4: Load
        load_data(analyzed_dataframe, output_file)
        
        print("✅ Pipeline finished successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred. Please check your database file and table.")
        print(f"Error Details: {e}")