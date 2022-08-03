from utilities.db import db_manager
theDB = db_manager.DBManager()


def new_user(name, email, phone, birthday, psw, file):
    res = True
    # check = get_user_by_name_email(name, email)
    check = (0, False)
    if check[1]:
        res = False
    else:
        query = "insert into users (name,email,phone, psw) values ( '%s', '%s', '%s', '%s')" % (name, email, phone, psw)
        commit_res = theDB.commit(query)
    return commit_res, res


def get_user_by_id(user_id):
    query = "select * from users where id ='%s';" % user_id
    user_rec = theDB.fetch(query)
    res = True
    if not user_rec:
        res = False
    user = theDB.fetch("select name, email, phone, birthday, psw  from users where id='%s';" % id)[0]
    return user[1], user[2], user[3], user[4], user[5], user[6], res


def get_user_by_name(user_name):
    query = "select * from users where user_name='%s';" % user_name
    user_rec = theDB.fetch(query)
    res = True
    if not user_rec:
        res = False
    return user_rec, res


def get_user_by_email(email):
    query = "select * from users where email='%s';" % email
    user_rec = theDB.fetch(query)
    res = True
    if not user_rec:
        res = False
    return user_rec, res


def get_user_by_name_email(name, email):
    query = "select * from users where email='%s' and name;" % (str(email), str(name))
    user_rec = theDB.fetch(query)
    res = True
    if not user_rec:
        res = False
    return user_rec, res


def get_user_by_name_password(user_name, password):
    query = ("SELECT name, email, phone, birthday, psw FROM users WHERE name='%s'and psw='%s';" % (user_name, password))
    user_rec = theDB.fetch(query)
    if not user_rec or user_rec == []:
        res = False
    else:
        res = True
    return user_rec[0], res
