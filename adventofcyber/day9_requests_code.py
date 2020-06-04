import requests

path = '/'
host = 'http://10.10.169.100:3000'
flag = ''
json = {'value' : '', 'next' : ''}
#response = requests.get(host + path)
#json = response.json()
#flag += json['value']

while json['next'] != 'end':
    response = requests.get(host + '/' + json['next'])
    json = response.json()
    if json['value'] != 'end':
      flag += json['value']


print(flag)
