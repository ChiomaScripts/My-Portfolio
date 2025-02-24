# Product Sales Automation

## 📌 Project Overview
This project automates the process of reading product sales transaction data from a text file (`product_sales.txt`), mapping product IDs to their corresponding names and prices, and generating a structured CSV report (`product_sales.csv`). It also performs additional sales analysis using **Pandas**.

## 🔧 Features
- Reads a list of product sales transactions from a text file.
- Assigns sequential transaction IDs.
- Fetches the current date for record-keeping.
- Maps product IDs to their respective names and prices.
- Exports the processed data to a CSV file.
- Performs sales analysis, grouping transactions and calculating total revenue per product.

## 📂 Project Structure
```
|-- product_sales.txt   # Input file containing product sales transactions
|-- product_sales.csv   # Output file with processed transaction data
|-- sales_analysis.py   # Python script performing sales aggregation 
|-- main.py             # Main script handling file processing & CSV generation
|-- README.md           # Project documentation 
```

## 🚀 Technologies Used
- **Python**
- **CSV Handling** (`csv` module)
- **Datetime** (`datetime` module)
- **Data Analysis** (`pandas`)

## 📜 Usage

1. **Navigate to the Directory**
```
https://github.com/ChiomaScripts/My-Portfolio.git
```
cd My-Portfolio/product-sales-automation


2. **Install Dependencies**
   Ensure you have Python installed (preferably 3.x) and install the required package `pip install pandas`

3. **Run the Script**
   `python product_sales_tracker-project.py`

4. **View Results**
   - Processed transaction data will be saved in `product_sales.csv`.
   - Sales summary will be displayed in the terminal.

## 🛠 Future Improvements
- Implement error handling for missing or incorrect product IDs.
- Allow user input for specifying the sales data file.
- Create a graphical dashboard for better visualisation.
