import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x= np.array([1,2,3,4,5,6])
y= np.array([3,6,2,4,3,7])

plt.title("Banyak Muncul Mata Dadu Budi dan")
plt.xlabel("Mata Dadu")
plt.ylabel("Banyak Muncul")
plt.axis([0,7,0,10])
plt.plot(x,y, marker="o", color="blue")
plt.grid()
plt.show()