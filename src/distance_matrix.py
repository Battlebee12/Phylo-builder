import numpy as np

def hamming_distance(seq1, seq2):
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

def compute_distance_matrix(sequences):
    """
    Takes a list of DNA sequences and returns a NumPy distance matrix.
    Distance = Hamming distance between sequences.
    """
    num = len(sequences)
    dist_matrix = np.zeros((num, num))
    for i in range(num):
        for j in range(i+1, num):
            dist = hamming_distance(sequences[i], sequences[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix
