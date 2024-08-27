import csv
import random
import faker

# Initialize Faker for generating random product names
fake = faker.Faker()

# File name for the CSV
file_name = 'products.csv'

# Number of rows
# num_rows = 1_000_000

# Options for the unit column
# units = ['kg', 'each']

# Open a CSV file for writing
# with open(file_name, mode='w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Write the header
#     writer.writerow(['name', 'unit', 'price'])
    
#     # Generate rows of data
#     for _ in range(num_rows):
#         name = fake.word().capitalize()
#         unit = random.choice(units)
#         price = round(random.uniform(0.5, 1000.0), 2)  # Price between 0.5 and 1000, with 2 decimal places
#         writer.writerow([name, unit, price])

# print(f'{num_rows} rows of product data have been written to {file_name}.')


from backend.database.config import db

with open('products.csv', mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.DictReader(file)
    
    # Prepare the list for data
    data = []
    
    for row in csv_reader:
        # Ensure each row is a dictionary
        if isinstance(row, dict):
            # Optionally convert the price to a float
            row['price'] = float(row['price'])
            data.append(row)
        else:
            raise TypeError(f"Expected a dict, but got {type(row)} instead.")
    
    # Insert data into MongoDB if the list is not empty
    if data:
        db.product.insert_many(data)
    else:
        print("No data found to insert.")

print(f"Inserted {len(data)} records into MongoDB.")
