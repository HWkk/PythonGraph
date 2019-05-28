import matplotlib.pyplot as plt

dir = '../../Data/Scalability/DenStream/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'CoverType', 'KDD98']

ordered_DenStream_16 = [0.553, 1.262, 2.33]
unordered_DenStream_16 = [1.835, 1.642, -0.985]
ordered_DenStream_32 = [4.975, 5.429, 32.154]
unordered_DenStream_32 = [10.515, 6.840, 35.587]
# ordered_DenStream_16 = [5.528, 6.691, 34.48]
# unordered_DenStream_16 = [12.35, 8.482, 34.602]

pos = list(range(len(unordered_DenStream_32)))
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

rects1 = plt.bar(pos, ordered_DenStream_32, width, color='lightpink', edgecolor='black')
rects2 = plt.bar(pos, ordered_DenStream_16, width, bottom=ordered_DenStream_32, color='lightpink', label="ordered-DenStream", edgecolor='black')

rects3 = plt.bar([p + width for p in pos], unordered_DenStream_32, width, color='lightgreen', hatch='xxx', edgecolor='black')
rects4 = plt.bar([p + width for p in pos], unordered_DenStream_16, width, bottom=unordered_DenStream_32, color='lightgreen', label="unordered-DenStream", hatch='xxx', edgecolor='black')

plt.ylabel('Latency(us)', size=10, weight='medium')
ax.set_xticks([p + 0.5 * width for p in pos])
ax.set_xticklabels(datasets)
plt.ylim(0, 40)

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
plt.show()
# plt.savefig(dir + "DenStream-p=16&32-Latency.pdf")
