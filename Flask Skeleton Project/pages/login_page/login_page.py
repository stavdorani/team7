from flask import Blueprint, render_template, Flask, redirect, url_for, request, session, jsonify
from utilities.db import users_manager

# about blueprint definition
login_page = Blueprint('login_page', __name__
                         ,static_folder='static', static_url_path='/login_page', template_folder='templates')


# Routes
@login_page.route('/', methods=['GET', 'POST'])
@login_page.route('/login_page', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        user_name = request.form['uname']
        password = request.form['psw']
        user_req = users_manager.get_user_by_name_password(user_name, password)
        print(user_req)
        if user_req[1]:
            if user_req[0][4] == password:
                session['user_name'] = user_name
                return render_template('service_selection.html',
                                       user_name=user_name)
            else:
                return render_template('login_page.html',
                                       message='Wrong password!')
        else:
            return render_template('login_page.html',
                                   message='Please sign in!')
    return render_template('login_page.html')
