from openpyxl import Workbook
from faker import Faker

# Create Faker instance
fake = Faker()

# Create a new Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Random Data"

# Define header
headers = ["ID", "Name", "Email", "Phone", "City"]
ws.append(headers)

# Generate 100 rows of random data
for i in range(1, 101):
    row = [
        i,
        fake.name(),
        fake.email(),
        fake.phone_number(),
        fake.city()
    ]
    ws.append(row)

# Save the workbook
wb.save("random_data.xlsx")

print("Excel sheet 'random_data.xlsx' created successfully.")