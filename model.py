from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()



class User(db.Model):
    """An User searching for a reservation"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                      primary_key=True, 
                      autoincrement=True)
   
    user_name = db.Column(db.String(50),
                     unique= True, nullable = False)
    
    # In the future can be used to send reminders of upcoming reservations
    email =  db.Column(db.String(50),
                     unique= True, nullable = False)
    
    reservations = db.relationship("Reservation", back_populates="users") 
    
    def __repr__(self):
        return f"""User\n user_id:{self.user_id}\n user_name:{self.user_name}"""


class Reservation(db.Model):
    """Reservations"""

    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, 
                      primary_key=True, 
                      autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    reserve_date = db.Column(db.Date, nullable = False)

    reserve_time= db.Column(db.Time, nullable = False)

    
    def __repr__(self):
        return f"""Reservation\n reservation_id: {self.reservation_id} \n user_id:{self.user_id} \n Date:{self.reserve_date} Time:{self.reserve_time}"""

    users = db.relationship("User", back_populates="reservations")



def connect_to_db(flask_app, db_uri="postgresql:///melon-reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
