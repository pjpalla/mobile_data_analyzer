from kpi.vodafone_bucket import VodafoneBucket
from kpi.const import KPI_NAMES
import pandas as pd

bucket = VodafoneBucket()
for x in KPI_NAMES:
    print(x)


kpi_name = KPI_NAMES[3] ### in_out_points

keys = bucket.get_kpi_files(kpi_name)
d = None

print(keys[0])
#d = pd.read_csv(keys[0])
#print(d.columns)

#for k in keys:
#    d = pd.read_csv(k)
#    print("Number of columns: {}".format(len(d.columns)))
#    print("Columns: ")
#    print(d.columns)