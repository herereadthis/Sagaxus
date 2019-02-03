'''
Get least squares fit over bivariate data
'''
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
    b1, b0 = np.linalg.lstsq(A, y, rcond=None)[0]

    print('$\\b1={:.5f}$'.format(b1))
    print('$\\b0={:.5f}$'.format(b0))

    plt.plot(x, y, 'or', label='Raw data')
    plt.plot(x, b1*x + b0, 'b', label='Fitted line')

    plt.xlim(1960,2020)
    plt.ylim(-0.1, 0.6)
    plt.grid(color='#DDDDDD')
    plt.legend()

    # pyplot.title() sets label for title
    plt.title(r'Least Squares Fit: $\beta_1 = {0:.4f}, \beta_0 = {0:.5f}$'.format(b1, b0))
    plt.show()

    '''
    Residuals are the leftovers from applying m*x+c formula and comparing it to
    the actual data value.
    '''
    residuals = [(y[index] - (b1*x_i + b0)) for index, x_i in enumerate(x)]
    '''
    Numpy formula for getting the sum of the squares of all the residuals.
    Ideally, this number should be close to 0
    '''
    residuals_sum = np.linalg.lstsq(A, y, rcond=None)[1][0] 
    plt.plot(x, residuals, 'or')
    plt.hlines(residuals_sum, x[0], x[-1,], 'b')
    plt.grid(color='#DDDDDD')
    plt.title('Residuals: sum = {0:.5f}'.format(residuals_sum))
    plt.show()

if __name__ == '__main__':
    main()
