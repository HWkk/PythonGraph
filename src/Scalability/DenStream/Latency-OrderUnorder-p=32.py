import matplotlib.pyplot as plt

dir = '../../Data/Scalability/DenStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['large-KDD99', 'large-CoverType', 'large-KDD98']

ordered_DenStream = [4.975, 5.429, 32.154]
unordered_Denstream = [10.515, 6.840, 35.587]

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

rects1 = plt.bar(pos, ordered_DenStream, width, color='lightpink', label="DistStream-DenStream", hatch='///', edgecolor='black')
rects2 = plt.bar([p + width for p in pos], unordered_Denstream, width, color='lightgreen', label="unordered-DenStream", hatch='xxx', edgecolor='black')

plt.ylabel('Latency(us)', size=10, weight='medium')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(datasets)
plt.ylim(0, 40)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.1f'%float(h),
                ha='center', va='bottom', fontsize=8, rotation=angle)

autolabel(rects1, 0, 0)
autolabel(rects2, 0, 0)
plt.legend(loc='upper left', prop=font, frameon=False)
plt.show()
# plt.savefig(dir + "DenStream-p=32-Latency.pdf")
