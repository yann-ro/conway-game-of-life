import numpy as np

def glider():
    """
    return a glider
    """
    return np.array([[0,1,0],
                     [0,0,1],
                     [1,1,1]], dtype=bool)