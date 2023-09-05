import requests

def post_test(user_id, user_name):
    url = f"http://127.0.0.1:5000/users/{user_id}"
    res = requests.post(url, json={"user_name":user_name})
    data = res.json()
    if res.ok:
        print(res.text)

    useradded = data['user_added']


    res1 = requests.get(url)

    data2 = res1.json()
    print (data2)
    if res.ok:
        userget = data2['user_name']
        print ("Response is ok")

    if useradded == userget:
        print ("user matched database")

    return userget

post_test(1,'john')


