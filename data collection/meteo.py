# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('https://api.meteomatics.com/2020-06-11T15:30:00ZP7D:PT2H/t_0m:C/50.6,3.06/json?model=mix', auth=HTTPBasicAuth('isen_meunier', 'rT2ql81CVUzpS'))

r.json() 