from create_so import generate_fake_data as generate_so_fake_data

TOTAL_SO = 100000
BATCH_SIZE = 1000  # Adjust this batch size
    

# generate_customer_fake_data(TOTAL_CUSTOMERS, BATCH_SIZE)
# generate_product_fake_data(TOTAL_PRODUCTS, BATCH_SIZE)
generate_so_fake_data(TOTAL_SO, BATCH_SIZE)
