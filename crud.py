from model import db, connect_to_db, User, Reservation
from datetime import date

# CREATE USERS AND RESERVATIONS

def create_user(user_name, email="not entered"):
    """Creates a user"""
    pass


def create_reservations(user_id, reserve_date, reserve_time):
    """Creates a reservation"""
    pass


# USER functions




# RESERVATIONS functions




if __name__ == '__main__':
    from server import app
    connect_to_db(app)