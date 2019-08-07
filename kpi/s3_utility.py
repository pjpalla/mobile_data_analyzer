import boto3
import re

### BASIC VALUES

KPI_NAMES = ["arrivals_attendances", "centrality", "co_visits_matrix", "in_out_points", 
    "mobility_graph", "visit_duration"]

KPI = ["/eventname=arrivals_attendances", "/eventname=centrality", "/eventname=co_visits_matrix", "/eventname=in_out_points", 
    "/eventname=mobility_graph", "/eventname=visit_duration"]   
## Disaggregation levels
DISAGGREGATION = ["/disaggregation=max", "/disaggregation=mid", "/disaggregation=min"]
## year
YEARS = ["/year=2019"]
## month
MONTHS = ["/month=03"]
## days
DAYS = ["/day=0" + str(i) if i <= 9 else "/day=" + str(i) for i in range(1,32)]
## day 
DAY= ["/day=31"]
### Build key
BASE_KEY = "VodafoneAnalytics"


def get_vodafone_bucket():
    session = boto3.Session(profile_name='vodafone_profile')
    s3 = session.resource('s3')
    bucket = s3.Bucket("vodafone-analytics")
    print("Connected to the bucket {}".format(bucket.name))
    return bucket    


def get_client():
    session = boto3.Session(profile_name='vodafone_profile')
    return session.client('s3')

def get_prefix(kpi_name, disaggregation, year, month, day, all_days=False):
    common_prefix = "VodafoneAnalytics"
    prefix = ""
    kpi = ""
    disaggregation_level = ""
    year_selected = str(year)
    month_selected = str(month) if month > 9 else "0" + str(month)
    day_selected = str(day) if day > 9 else "0" + str(day)
    
    for k in KPI:
        if re.search(kpi_name, k):
            kpi = k
            break
# =============================================================================
#         else:
#             raise Exception("The kpi selected does not exist!")
#             
# =============================================================================
    for d in DISAGGREGATION:
        if re.search(disaggregation, d):
            disaggregation_level = d
            break
#        else:
#            raise Exception("Wrong disaggregation level")
        
    for y in YEARS:
        if re.search(year_selected, y):
            year_selected = y
#        else:
#            raise Exception("Year out of range!")
    
    for m in MONTHS:
        if re.search(month_selected, m):
            month_selected = m

    for d in DAYS:
        if re.search(day_selected, d):
            day_selected = d
            
    prefix = common_prefix + "{}{}{}{}{}".format(kpi, disaggregation_level, year_selected, month_selected, day_selected)
    return(prefix)#print(prefix)


 

#get_prefix("arrivals_attendances", "max", 2019, 3, 9)

bucket = get_vodafone_bucket()
pref = get_prefix(kpi_name="in_out_points", disaggregation = "mid", year = 2019, month = 3, day = 5)
client = get_client()

result = client.list_objects_v2(Bucket=bucket.name, Prefix = pref)
key =  result['Contents'][0]['Key']
print("Bucket key: ")
print(key)
    
    
             
    



