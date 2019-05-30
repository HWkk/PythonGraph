import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import os, sys

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally

dir = '../../Data/ClusteringQuality/DenStream/'
fileName = 'DenStream-Cover-Normalized'
data = pd.read_excel(dir + fileName + '.xlsx')

plt.rc('pdf', fonttype=42)
#plt.rc('font', family='Arial', size=10, weight='roman')

plt.figure(figsize=(4.0, 2.5))
plt.subplots_adjust(
    left=0.13,
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

# plt.xticks(fontsize=8, weight='medium')
# plt.yticks(fontsize=8, weight='medium')
plt.xlabel('The number of arriving records (' + r'$\times{10^3}$' + ')')#, size=8, weight='medium')
plt.ylabel('Normalized CMM')#, size=8, weight='medium')
plt.ylim(0.2, 1.05)
plt.xlim(0, 600)

marksize = 2
linewidth = 1

plt.plot(data[data.columns[0]], data[data.columns[1]], linestyle=":", linewidth=linewidth, color='black')
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='^', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='D', markersize=marksize, linewidth=linewidth, color='r')
#plt.legend(loc=8, frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3]], ncol=2, loc=8,
           frameon=False, #bbox_to_anchor=(0.55, 0),
           labelspacing=0.05, markerfirst=True,
           borderaxespad=0.1, columnspacing=-2, handletextpad=0.3)



#plt.show()
plt.savefig(dir + fileName + ".pdf")

