from model import db, connect_to_db, User, Reservation
from datetime import date

# CREATE USERS AND RESERVATIONS

def create_user(user_name, email="not entered"):
    """Creates a user"""
    new_user = User(user_name=user_name, email = email)

    db.session.add(new_user)
    db.session.commit()
    


def create_reservations(user_id, reserve_date, reserve_time):
    """Creates a reservation"""
    new_reservation = Reservation(user_id= user_id, reserve_date = reserve_date, reserve_time= reserve_time)

    db.session.add(new_reservation)
    db.session.commit()
    


# USER functions
def get_user_by_id(user_id):
    """Gets an instance of a user by the user_id"""


    return User.query.get(user_id)


def get_user_by_email(email):
    """Gets an instance of a user by email"""

    return User.query.filter(User.email == email).first()

# RESERVATIONS functions
def get_all_reservations(desired_date):
    """Get's all reservations on the day the user 
       wants to make a reservation"""

    reservations = Reservation.query.filter(Reservation.reserve_date == desired_date).all()

    return reservations



if __name__ == '__main__':
    from server import app
    connect_to_db(app)