import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')
plt.rc('pdf', fonttype=42)

dir = '../../Data/ClusteringQuality/DStream/'


datasets = ['KDD-99', 'CoverType', 'KDD-98']

moa = [1.0, 1.0, 1.0]
ordered_DStream = [0.98, 0.850626809/0.883024494, 0.813879493/0.883024494]
unordered_DStream = [0.669867865/0.883024494, 0.6/0.883024494, 0.88]

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

rects3 = plt.bar([p + width for p in pos], unordered_DStream, width, color='lightgreen', label="unordered-DStream", hatch='///', edgecolor='black')

rects2 = plt.bar([p + width * 2 for p in pos], ordered_DStream, width, color='deepskyblue', label="DistStream-DStream", hatch='\\\\\\',  edgecolor='black')


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

autolabel(rects1, 0, 45)
autolabel(rects2, 0, 45)
autolabel(rects3, 0, 45)
#plt.show()
plt.savefig(dir + "DStreamAverageCMM-order-unorder.pdf")
