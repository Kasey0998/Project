from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(15), unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20))  # admin, marketing, sales

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    apartments = db.relationship('Apartment', backref='building', lazy=True)

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), nullable=False)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    unit_number = db.Column(db.String(50))
    price = db.Column(db.Float)
    area_sqft = db.Column(db.Float)
    rooms = db.Column(db.Integer)
    is_sold = db.Column(db.Boolean, default=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15), unique=True)
    interested = db.Column(db.Boolean)
    status = db.Column(db.String(20))  # open, sold, not_interested
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'))
    added_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'))

def create_default_admin():
    if not User.query.filter_by(role='admin').first():
        admin = User(name='Admin', email='admin@example.com', phone='9999999999', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
