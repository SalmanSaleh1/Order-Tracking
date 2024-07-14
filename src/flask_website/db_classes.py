import db_connection

app = db_connection.app
db = db_connection.db
bcrypt = db_connection.bcrypt

class Department(db.Model):
    __tablename__ = 'department'
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Department {self.department_name}>'

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'), nullable=False)
    department = db.relationship('Department', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'<User {self.user_name}>'

class AddOrder(db.Model):
    __tablename__ = 'addOrders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    order_name = db.Column(db.String(255), nullable=True)
    order_description = db.Column(db.String(255), nullable=True)
    order_state = db.Column(db.String(255), nullable=True)
    order_date = db.Column(db.DateTime, nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'), nullable=False)
    user = db.relationship('User', backref=db.backref('addOrders', lazy=True))
    department = db.relationship('Department', backref=db.backref('addOrders', lazy=True))

    def __repr__(self):
        return f'<AddOrder {self.order_name}>'

class Order(db.Model):
    __tablename__ = 'Orders'
    order_id = db.Column(db.Integer, db.ForeignKey('addOrders.order_id'), primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'), primary_key=True)
    addOrder = db.relationship('AddOrder', backref=db.backref('orders', lazy=True))
    department = db.relationship('Department', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f'<Order {self.order_id}>'