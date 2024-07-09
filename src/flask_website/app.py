from flask import Flask , render_template


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/order_history')
def order_history():
    return render_template('order_history.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
