from datetime import datetime
from db_connection import db

class AddOrder(db.Model):
    __tablename__ = 'addOrders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_name = db.Column(db.String(255), nullable=False)
    order_description = db.Column(db.String(255))
    department_name = db.Column(db.String(255), nullable=False)
    order_state = db.Column(db.String(255), default='waiting')
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<AddOrder {self.order_name}>"

class Order(db.Model):
    __tablename__ = 'Orders'
    order_id = db.Column(db.Integer, db.ForeignKey('addOrders.order_id'), primary_key=True)
    department_name = db.Column(db.String(255), primary_key=True)

    addOrder = db.relationship('AddOrder', backref=db.backref('orders', lazy=True))