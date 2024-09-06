import xmlrpc.client

# Set up your Odoo credentials and endpoint
url = "https://localhost"
db = "database_name"
username = "account"
password = "password"

# Connect to Odoo
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")