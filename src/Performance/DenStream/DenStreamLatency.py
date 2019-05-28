import matplotlib.pyplot as plt

dir = '../../Data/Performance/DenStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

#DenStream
#latency
moa = [0.0401, 0.0449, 0.1176]
ordered_DenStream = [0.0454, 0.0510, 0.1402]
unordered_DenStream = [0.0563, 0.0658, 0.1561]

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

rects2 = plt.bar([p + width for p in pos], ordered_DenStream, width, color='lightgreen', label="ordered-CluStream", hatch='xxx', edgecolor='black')

rects3 = plt.bar([p + width * 2 for p in pos], unordered_DenStream, width, color='deepskyblue', label="unordered-CluStream", hatch='\\\\\\', edgecolor='black')

plt.ylabel('Latency(ms)', size=10, weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)

plt.ylim(0, 0.4)
plt.legend(loc='upper left', prop=font, frameon=False)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.2f'%float(h),
                ha='center', va='bottom', fontsize=8, rotation=angle)

autolabel(rects1, 0, 45)
autolabel(rects2, 0, 45)
autolabel(rects3, 0, 45)

plt.show()
# plt.savefig(dir + "Latency-DenStream.pdf")