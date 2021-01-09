from des_function import des_f
from tables import *


def encrypt(text, keys, index, num):
    binary_64 = bin(int(text, 16))[2:].zfill(64)
    p = ""
    for ind in initial_permutation:
        p += binary_64[ind - 1]

    ln = p[:32]
    rn = p[32:]

    for i in range(16):
        dum = rn
        rn = bin(int(ln, 2) ^ int(des_f(rn, keys[i]), 2))[2:].zfill(32)
        ln = dum

    combined = rn + ln

    cipher = ""
    for ind in inverse_initial_permutation:
        cipher += combined[ind - 1]

    output = ""
    output += hex(int(cipher, 2))[2:]

    if index == num:
        return output

    return encrypt(output, keys, index+1, num)
