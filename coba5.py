import matplotlib.pyplot as plt
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm

# cara membuat samplle data
sample = normal(loc=50, scale=5, size=1000)
sample_mean = mean(sample)
sample_std = std(sample)
print("Mean=%.3f \nStandard Deviation=%.3f" % (sample_mean, sample_std))
dist = norm(sample_mean, sample_std)
dist
# pertama, buat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)]  # menggunakan list comprehension
# manfaatkan list comprehension untuk menerapkan method pdf
# berdasarkan value (yang telah disiapkan sebelumnya) pada data dist
probabilitas = [dist.pdf(value) for value in values]
probabilitas  # panggil variabel probabilitas untuk mengetahui hasilnya
# panggil variabel sample untuk mengetahui hasilnya
plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilitas)
# sample
# atau tampilkan dalam bentuk histogram
plt.figure(figsize=(5, 4))  # perkecil media gambar
plt.hist(sample, bins=10, density=True)
plt.show()
