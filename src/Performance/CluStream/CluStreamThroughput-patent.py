#coding:utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

dir = '../../Data/Performance/CluStream/'


datasets = ['large-KDD99', 'large-CoverType', 'large-KDD98']

# CluStream
# throughput
moa = [14.634, 23.011, 5.548]
ordered_CluStream = [13.253, 20.988, 4.446]
unordered_CluStream = [10.854, 10.557, 4.224]

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



rects1 = plt.bar(pos, moa, width, color='white', label=u"单机CluStream", edgecolor='black')

rects3 = plt.bar([p + width for p in pos], unordered_CluStream, width,  color='gray', label=u"无序CluStream", hatch='///', edgecolor='black')

rects2 = plt.bar([p + width * 2 for p in pos], ordered_CluStream, width,  color='white',label=u"有序CluStream", hatch='\\\\\\', edgecolor='black')


plt.ylabel(u'吞吐率 (' + r'${\times 10^3}$' + u' 条数据/秒)', weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)
plt.xticks(fontsize=10)

plt.ylim(0, 45)
plt.legend(loc='upper left', frameon=False, labelspacing=0.3, borderaxespad=0.2, columnspacing=2.2, handletextpad=0.5)

def autolabel(rects, loc, angle):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.+loc, 1.01*h, '%0.1f'%float(h),
                ha='center', va='bottom', fontsize=11, rotation=angle)

autolabel(rects1, 0.01, 45)
autolabel(rects2, 0.01, 45)
autolabel(rects3, 0.01, 45)
# plt.show()
plt.savefig(dir + "ThroughPut-CluStream-patent.png")
