from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
ride_details = Blueprint('ride_details', __name__
                         ,static_folder='static', static_url_path='/ride_details', template_folder='templates')


# Routes
@ride_details.route('/ride_details')
def index():
    return render_template('ride_details.html')