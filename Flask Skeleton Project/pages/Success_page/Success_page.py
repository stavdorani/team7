from flask import Blueprint, render_template, request, redirect, jsonify, url_for

# about blueprint definition
Success_page = Blueprint('Success_page', __name__
                         ,static_folder='static', static_url_path='/Success_page', template_folder='templates')


# Routes
@Success_page.route('/Success_page', methods=['GET', 'POST'])
def index():
    return render_template('Success_page.html')