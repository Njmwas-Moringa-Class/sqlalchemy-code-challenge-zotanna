import sys
sys.path.append('/home/denkim/sqlalchemy-code-challenge-zotanna/lib')

from models import Restaurant, Customer, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print("Connecting to the database...")
# Create an engine
engine = create_engine('sqlite:///restaurants.db')

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

print("Creating new restaurant object...")
# Create a new restaurant
restaurant = Restaurant(name='Sample Restaurant', price=50)

print("Creating new customer object...")
# Create a new customer
customer = Customer(first_name='John', last_name='Doe')

print("Adding a review for the restaurant by the customer...")
# Add a review for the restaurant by the customer
review = Review(comment='Great food!', star_rating=5, restaurant=restaurant, customer=customer)

# Add objects to the session
session.add(restaurant)
session.add(customer)
session.add(review)

print("Committing the transaction...")
# Commit the transaction
session.commit()

print("Transaction committed successfully.")
