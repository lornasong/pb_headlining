#path: Set-Location C:\Users\lsong\Documents\GitHub\pb_play
#GUI for headlining
import sys
from PyQt4 import QtGui, QtCore
import pandas as pd
import numpy as np

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import gui_data
from subprocess import Popen

from random import randint
class MainApp(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		
		#Labels for user and outputs
		school_l = QtGui.QLabel('Select Schools:', self)
		high_s = QtGui.QLabel('High Performing Schools:', self)
		high_p = QtGui.QLabel('%:', self)
		low_s = QtGui.QLabel('Low Performing Schools', self)
		low_p = QtGui.QLabel('%:', self)
		
		#Check box list that populates unique schools
		self.schoolWidget = QListWidget()
		for i in gui_data.unique_schools:
			item = QtGui.QListWidgetItem(self.schoolWidget)
			ch = QtGui.QCheckBox()
			ch.setText(i)
			ch.setObjectName(i)
			self.schoolWidget.setItemWidget(item, ch)
			
		#Check boxes for percentages: PB % and Pure %
		self.ch_pu = QtGui.QCheckBox()
		self.ch_pu.setText('Pure %')
		self.ch_pb = QtGui.QCheckBox()
		self.ch_pb.setText('PB %')
		
		#Buttons: Quit and Run
		quit = QtGui.QPushButton('Quit', self)
		quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
		run = QtGui.QPushButton('Run', self)
		run.clicked.connect(self.run_clicked)
		
		#Output list boxes: high and low schools and %
		self.h_school = QtGui.QListWidget()
		self.h_percent = QtGui.QListWidget()
		
		self.l_school = QtGui.QListWidget()
		self.l_percent = QtGui.QListWidget()
			
		#Set up Grid
		grid = QtGui.QGridLayout()
		grid.setColumnMinimumWidth(0, 225)
		grid.setSpacing(10)
		
		grid.addWidget(school_l, 0, 0)
		grid.addWidget(self.schoolWidget, 1, 0, 3, 3)
		grid.addWidget(self.ch_pb, 4, 1)
		grid.addWidget(self.ch_pu, 4, 2)
		
		grid.addWidget(run, 4, 4)
		grid.addWidget(quit, 4, 5)
		
		grid.addWidget(high_s, 0, 3)
		grid.addWidget(high_p, 0, 5)
		grid.addWidget(low_s, 2, 3)
		grid.addWidget(low_p, 2, 5)
		grid.addWidget(self.h_school, 1, 3, 1, 2)
		grid.addWidget(self.h_percent, 1, 5)
		grid.addWidget(self.l_school, 3, 3, 1, 2)
		grid.addWidget(self.l_percent, 3, 5)
		
		#Window Attributes
		self.setLayout(grid)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Massachusetts A3 Headlining')
		self.resize(550, 550)
		self.show()
	
	def run_clicked(self):
		#Return dataframe of school list and whether chosen or not (0, 2)
		checked = []
		for index in xrange(self.schoolWidget.count()):
			check_box = self.schoolWidget.itemWidget(self.schoolWidget.item(index))
			state = check_box.checkState()
			checked.append(state)
		user = pd.DataFrame(data = gui_data.unique_schools)
		user.rename(columns = {0: 'schools'}, inplace = True)
		user['checked'] = checked
		
		#Clear list box
		self.h_school.clear()
		self.h_percent.clear()
		self.l_school.clear()
		self.l_percent.clear()
		
		#Check which data set to use
		pure = self.ch_pu.checkState()
		pb = self.ch_pb.checkState()
		
		#Populate user output
		if pure == 2 & pb == 2:
			pass
		elif pure == 2:

			for i in gui_data.high['school_name']:
				self.h_school.addItem(i)
			for i in gui_data.high['percent']:
				self.h_percent.addItem(str(i))
			
			for i in gui_data.low['school_name']:
				self.l_school.addItem(i)
			for i in gui_data.low['percent']:
				self.l_percent.addItem(str(i))
			
		elif pb == 2:
		
			for i in gui_data.high['school_name']:
				self.h_school.addItem(i)
			for i in gui_data.high['percent']:
				self.h_percent.addItem(str(i))
			
			for i in gui_data.low['school_name']:
				self.l_school.addItem(i)
			for i in gui_data.low['percent']:
				self.l_percent.addItem(str(i))
				
		else:
			pass

def main():

	app = QtGui.QApplication(sys.argv)
	ex = MainApp()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()