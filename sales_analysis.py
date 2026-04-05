# Import pandas library
import pandas as pd

# -------------------------------
# Day 1: Load Data
# -------------------------------
# Load CSV file
df = pd.read_csv('sales_data.csv')

# -------------------------------
# Day 2: Explore Data
# -------------------------------
print("First 5 rows:\n", df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:\n", df.isnull().sum())

# -------------------------------
# Day 3: Clean Data
# -------------------------------

# Drop duplicates
df = df.drop_duplicates()

# Handle missing values
# Fill numeric columns with 0
df.fillna(0, inplace=True)

# -------------------------------
# Day 4: Analyze Sales
# -------------------------------

# Total Revenue
total_sales = df['Total_Sales'].sum()

# Best-selling product (by total sales)
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Sales by product
sales_by_product = df.groupby('Product')['Total_Sales'].sum()

# Average sales
average_sales = df['Total_Sales'].mean()

# -------------------------------
# Day 5: Create Report
# -------------------------------

print("\n===== SALES REPORT =====")
print(f"Total Revenue: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Best-Selling Product: {best_product}")

print("\nSales by Product:")
print(sales_by_product)

# Save report to file
with open("analysis_report.txt", "w") as f:
    f.write("SALES ANALYSIS REPORT\n")
    f.write("=====================\n")
    f.write(f"Total Revenue: ₹{total_sales:,.2f}\n")
    f.write(f"Average Sales: ₹{average_sales:,.2f}\n")
    f.write(f"Best-Selling Product: {best_product}\n\n")
    f.write("Sales by Product:\n")
    f.write(str(sales_by_product))
