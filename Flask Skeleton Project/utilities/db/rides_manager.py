from utilities.db import db_manager
theDB = db_manager.DBManager()


def get_ride_history_by_id(user_id):
    print("etet")
    query = "select * from Rides where driver_id='%s' or pas1='%s' or pas2='%s' or pas3='%s' or pas4='%s' ;" % (user_id, user_id, user_id, user_id, user_id)
    rid_his = theDB.fetch(query)
    res = True
    if not rid_his:
        res = False
    return rid_his, res


