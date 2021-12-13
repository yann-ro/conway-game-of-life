import numpy as np
import item

def save(name):
    with open(f'item/{name}.npy', 'wb') as f:
        np.save(f, item.oscillator.snowflakes())

save('101')