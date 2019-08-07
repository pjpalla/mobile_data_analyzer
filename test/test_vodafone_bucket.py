# -*- coding: utf-8 -*-
import unittest
import logging
from kpi.vodafone_bucket import VodafoneBucket
import kpi.const
import sys
import pandas as pd


class TestVodafoneBucket(unittest.TestCase):
    
    def setUp(self):
        print("Start")
        ### Set Logger ###
#        self.logger = logging.getLogger()
#        self.logger.setLevel(logging.DEBUG)
#        ch = logging.StreamHandler(sys.stdout)
#        #console handler with level debug
        #ch.setLevel(logging.CRITICAL)
#        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#        ch.setFormatter(formatter)
#        self.logger.addHandler(ch)
#        
        ##boto 3 log level settings ##
        #boto3.set_stream_logger('boto3.resources', logging.CRITICAL)
        
        self.vodafone_bucket = VodafoneBucket()
        
    def tearDown(self):   
        print("End")
#        self.logger = None
        self.vodafone_bucket = None
        

    @unittest.SkipTest
    def test_init(self):
        self.assertIsNotNone(self.vodafone_bucket)
        self.assertIsInstance(self.vodafone_bucket, VodafoneBucket)

    @unittest.SkipTest        
    def test_get_bucket(self):
        bucket = self.vodafone_bucket.get_bucket()
        #logging.debug("Bucket name: " + bucket.name)

        #self.logger.debug("Bucket name: " + bucket.name)
        print("Bucket name: " + bucket.name)
        self.assertIsNotNone(bucket)
        self.assertEqual(bucket.name, kpi.const.VODAFONE_BUCKET, "the bucket name is: {}".format(bucket.name))
    
    @unittest.SkipTest            
    def test_get_client(self):
        client = self.vodafone_bucket.get_client()
        self.assertIsNotNone(client)
        
    @unittest.SkipTest
    def test_get_prefix(self):
        year = 2019
        month = 3
        day = 4
        disaggregation = "mid"
        kpi_name = kpi.const.KPI_NAMES[0]
        prefix = self.vodafone_bucket.build_prefix(kpi_name, disaggregation, year, month, day)
        self.assertEqual(prefix, "VodafoneAnalytics/eventname=arrivals_attendances/disaggregation=mid/year=2019/month=03/day=04")
        self.assertNotEqual(prefix, "VodafoneAnalytics/eventname=visit_duration/disaggregation=mid/year=2019/month=03/day=04")       
        print(prefix)
     
    @unittest.SkipTest    
    def test_get_file(self):
        year = 2019
        month = 3
        day = 31
        disaggregation = "mid"
        kpi_name = kpi.const.KPI_NAMES[0]
        prefix = self.vodafone_bucket.build_prefix(kpi_name, disaggregation, year, month, day)
        
        file = self.vodafone_bucket.get_file(prefix)
        self.assertIsNotNone(file)
        data = pd.read_csv(file)
        self.assertIsNotNone(data)
        print(data.columns)
#        filename = key.split("/")[-1]
#        self.assertIsNotNone(filename)
#        #self.assertNotEqual(filename, "20190331.csv")
        
    #@unittest.SkipTest
    def test_get_files(self):
        year, month, day = 2019, 3, 12
        kpi_name = kpi.const.KPI_NAMES[0]
        files = self.vodafone_bucket.get_kpi_files(kpi_name, disaggregation="max")
        self.assertIsNotNone(files)
        print(len(files))
#        for f in files:
#            d = pd.read_csv(f)
#            print("Number of columns: {}".format(d.shape[1]))
        
        
 

    if __name__ == '__main__':
        unittest.main()       
