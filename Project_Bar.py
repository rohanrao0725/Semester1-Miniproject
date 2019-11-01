import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
#2016
xls = pd.ExcelFile('Dataset-16.xlsx')
df5 = pd.read_excel(xls, 'SensorvsPol', index_col=False)

df5.iloc[:,:].plot(kind='bar')


plt.xlabel('LocationSensor')
plt.ylabel('Pollutants Value')
n_groups = 4
index = np.arange(n_groups)
bar_width = 0
#opacity = 0.8

#x_values = list(df5)
#x_count = np.arange(len(x_values))

plt.title('LocationVsPollutants')
plt.xticks(index + bar_width,('CR2016', 'KDB2016', 'BTM2016', 'PNY2016'))
plt.show()

'''
#2017
xls = pd.ExcelFile('Dataset-17.xlsx')
df5 = pd.read_excel(xls, 'SensorVspol', index_col=False)

df5.iloc[:,:].plot(kind='bar')


plt.xlabel('LocationSensor')
plt.ylabel('Pollutants Value')
n_groups = 4
index = np.arange(n_groups)
bar_width = 0
#opacity = 0.8

#x_values = list(df5)
#x_count = np.arange(len(x_values))

plt.title('LocationVsPollutants')
plt.xticks(index + bar_width,('CR2017', 'KDB2017', 'BTM2017'))
plt.show()
