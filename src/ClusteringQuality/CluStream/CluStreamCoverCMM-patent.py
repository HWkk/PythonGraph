#coding:utf-8
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import os, sys

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

dir = '../../Data/ClusteringQuality/CluStream/'
fileName = 'CluStream-Cover-Normalized-patent'
data = pd.read_excel(dir + fileName + '.xlsx')

plt.rc('pdf', fonttype=42)
#plt.rc('font', family='Arial', size=10, weight='roman')

plt.figure(figsize=(4.0, 2.5))
plt.subplots_adjust(
     left=0.12,
     bottom=0.18,
     right=0.96,
     top=0.94,
     wspace=0.00,
     hspace=0.00)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

font = {'family': 'Helvetica',
          'weight': 'demibold',
          'size': 12,
          }

plt.xlabel(u'数据量 (' + r'$\times{10^3}$' + ')')#, size=8, weight='medium')
plt.ylabel(u'聚类质量CMM')#, size=8, weight='medium')

plt.ylim(0.3, 1.05)
plt.xlim(0, 600)

marksize = 2
linewidth = 1

plt.plot(data[data.columns[0]], data[data.columns[1]], linestyle=":", linewidth=linewidth, color='black')#color='#978a84')
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='D', markersize=marksize, linewidth=linewidth, color='gray')
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='^', markersize=marksize, linewidth=linewidth, color='black')

#plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3]], loc=8, prop=font, frameon=False, bbox_to_anchor=(0.65, 0))
plt.legend(labels=[data.columns[1], data.columns[3], data.columns[2]], loc=8, frameon=False, bbox_to_anchor=(0.65, 0), markerfirst=True)

# plt.show()
plt.savefig(dir + fileName + ".png")

