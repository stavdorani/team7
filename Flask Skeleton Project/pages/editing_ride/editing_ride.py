from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
editing_ride = Blueprint('editing_ride', __name__
                         ,static_folder='static', static_url_path='/editing_ride', template_folder='templates')


# Routes
@editing_ride.route('/editing_ride')
def index():
    return render_template('editing_ride.html')