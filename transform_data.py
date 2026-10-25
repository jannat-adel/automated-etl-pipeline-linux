import os
import glob
import csv

raw_dir = "raw_data"
processed_dir = "processed_data"
os.makedirs(processed_dir, exist_ok=True)

list_of_files = glob.glob(os.path.join(raw_dir, 'sales_data_*.csv'))
if not list_of_files:
    print("No raw data files found!")
    exit()

latest_file = max(list_of_files, key=os.path.getctime)
print(f"Processing file: {latest_file}")


processed_rows = []
with open(latest_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        
        price = float(row['price'])
        quantity = int(row['quantity'])
        total_price = price * quantity

        
        row['total_price'] = round(total_price, 2)
        processed_rows.append(row)


output_file = os.path.join(processed_dir, os.path.basename(latest_file).replace("sales_data", "processed_sales"))

fieldnames = ["product_id", "product_name", "price", "quantity", "total_price"]
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_rows)

print(f"Data transformed successfully and saved at: {output_file}")
