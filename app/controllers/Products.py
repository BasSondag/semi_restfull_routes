from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')

    def index(self):
        product = self.models['Product'].display_all()
        return self.load_view('index.html', product = product)

    def new_prod(self):
        return self.load_view('addnew.html')

    def edit_prod(self, id):
        product = self.models['Product'].show_prod(id)
        return self.load_view('edit.html', product = product)  

    def show_prod(self, id):
        product = self.models['Product'].show_prod(id)
        return self.load_view('show.html', product = product)

    def create(self):
        product_details = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        create_status = self.models['Product'].create(product_details)
        if create_status['status'] == True:
            return redirect('/')
        else:
            for message in create_status['errors']:
                flash(message, "regis_errors")
                return redirect('/addnew')

    def update(self):
        update_details = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'id': request.form['id']
        }
        product = self.models['Product'].update_prod(update_details)
        return redirect('/')

    def delete(self, id):
        self.models['Product'].delete_prod_by_id(id)
        return redirect('/') 

