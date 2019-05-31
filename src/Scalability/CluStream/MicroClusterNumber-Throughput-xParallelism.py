import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')
plt.rc('pdf', fonttype=42)

dir = '../../Data/Scalability/CluStream/'
fileName = 'Clustream-MicroCluster-KDD98-Throughput-xParallelism'
data = pd.read_excel(dir + fileName + '.xlsx')
# plt.figure(figsize=(3.8, 2.3))
# plt.subplots_adjust(
#     left=0.16,
#     bottom=0.15,
#     right=0.97,
#     top=0.94,
#     wspace=0.00,
#     hspace=0.00)

fig, ax = plt.subplots(figsize=(3.6, 2.4))

plt.subplots_adjust(
    left=0.12,
    bottom=0.19,
    right=0.97,
    top=0.99,
    wspace=0.00,
    hspace=0.00)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


plt.xlabel('Parallelism degree')#, size=8, weight='medium')

plt.ylabel('Throughput (' + r'$\times{10^3}$' + ' records/s)')
# plt.xlim(15, 160)
# plt.ylim(0, 55000)

marksize = 3
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='D', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='o', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='s', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[4]], marker='^', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[5]], marker='*', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[6]], marker='p', markersize=marksize, linewidth=linewidth)

plt.legend(loc='best', frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + fileName + ".pdf")

