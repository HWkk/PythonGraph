import matplotlib.pyplot as plt
import pandas as pd

dir = '../../Data/Scalability/DenStream/'
fileName = 'DenStream-MaxSpeedup'
data = pd.read_excel(dir + fileName + '.xlsx')
print data
print data.columns

plt.figure(figsize=(3.8, 2.3))
plt.subplots_adjust(
    left=0.13,
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
plt.xlabel('Parallelism', size=8, weight='medium')
plt.ylabel('Throughput Gain', size=8, weight='medium')

marksize = 3
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='D', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='o', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='s', markersize=marksize, linewidth=linewidth)

plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3]], loc='best', prop=font, frameon=False)
plt.show()
# plt.savefig(dir + fileName + ".pdf")

