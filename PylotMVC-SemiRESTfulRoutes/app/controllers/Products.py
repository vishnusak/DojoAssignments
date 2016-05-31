from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.__db = self.models['Product']

    def index(self):
        db_products = self.__db.get_products()
        return self.load_view('index.html', products=db_products)

    def new(self):
        return self.load_view('add.html')

    def create(self):
        pdt = {
            'name': request.form['name'],
            'price': request.form['price'],
            'description': request.form['description']
        }

        self.__db.add_product(pdt)

        return redirect('/')

    def show(self, id):
        pdt_detail = self.__db.get_product_detail(id)[0]
        pdt_detail['id'] = id
        return self.load_view('show.html', pdt=pdt_detail)

    def edit(self, id):
        pdt_detail = self.__db.get_product_detail(id)[0]
        pdt_detail['id'] = id
        return self.load_view('edit.html', pdt=pdt_detail)

    def update(self, id):
        pdt = {
            'id': id,
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }

        self.__db.update_product(pdt)

        return redirect('/')

    def destroy(self, id):
        self.__db.remove_product(id)
        
        return redirect('/')
