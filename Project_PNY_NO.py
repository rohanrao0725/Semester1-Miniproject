import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def setup_figure_plot_env(title):
	fig = plt.figure(figsize = (6,8), dpi = 100)

	plt.xlabel('Days 1-365')
	plt.ylabel('NO')
	plt.title(title)

def get_data():
	xls = pd.ExcelFile('Dataset-16.xlsx')
	df4 = pd.read_excel(xls, 'Peenya 2016', index_col=False)
	return df4

def show_plot():
	setup_figure_plot_env('PNY2016_NO')
	df11 = get_data()
	plt.plot(df11['S.No'], df11['NO'], linestyle="dotted", marker='^', color="purple", label = 'NO')
	plt.show()

if __name__ == '__main__':
	show_plot()