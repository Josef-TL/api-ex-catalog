import os
import database
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


database.init()

@app.route('/')
def index():
    return "Welcome to API :)"

@app.route('/products')
def get_products():
    try:
        res = database.read_all()
        return jsonify(res), 200
    except:
        return jsonify(message="Connection Error"), 500

# Get one
@app.route('/products/<int:id>')
def get_member(id):
    res = database.read(id)

    if not res:
        return jsonify(message="Products not found"), 404

    return jsonify(res), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0',port=port)