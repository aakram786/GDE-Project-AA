from backend_testing import post_test
from frontend_testing import check_user
import db_connector

useridadd = 2
usernameadd = 'jack'

check_user_added = post_test(useridadd, usernameadd)

conn = db_connector.get_con()
cursor = conn.cursor()
query =f"SELECT user_name FROM sql8641160.users WHERE user_id = {useridadd}"
cursor.execute(query)
user = cursor.fetchall()
print (f'Username from db call {user[0]} for is {useridadd}')
cursor.close()
conn.close()

name_added = check_user(useridadd)
print(f'The user added by the backend testing {check_user_added}check_user_added')
print(f'The user added by the frontend testing {name_added} name_added')

if check_user_added == name_added:
    print ("name is correct")
else:
    print ("Names did not match see above")




