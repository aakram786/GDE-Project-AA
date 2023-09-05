import requests



requests.delete('http://127.0.0.1:5000/users/1')
requests.delete('http://127.0.0.1:5000/users/2')

res1 = requests.get('http://127.0.0.1:5000/stop_server')
res2 = requests.get('http://127.0.0.1:5001/stop_server')

print(f'Server for rest stopped {res1.status_code}')
print(f'Server for app stopped {res2.status_code}')
print(res2.status_code)


