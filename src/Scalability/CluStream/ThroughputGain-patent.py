
#coding:utf-8
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
# plt.rc('font', family='Helvetica', size=11, weight='roman')
plt.rc('pdf', fonttype=42)

dir = '../../Data/Scalability/CluStream/'
fileName = 'CluStream-MaxSpeedup'
data = pd.read_excel(dir + fileName + '.xlsx')

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(3.6, 2.4))

# plt.subplots_adjust(
#      left=0.16,
#      bottom=0.16,
#      right=0.97,
#      top=0.99,
#      wspace=0.00,
#      hspace=0.00)

plt.subplots_adjust(
    left=0.17,
    bottom=0.19,
    right=0.97,
    top=0.99,
    wspace=0.00,
    hspace=0.00)


# plt.figure(figsize=(3.8, 2.3))
# plt.subplots_adjust(
#     left=0.15,
#     bottom=0.15,
#     right=0.97,
#     top=0.94,
#     wspace=0.00,
#     hspace=0.00)



#plt.xticks(fontsize=8, weight='medium')
#plt.yticks(fontsize=8, weight='medium')
plt.xlabel(u'并行度')#, size=8, weight='medium')
plt.ylabel(u'吞吐量增长率')#, size=8, weight='medium')
plt.ylim(0, 14)
marksize = 4
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='s', markersize=marksize, linewidth=linewidth, color='black')
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='^', markersize=marksize, linewidth=linewidth, color='grey')
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='D', markersize=marksize, linewidth=linewidth, color='dimgray')

plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3]], loc='best', frameon=False)
plt.show()
# plt.savefig(dir + fileName + "-patent.pdf")

