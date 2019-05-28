import matplotlib.pyplot as plt

dir = '../../Data/Scalability/CluStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

ordered_CluStream_16 = [8.56, 15.42, 3.68]
unordered_Clustream_16 = [7.62, 14.90, 3.47]
ordered_CluStream_32 = [1.83, 4.00, 0.97]
unordered_Clustream_32 = [1.99, 2.02, -0.45]
# ordered_CluStream_32 = [10.39, 19.42, 4.65]
# unordered_Clustream_32 = [9.61, 16.92, 3.02]

pos = list(range(len(ordered_CluStream_16)))
width = 0.2

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
fig, ax = plt.subplots(figsize=(4.3, 2.5))
plt.subplots_adjust(
    left=0.15,
    bottom=0.13,
    right=0.95,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

rects1 = plt.bar(pos, ordered_CluStream_16, width, color='lightpink', edgecolor='black')
rects2 = plt.bar(pos, ordered_CluStream_32, width, bottom=ordered_CluStream_16, color='lightpink', label="ordered-CluStream", edgecolor='black')

rects3 = plt.bar([p + width for p in pos], unordered_Clustream_16, width, color='lightgreen', hatch='xxx', edgecolor='black')
rects4 = plt.bar([p + width for p in pos], unordered_Clustream_32, width, bottom=unordered_Clustream_16, color='lightgreen', label="unordered-CluStream", hatch='xxx', edgecolor='black')

plt.ylabel('Throughput(' + r'${10^4}$' + ' records/s)', size=10, weight='medium')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(datasets)
plt.ylim(0, 25)

# def autolabel(rects, loc, angle, multiple):
#     for rect in rects:
#         h = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2.+loc, multiple*h, '%d'%int(h),
#                 ha='center', va='bottom', fontsize=8, rotation=angle)
#
# autolabel(rects1, 0, 0, 1.01)
# autolabel(rects2, 0, 0, 5)
# autolabel(rects3, 0, 0, 1.01)
# autolabel(rects4, 0, 0, 5)
plt.legend(loc="upper left", prop=font, frameon=False, labelspacing=0.2, ncol=3, borderaxespad=0.3, columnspacing=1.2, handletextpad=0.5)
# plt.show()
plt.savefig(dir + "Clustream-p=16&32-Throughput.pdf")
