import backend_testing
import frontend_testing
import db_connector

check_user_added = backend_testing.post_test(1, 'john')

conn = db_connector.get_con()
cursor = conn.cursor()
query =f"SELECT user_name FROM sql8641160.users WHERE user_id = 1"
cursor.execute(query)
user = cursor.fetchall()
print (f'Username from db call {user[0]} for is 1')
cursor.close()
conn.close()

name_added = frontend_testing.check_user(1)
print(f'The user added by the backend testing {check_user_added}check_user_added')
print(f'The user added by the frontend testing {name_added} name_added')

if check_user_added == name_added:
    print ("name is correct")
else:
    print ("Names did not match see above")




