import csv
import datetime

products_map = {"product_id": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010"],
                "product_name": ["Wireless Headphones", "Laptop Backpack", "Bluetooth Speaker", "USB Flash Drive", "Mobile Phone Case", "Wireless Mouse", "Laptop Stand", "HDMI Cable", "Smartphone", "External Hard Drive"],
                "product_price": [100, 60, 50, 20, 15, 30, 40, 15, 600, 100 ]}

transaction_report = []
transaction_id = 1
transaction_date = datetime.date.today().strftime("%d-%m-%Y")

with open("product_sales.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        product_id = line.strip() #to remove newline  whitespace

        if product_id in products_map["product_id"]:
            index = products_map["product_id"].index(product_id)
            product_name = products_map["product_name"][index]
            product_price = products_map["product_price"][index]

            # Append to transaction report
            transaction_report.append([transaction_date, transaction_id, product_id, product_name, product_price])


            transaction_id += 1


with open("product_sales.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # write the Headers first
    csv_writer.writerow(["Transaction Date", "Transaction ID", "Product ID", "Product Name", "Product Price"])

    csv_writer.writerows(transaction_report)

# Additional Analysis
import pandas as pd

df = pd.read_csv("product_sales.csv")
sales = df.groupby("Product ID").agg(Total_Amt=("Product Price", "sum"), Number_of_transactions=("Product ID", "size")).sort_values(by="Total_Amt", ascending=False)
print(sales)
