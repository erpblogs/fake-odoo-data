from common import * 
from faker import Faker

# Initialize Faker for English and Vietnamese
fake_en = Faker()
fake_vi = Faker('vi_VN')

def get_random_name_and_email(locale='en'):
    if locale == 'vi':
        name = fake_vi.name()
        email = fake_vi.email()
    else:
        name = fake_en.name()
        email = fake_en.email()
    return name, email

# Helper function to create fake customers in batches
def create_customers_in_batch(batch_size):
    for _ in range(batch_size):
        name, email = get_random_name_and_email()
        partner_vals = {
            'name': name,
            'email': email,
            'customer_rank': 1,  # Mark the partner as a customer
        }
        models.execute_kw(db, uid, password, 'res.partner', 'create', [partner_vals])
    return True 

# Main function to execute batch processing
def generate_fake_data(total_customers, customer_batch_size):
    print(f"Start create customers!")
    for _ in range(total_customers // customer_batch_size):
        create_customers_in_batch(customer_batch_size)
        print(f"Created customers, processing {_ * customer_batch_size} so far.")

    
