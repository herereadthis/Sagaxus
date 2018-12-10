from scipy import stats

# all 20 will be successes
pmf = stats.binom.pmf(20,20,0.9)
print(pmf)
# at least 18 successes out of 20
cdf = stats.binom.pmf(18,20,0.9)
print(cdf)

