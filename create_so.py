import random
from datetime import datetime, timedelta
from common import * 

# Helper function to create fake sale orders in batches
def create_sale_orders_in_batch(batch_size, customer_ids, product_ids, state='sale'):
    for _ in range(batch_size):
        partner_id = random.choice(customer_ids)
        product_count = random.randint(1, 5)
        selected_products = random.sample(product_ids, product_count)
        qty_list = [random.randint(1, 10) for _ in range(product_count)]
        price_list = [random.uniform(50, 500) for _ in range(product_count)]
        
        sale_order_vals = {
            'partner_id': partner_id,
            'state': state,
            'date_order': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S'),
        }
        sale_order_id = models.execute_kw(db, uid, password, 'sale.order', 'create', [sale_order_vals])
        
        for product_id, qty, price in zip(selected_products, qty_list, price_list):
            sale_order_line_vals = {
                'order_id': sale_order_id,
                'product_id': product_id,
                'product_uom_qty': qty,
                'price_unit': price,
            }
            models.execute_kw(db, uid, password, 'sale.order.line', 'create', [sale_order_line_vals])

# Main function to execute batch processing
def generate_fake_data(total_sale_orders, sale_order_batch_size):
    # Generate 100,000 fake customers in batches
    customer_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])
    product_ids = models.execute_kw(db, uid, password, 'product.product', 'search', [[]])
    # Generate 10,000,000 fake sale orders in batches
    for _ in range(total_sale_orders // sale_order_batch_size):
        create_sale_orders_in_batch(sale_order_batch_size, customer_ids, product_ids)
        print(f"Created sale orders, processing {_ * sale_order_batch_size} so far.")
        
def generate_fake_quotation_data(total_sale_orders, sale_order_batch_size):
    # Generate 100,000 fake customers in batches
    customer_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])
    product_ids = models.execute_kw(db, uid, password, 'product.product', 'search', [[]])
    # Generate 10,000,000 fake sale orders in batches
    for _ in range(total_sale_orders // sale_order_batch_size):
        create_sale_orders_in_batch(sale_order_batch_size, customer_ids, product_ids, 'draft')
        print(f"Created sale quotation orders, processing {_ * sale_order_batch_size} so far.")
