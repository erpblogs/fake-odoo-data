import random
from common import * 

from faker import Faker

import faker_commerce

fake_en = Faker()
fake_en.add_provider(faker_commerce.Provider)

# Initialize Faker for English and Vietnamese
fake_vi = Faker('vi_VN')
fake_vi.add_provider(faker_commerce.Provider)


# Helper function to create fake products in batches
def create_products_in_batch(batch_size, category_id, locale='en'):
    fake = fake_en if locale == 'en' else fake_vi
    for _ in range(batch_size):
        product_name = fake.ecommerce_name()
        product_vals = {
            'name': product_name,
            'purchase_ok': True,
            'list_price': random.uniform(50, 500),
            'description_sale': False,
            'categ_id': category_id,
        }
        models.execute_kw(db, uid, password, 'product.product', 'create', [product_vals])
    return True

# Function to generate product categories and products
def generate_fake_data(total_products, product_batch_size):
    print(f"Start create products !")
    categories = models.execute_kw(db, uid, password, 'product.category', 'search', [[]])
    if not categories:
        print("No categories found.")
        return
    # Calculate the total number of products per category
    products_per_category = total_products // len(categories) or 1
    
    # Create products under each category
    for category in categories:
        num_batches = products_per_category // product_batch_size
        
        for _ in range(num_batches):
            create_products_in_batch(product_batch_size, category)
            print(f"Created {product_batch_size} products for category {category}")

        # Handle any remainder products (if total products per category is not divisible by batch size)
        remainder = products_per_category % product_batch_size
        if remainder > 0:
            create_products_in_batch(remainder, category)
            print(f"Created {remainder} remaining products for category {category}")

