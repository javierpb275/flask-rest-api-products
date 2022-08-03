from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run(debug=True, port=4000)
