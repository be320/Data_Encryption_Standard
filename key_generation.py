from tables import *
import random


def keys_generator(key_input):
    key_64 = bin(int(key_input, 16))[2:].zfill(64)
    key_56 = ""
    for ind in permutedChoice_1:
        key_56 += key_64[ind-1]

    c0 = key_56[:28]
    d0 = key_56[28:]
    keys_c = []
    keys_d = []
    for i in range(0, 16):
        ind = left_circular_shift[i]
        dum = c0[0:ind]
        c0 = c0[ind:] + dum
        keys_c.append(c0)
        dum = d0[0:ind]
        d0 = d0[ind:] + dum
        keys_d.append(d0)


    keys = []
    for i in range(16):
        mix = keys_c[i] + keys_d[i]
        dum = ""
        for ind in permutedChoice_2:
            dum += mix[ind-1]
        keys.append(dum)

    return keys
