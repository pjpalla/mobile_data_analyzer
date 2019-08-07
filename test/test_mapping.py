# -*- coding: utf-8 -*-
import unittest
from kpi.mapping import Mapping
from pandas.core.frame import DataFrame

class TestMapping(unittest.TestCase):
    def setUp(self):
        print("Start")
        #self.mapping = Mapping()
 
    def tearDown(self):
        #self.mapping = None
        print("End")
        
    @unittest.SkipTest
    def test_init(self):
        print("skip")
#        self.assertIsNotNone(self.mapping)
#        self.assertIsInstance(self.mapping, Mapping)
        
    #@unittest.SkipTest    
    def test_get_map(self):
        map1 = Mapping().get_map(1)
        self.assertIsNotNone(map1)
        self.assertIsInstance(map1, DataFrame)
        map2 = Mapping().get_map(2)
        map3 = Mapping().get_map(3)
        map4 = Mapping().get_map(4)
        
        print(map1.head())
        print(map2.head())
        print(map3.head())
        print(map4.head())
        
        
        
    if __name__ == '__main__':
        unittest.main()       
        