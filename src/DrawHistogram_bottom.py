import matplotlib.pyplot as plt

dir = '/Users/kk/Documents/ISCAS/StreamingML/document/clustering/streamclustering/TestResult/pic/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

params = ['1-32', '1-16', '5-32', '5-16', '10-32', '10-16']

find = [90658.00023, 117010.9985, 64338.99999, 108829.9999, 63755.00011, 104010.9999]
localU = [29399.0001678466, 24964.99872, 18405.00021, 16519.9995, 14479.00033, 13990.99994]
globalU = [1259, 1006, 2717, 2755, 8562, 8728]

pos = list(range(len(find)))
width = 0.8

fig, ax = plt.subplots(figsize=(5.5, 3.5))
plt.subplots_adjust(
    left=0.18,
    bottom=0.19,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

plt.bar(pos, find, width, label="FindMicroCluster", color='deepskyblue', hatch='\\\\\\', edgecolor='black')
plt.bar(pos, localU, width, bottom=find, label='LocalUpdate', color='lightgreen', hatch='xxx', edgecolor='black')
plt.bar(pos, globalU, width, bottom=list(map(sum, zip(list(localU), list(find)))), label='GlobalUpdate', color='lightpink', edgecolor='black')

plt.xlabel('BatchInterval-Parallelism', size=10, weight='medium')
plt.ylabel('ProcessTime(ms)', size=10, weight='medium')
# plt.ylabel('Latency(s)', size=10, weight='medium')
ax.set_xticks(pos)
ax.set_xticklabels(params)

# plt.xlim(min(pos) - width, max(pos) + width * 4)
plt.ylim([0, max(find + localU + globalU) * 1.5])

plt.legend(loc=1, prop=font, frameon=False, labelspacing=0.2, markerfirst=False, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + "KDD99-Clustream-BottleNeck.pdf")

#xxx
#SkyBlue +++
#IndianRed ///
