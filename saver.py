import numpy as np

def save(name,array):
    with open(f'item/{name}.npy', 'wb') as f:
        np.save(f, array)
