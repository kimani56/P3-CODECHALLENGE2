from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .conftest import SQLITE_URL
from models import Customer, Restaurant, Review

from .utils import clear_db

class TestRestaurant:
    def test_creating_restaurant_instance(self):
        restaurant = Restaurant(name="R", price=1000)

        assert restaurant != None
        assert restaurant.name == "R"
        assert restaurant.price == 1000

    def test_get_reviews(self):
        """
            Returns a collection of all the reviews for the `Restaurant`
        """
        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        clear_db(session)

        customer = Customer(first_name="John", last_name="Doe")
        customer2 = Customer(first_name="John1", last_name="Doe1")
        session.add(customer)
        session.add(customer2)

        session.commit()

        customer = session.query(Customer).first()
        customer2 = session.query(Customer).all()[1]

        restaurant1 = Restaurant(name="R1", price=1000)
        restaurant2 = Restaurant(name="R2", price=2000)
        session.bulk_save_objects([restaurant1, restaurant2])

        session.commit()

        restaurant1 = session.query(Restaurant).first()
        restaurant2 = session.query(Restaurant).all()[1]

        review1c1 = Review(star_rating=5, customer_id=customer.id, restaurant_id=restaurant1.id)
        review2c1 = Review(star_rating=8, customer_id=customer.id, restaurant_id=restaurant2.id)
        review1c2 = Review(star_rating=6, customer_id=customer2.id, restaurant_id=restaurant1.id)
        review2c2 = Review(star_rating=10, customer_id=customer2.id, restaurant_id=restaurant2.id)

        session.bulk_save_objects([review1c1, review2c1, review1c2, review2c2])
        session.commit()

        restaurant1 = session.query(Restaurant).first()
        restaurant2 = session.query(Restaurant).all()[1]

        assert len(restaurant1.get_reviews()) == 2
        assert len(restaurant2.get_reviews()) == 2

        clear_db(session)

    def test_get_customers(self):
        """
            Returns a collection of all the customers who reviewed the `Restaurant`
        """
        engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        clear_db(session)

        customer = Customer(first_name="John", last_name="Doe")
        customer2 = Customer(first_name="John1", last_name="Doe1")
        session.add(customer)
        session.add(customer2)

        session.commit()

        customer = session.query(Customer).first()
        customer2 = session.query(Customer).all()[1]

        restaurant1 = Restaurant(name="R1", price=1000)
        restaurant2 = Restaurant(name="R2", price=2000)
        session.bulk_save_objects([restaurant1, restaurant2])

        session.commit()

        restaurant1 = session.query(Restaurant).first()
        restaurant2 = session.query(Restaurant).all()[1]

        review1c1 = Review(star_rating=5, customer_id=customer.id, restaurant_id=restaurant1.id)
        review2c1 = Review(star_rating=8, customer_id=customer.id, restaurant_id=restaurant2.id)
        review1c2 = Review(star_rating=6, customer_id=customer2.id, restaurant_id=restaurant1.id)
        review2c2 = Review(star_rating=10, customer_id=customer2.id, restaurant_id=restaurant2.id)

        session.bulk_save_objects([review1c1, review2c1, review1c2, review2c2])
        session.commit()

        customer = session.query(Customer).first()
        customer2 = session.query(Customer).all()[1]

        assert len(restaurant1.get_reviews()) == 2
        assert len(restaurant2.get_customers()) == 2

        clear_db(session)







