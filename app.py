from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})


@app.route('/products')
def get_products():
    return jsonify({"products": products})


@app.route('/products/<string:name>')
def get_product(name):
    products_found = [product for product in products if product['name'] == name]
    if len(products_found) > 0:
        return jsonify({"product": products_found[0]})
    return jsonify({"message": "Product Not Found"})


@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
    }
    products.append(new_product)
    return jsonify({"product": new_product})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
