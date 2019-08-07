# -*- coding: utf-8 -*-
import requests
 
url = "https://api.analytics.vodafone.it/api/userbackend/info"
 
payload = "{}"
headers = {
    'Content-Type': "application/json",
    'X-API-KEY': "16e8b843-d0fb-4a72-8f34-c5599b1a34e3"
    }
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)

