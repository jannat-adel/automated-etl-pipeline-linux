import os
import csv
from datetime import datetime


output_dir = "raw_data"
os.makedirs(output_dir, exist_ok=True)


file_name = f"sales_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
file_path = os.path.join(output_dir, file_name)

data = [
    ["product_id", "product_name", "price", "quantity"],
    [101, "Laptop", 1200.50, 2],
    [102, "Mouse", 25.00, 10],
    [103, "Keyboard", 45.75, 5],
    [104, "Monitor", 300.00, 3]
]

with open(file_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Data successfully generated and saved at: {file_path}")
