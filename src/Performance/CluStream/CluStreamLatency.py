import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')

dir = '../../Data/Performance/CluStream/'


datasets = ['large-KDD99', 'large-CoverType', 'large-KDD98']

# CluStream
# latency
moa = [68.3, 43.5, 180.2]
ordered_CluStream = [75.5, 47.6, 224.9]
unordered_CluStream = [92.1, 94.7, 236.7]

pos = list(range(len(moa)))
width = 0.23
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(3.6, 2.2))
plt.rc('pdf', fonttype=42)
plt.subplots_adjust(
    left=0.15,
    bottom=0.1,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, moa, width, label="MOA", color='pink', edgecolor='black')

rects3 = plt.bar([p + width for p in pos], unordered_CluStream, width, color='lightgreen', label="Unordered-CluStream", hatch='///', edgecolor='black')

rects2 = plt.bar([p + width * 2 for p in pos], ordered_CluStream, width, color='lightblue', label="DistStream-CluStream", hatch='\\\\\\', edgecolor='black')


plt.ylabel('Latency per record ($\mu s$)')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)
plt.xticks(fontsize=10)

plt.ylim(0, 400)
plt.legend(loc='upper left', frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%d'%int(h),
                ha='center', va='bottom', rotation=angle)

autolabel(rects1, 0, 45)
autolabel(rects2, 0, 45)
autolabel(rects3, 0, 45)
# plt.show()
plt.savefig(dir + "Latency-CluStream.pdf")
