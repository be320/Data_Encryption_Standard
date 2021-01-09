from tables import *


def des_f(right_half_32, round_key):

    right_half_48 = ""
    for ind in expansion_permutation:
        right_half_48 += right_half_32[ind - 1]

    right_half_48 = int(right_half_48, 2) ^ int(round_key, 2)
    right_half_48 = bin(right_half_48)[2:].zfill(48)

    right_half_6_list = []
    for i in range(0, 48, 6):
        right_half_6_list.append(right_half_48[i:i + 6])

    right_half_32 = ""
    for i in range(8):
        part = right_half_6_list[i]
        row = int(part[0] + part[5], 2)
        col = int(part[1:5], 2)
        right_half_32 += (bin(s_box[i][row][col])[2:].zfill(4))

    output = ""
    for ind in permutation_table:
        output += right_half_32[ind - 1]

    return output




