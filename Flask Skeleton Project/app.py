from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from datetime import timedelta

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=25)

###### Pages
from pages.login_page.login_page import login_page
app.register_blueprint(login_page)


from pages.create_account.create_account import create_account
app.register_blueprint(create_account)


from pages.choose_ride.choose_ride import choose_ride
app.register_blueprint(choose_ride)


from pages.service_selection.service_selection import service_selection
app.register_blueprint(service_selection)


from pages.find_ride.find_ride import find_ride
app.register_blueprint(find_ride)


from pages.ride_details.ride_details import ride_details
app.register_blueprint(ride_details)


from pages.rides_history.ride_history import ride_history
app.register_blueprint(ride_history)


from pages.reset_password.reset_password import reset_password
app.register_blueprint(reset_password)


from pages.editing_ride.editing_ride import editing_ride
app.register_blueprint(editing_ride)


from pages.Success_page.Success_page import Success_page
app.register_blueprint(Success_page)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)


@app.route('/log_out')
def logout_func():
    session.clear()
    return render_template('login_page.html')


@app.route('/session')
def session_func():
    return jsonify(dict(session))