'''
Find the stationary distribution of a Markov Matrix
lots of help from https://stackoverflow.com/questions/33385763/
Reference: sagaxus/docs/markov-chains.md
'''
import numpy as np
import scipy.sparse.linalg as sla

'''
This is the array. It is doubly stochastic as the rows and columns add up to 1.
'''
transition_matrix = [
    [.25, .20, .25, .30],
    [.20, .30, .25, .30],
    [.25, .20, .40, .10],
    [.30, .30, .10, .30]
]

'''
scipy.sparse.linalg.eigs gives two arrays, the eigenvalues and the eigenvectors
We only k=1 eigenvector, LM = largest magnitude
'''
eigenvalue, eigenvector = sla.eigs(np.array(transition_matrix), k=1, which='LM')

'''
normalize the eigenvector (the column adds up to one) and return as real numbers
'''
stationary_distribution = (eigenvector/eigenvector.sum()).real

print(stationary_distribution)


