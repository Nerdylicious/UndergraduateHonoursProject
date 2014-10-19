#Purpose: Compute gram matrix for a set of strings
import numpy as np
from kc import *

def calculate_gram_matrix(strings):

    n = len(strings)

    distances = []
    for s_i in strings:
        for s_j in strings:
            #this calculation for NID does not work well with scikit-learn
            #NID = approximate_NID(s_i, s_j)
            NID = 1 - approximate_NID(s_i, s_j)
            distances.append(NID)

    #for reshaping 1d array, specify the dimensions to be n columns and the appropriate number of rows (specified by -1)
    #create an n x n gram matrix 
    gram_matrix = np.reshape(distances, (-1, n))
    return gram_matrix
