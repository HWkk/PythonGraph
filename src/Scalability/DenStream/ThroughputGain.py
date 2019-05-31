import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally
plt.rc('font', family='Helvetica', size=11, weight='roman')
plt.rc('pdf', fonttype=42)

dir = '../../Data/Scalability/DenStream/'
fileName = 'DenStream-MaxSpeedup'
data = pd.read_excel(dir + fileName + '.xlsx')
print data
print data.columns

fig, ax = plt.subplots(figsize=(3.6, 2.4))

plt.subplots_adjust(
    left=0.14,
    bottom=0.19,
    right=0.97,
    top=0.99,
    wspace=0.00,
    hspace=0.00)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'




plt.xlabel('Parallelism degree')#, size=8, weight='medium')
plt.ylabel('Throughput gain')#, size=8, weight='medium')

marksize = 4
linewidth = 1.2

plt.plot(data[data.columns[0]], data[data.columns[1]], marker='s', markersize=marksize, linewidth=linewidth, color='b')
plt.plot(data[data.columns[0]], data[data.columns[2]], marker='^', markersize=marksize, linewidth=linewidth, color='g')
plt.plot(data[data.columns[0]], data[data.columns[3]], marker='D', markersize=marksize, linewidth=linewidth, color='r')

plt.legend(labels=[data.columns[1], data.columns[2], data.columns[3]], loc='best', frameon=False)
#plt.show()
plt.savefig(dir + fileName + ".pdf")

