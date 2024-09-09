# from create_customer import generate_fake_data as generate_customer_fake_data
# from create_product import generate_fake_data as generate_product_fake_data
# from create_so import generate_fake_data as generate_so_fake_data

# TOTAL_CUSTOMERS = 2000
# TOTAL_PRODUCTS = 100000
# TOTAL_SO = 10000000
# BATCH_SIZE = 1000  # Adjust this batch size
    

# generate_customer_fake_data(TOTAL_CUSTOMERS, BATCH_SIZE)
# generate_product_fake_data(TOTAL_PRODUCTS, BATCH_SIZE)
# generate_so_fake_data(TOTAL_SO, BATCH_SIZE)

"""
Using faker food to generate your food data
https://pypi.org/project/faker_food/


Project description
faker_food: food provider for Faker
An add-on provider for the Python Faker module to generate random and/or fake data for food-related categories.

Description
faker_food provides food-related fake data for testing purposes.

Installation
Install the faker-food library with your package management tool.

pip install faker-food
Usage
Add as a provider to your Faker instance:

>>> from faker import Faker
>>> from faker_food import FoodProvider
>>> fake = Faker()
>>> fake.add_provider(FoodProvider)
Now you can start to generate data:

>>> fake.dish()
>>> fake.dish_description()
>>> fake.ethnic_category()
>>> fake.fruit()
>>> fake.ingredient()
>>> fake.measurement()
>>> fake.metric_measurement()
>>> fake.measurement_size()
>>> fake.spice()
>>> fake.sushi()
>>> fake.vegetable()

"""
