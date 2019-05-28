import matplotlib.pyplot as plt

dir = '../../Data/Scalability/DenStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

ordered_DenStream = [20.10, 18.42, 3.11]
unordered_Denstream = [9.51, 14.62, 2.81]

pos = list(range(len(ordered_DenStream)))
width = 0.2

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
fig, ax = plt.subplots(figsize=(4.3, 2.5))
plt.subplots_adjust(
    left=0.13,
    bottom=0.13,
    right=0.95,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, ordered_DenStream, width, color='lightpink', label="ordered-DenStream", edgecolor='black')

rects2 = plt.bar([p + width for p in pos], unordered_Denstream, width, color='lightgreen', label="unordered-DenStream", hatch='xxx', edgecolor='black')

plt.ylabel('Throughput(' + r'${10^4}$' + ' records/s)', size=10, weight='medium')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(datasets)
plt.ylim(0, 25)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%d'%int(h),
                ha='center', va='bottom', fontsize=8, rotation=angle)

autolabel(rects1, 0, 0)
autolabel(rects2, 0, 0)
plt.legend(loc="upper left", prop=font, frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
plt.show()
# plt.savefig(dir + "DenStream-p=32-Throughput.pdf")
