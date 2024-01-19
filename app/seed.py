from models import db, Vendor, Sweet, VendorSweet
from app import app


with app.app_context():
    db.create_all()

    # some seed data
    vendor1 = Vendor(name='Insomnia Cookies')
    vendor2 = Vendor(name='Cookies Cream')
    vendor3 = Vendor(name='Sweet Indulgence')
    vendor4 = Vendor(name='Sugar Plums')
    vendor5 = Vendor(name='Crafted Confections')

    sweet1 = Sweet(name='Chocolate Chip Cookie')
    sweet2 = Sweet(name='Brownie')
    sweet3 = Sweet(name='Cupcakes')
    sweet4 = Sweet(name='Popsicles')
    sweet5 = Sweet(name='Ice Cream')

    vendor_sweet1 = VendorSweet(price=200, vendor=vendor1, sweet=sweet1)
    vendor_sweet2 = VendorSweet(price=300, vendor=vendor1, sweet=sweet2)
    vendor_sweet3 = VendorSweet(price=150, vendor=vendor2, sweet=sweet3)
    vendor_sweet4 = VendorSweet(price=250, vendor=vendor3, sweet=sweet4)
    vendor_sweet5 = VendorSweet(price=350, vendor=vendor4, sweet=sweet5)

    db.session.add(vendor1)
    db.session.add(vendor2)
    db.session.add(vendor3)
    db.session.add(vendor4)
    db.session.add(vendor5)
    db.session.add(sweet1)
    db.session.add(sweet2)
    db.session.add(sweet3)
    db.session.add(sweet4)
    db.session.add(sweet5)
    db.session.add(vendor_sweet1)
    db.session.add(vendor_sweet2)
    db.session.add(vendor_sweet3)
    db.session.add(vendor_sweet4)
    db.session.add(vendor_sweet5)

    db.session.commit()
