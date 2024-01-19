#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Vendor, Sweet, VendorSweet, VendorSchema, SweetSchema, VendorSweetSchema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
sweet_schema = SweetSchema()
sweets_schema = SweetSchema(many=True)
vendor_sweet_schema = VendorSweetSchema()
vendor_sweets_schema = VendorSweetSchema(many=True)

@app.route('/')
def home():
    return ('''<h1> Sweets Vendors</h1>
                <h2>Welcome to the Sweets Vendors!</h2>''')

@app.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify(vendors_schema.dump(vendors))

@app.route('/vendors/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    vendor = Vendor.query.get(vendor_id)
    if vendor is None:
        return jsonify({'error': 'Vendor not found'}), 404
    if vendor.vendor_sweets is None:
        vendor.vendor_sweets = []
    return jsonify(vendor_schema.dump(vendor))

@app.route('/sweets', methods=['GET'])
def get_sweets():
    sweets = Sweet.query.all()
    return jsonify(sweets_schema.dump(sweets))

@app.route('/sweets/<int:sweet_id>', methods=['GET'])
def get_sweet(sweet_id):
    sweet = Sweet.query.get(sweet_id)
    if sweet is None:
        return jsonify({'error': 'Sweet not found'}), 404
    if sweet.vendor_sweets is None:
        sweet.vendor_sweets = []
    return jsonify(sweet_schema.dump(sweet))

@app.route('/vendor_sweets', methods=['POST'])
def create_vendor_sweet():
    if not request.json or 'price' not in request.json or 'vendor_id' not in request.json or 'sweet_id' not in request.json:
        abort(400)
    vendor_sweet = VendorSweet(price=request.json['price'], vendor_id=request.json['vendor_id'], sweet_id=request.json['sweet_id'])
    db.session.add(vendor_sweet)
    db.session.commit()
    
    data = vendor_sweet_schema.dump(vendor_sweet)
    data['name'] = vendor_sweet.sweet.name
    
    return jsonify(data), 201


@app.route('/vendor_sweets/<int:vendor_sweet_id>', methods=['DELETE'])
def delete_vendor_sweet(vendor_sweet_id):
    vendor_sweet = VendorSweet.query.get(vendor_sweet_id)
    if vendor_sweet is None:
        return jsonify({'error': 'VendorSweet not found'}), 404
    db.session.delete(vendor_sweet)
    db.session.commit()
    return jsonify({})


if __name__ == '__main__':
    app.run(port=5555, debug=True)