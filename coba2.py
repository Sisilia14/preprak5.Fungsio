import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 4, 6, 8, 10, 2, 4, 6, 8, 10])
ypoints = np.array([2, 4, 2, 4, 2, 2, 4, 2, 4, 2])

plt.figure(figsize=(5, 5))
plt.plot(xpoints, ypoints, color="green")
plt.xlim([0, 15])
plt.ylim([0, 15])

plt.title("ini Percobaan 2")
plt.xlabel("Nilai X")
plt.ylabel("Nilai Y")

plt.show()
