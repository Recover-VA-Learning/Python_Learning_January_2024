import pandas as pd
import sys
import os
import datetime as dt
import random

# filename as cli argument 1
filename = sys.argv[1]

# check if filename in call
if len(sys.argv) < 2:
   print("Please specify correct file path")

# create data 
timestamp = dt.datetime.now()
data = random.randrange(0, 100) # rand int 0 - 100

# specify column names
column_names = ['time', 'data']

# make data frame
df = pd.DataFrame([[timestamp, data]], columns=column_names)

if not os.path.isfile(filename):
   df.to_csv(filename, header=column_names, index=False)
else: # else it exists so append without writing the header
   df.to_csv(filename, mode = 'a',header=False, index=False)