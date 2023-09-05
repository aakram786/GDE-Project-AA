from flask import Flask, request, jsonify, Response
import db_connector
import os
import signal



app = Flask(__name__)

# using route and then based on method returning appropriate result.
@app.route('/get_user_name')
@app.route('/get_user_name/<user_id>')
def get_user_name(user_id):
   # username = db_connector.get_user_name_from_db(user_id)
   try:
       conn = db_connector.get_con()
       cursor = conn.cursor()
       query = f"SELECT user_name FROM sql8641160.users WHERE user_id = {user_id}"
       cursor.execute(query)
       user = str(cursor.fetchall()[0])
       cursor.close()
       conn.close()
       return "<H1 id = 'user'>" + user + "</H1>", 200  # status code
   except:
       return "<H1 id = 'error'>" "no such user" + user + "</H1>", 500  # status code
#Use this to stop the server
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'

# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)