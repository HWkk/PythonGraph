import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')

dir = '../../Data/Performance/DenStream/'


datasets = ['large-KDD99', 'large-CoverType', 'large-KDD98']

##DenStream
#throughput
moa = [24.931, 21.787, 8.506]
ordered_DenStream = [23.570, 19.616, 7.135]
unordered_DenStream = [17.770, 15.196, 6.406]

pos = list(range(len(moa)))
width = 0.23
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rc('pdf', fonttype=42)
fig, ax = plt.subplots(figsize=(3.6, 2.2))

plt.subplots_adjust(
    left=0.15,
    bottom=0.1,
    right=0.97,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, moa, width, color='lightpink', label="MOA-DenStream", edgecolor='black')

rects3 = plt.bar([p + width for p in pos], unordered_DenStream, width, color='lightgreen', label="Unordered-DenStream", hatch='///', edgecolor='black')

rects2 = plt.bar([p + width * 2 for p in pos], ordered_DenStream, width, color='deepskyblue', label="DistStream-DenStream", hatch='\\\\\\', edgecolor='black')


plt.ylabel('Throughput (' + r'${\times 10^3}$' + ' records/s)', weight='roman')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)

plt.xticks(fontsize=10)

plt.ylim(0, 45)
plt.legend(loc='upper right',frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)


def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.1f'%float(h),
                ha='center', va='bottom', fontsize=11, rotation=angle)

autolabel(rects1, 0.01, 45)
autolabel(rects2, 0.01, 45)
autolabel(rects3, 0.01, 45)

# plt.show()
plt.savefig(dir + "ThroughPut-DenStream.pdf")