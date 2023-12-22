import csv
import json

csv_file_path = 'price_list.csv'  # Replace with your CSV file path

merged_data = []

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Read the header row

    for index, row in enumerate(csv_reader, start=1):
        if len(row) >= 2:  # Ensure at least two columns exist in the row
            product_name = row[0]  # Replace with the column index for product names
            product_price = float(row[1])  # Replace with the column index for product prices

            if product_name and product_price:
                # Create a dictionary matching the JSON fixture structure
                csv_data = {
                    "model": "items.myproducts",
                    "pk": index,
                    "fields": {
                        "code": product_name.upper().replace(" ", "_"),
                        "product_name": product_name,
                        "category_id": 1,
                        "brand": 1,
                        "unit": 1,
                        "price": product_price,
                        "cost": 0,
                        "qty": 100,
                        "product_desc": f"Delicious {product_name} bread"  # Modify the description as needed
                    }
                }
                merged_data.append(csv_data)

# Write merged data into initial_data.json
with open('initial_data.json', 'w') as json_file:
    json.dump(merged_data, json_file, indent=4)

# Print the merged data (list of dictionaries)
for item in merged_data:
    print(item)
