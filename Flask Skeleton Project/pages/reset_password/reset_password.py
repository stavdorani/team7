from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
reset_password = Blueprint('reset_password', __name__
                         ,static_folder='static', static_url_path='/reset_password', template_folder='templates')


# Routes
@reset_password.route('/reset_password')
def index():
    return render_template('reset_password.html')