# ----------------------
import os 

# ----------------------
from flask import Flask, render_template, flash, redirect, url_for, request
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
    # Fetch orders sorted by order_id in descending order (newest first)
    last_orders = AddOrder.query.order_by(AddOrder.order_id.desc()).limit(6).all()
    return render_template('orders.html', last_orders=last_orders)

@app.route('/edit_order/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = AddOrder.query.get_or_404(order_id)
    form = AddOrderForm(obj=order)
    if form.validate_on_submit():
        order.order_name = form.order_name.data
        order.order_description = form.order_description.data
        order.department_name = form.department_name.data
        order.order_state = form.order_state.data
        db.session.commit()
        flash('Order updated successfully!', 'success')
        return redirect(url_for('orders'))
    return render_template('edit_order.html', form=form, order=order)


@app.route('/order_history')
def order_history():
    # Retrieve orders that are in the 'completed' state
    completed_orders = AddOrder.query.filter_by(order_state='completed').order_by(AddOrder.order_date.desc()).all()
    return render_template('order_history.html', completed_orders=completed_orders)


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


@app.route('/view_order/<int:order_id>')
def view_order(order_id):
    # Retrieve the order by its ID
    order = AddOrder.query.get_or_404(order_id)
    return render_template('view_order.html', order=order)


# api route 
@app.route('/api/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = AddOrder.query.get(order_id)
    if order:
        return {
            'order_id': order.order_id,
            'order_name': order.order_name,
            'order_description': order.order_description,
            'department_name': order.department_name,
            'order_state': order.order_state,
            'order_date': order.order_date.strftime('%Y-%m-%d %H:%M:%S')
        }, 200
    return {'error': 'Order not found'}, 404

@app.route('/order_info')
def order_info():
    return render_template('order_info.html')


@app.route('/delete_order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = AddOrder.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    flash('Order deleted successfully!', 'success')
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
