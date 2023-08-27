from flask import Flask, request, jsonify, Response
import db_connector



app = Flask(__name__)

# using route and then based on method returning appropriate result.
@app.route('/users')
@app.route('/users/<user_id>', methods=['GET','POST','PUT','DELETE'])
def user(user_id):
    if request.method == 'POST':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            conn = db_connector.get_con()
            conn.autocommit(True)
            cursor = conn.cursor()
            query =f"INSERT into sql8641160.users (user_name, user_id) VALUES ('{user_name}',{user_id})"
            cursor.execute(query)
            cursor.close()
            conn.close()
            return jsonify({ "status":"ok", "user_added":user_name }), 200 # status code
        except:
            return jsonify({"status": "error", "reason": "id already exists"}), 500  # status code
    elif request.method == 'GET':
        try:
            conn = db_connector.get_con()
            cursor = conn.cursor()
            query =f"SELECT user_name FROM sql8641160.users WHERE user_id = {user_id}"
            cursor.execute(query)
            user = cursor.fetchall()
            cursor.close()
            conn.close()
            return jsonify({ "status":"ok", "user_name":user }), 200 # status code
        except:
            return jsonify({"status": "error", "reason": "no such id"}), 500  # status code
    elif request.method == 'PUT':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            conn = db_connector.get_con()
            conn.autocommit(True)
            cursor = conn.cursor()
            query = f"UPDATE sql8641160.users SET user_name = '{user_name}' WHERE user_id = {user_id}"
            cursor.execute(query)
            cursor.close()
            conn.close()
            return jsonify({ "status":"ok", "user_updated":user_id }), 200 # status code
        except:
            return jsonify({"status": "error", "reason": "no such id"}), 500  # status code
    elif request.method == 'DELETE':
        try:
            conn = db_connector.get_con()
            conn.autocommit(True)
            cursor = conn.cursor()
            query = f"DELETE FROM sql8641160.users WHERE user_id = {user_id}"
            cursor.execute(query)
            cursor.close()
            conn.close()
            return jsonify({ "status":"ok", "user_deleted":user_id }), 200 # status code
        except:
            return jsonify({"status": "error", "reason": "no such id"}), 500  # status code



# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5000)