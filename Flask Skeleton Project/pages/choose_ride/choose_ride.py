from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
choose_ride = Blueprint('choose_ride', __name__
                         ,static_folder='static', static_url_path='/choose_ride', template_folder='templates')


# Routes
@choose_ride.route('/choose_ride')
def index():
    return render_template('choose_ride.html')