import math as m


def compact_code(int):
    return bin(int+2)[3:]

def kolmogorov_conditional_complexity(formula,bit_size_symbol=5):
    kc=bit_size_symbol
    for elem in formula.split():
        if elem[0]=='#':
            kc += len(compact_code(int(elem[1:])))
        elif elem[0]=='^': 
            kc += 2*bit_size_symbol+len(compact_code(int(elem[1:])))
        else:
            kc += bit_size_symbol
    
    return kc

def causal_complexity(array):
    """
    causal_complexity = - log2(1/P) hors ici P = 2^(nb_pixels) d'où la simplification
    """
    if len(array.shape)==1:
        return int(array.shape[0])

    else:
        return int(array.shape[0]*array.shape[1])

def specified_complexity(formula,array):
    return causal_complexity(array)-kolmogorov_conditional_complexity(formula)