from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from sqlalchemy.orm import validates
from datetime import datetime
from pytz import timezone

db = SQLAlchemy()

class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', backref='vendor', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone('Africa/Nairobi')))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone('Africa/Nairobi')), onupdate=datetime.now(timezone('Africa/Nairobi')))

class Sweet(db.Model):
    __tablename__ = 'sweet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', backref='sweet', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone('Africa/Nairobi')))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone('Africa/Nairobi')), onupdate=datetime.now(timezone('Africa/Nairobi')))

class VendorSweet(db.Model):
    __tablename__ = 'vendor_sweet'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone('Africa/Nairobi')))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone('Africa/Nairobi')), onupdate=datetime.now(timezone('Africa/Nairobi')))

    @validates('price')
    def validate_price(self, key, price):
        if price is None:
            raise AssertionError('No price provided')
        if price < 0:
            raise AssertionError('Price cannot be a negative number')
        return price

class VendorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        include_relationships = True
        load_instance = True

class SweetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Sweet
        include_relationships = True
        load_instance = True

class VendorSweetSchema(SQLAlchemyAutoSchema):
    vendor = fields.Nested('VendorSchema', only=('id', 'name'))
    sweet = fields.Nested('SweetSchema', only=('id', 'name'))
    class Meta:
        model = VendorSweet
        include_relationships = True
        load_instance = True
