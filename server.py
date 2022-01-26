import crud
from datetime import date,time
from flask import (Flask, render_template, request, 
                   redirect, session, flash, jsonify,
                   Markup)
from model import connect_to_db
import os

app = Flask(__name__)
app.secret_key = "Melon-Appointment"

@app.route("/")
def login_page():
    """Shows login page"""
    return render_template("login.html")


@app.route("/sign-in", methods=["POST"])
def sign_in():
    """Gets user by email"""
    email = request.form.get('email')
    user = crud.get_user_by_email(email)

    session['user_id'] = user.user_id

    return redirect(f"/profile/{user.user_id}")


@app.route('/logout')
def clear_session():
    """ Log user out """
    session.clear()
    return redirect('/')

@app.route("/profile/<user_id>")
def profile_page(user_id):
    """Shows profile page"""
    # Shows Name
    # reservations   
    user = crud.get_user_by_id(user_id)
    # reservations = [reservation.reserve_date.strftime('%Y-%m-%d')for reservation in user.reservations]
    # print(reservations)

    return render_template("profile.html", user= user)

@app.route("/search_time_slots")
def reserve_time_slot():
    # shows form to choose time
    # I want to dynamically show available times on a calendar
    # create time slots available
    pass

@app.route("/create_reservation", methods=["POST"])
def create_reservation():
    """Creates a reservation for user"""
    pass

if __name__ == '__main__':
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host='000.0.0.0')