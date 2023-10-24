import numpy as np

def rotation(alpha):
    row_1 = [np.cos(alpha), -np.sin(alpha)]
    row_2 = [np.sin(alpha), np.cos(alpha)]

    return [row_1, row_2]
