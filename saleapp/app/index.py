from flask import Flask, render_template, request
from dao import load_categories, load_products

app = Flask(__name__)

@app.route('/')
def index():
    kw = request.args.get("kw")
    cates = load_categories()
    products = load_products(kw)
    return render_template('index.html', categories=cates, products = products)


@app.route('/hello')
def hello():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug=True)