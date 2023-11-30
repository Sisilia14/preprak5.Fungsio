import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]
a = [2, 3, 4, 5, 6]
b = [4, 8, 3, 9, 6]

plt.scatter(a, b, label="Titik Gabungan AB", color="red")
plt.scatter(x, y, label="Titik Gabungan XY", color="blue")


plt.title("Scatter Plot Percobaan 4")
plt.xlabel("Nilai X")
plt.ylabel("Nilai Y")


plt.legend()
plt.show()
