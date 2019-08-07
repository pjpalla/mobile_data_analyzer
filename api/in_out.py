import requests
 
url = "https://api.analytics.vodafone.it/api/apibackend/external"
 
#payload = "{\"date\": \"20190301\" ,\"dimensionsList\": [\"adr_id\", \"map\", \"province\", \"region\", \"country\", \"gender\", \"user_type\", \"user_type_2\", \"age_range\", \"repetitiveness\", \"travel_type\", \"dest_post_in\", \"dest_post_out_province\", \"dest_post_out_region\", \"dest_post_out_country\"],\"filtersList\": [{\"filter\": \"gender\",\"relation\": 1,\"values\": [\"M\", \"F\"]},{\"filter\": \"user_type\",\"relation\": 1,\"values\": [\"INT\"]},{\"filter\": \"user_type_2\",\"relation\": 1,\"values\": [\"Y\", \"N\"]},{\"filter\": \"adr_id\",\"relation\": 1,\"values\": [\"364\"]}, {\"filter\": \"map\",\"relation\": 1,\"values\": [\"3\"]}]}"

payload = "{\"date\": \"20190301\" ,\"dimensionsList\": [\"adr_id\", \"map\"],\"filtersList\": [{\"filter\": \"adr_id\",\"relation\": 1,\"values\": [\"364\"]}, {\"filter\": \"map\",\"relation\": 1,\"values\": [\"3\"]}]}"
headers = {
    'Content-Type': "application/json",
    'x-api-key': "16e8b843-d0fb-4a72-8f34-c5599b1a34e3"
    }
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)# -*- coding: utf-8 -*-

