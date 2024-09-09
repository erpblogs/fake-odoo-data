import csv
from common import * 


# Path to your CSV file
csv_file_path = 'amazon_categories.csv'  # Ensure this file is in the correct path


def import_product_category_data():
    # Read the CSV file into an array (list of dictionaries)
    categories = []
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories.append(row)

    # Fetch all existing category names in one request
    existing_categories = models.execute_kw(db, uid, password, 'product.category', 'search_read', 
                                            [[]],  # Empty list to fetch all categories
                                            {'fields': ['name']})

    # Convert to a set of category names for faster lookups
    existing_category_names = {category['name'] for category in existing_categories}

    # Now process the CSV data
    for category in categories:
        category_name = category['category_name']

        # Check if the category already exists in the set
        if category_name not in existing_category_names:
            # Create a new product category
            category_id = models.execute_kw(db, uid, password, 'product.category', 'create', [{
                'name': category_name
            }])
            print(f"Created category: {category_name} with ID {category_id}")
        else:
            print(f"Category {category_name} already exists")
                
import_product_category_data()