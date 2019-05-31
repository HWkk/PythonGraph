import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')
plt.rc('pdf', fonttype=42)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

dir = '../../Data/Scalability/CluStream/'
fileName = 'Clustream-Dimension-KDD98-Latency-xDimension'
data = pd.read_excel(dir + fileName + '.xlsx')

fig, ax = plt.subplots(figsize=(3.6, 2.4))

plt.subplots_adjust(
    left=0.16,
    bottom=0.19,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)






plt.xlabel('Feature number')
plt.ylabel('Latency per micro-cluster ($\mu s$)')#, size=10, weight='medium')
plt.ylim(0, 1.3)

marksize = 3
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='D', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='o', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='s', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[4]], marker='^', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[5]], marker='*', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[6]], marker='p', markersize=marksize, linewidth=linewidth)

plt.legend(loc="best", frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + fileName + ".pdf")