import matplotlib.pyplot as plt
import pandas as pd

dir = '../../Data/Scalability/CluStream/'
fileName = 'Clustream-Dimension-KDD98-Latency'
data = pd.read_excel(dir + fileName + '.xlsx')

plt.figure(figsize=(3.8, 2.3))
plt.subplots_adjust(
    left=0.18,
    bottom=0.15,
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
plt.xlabel('Dimension', size=8, weight='medium')
plt.ylabel('Latency(us)', size=8, weight='medium')
plt.ylim(0, 0.35)

marksize = 3
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='D', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='o', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='s', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[4]], marker='*', markersize=marksize+2, linewidth=linewidth)

plt.legend(loc="best", prop=font, frameon=False, labelspacing=0.2, ncol=2, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + fileName + ".pdf")