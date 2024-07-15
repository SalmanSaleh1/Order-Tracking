from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect, render_template, url_for
from db_connection import db  # Import SQLAlchemy instance from db_connection
from db_classes import AddOrder
from datetime import datetime

class AddOrderForm(FlaskForm):
    order_name = StringField('Order Name', validators=[DataRequired()])
    order_description = StringField('Order Description')
    department_name = StringField('Department Name', validators=[DataRequired()])
    submit = SubmitField('Add Order')

def add_order():
    form = AddOrderForm()
    
    if form.validate_on_submit():
        order_name = form.order_name.data
        order_description = form.order_description.data
        department_name = form.department_name.data
        
        # Create a new AddOrder instance with form data
        new_order = AddOrder(
            order_name=order_name,
            order_description=order_description,
            department_name=department_name,
            order_date=datetime.utcnow()  # Assuming you want to timestamp the order
        )
        
        # Add new order to the database
        try:
            db.session.add(new_order)
            db.session.commit()
            db.session.close()
            return redirect(url_for('orders'))  # Redirect to orders page after successful submission
        except Exception as e:
            print(f"Failed to add order to database: {e}")
            db.session.rollback()
            db.session.close()
    
    return render_template('add_order.html', form=form)
