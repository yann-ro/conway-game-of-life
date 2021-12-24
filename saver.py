import numpy as np
import matplotlib.pyplot as plt

def save(name,array):
    with open(f'item/{name}.npy', 'wb') as f:
        np.save(f, array)


array = np.array([
    [0,1,0,0,1],
    [1,0,0,0,0],
    [1,0,0,0,1],
    [1,1,1,1,0],
],dtype=bool)[:,::-1]

plt.imshow(array)
plt.show()

save('lightweight_spaceship',array)
