#Purpose: Compute gram matrix for a set of strings
import numpy as np
from kc import *

def calculate_gram_matrix(strings):

    n = len(strings)
    print "Gram matrix dimensions: %d x %d" % (n, n)

    distances = []
    for s_i in strings:
        for s_j in strings:
            NID = approximate_NID(s_i, s_j)
            print "i: %s, j: %s, NID: %f" % (s_i, s_j, NID)
            distances.append(NID)

    #for reshaping 1d array, specify the dimensions to be n columns and the appropriate number of rows (specified by -1)
    #create an n x n gram matrix 
    gram_matrix = np.reshape(distances, (-1, n))
    return gram_matrix

strings = [
    "ACCTGCGGATATTAATTAACTGACC",
    "TCCTCTATTAATCGGTGGATGTCGG",
    "AGAATTAATTACTGATATTCTTTCA",
    "CATAGTCGGCAGCCGTCACGACCCT"
]

gram_matrix = calculate_gram_matrix(strings)
print gram_matrix
