from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant,Customer,Review

fake=Faker()

if __name__=='__main__':

    engine=create_engine('sqlite:///restaurants.db')
    Session=sessionmaker(bind=engine)
    session=Session()
    
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()
    session.commit()

    print("seeding.....")

    restaurants=[]
    for i in range(60):
        restaurant=Restaurant(
            name=fake.name(),
            price=fake.pyint()
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)
    
    customers=[]
    for i in range(50):
        customer=Customer(
            first_name=fake.name(),
            last_name=fake.name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)

    reviews=[]
    for restaurant in restaurants:
        for i in range(random.randint(1,100)):
            customer=random.choice(customers)

            review=Review(
                comment=fake.sentence(),
                star_rating=random.randint(1,10),
                restaurant_id=restaurant.id,
                customer_id=customer.id
            )
            if restaurant not in customer.restaurants:
                session.add(review)
                session.commit()
                customer.reviews.append(review)
            
           
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()        