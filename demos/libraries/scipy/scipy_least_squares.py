from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1963, 1968, 1971, 1974, 1975, 1978, 1981, 1985, 1988, 1991, 1995, 
    1999, 2001, 2002, 2006, 2007, 2008, 2009, 2012, 2013, 2014])
y = np.array([.05, .06, .08, .10, .13, .15, .20, .22, .25, .29, .32, .33, .34, 
    .37, .39, .41, .42, .44, .45, .46, .49])

def main():
    plt.plot(x, y, 'or')
    plt.xlim(1960,2020)
    plt.ylim(0, 0.6)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
