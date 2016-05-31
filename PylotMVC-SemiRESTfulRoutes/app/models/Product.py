from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
        self.__query = ''
        self.__data = {}

    def exec_query(self, query, data):
        return self.db.query_db(query, data)

    def get_products(self):
        self.__query = "SELECT id, name, description, price FROM products"
        self.__data = {}
        return self.exec_query(self.__query, self.__data)

    def get_product_detail(self, id):
        self.__query = "SELECT name, description, price FROM products where id = :id"
        self.__data = {
            'id': id
        }
        return self.exec_query(self.__query, self.__data)

    def remove_product(self, id):
        self.__query = "DELETE FROM products where id = :id"
        self.__data = {
            'id': id
        }
        return self.exec_query(self.__query, self.__data)

    def update_product(self, pdt):
        self.__query = "UPDATE products SET name = :name, description = :description, price = :price, modified_at = NOW() WHERE id = :id"
        self.__data = {
            'id': pdt['id'],
            'name': pdt['name'],
            'description': pdt['description'],
            'price': pdt['price']
        }
        return self.exec_query(self.__query, self.__data)

    def add_product(self, pdt):
        self.__query = "INSERT INTO products (name, description, price, created_at, modified_at) VALUES (:name, :description, :price, NOW(), NOW())"
        self.__data = {
            'name': pdt['name'],
            'description': pdt['description'],
            'price': pdt['price']
        }
        return self.exec_query(self.__query, self.__data)
