from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
find_ride = Blueprint('find_ride', __name__
                         ,static_folder='static', static_url_path='/find_ride', template_folder='templates')


# Routes
@find_ride.route('/find_ride')
def index():
    return render_template('find_ride.html')