
from system.core.model import Model
import re
class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def create(self,product):
        VALUE_REGEX = re.compile(r'^[0-99]+\.+[0-99]*$')
        errors = []
        if not product['price']:
            errors.append('price can not be blanck')
        elif not VALUE_REGEX.match(product['price']):
            errors.append('price can only be in numbers with 2 decimal')
        if errors:
            return {"status": False, "errors": errors}
        else:
            query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
            data = [product['name'], product['description'], product['price']]
            products = self.db.query_db(query, data)
            return {"status": True}
        
    def display_all(self):
        query = "SELECT * FROM products"
        return self.db.query_db(query)

    def show_prod(self, id):
        query = "SELECT * FROM products WHERE id = %s"
        data = [id]
        return self.db.query_db(query, data)

    def delete_prod_by_id(self, id):
        query = " DELETE FROM products WHERE id = %s"
        data =[id]
        return self.db.query_db(query, data)  

    def update_prod(self, product):
        query = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"  
        data = [product['name'], product['description'], product['price'], product['id']]
        return self.db.query_db(query, data)