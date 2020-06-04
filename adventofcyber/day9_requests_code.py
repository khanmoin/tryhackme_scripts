"""
    Python script to get flag for the day 9 challenge of advent of cyber
"""

import requests


path = '/'
host = 'http://10.10.169.100:3000'
flag = ''
json = {'value' : '', 'next' : ''}          # dummy values since we know the response


while json['next'] != 'end':
    response = requests.get(host + '/' + json['next'])
    json = response.json()
    # remove end from the flag
    if json['value'] != 'end':
      flag += json['value']


print(flag)
