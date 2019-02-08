'''
Generate a bunch of random numbers from a normal distribution, then determine
the distribution from the samples, and get stats from
'''
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

population_mean = 0
population_std = 1

# Grab a bunch of samples from a normal distribution with mean = 0, variance=4
data = scipy.stats.norm.rvs(
    size=100000,
    loc=0,
    scale=population_std**2,
    random_state=123
)
data_histogram = np.histogram(data, bins=100)

print('Sample Data: min={:.5f}, max={:.5f}'.format(np.min(data), np.max(data)))

# Create a distribution from the samples. Treat it as a continuous distribution.
histogram_distribution = scipy.stats.rv_histogram(data_histogram)
# PDF at min and max should  be close to 0
pdf_min = histogram_distribution.pdf(np.min(data))
pdf_max = histogram_distribution.pdf(np.max(data))
pdf_mean = histogram_distribution.pdf(population_mean)
print('PDF: min={:.05f}, max={:.05f}, mean={:.05f}'.format(
    pdf_min, pdf_max, pdf_mean
))
# CDF at min should be 0, CDF at max should be 1
cdf_min = histogram_distribution.cdf(np.min(data))
cdf_max = histogram_distribution.cdf(np.max(data))
cdf_mean = histogram_distribution.cdf(population_mean)
print('CDF: min={:.05f}, max={:.05f}, mean={:.05f}'.format(
    cdf_min, cdf_max, cdf_mean
))
# get the mean, standard deviation, variance, and stats
hist_mean = histogram_distribution.mean()
hist_std = histogram_distribution.std()
hist_var = histogram_distribution.var()
print('Histogram: mean={:.05f}, s.d.={:.05f}, variance={:.05f}'.format(
    hist_mean, hist_std, hist_var
))

x = np.linspace(-5, 5, 100)
plt.title('PDF from sample data')
plt.hist(data, density=True, bins=50, color='b', edgecolor='w')
plt.plot(x, histogram_distribution.pdf(x), label='PDF')
plt.plot(x, histogram_distribution.cdf(x), label='CDF')
plt.legend()
plt.xlim(-6,6)
plt.show()

