import os
import database
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


database.init()

@app.route('/')
def index():
    return "Welcome to API :)"

# Get All
@app.route('/products')
def get_products():
    try:
        res = database.read_all()
        return jsonify(res), 200
    except:
        return jsonify(message="Connection Error"), 500

# Get one
@app.route('/products/<int:id>')
def get_product(id):
    res = database.read(id)

    if not res:
        return jsonify(message="Products not found"), 404

    return jsonify(res), 200


@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data:
        return jsonify(message="Data is required"), 400
    
    if database.read(data['product_id']):
        return jsonify(message="Product already exists"), 409

    id = database.create(data)

    if not id:
        return jsonify(message="Connection Error"), 500
    
    return jsonify({'message': f'Product created successfully'}), 201



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0',port=port)