#Takes care of the data that goes in and out of the headline_gui
import pandas as pd
import numpy as np
import glob

# Calls PB data export
path =r'C:\Users\lsong\Documents\GitHub'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list = []

#Column 0 of export is school names. Column 8 is interim grades
for files in allFiles:
	df = pd.read_csv(files, usecols = [0 ,8], index_col=None, header=0, low_memory = False, na_values=['null',])
	list.append(df)
	frame = pd.concat(list)

#Creates a unique list of school names to put into schools for user to choose from
unique_schools = pd.unique(df['School Name'].values.ravel())
unique_grades = pd.unique(df['Interim Grade'].values.ravel())

#Read fake output data frames
high_pb_file = 'high_pb.csv'
low_pb_file = 'low_pb.csv'
high_pure_file = 'high_pure.csv'
low_pure_file = 'low_pure.csv'
high_pb = pd.read_csv(high_pb_file)
low_pb = pd.read_csv(low_pb_file)
high_pure = pd.read_csv(high_pure_file)
low_pure = pd.read_csv(low_pure_file)