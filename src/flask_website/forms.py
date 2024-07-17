from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

# Define Flask-WTF form for adding orders
class AddOrderForm(FlaskForm):
    order_name = StringField('Order Name', validators=[DataRequired()])
    order_description = TextAreaField('Order Description')
    department_name = StringField('Department Name', validators=[DataRequired()])
    order_state = SelectField('Order State', choices=[('waiting', 'Waiting'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='waiting')