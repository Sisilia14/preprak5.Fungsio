import matplotlib.pyplot as plt
import numpy as np

Y1 = np.array([1, 3, 5, 7, 9])
Y2 = np.array([2, 4, 6, 8, 10])
Y3 = np.array([3, 5, 7, 9])
Y4 = np.array([7, 5, 3, 1])
Y5 = np.array([8, 6, 4, 2])
Y6 = np.array([1, 2, 4, 5, 7, 8, 10])

plt.plot(Y1, label="Garis 1")
plt.plot(Y2, label="Garis 2")
plt.plot(Y3, label="Garis 3")
plt.plot(Y4, label="Garis 4")
plt.plot(Y5, label="Garis 5")
plt.plot(Y6, label="Garis 6")

plt.title("ini percobaan 3")
plt.xlabel("Nilai x")
plt.ylabel("Nilai y")

plt.legend()
plt.show()
