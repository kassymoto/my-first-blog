from matplotlib import rcParams
import random

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
a = random.sample(range(1,10), k=3)
ax.plot(a, label='test')

ax.legend()
plt.show()
