import matplotlib.pyplot as plt

dir = '/Users/kk/Documents/ISCAS/StreamingML/document/clustering/streamclustering/TestResult/pic/'
font = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 10,
        }

datasets = ['KDD99', 'Cover', 'KDD98']
#throughput
# moa = [2148, 5865, 1244]
# tenK = [7325, 8599, 2885]
# fiftyK = [7864, 8347, 3072]

#latency
moa = [229, 99, 76]
tenK = [67, 67, 33]
fiftyK = [62, 69, 31]

#CMM
# moa = [0.929459308337903, 0.868509414589778, 0.988369311594295]
# tenK = [0.932866419332979, 0.870069867692679, 0.97501592580036]
# fiftyK = [0.918654811278336, 0.876945452702443, 0.982762752745903]

pos = list(range(len(moa)))
width = 0.2

fig, ax = plt.subplots(figsize=(5.3, 2.5))
plt.subplots_adjust(
    left=0.11,
    bottom=0.19,
    right=0.68,
    top=0.95,
    wspace=0.00,
    hspace=0.00)

# plt.ylim(0, 1.0)
plt.bar(pos, moa, width, color='lightpink', label="MOA", edgecolor='black')

plt.bar([p + width for p in pos], tenK, width, color='lightgreen', label="10K(5K for KDD98)", hatch='xxx', edgecolor='black')

plt.bar([p + width * 2 for p in pos], fiftyK, width, color='deepskyblue', label="50K(10K for KDD98)", hatch='\\\\\\', edgecolor='black')

plt.xlabel('Dataset', size=10, weight='medium')
# plt.ylabel('CMM', size=10, weight='medium')
plt.ylabel('Latency(s)', size=10, weight='medium')
ax.set_xticks([p + 1.0 * width for p in pos])
ax.set_xticklabels(datasets)

# plt.xlim(min(pos) - width, max(pos) + width * 4)
# plt.ylim([0, max(moa + tenK + fiftyK) * 1.5])

plt.legend(loc='upper right', bbox_to_anchor=(1.6, 0.65), prop=font, frameon=False)
# plt.show()
# plt.savefig(dir + "ThroughPut-MOA-Clustream.pdf")
plt.savefig(dir + "Latency-MOA-Clustream.pdf")
# plt.savefig(dir + "CMM-MOA-Clustream.pdf")
