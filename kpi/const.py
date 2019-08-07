# -*- coding: utf-8 -*-

## Vodafaone Bucket Information ###
VODAFONE_BUCKET = "vodafone-analytics"
VODAFONE_PROFILE = 'vodafone_profile'
BASE_PREFIX = "VodafoneAnalytics"

### Vodafone Constants ###
## kpi names ##
KPI_NAMES = ["arrivals_attendances", "centrality", "co_visits_matrix", "in_out_points", 
    "mobility_graph", "visit_duration"]
## kpi partitions ##
KPI = ["/eventname=arrivals_attendances", "/eventname=centrality", "/eventname=co_visits_matrix", "/eventname=in_out_points", 
    "/eventname=mobility_graph", "/eventname=visit_duration"]   
## Disaggregation levels
DISAGGREGATION = ["/disaggregation=max", "/disaggregation=mid", "/disaggregation=min"]
## year
YEARS = ["/year=2019"]

## month --- preview kpi month is march 
MONTHS = ["/month=0" + str(i) if i <= 9 else "/month=" + str(i) for i in range(1,13)]
## days
DAYS = ["/day=0" + str(i) if i <= 9 else "/day=" + str(i) for i in range(1,32)]
## day 
DAY= ["/day=31"]

