import matplotlib.pyplot as plt

dir = '/Users/kk/Documents/ISCAS/StreamingML/document/clustering/streamclustering/TestResult/pic/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

phases = ['FindMicroCluster', 'LocalUpdate', 'GlobalUpdate']

#calculate Time
p16 = [56869.5625, 5415.125, 1106]
p32 = [43830.875, 5037.3125, 1600]

#time
p16 = [89845, 13135, 1106]
p32 = [82967, 17572, 1600]

pos = list(range(len(p16)))
width = 0.2

fig, ax = plt.subplots(figsize=(3.8, 2.5))
plt.subplots_adjust(
    left=0.23,
    bottom=0.19,
    right=0.95,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

plt.bar(pos, p16, width, color='lightpink', label="p=16", edgecolor='black')

plt.bar([p + width for p in pos], p32, width, color='lightgreen', label="p=32", hatch='xxx', edgecolor='black')

plt.xlabel('Phase', size=10, weight='medium')
plt.ylabel('ProcessTime(ms)', size=10, weight='medium')
# plt.ylabel('Latency(s)', size=10, weight='medium')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(phases)

plt.legend(loc=1, prop=font, frameon=False)
# plt.show()
plt.savefig(dir + "Clustream-Cover-BottleNeck.pdf")
# plt.savefig(dir + "Clustream-Cover-BottleNeck-CaculateTime.pdf")

#IndianRed xxx
#SkyBlue +++