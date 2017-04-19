import matplotlib.pyplot as plt
import numpy as np

with open('test.log', 'r') as f:
	acc_y = map(lambda x: float(x), f.readlines()[1:])
x = np.linspace(0, len(acc_y), len(acc_y))

with open('train.log', 'r') as f:
	loss_y = map(lambda x: float(x), f.readlines()[1:])

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(x, loss_y)
ax1.set_ylim(0.0, 0.3)
ax1.set_ylabel("Loss")
ax1.set_title("Loss & Acc")

ax2 = ax1.twinx()
ax2.set_ylim(0.0, 1.0)
ax2.plot(x, acc_y, 'r')
ax2.set_ylabel("Acc")

plt.show()
