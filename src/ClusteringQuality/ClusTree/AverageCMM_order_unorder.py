import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')

dir = '../../Data/ClusteringQuality/ClusTree/'

plt.rc('pdf', fonttype=42)
#plt.rc('font', family='Arial', size=10, weight='roman')




datasets = ['KDD-99', 'CoverType', 'KDD-98']

#moa = [0.921711248, 0.793698678, 0.851896573]
moa = [1, 1, 1]
ordered_ClusTree = [0.99, 0.97, 0.99]
unordered_ClusTree = [0.7873491934351042/0.921711248, 0.583772748/0.793698678, 0.806930145/0.851896573]

pos = list(range(len(moa)))
width = 0.23
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(4.0, 2.3))

plt.subplots_adjust(
    left=0.12,
    bottom=0.09,
    right=0.97,
    top=0.97,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, moa, width, color='lightpink', label="MOA", edgecolor='black')

rects3 = plt.bar([p + width for p in pos], unordered_ClusTree, width, hatch='///', color='lightgreen', label="Unordered-ClusTree", edgecolor='black')

rects2 = plt.bar([p + width * 2 for p in pos], ordered_ClusTree, width, hatch='\\\\\\', color='deepskyblue', label="DistStream-ClusTree", edgecolor='black')


plt.ylabel('Normalized CMM')#, size=10, weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)

plt.ylim(0, 2.0)
# plt.legend(loc='upper left', prop=font, frameon=False)
plt.legend(loc='upper left', frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.2f'%float(h),
                ha='center', va='bottom', rotation=angle)

autolabel(rects1, 0, 30)
autolabel(rects2, 0, 30)
autolabel(rects3, 0, 30)
#plt.show()
plt.savefig(dir + "ClusTreeAverageCMM-order-unorder.pdf")
