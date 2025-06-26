from app import db

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    flats = db.relationship('Flat', backref='apartment', lazy=True)

class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    bhk_type = db.Column(db.String(10), nullable=False)  # '1BHK', '2BHK', '3BHK'
    status = db.Column(db.String(20), default='available')  # 'available', 'sold'

class ClientLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    interested_apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'))
    status = db.Column(db.String(50), default='pending')  # 'pending', 'sold', 'not_interested'
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

    apartment = db.relationship('Apartment', backref='leads')
