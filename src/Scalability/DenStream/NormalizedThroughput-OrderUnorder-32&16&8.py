import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')

dir = '../../Data/Scalability/DenStream/'

datasets = ['large-KDD99', 'large-CoverType', 'large-KDD98']

# CluStream
# throughput
p_8 = [2.40, 1.53, 1.02]
p_16 = [2.23, 1.23, 1.01]
p_32 = [2.11, 1.26, 1.11]

pos = list(range(len(p_8)))
width = 0.23
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.rc('pdf', fonttype=42)
fig, ax = plt.subplots(figsize=(3.6, 2.2))

plt.subplots_adjust(
    left=0.12,
    bottom=0.1,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)



rects1 = plt.bar(pos, p_8, width, color='lightpink', label="p=8", edgecolor='black')

rects3 = plt.bar([p + width for p in pos], p_16, width,  color='lightgreen', label="p=16", hatch='///', edgecolor='black')

rects2 = plt.bar([p + width * 2 for p in pos], p_32, width,  color='deepskyblue',label="p=32", hatch='\\\\\\', edgecolor='black')


plt.ylabel('Normalized Throughput', weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)
plt.xticks(fontsize=10)

plt.ylim(0, 3.5)
# plt.legend(loc='upper left', frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)
plt.legend(ncol=3, loc="upper left",
           frameon=False, #bbox_to_anchor=(0.55, 0),
           labelspacing=0.05, markerfirst=True,
           borderaxespad=0.1, handletextpad=0.3)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.2f'%float(h),
                ha='center', va='bottom', fontsize=11, rotation=angle)

autolabel(rects1, 0.01, 320)
autolabel(rects2, 0.01, 320)
autolabel(rects3, 0.01, 320)
plt.show()
# plt.savefig(dir + "NormalizedThroughPut-CluStream-8&16&32.pdf")
