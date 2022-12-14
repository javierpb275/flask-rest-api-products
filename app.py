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
    return jsonify({"new_product": new_product})


@app.route('/products/<string:name>', methods=['PUT'])
def update_product(name):
    products_found = [product for product in products if product['name'] == name]
    if len(products_found) <= 0:
        return jsonify({"message": "Product Not Found"})
    products_found[0]['name'] = request.json['name']
    products_found[0]['price'] = request.json['price']
    products_found[0]['quantity'] = request.json['quantity']
    return jsonify({"updated_product": products_found[0]})


@app.route('/products/<string:name>', methods=['DELETE'])
def delete_product(name):
    products_found = [product for product in products if product['name'] == name]
    if len(products_found) <= 0:
        return jsonify({"message": "Product Not Found"})
    products.remove(products_found[0])
    return jsonify({"deleted_product": products_found[0]})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
