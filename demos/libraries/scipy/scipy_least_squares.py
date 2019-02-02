'''
Get least squares fit over bivariate data
'''
from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1963, 1968, 1971, 1974, 1975, 1978, 1981, 1985, 1988, 1991, 1995, 
    1999, 2001, 2002, 2006, 2007, 2008, 2009, 2012, 2013, 2014])
y = np.array([.05, .06, .08, .10, .13, .15, .20, .22, .25, .29, .32, .33, .34, 
    .37, .39, .41, .42, .44, .45, .46, .49])

def main():

    # we want to solve the equation y = A*p
    A = np.vstack([x, np.ones(len(x))]).T
    # solve for p
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    print('m = {:.5f}'.format(m))
    print('c = {:.5f}'.format(c))


    plt.plot(x, y, 'or', label='Raw data')
    plt.plot(x, m*x + c, 'b', label='Fitted line')

    plt.xlim(1960,2020)
    plt.ylim(-0.1, 0.6)
    plt.grid(color='#DDDDDD')
    plt.legend()

    # pyplot.title() sets label for title
    plt.title('Least Squares Fit: m = {0:.4f}, c = {0:.5f}'.format(m, c))
    plt.show()

if __name__ == '__main__':
    main()
