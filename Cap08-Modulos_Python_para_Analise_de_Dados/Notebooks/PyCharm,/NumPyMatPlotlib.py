import numpy as np
import matplotlib.pylot as plt

a = np.random.randn(400,2)
print(a)
m = a.mean(0)
print (m, m.shape)

plt.plot(a[:,0], a[:,1], 'o', markersize=5, alpha=0.50)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()