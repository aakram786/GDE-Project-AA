import pymysql

def get_con():
    return pymysql.connect(host='sql8.freemysqlhosting.net',port=3306,user='sql8641160',passwd='wjEBTZKuWZ',db='sql8641160')
def get_user_name_from_db(user_id):
    conn = pymysql.connect(host='sql8.freemysqlhosting.net',port=3306,user='sql8641160',passwd='wjEBTZKuWZ',db='sql8641160')
    cursor = conn.cursor()
    query = f"SELECT user_name FROM sql8641160.users WHERE user_id = {user_id}"
    cursor.execute(query)
    username = cursor.fetchall()
    cursor.close()
    conn.close()
    return username
