from models import db, Vendor, Sweet, VendorSweet
from app import app

with app.app_context():
    db.create_all()

    # some seed data
    vendor_names = ['Insomnia Cookies', 'Cookies Cream', 'Sweet Indulgence', 'Sugar Plums', 'Crafted Confections']
    sweet_names = ['Chocolate Chip Cookie', 'Brownie', 'Cupcakes', 'Popsicles', 'Ice Cream']
    prices = [200, 300, 150, 250, 350]

    vendors = [Vendor(name=name) for name in vendor_names]
    sweets = [Sweet(name=name) for name in sweet_names]
    vendor_sweets = [VendorSweet(price=price, vendor=vendors[i], sweet=sweets[i]) for i, price in enumerate(prices)]

    db.session.add_all(vendors)
    db.session.add_all(sweets)
    db.session.add_all(vendor_sweets)

    db.session.commit()

    print("Seed data has been successfully added!")
