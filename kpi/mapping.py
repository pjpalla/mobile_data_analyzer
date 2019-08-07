# -*- coding: utf-8 -*-
import pandas as pd
import os

MAP_FOLDER = "C://Users//piepalla//vodafone//files//"

class Mapping:
    def __init__(self):
        self.map1_path = os.path.join(MAP_FOLDER, "1.csv")  
        self.map2_path = os.path.join(MAP_FOLDER, "2.csv")  
        self.map3_path = os.path.join(MAP_FOLDER, "3.csv")  
        self.map4_path = os.path.join(MAP_FOLDER, "4.csv")  
     
    def get_map(self, map_number):
         map_number = int(map_number)
         if map_number == 1:
             return pd.read_csv(self.map1_path)
         elif map_number == 2:
             return pd.read_csv(self.map2_path)
         elif map_number == 3:
             return pd.read_csv(self.map3_path)
         elif map_number == 4:
             return pd.read_csv(self.map4_path)
         
     
     def get_area_name(self, map_number, area_id):
         data = self.get_map(map_number)
         
         