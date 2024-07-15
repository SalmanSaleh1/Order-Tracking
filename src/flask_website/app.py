# ----------------------
import os 

# ----------------------
from flask import Flask, render_template
from dotenv import load_dotenv


# ----------------------

import forms
import db_connection

app = db_connection.app
db = db_connection.db
bcrypt = db_connection.bcrypt



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/order_history')
def order_history():
    return render_template('order_history.html')

# Route to call add_order function from forms.py
@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    return forms.add_order()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
