# Set-Location C:\Users\lsong\Documents\GitHub\pb_play

import pandas as pd
import numpy as np
import glob

# Calls all data exports
path =r'C:\Users\lsong\Documents\GitHub\pb_data_exports'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list = []

#User chooses demographic information to analyse
special = raw_input(">> Choose demographic category (FRL, LEP, SPED, ELL, NONE): ")

if special == 'FRL':
	special = 'Free Reduced Lunch'
elif special == 'LEP':
	special = 'Limited English Proficiency'
elif special == 'SPED':
	special = 'Special Education'
elif special == 'ELL':
	special = 'English Language Learner'
else:
	special = 3 #just skip

#Appends all files together and returns 'frame'
#Col 3 = State, 4 = District, 11 = Interim Grade, 12 = Grade 30 - 37 Scores A1 to A3
for files in allFiles:
	df = pd.read_csv(files, usecols = [3, 4, 11, 12, 30, 31, 32, 33, 34, 35, special], index_col=None, header=0, low_memory = False, na_values=['null',])
	list.append(df)
	frame = pd.concat(list)

#Remove rows in which students test off grade level
frame = frame[frame['Grade'] == frame['Interim Grade']]
#Remove rows in which Network is not MA
frame = frame[frame['State'] == 'Massachusetts']
#Remove rows that do not fall in special category
if special != 3:
	frame = frame[frame[special] == 1]

#Calculate % for each interim
frame['A1'] = frame['A1 Raw Score']/frame['A1 Points Possible']
frame['A2'] = frame['A2 Raw Score']/frame['A2 Points Possible']
frame['A3'] = frame['A3 Raw Score']/frame['A3 Points Possible']

#ANALYSIS FOR HIGHEST PERFORMING DISTRICT BY GRADE
#Get user input
interim = raw_input(">> Choose Interim (A1, A2, A3) to Analyse: ")

#Create dataframe to examine district performance across grades
df_g = frame.groupby(['Interim Grade', 'District'], as_index = False).mean()
df_g.fillna(0, inplace = True)
#Identifies highest performing district across grades
df_grade = df_g.sort(interim, ascending = False).groupby('Interim Grade', as_index = False).nth(0)

#Identifying second highest performing district to recognize significance of highest performance district
second = df_g.sort(interim, ascending = False).groupby('Interim Grade', as_index = False).nth(1)
sig_d = df_grade[interim] - second[interim]
df_grade['Significance'] = sig_d

print '--------' * 10
print 'Highest Performing District By Grade:\n'
print df_grade[['Interim Grade', 'District', interim, 'Significance']]

#ANALYSIS FOR HIGHEST PERFORMING DISTRICT OVER ALL
df_d = frame.groupby(['District'], as_index = False).mean()
df_d.fillna(0, inplace = True)
df_dis = df_d.sort(interim, ascending = False)
sig_d = df_dis.loc[1, interim] - df_dis.loc[0, interim]
df_d['Significance'] = sig_d

print '--------' * 10
print '\nHighest Performing District Overall:\n'
print df_grade[['District', interim, 'Significance']].loc[0]
