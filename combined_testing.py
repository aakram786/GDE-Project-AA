import backend_testing
import frontend_testing
import db_connector

check_user_added = backend_testing.post_test(1,'john')

conn = db_connector.get_con()
cursor = conn.cursor()
query =f"SELECT user_name FROM sql8641160.users WHERE user_id = 1"
cursor.execute(query)
user = cursor.fetchall()
cursor.close()
conn.close()

for entry in user:
    print (entry)

name_added = frontend_testing.check_user(1)

if check_user_added == name_added:
    print ("name is correct")

