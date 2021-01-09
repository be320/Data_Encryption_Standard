from des_function import des_f
from tables import *


def decrypt(cipher, keys, index, num):
    binary_64 = bin(int(cipher, 16))[2:].zfill(64)
    p = ""
    for number in initial_permutation:
        p += binary_64[number - 1]

    ln = p[:32]
    rn = p[32:]

    for i in range(15, -1, -1):
        temp = ln
        ln = bin(int(rn, 2) ^ int(des_f(ln, keys[i]), 2))[2:].zfill(32)
        rn = temp

    combined = rn + ln
    plainText = ""
    for number in inverse_initial_permutation:
        plainText += combined[number - 1]

    output = ""
    output += hex(int(plainText, 2))[2:]

    if index == num:
        return output

    return decrypt(output, keys, index + 1, num)

