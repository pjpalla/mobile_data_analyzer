# -*- coding: utf-8 -*-
import requests
 
url = "https://api.analytics.vodafone.it/api/userbackend/login"
 
payload = "{\"accessKey\": \"YaIPi1UIqck6nQlw6qs215zpJHZfjgFi\",\"secretKey\": \"VDkC0ZsDBA8wXhr8MicKGLrFFjFMUs2x\"}"

headers = {'Content-Type': 'application/json'}
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)

