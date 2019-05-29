import matplotlib.pyplot as plt

dir = '../../Data/ClusteringQuality/DStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

moa = [0.883024494, 0.800474895, 0.811129942]
ordered_DStream = [0.889086355, 0.780626809, 0.813879493]
unordered_DStream = [0.669867865, 0.669867865, 0.714152371]

pos = list(range(len(moa)))
width = 0.2
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(4.9, 2.2))
plt.subplots_adjust(
    left=0.12,
    bottom=0.1,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, moa, width, color='lightpink', hatch='///', label="MOA", edgecolor='black')

rects2 = plt.bar([p + width for p in pos], ordered_DStream, width, color='lightgreen', label="ordered-DStream", hatch='xxx', edgecolor='black')

rects3 = plt.bar([p + width * 2 for p in pos], unordered_DStream, width, color='deepskyblue', label="unordered-DStream", hatch='\\\\\\', edgecolor='black')

plt.ylabel('Average CMM', size=10, weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)

plt.ylim(0, 1.15)
# plt.legend(loc='upper left', prop=font, frameon=False)
plt.legend(loc='upper left', prop=font, frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.2f'%float(h),
                ha='center', va='bottom', fontsize=8, rotation=angle)

autolabel(rects1, 0, 0)
autolabel(rects2, 0, 0)
autolabel(rects3, 0, 0)
plt.show()
# plt.savefig(dir + "DStreamAverageCMM-order-unorder.pdf")
