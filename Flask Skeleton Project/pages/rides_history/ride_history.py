from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from utilities.db import rides_manager
# about blueprint definition
ride_history = Blueprint('ride_history', __name__
                         ,static_folder='static', static_url_path='/rides_history', template_folder='templates')


# Routes
@ride_history.route('/rides-history', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        user_id = request.form['uname']
        history = rides_manager.get_ride_history_by_id(user_id)

    return render_template('rides_history.html', history)