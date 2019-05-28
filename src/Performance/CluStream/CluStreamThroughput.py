import matplotlib.pyplot as plt

dir = '../../Data/Performance/CluStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

# CluStream
# throughput
moa = [14.634, 23.011, 5.548]
ordered_CluStream = [13.253, 20.988, 4.446]
unordered_CluStream = [10.854, 10.557, 4.224]

pos = list(range(len(moa)))
width = 0.2
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(3.5, 2.2))
plt.subplots_adjust(
    left=0.16,
    bottom=0.1,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, moa, width, color='lightpink', hatch='///', label="MOA", edgecolor='black')

rects2 = plt.bar([p + width for p in pos], ordered_CluStream, width, color='lightgreen', label="ordered-CluStream", hatch='xxx', edgecolor='black')

rects3 = plt.bar([p + width * 2 for p in pos], unordered_CluStream, width, color='deepskyblue', label="unordered-CluStream", hatch='\\\\\\', edgecolor='black')

plt.ylabel('Throughput(' + r'${10^3}$' + ' records/s)', size=10, weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)

plt.ylim(0, 40)
plt.legend(loc='upper left', prop=font, frameon=False)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%d'%int(h),
                ha='center', va='bottom', fontsize=8, rotation=angle)

autolabel(rects1, 0, 0)
autolabel(rects2, 0, 0)
autolabel(rects3, 0, 0)
plt.show()
# plt.savefig(dir + "ThroughPut-CluStream.pdf")
