import requests



del1=requests.delete('http://127.0.0.1:5000/users/1')
del2=requests.delete('http://127.0.0.1:5000/users/2')

print(f'Server for rest stopped {del1.status_code}')
print(f'Server for app stopped {del2.status_code}')

try:
    res1 = requests.get('http://127.0.0.1:5000/stop_server')
    res2 = requests.get('http://127.0.0.1:5001/stop_server')

    print(f'Server for rest stopped {res1.status_code}')
    print(f'Server for app stopped {res2.status_code}')
except:
    print ('Issue during cleanup')




