import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv(r"C:\Users\dhans\Downloads\sales_data.csv")

# Step 2: Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Check basic information
print("\nDataset Information:")
print(df.info())

# Step 4: Handle missing values
# Filling missing numerical values with 0
df.fillna(0, inplace=True)

# Step 5: Calculate Total Sales
total_sales = df['Total_Sales'].sum()

# Step 6: Find best-selling product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
best_product_sales = df.groupby('Product')['Total_Sales'].sum().max()

# Step 7: Calculate average sales
average_sales = df['Total_Sales'].mean()

# Step 8: Generate report
print("\nSALES DATA ANALYSIS REPORT")
print("----------------------------")
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales:.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Sales of Best Product: {best_product_sales}")
