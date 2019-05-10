import matplotlib.pyplot as plt
import pandas as pd

dir = '/Users/kk/Documents/ISCAS/StreamingML/document/clustering/streamclustering/TestResult/pic/'
fileName = 'Cover-Throughput-10w-10s'
data = pd.read_excel(dir + fileName + '.xlsx')
print data
print data.columns

plt.figure(figsize=(3.8, 2.3))
plt.subplots_adjust(
    left=0.18,
    bottom=0.13,
    right=0.97,
    top=0.94,
    wspace=0.00,
    hspace=0.00)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 8,
        }

plt.xticks(fontsize=8, weight='medium')
plt.yticks(fontsize=8, weight='medium')
plt.xlabel('Parallelism', size=8, weight='medium')
plt.ylabel('Throughput(records/s)', size=8, weight='medium')

marksize = 3
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='D', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='o', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='s', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[4]], marker='*', markersize=marksize+2, linewidth=linewidth)

plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3], data.columns[4]], loc='best', prop=font, frameon=False)
# plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3]], loc='best', prop=font, frameon=False)
# plt.grid(axis='y')
# plt.show()
plt.savefig(dir + fileName + ".pdf")

#goldenrod seagreen darkviolet dodgerblue red
