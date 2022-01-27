import crud
from datetime import date,time, datetime
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
   
    # I want to dynamically show available times on a calendar in the future
    # create time slots available in calendar
    return render_template("calendar.html")

@app.route("/reservation_options", methods=["POST"])
def show_reservation_options():
    """Shows reservation options to user"""
    time_min = request.json.get('min-time')
    time_max = request.json.get('max-time')
    input_date = request.json.get('input-date')

    min_time = datetime.strptime(time_min, '%H:%M').time()
    max_time = datetime.strptime(time_max, '%H:%M').time()
    desired_date = datetime.strptime(input_date, '%Y-%M-%d').date()
    
    if crud.check_duplicate_reservation(session['user_id'], desired_date):
        return jsonify('You already have a melontastic tasting on this day!')
        
    
    else:
        times = crud.get_available_times(desired_date, min_time, max_time)
        print(times)
        return jsonify(times)


@app.route('/create_reservation', methods=['POST'])
def create_reservation():
    """Creates reservation for user"""

    in_time = request.json.get('inputTime')
    in_date = request.json.get('inputDate')
    
    desired_time = datetime.strptime(in_time, "%I:%M %p").time()
    desired_date = datetime.strptime(in_date, '%Y-%M-%d').date()

    crud.create_reservations(session['user_id'], desired_date, desired_time)
    message= f'Reservation sucessfully made! See you on {in_date} at {in_time}!'
    return jsonify(message)



if __name__ == '__main__':
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host='127.0.0.1', port=5002)