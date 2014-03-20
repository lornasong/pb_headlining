#03.14 Purpose: Create a dataframe that has the PB data exports for A3 MA ELA
#Path to access MA data exports: G:\Reporting\Network Performance Analyst\Projects\Python Resources
#Download all .csv files into same path
#Make sure you have appropriate libraries (pandas and numpy)

import pandas as pd
import numpy as np
import glob

#***MUST PASTE path of .csv files between apostrophes:
path =r'C:\Users\lsong\Documents\GitHub\pb_play'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list = []

#Appends all files together and returns 'frame'
for files in allFiles:
	df = pd.read_csv(files,index_col=None, header=0, low_memory = False)
	list.append(df)
	frame = pd.concat(list)

#'frame' is the variable to use to access the dataframe of all A3 MA ELA.
#It's a huge dataframe so par it down as necessary
print frame

