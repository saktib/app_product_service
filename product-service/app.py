import os
from flask import Flask, jsonify, render_template, request, url_for, redirect
from models import Product, db

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# Routes
@app.route('/')
def get_all_products():
    products = Product.query.all()
    # Serialize for JSON
    return jsonify([product.serialize() for product in products])


@app.route('/product', methods=['POST'])
def products():
    data = request.get_json()  # Get data from request body
    print(data)

    if not data or not data.get('action') or not data.get('product_code'):
        return "Missing required fields", 400  # Bad request
    
    if data.get('action') == 'create_product':
        if not data.get('name') or not data.get('price'):
             return "Missing Product Name or Price fields", 400 
        
        product = Product(name=data['name'], description=data.get(
                'description'), price=data['price'], quantity=data['quantity'], product_code=data['product_code'])
        db.session.add(product)
        db.session.commit()
        return jsonify(product.serialize())  # Return created product
    
    if data.get('action') == 'update_product':
        product = Product.query.filter_by(product_code=data['product_code']).first()
        if product is None:
                return "Product not found", 404

        if data.get('name'):
                product.name = data['name']
        if data.get('description'):
                product.description = data['description']
        if data.get('price'):
                product.price = data['price']
        if data.get('quantity'):
                product.quantity = data['quantity']

        db.session.commit()
        return jsonify(product.serialize())
    
    if data.get('action') == 'delete_product':
        product = Product.query.filter_by(product_code=data['product_code']).first()
        if product is None:
                return "Product not found", 404
        
        db.session.delete(product)
        db.session.commit()
        return "Product deleted", 204
    
    if data.get('action') == 'get_product_by_id':
        product = Product.query.filter_by(product_code=data['product_code']).first()
        if product is None:
                return "Product not found", 404
        
        return jsonify(product.serialize())
        

# Utility method for product serialization


def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'price': self.price,
        'quantity': self.quantity
    }


Product.serialize = serialize  # Add serialize method to Product class

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(host='0.0.0.0', debug=True)
