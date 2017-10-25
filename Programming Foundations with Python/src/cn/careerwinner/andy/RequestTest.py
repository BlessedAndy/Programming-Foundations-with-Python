'''
Created on Sep 30, 2017

@author: I310003
'''

import requests

r = requests.get('https://api.github.com/events')

print(r.text)