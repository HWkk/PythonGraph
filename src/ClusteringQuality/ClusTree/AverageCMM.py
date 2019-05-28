import matplotlib.pyplot as plt

dir = '../../Data/ClusteringQuality/ClusTree/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

moa = [0.921711248, 0.793698678, 0.851896573]
distStream = [0.927299924, 0.784683554, 0.822933404]

pos = list(range(len(moa)))
width = 0.2

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
fig, ax = plt.subplots(figsize=(4.3, 2.5))
plt.subplots_adjust(
    left=0.15,
    bottom=0.13,
    right=0.95,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, moa, width, color='lightpink', label="MOA", edgecolor='black')

rects2 = plt.bar([p + width for p in pos], distStream, width, color='lightgreen', label="DistStream-ClusTree", hatch='xxx', edgecolor='black')

plt.ylabel('Average CMM', size=10, weight='medium')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(datasets)
plt.ylim(0, 1.15)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.2f'%float(h),
                ha='center', va='bottom', fontsize=8, rotation=angle)

autolabel(rects1, 0, 0)
autolabel(rects2, 0, 0)
plt.legend(loc=1, prop=font, frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + "ClusTreeAverageCMM.pdf")
