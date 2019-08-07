# -*- coding: utf-8 -*-
from kpi import const
import boto3
import re


class VodafoneBucket:
    def __init__(self):
        session = boto3.Session(profile_name = const.VODAFONE_PROFILE)
        s3 = session.resource('s3')
        self.bucket = s3.Bucket(const.VODAFONE_BUCKET)
        self.client = session.client('s3')
     
    def get_bucket(self):
        return(self.bucket)
    
    def get_client(self):
        return(self.client)
        
    def build_prefix(self, kpi_name, disaggregation, year=2019, month=3, day=1, all_days=False):
        common_prefix = const.BASE_PREFIX
        prefix = ""
        prefix_array = []
        kpi = ""
        disaggregation_level = ""
        year_selected = str(year)
        month_selected = str(month) if month > 9 else "0" + str(month)
        day_selected = str(day) if day > 9 else "0" + str(day)
        
        for k in const.KPI:
            if re.search(kpi_name, k):
                kpi = k
                break
                
        if kpi == "":
            raise Exception("the kpi selected does not exist!")

        for d in const.DISAGGREGATION:
            if re.search(disaggregation, d):
                disaggregation_level = d
                break
        if disaggregation_level == "":
            raise Exception("Wrong disaggregation level")
            
        for y in const.YEARS:
            if re.search(year_selected, y):
                year_selected = y
        
        if year_selected == "":
                raise Exception("Year out of range!")
        
        for m in const.MONTHS:
            if re.search(month_selected, m):
                month_selected = m
                
        if month_selected == "":
            raise Exception("Month out of range!")
    
        if all_days:
            base_prefix = common_prefix + "{}{}{}{}".format(kpi, disaggregation_level, year_selected, month_selected)
            prefix_array = [base_prefix + d for d in const.DAYS]
            return(prefix_array)
            
       #### single prefix ### 
        for d in const.DAYS:
            if re.search(day_selected, d):
                day_selected = d
        if day_selected == "":
            raise Exception("Day out of range!")
                
        prefix = common_prefix + "{}{}{}{}{}".format(kpi, disaggregation_level, year_selected, month_selected, day_selected)
        return(prefix)#print(prefix)
    
    
    def get_file(self, prefix):
        result = self.client.list_objects_v2(Bucket=self.bucket.name, Prefix = prefix)
        keys = list(result.keys())
        if "Contents" not in keys:
            raise Exception("The file does not exist")
        
        key = result['Contents'][-1]['Key']
        ### return the corresponding file ###
        obj = self.bucket.Object(key)
        resp = obj.get()
        data = resp['Body']
        return(data)
        
    def get_kpi_files(self, kpi, disaggregation = "min"):
        base_prefix = const.BASE_PREFIX
        prefix = base_prefix
        disaggregation_level = ""
        files = []
        for k in const.KPI:
            if re.search(kpi, k):
                prefix += k
                break
            
        for d in const.DISAGGREGATION:
            if re.search(disaggregation, d):
                prefix += d
                break
            
       
        result = self.client.list_objects_v2(Bucket=self.bucket.name, Prefix = prefix)
        keys = list(result.keys())
        if "Contents" not in keys:
           raise Exception("Wrong kpi!")
           
        keys = [el['Key'] for el in result['Contents']]
        
        for k in keys:
            obj = self.bucket.Object(k)
            resp = obj.get()
            data = resp['Body']
            files.append(data)
        
        return(files)     
            
            
            

             
