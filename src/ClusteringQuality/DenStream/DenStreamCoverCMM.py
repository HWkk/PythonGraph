import matplotlib.pyplot as plt
import pandas as pd

dir = '../../Data/ClusteringQuality/DenStream/'
fileName = 'DenStream-Cover-Normalized'
data = pd.read_excel(dir + fileName + '.xlsx')

plt.figure(figsize=(4.5, 2.7))
plt.subplots_adjust(
    left=0.1,
    bottom=0.13,
    right=0.96,
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
plt.xlabel('length of stream(' + r'$\times{10^3}$' + ')', size=8, weight='medium')
plt.ylabel('Normalized CMM', size=8, weight='medium')
plt.ylim(0.3, 1.05)
plt.xlim(0, 600)

marksize = 2
linewidth = 1

plt.plot(data[data.columns[0]], data[data.columns[1]], linestyle=":", linewidth=linewidth - 0.2, color='#978a84')
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='^', markersize=marksize, linewidth=linewidth)
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='D', markersize=marksize, linewidth=linewidth)
plt.legend(loc=8, prop=font, frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + fileName + ".pdf")

