import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

data = np.loadtxt("notas.csv", skiprows=1)
print(data)

print(st.describe(data))                                                       # Descripcion rapida de los datos

plt.hist(data, range(0, 11))                                                   # Histograma con plt
plt.xticks(range(0, 11))
plt.grid(True)

plt.vlines(5, 0, 100, lw=5, colors='red', alpha=0.8)
plt.fill_between([0, 5], [100, 100], color='red', alpha=0.5)
plt.show()


plt.hist(data, range(0, 11), cumulative=True)                                  # Histograma acumulado
plt.xticks(range(0, 11))

plt.vlines(5, 0, 400, lw=5, colors='red', alpha=0.8)
plt.fill_between([0, 5], [400, 400], color='red', alpha=0.5)

plt.grid(True)
plt.show()


from numpy import nanmean, nanstd
mean = nanmean(data)                                                           # Media
print(mean)

typ_dev = nanstd(data)
print(typ_dev)                                                                 # Desviacion tipica


# Distribucion normal
norm_dist = st.norm(loc=mean, scale=typ_dev)

x = np.linspace(0, 10, 100)

y1 = norm_dist.pdf(x)                                                          # Funcion densidad de probabilidad ("probability density function") 'pdf'
print(y1)

plt.plot(x, y1)
plt.grid(True)
plt.show()

y2 = norm_dist.cdf(x)                                                          # Funcion de distribucion ("cumulative distribution function") 'cdf'
print(y2)

plt.plot(x, y2)
plt.grid(True)


# Test de Kolmogorov-Smirnov
data2 = norm_dist.cdf
print(st.kstest(data, norm_dist.cdf))

print(st.normaltest(data))                                                     # Test de contraste de bondad de ajuste con un valor p mas alto
