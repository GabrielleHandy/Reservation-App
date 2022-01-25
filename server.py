import crud
from datetime import date
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
    pass

@app.route("profile/<user_name>")
def profile_page(user_name):
    """Shows profile page"""
    # Shows Name
    # reservations   
    pass

@app.route("search_time_slots")
def reserve_time_slot():
    # shows form to choose time
    # I want to dynamically show available times on a calendar
    # create time slots available
    pass

@app.route("create_reservation", methods=["POST"])
def create_reservation():
    """Creates a reservation for user"""
    pass