from flask import Flask, request, jsonify, Response
import db_connector



app = Flask(__name__)

# using route and then based on method returning appropriate result.
@app.route('/get_user_name')
@app.route('/get_user_name/<user_id>')
def get_user_name(user_id):
    username = db_connector.get_user_name_from_db(user_id)
    return username

# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)