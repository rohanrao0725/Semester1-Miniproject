import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

'''
#2016
def setup_figure_plot_env(title):
	fig= plt.figure(figsize = (6,8), dpi = 100)
	#ax = plt.subplots()

	plt.xlabel('Days 1-365')
	plt.ylabel('SO2')
	plt.title(title)

def get_data():
	xls = pd.ExcelFile('Dataset-16.xlsx')
	df1 = pd.read_excel(xls, 'Cityrailway 2016', index_col=False)
	return df1

def show_plot():
	setup_figure_plot_env('CR2016_SO2')
	df11 = get_data()
	plt.plot(df11['S.No'], df11['SO2'], linestyle="dotted", marker='^', color="yellow", label = 'SO2')
	plt.axhline(y=80, xmin=0.0, xmax=1.0, color='r', label = 'Threshold')
	plt.legend()    
	plt.show()
    

if __name__ == '__main__':
	show_plot()	
'''
#2017
def setup_figure_plot_env(title):
	fig= plt.figure(figsize = (6,8), dpi = 100)
	#ax = plt.subplots()

	plt.xlabel('Days 1-365')
	plt.ylabel('SO2')
	plt.title(title)

def get_data():
	xls = pd.ExcelFile('Dataset-17.xlsx')
	df1 = pd.read_excel(xls, 'Cityrailway 2017', index_col=False)
	return df1

def show_plot():
	setup_figure_plot_env('CR2017_SO2')
	df11 = get_data()
	plt.plot(df11['S.No'], df11['SO2'], linestyle="dotted", marker='^', color="yellow", label = 'SO2')
	plt.axhline(y=80, xmin=0.0, xmax=1.0, color='r', label = 'Threshold')
	plt.legend()    
	plt.show()
    

if __name__ == '__main__':
	show_plot()		