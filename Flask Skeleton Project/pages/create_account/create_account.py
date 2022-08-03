from flask import Blueprint, render_template, Flask, redirect, url_for, request, session, jsonify
from utilities.db import users_manager

# about blueprint definition
create_account = Blueprint('create_account', __name__
                         ,static_folder='static', static_url_path='/create_account', template_folder='templates')


# Routes
@create_account.route('/create_account', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        user_name = request.form['uname']
        email = request.form['email']
        phone = request.form['phone']
        birthday = request.form['date']
        psw = request.form['psw']
        file = request.form['myFile']
        users_manager.new_user(user_name, email, phone, birthday, psw, file)
    return render_template('create_account.html')



