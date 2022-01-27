from model import db, connect_to_db, User, Reservation
from datetime import date, time, timedelta, datetime









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

def check_duplicate_reservation(user_id, desired_date):
    """Check to see if user already has reservation"""
    return Reservation.query.filter(Reservation.user_id == user_id, Reservation.reserve_date == desired_date).all()

def get_all_reservations(desired_date):
    """Get's all reservations on the day the user 
       wants to make a reservation"""

    reservations = Reservation.query.filter(Reservation.reserve_date == desired_date).all()

    return reservations

# helper function for finding availble times 
def get_available_times(desired_date, min_time, max_time):
    """Returns the times in range to user time frame as a list"""
    # ________DATE____
    day_reserved = Reservation.query.filter(Reservation.reserve_date == desired_date)

    reserved_in_range = day_reserved.filter(Reservation.reserve_time > min_time, Reservation.reserve_time < max_time).all()



    # _________TIME____
    allday_30min = []
    allday_30min.append(datetime(2000,1,1, hour= min_time.hour, minute= 0))
    for i in range(min_time.hour-1, max_time.hour+ 1):
        old_time = allday_30min[-1]
        
        allday_30min.append(old_time + timedelta(minutes=30))

    avail_time = []

    for avail in set(allday_30min):
        if avail.time() >= min_time and avail.time() <= max_time:
            if reserved_in_range:
                for already_taken in reserved_in_range:
                    if already_taken.reserve_time == avail.time():
                        continue
                    else:
                        avail_time.append(avail.time().strftime("%I:%M %p")) 
            else:
                avail_time.append(avail.time().strftime("%I:%M %p"))
        else:
            continue
        
               
    return(avail_time)


   

if __name__ == '__main__':
    from server import app
    connect_to_db(app)