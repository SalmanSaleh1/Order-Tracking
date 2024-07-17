# ----------------------
import os 

# ----------------------
from flask import Flask, render_template, flash, redirect, url_for
from dotenv import load_dotenv


# ----------------------
from forms import AddOrderForm
import db_connection
from db_classes import AddOrder

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

# Route for adding an order
@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    form = AddOrderForm()
    if form.validate_on_submit():
        order = AddOrder(
            order_name=form.order_name.data,
            order_description=form.order_description.data,
            department_name=form.department_name.data,
            order_state=form.order_state.data
        )
        db.session.add(order)
        db.session.commit()
        flash('Order added successfully!', 'success')
        return redirect(url_for('orders'))  # Assuming 'orders' is the route to display all orders
    return render_template('add_order.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
