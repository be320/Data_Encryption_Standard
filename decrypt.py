from des_function import des_f
from tables import *


def decrypt(cipher, keys):

    blocks = []
    for i in range(0, len(cipher), 64):
        blocks.append(cipher[i:i + 64])

    dec_chunk_list = []
    for block in blocks:
        p = ""
        for number in initial_permutation:
            p += block[number - 1]

        ln = p[:32]
        rn = p[32:]

        for i in range(15, -1, -1):
            temp = ln
            ln = bin(int(rn, 2) ^ int(des_f(ln, keys[i]), 2))[2:].zfill(32)
            rn = temp

        combined = ln + rn
        plainText = ""
        for number in inverse_initial_permutation:
            plainText += combined[number - 1]

        dec_chunk_list.append(plainText)

    output = ""
    for block in dec_chunk_list:
        output += hex(int(block, 2))

    return output

