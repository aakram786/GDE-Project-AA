import requests

res1 = requests.get('http://127.0.0.1:5000/stop_server')
res2 = requests.get('http://127.0.0.1:5001/stop_server')

print(res1.status_code)
print(res2.status_code)


