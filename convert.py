import csv
import json
import re
# Load JSON data
with open("indices.json", "r") as file:
    etf_data = json.load(file)

# Define CSV file path
csv_file_path = "indices.csv"


# unique_bonds = []
# unique_names = set()

# for data in etf_data:
#     if data['Name'] not in unique_names:
#         unique_bonds.append(data)
#         unique_names.add(data['Name'])

# print(unique_bonds)

def extract_bond_info(name):
    parts = name.split("\n")
    ticker = parts[0] if len(parts) > 0 else ""
    na = parts[1] if len(parts) > 1 else ""

    
    return ticker, na

with open(csv_file_path, "w", newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Create CSV writer
    writer.writerow(["ticker", "name"])
    
    # Iterate over unique bonds data and write rows
    for data in etf_data:
        ticker, na = extract_bond_info(data["Name"])
        
        row = [
            ticker,
            na
        ]
        writer.writerow(row)



print("CSV file has been written successfully.")
