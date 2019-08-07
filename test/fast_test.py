 # -*- coding: utf-8 -*-
from kpi.vodafone_bucket import VodafoneBucket
import kpi.const as const

bucket = VodafoneBucket(const.VODAFONE_BUCKET, const.VODAFONE_PROFILE)
kpi = const.KPI_NAMES[0]
disaggregation = "mid"
year = 2019
month = 3
day = 4

#pref_array = bucket.build_prefix(kpi, "min", all_days=True)
#
#for x in pref_array:
#    print(x)
    

client = bucket.get_client()
prefix = "VodafoneAnalytics/eventname=arrivals_attendances/"
bucket_name = bucket.get_bucket().name
print(bucket_name)    
result = client.list_objects_v2(Bucket = bucket_name, Prefix = prefix)

print(list(result.keys()))
print(result['Contents'])    