
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
#2016
def setup_figure_plot_env(title):
	fig = plt.figure(figsize = (6,8), dpi = 100)

	plt.xlabel('Days 1-365')
	plt.ylabel('Pollutants')
	plt.title(title)

def get_data():
	xls = pd.ExcelFile('Dataset-16.xlsx')
	df1 = pd.read_excel(xls, 'Cityrailway 2016', index_col=False)
	#df2 = pd.read_excel(xls, 'Kadablli 2016', index_col=False)
	#df3 = pd.read_excel(xls, 'BTM 2016', index_col=False)
	#df4 = pd.read_excel(xls, 'Peenya 2016', index_col=False)
	return df1

def show_plot():
	setup_figure_plot_env('CR2016')
	df11 = get_data()
	plt.plot(df11['S.No'], df11['PM10'], linestyle="dotted", marker='^', color="red", label = 'PM10')
	plt.plot(df11['S.No'], df11['CO'], linestyle="solid", marker='o', color="green", label = 'CO')
	plt.plot(df11['S.No'], df11['NO'], linestyle="dashed", marker='>', color="blue", label = 'NO')
	plt.plot(df11['S.No'], df11['NO2'], linestyle="dotted", marker='<', color="yellow", label = 'NO2')
	plt.plot(df11['S.No'], df11['SO2'], linestyle="dashed", marker='o', color="black", label = 'SO2')
	
	plt.legend()

	plt.show()


if __name__ == '__main__':
	show_plot()
'''
#2017
def setup_figure_plot_env(title):
	fig = plt.figure(figsize = (6,8), dpi = 100)

	plt.xlabel('Days 1-365')
	plt.ylabel('Pollutants')
	plt.title(title)

def get_data():
	xls = pd.ExcelFile('Dataset-17.xlsx')
	df1 = pd.read_excel(xls, 'Cityrailway 2017', index_col=False)
	#df2 = pd.read_excel(xls, 'Kadablli 2016', index_col=False)
	#df3 = pd.read_excel(xls, 'BTM 2016', index_col=False)
	#df4 = pd.read_excel(xls, 'Peenya 2016', index_col=False)
	return df1

def show_plot():
	setup_figure_plot_env('CR2017')
	df11 = get_data()
	plt.plot(df11['S.No'], df11['PM10'], linestyle="dotted", marker='^', color="red", label = 'PM10')
	plt.plot(df11['S.No'], df11['CO'], linestyle="solid", marker='o', color="green", label = 'CO')
	plt.plot(df11['S.No'], df11['NO'], linestyle="dashed", marker='>', color="blue", label = 'NO')
	plt.plot(df11['S.No'], df11['NO2'], linestyle="dotted", marker='<', color="yellow", label = 'NO2')
	plt.plot(df11['S.No'], df11['SO2x'], linestyle="dashed", marker='o', color="black", label = 'SO2')
	
	plt.legend()

	plt.show()


if __name__ == '__main__':
	show_plot()	

	