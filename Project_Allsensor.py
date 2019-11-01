import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

xls = pd.ExcelFile('Dataset-16.xlsx')
df1 = pd.read_excel(xls, 'Cityrailway 2016', index_col=False)
df2 = pd.read_excel(xls, 'Kadablli 2016', index_col=False)
df3 = pd.read_excel(xls, 'BTM 2016', index_col=False)
df4 = pd.read_excel(xls, 'Peenya 2016', index_col=False)

fig = plt.figure(figsize = (6,8), dpi = 100)
ax1 = fig.add_subplot(2,2,1)
plt.plot(df1['S.No'], df1['PM10'], linestyle="dotted", marker='^', color="red", label = 'PM10')

plt.plot(df1['S.No'], df1['CO'], linestyle="solid", marker='o', color="green", label = 'CO')

plt.plot(df1['S.No'], df1['NO'], linestyle="dashed", marker='>', color="blue", label = 'NO')

plt.plot(df1['S.No'], df1['NO2'], linestyle="dotted", marker='<', color="yellow", label = 'NO2')

plt.plot(df1['S.No'], df1['SO2'], linestyle="dashed", marker='o', color="black", label = 'SO2')

plt.xlabel('Days 1-365')
plt.ylabel('Pollutants')

plt.legend()

plt.title('CR2016')


ax2 = fig.add_subplot(2,2,2)
plt.plot(df2['S.No'], df2['CO'], linestyle="solid", marker='o', color="green", label = 'CO')

plt.plot(df2['S.No'], df2['PM2.5'], linestyle="dotted", marker='^', color="red", label = 'PM2.5')

plt.plot(df2['S.No'], df2['NO'], linestyle="dashed", marker='>', color="blue", label = 'NO')

plt.plot(df2['S.No'], df2['NO2'], linestyle="dotted", marker='<', color="yellow", label = 'NO2')

plt.plot(df2['S.No'], df2['SO2'], linestyle="dashed", marker='o', color="black", label = 'SO2')

plt.xlabel('Days 1-365')
plt.ylabel('Pollutants')

plt.legend()

plt.title('KDBLLI2016')



ax3 = fig.add_subplot(2,2,3)

plt.plot(df3['S.No'], df3['CO'], linestyle="solid", marker='o', color="green", label = 'CO')

plt.plot(df3['S.No'], df3['PM2.5'], linestyle="dotted", marker='^', color="red", label = 'PM2.5')

plt.plot(df3['S.No'], df3['NO'], linestyle="dashed", marker='>', color="blue", label = 'NO')

plt.plot(df3['S.No'], df3['NO2'], linestyle="dotted", marker='<', color="yellow", label = 'NO2')

plt.plot(df3['S.No'], df3['SO2'], linestyle="dashed", marker='o', color="black", label = 'SO2')

plt.xlabel('Days 1-365')
plt.ylabel('Pollutants')

plt.legend()

plt.title('BTM2016')


ax4 = fig.add_subplot(2,2,4)

plt.plot(df4['S.No'], df4['CO'], linestyle="solid", marker='o', color="green", label = 'CO')

plt.plot(df4['S.No'], df4['PM2.5'], linestyle="dotted", marker='^', color="red", label = 'PM2.5')

plt.plot(df4['S.No'], df4['NO'], linestyle="dashed", marker='>', color="blue", label = 'NO')

plt.plot(df4['S.No'], df4['NO2'], linestyle="dotted", marker='<', color="yellow", label = 'NO2')

plt.plot(df4['S.No'], df4['SO2'], linestyle="dashed", marker='o', color="black", label = 'SO2')

plt.xlabel('Days 1-365')
plt.ylabel('Pollutants')

plt.legend()

plt.title('PEENYA2016')


plt.tight_layout()

plt.show()

#plt.savefig()