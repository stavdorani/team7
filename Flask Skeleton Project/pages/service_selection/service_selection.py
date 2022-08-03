from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
service_selection = Blueprint('service_selection', __name__
                         ,static_folder='static', static_url_path='/service_selection', template_folder='templates')


# Routes
@service_selection.route('/service_selection', methods=['GET', 'POST'])
def index():
    return render_template('service_selection.html')