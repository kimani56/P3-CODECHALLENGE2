#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import  Customer, Restaurant, Review


if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Customer).delete()
    session.query(Restaurant).delete()
    session.query(Review).delete()

    fake = Faker()

    customers = []
    for i in range(5):  # Generate 5 customer records
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )

        # add and commit individually to get IDs back
        session.add(customer)
        session.commit()

        customers.append(customer)

    restaurants = []
    for i in range(5):  # Generate 5 restaurant records
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(5, 50) * 5
        )

        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)

    reviews = []
    for i in range(5):  # Generate 5 review records
        review = Review(
            star_rating=random.randint(1, 5),
            customer_id=random.randint(1, 5),  # Match the number of customers
            restaurant_id=random.randint(1, 5),  # Match the number of restaurants
        )

        reviews.append(review)

    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
