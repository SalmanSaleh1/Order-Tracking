# ----------------------
import os 

# ----------------------
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
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


# Original route for displaying the orders page
@app.route('/orders')
def orders():
    return render_template('orders.html')


# Route to fetch orders via AJAX
@app.route('/api/orders')
def api_orders():
    last_orders = AddOrder.query.filter(AddOrder.order_state != 'completed').order_by(AddOrder.order_id.desc()).limit(6).all()
    orders_list = [{
        'order_id': order.order_id,
        'order_name': order.order_name,
        'order_description': order.order_description,
        'department_name': order.department_name,
        'order_state': order.order_state
    } for order in last_orders]
    
    return jsonify(orders=orders_list)


# Route for change order state with ajax
@app.route('/change_order_state/<int:order_id>', methods=['POST'])
def change_order_state(order_id):
    order = AddOrder.query.get(order_id)
    if order:
        new_state = request.form.get('new_state')
        order.order_state = new_state
        db.session.commit()
        return jsonify({'success': True, 'order_id': order_id, 'new_state': new_state})
    return jsonify({'success': False}), 404


# Route for edit order information
@app.route('/edit_order/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = AddOrder.query.get_or_404(order_id)
    
    if request.method == 'GET':
        form = AddOrderForm(obj=order)
        return render_template('edit_order.html', form=form, order=order)
    
    if request.method == 'POST':
        form = AddOrderForm()
        if form.validate_on_submit():
            order.order_name = form.order_name.data
            order.order_description = form.order_description.data
            order.department_name = form.department_name.data
            order.order_state = form.order_state.data
            db.session.commit()
            return jsonify({'success': True, 'message': 'Order updated successfully!'})
        
        return jsonify({'success': False, 'errors': form.errors})


# Route for display order history 
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


# Route for view order page
@app.route('/view_order/<int:order_id>')
def view_order(order_id):
    # Retrieve the order by its ID
    order = AddOrder.query.get_or_404(order_id)
    return render_template('view_order.html', order=order)


# Route for Display information API
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


# Route for send order information to API
@app.route('/order_info')
def order_info():
    return render_template('order_info.html')


# Route for delete orders
@app.route('/delete_order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = AddOrder.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    flash('Order deleted successfully!', 'success')
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
