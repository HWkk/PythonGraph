import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')

dir = '../../Data/Scalability/CluStream/'


datasets = ['large-KDD99', 'large-CoverType', 'large-KDD98']

ordered_CluStream = [103.9, 194.2, 46.5]
unordered_Clustream = [96.1, 169.2, 30.2]

pos = list(range(len(ordered_CluStream)))
width = 0.23

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.rc('pdf', fonttype=42)
fig, ax = plt.subplots(figsize=(3.6, 2.2))

plt.subplots_adjust(
    left=0.16,
    bottom=0.1,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects2 = plt.bar(pos, unordered_Clustream, width, color='lightgreen', label="Unordered-CluStream", hatch='///',  edgecolor='black')

rects1 = plt.bar([p + width for p in pos],ordered_CluStream, width, color='deepskyblue', label="DistStream-CluStream", hatch='\\\\\\',  edgecolor='black')


plt.ylabel('Throughput (' + r'$\times{10^3}$' + ' records/s)')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(datasets)
plt.ylim(0, 320)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.0f'%float(h),
                ha='center', va='bottom', rotation=angle)

autolabel(rects1, 0, 40)
autolabel(rects2, 0, 40)
plt.legend(loc="upper left", frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + "Clustream-p=32-Throughput.pdf")
