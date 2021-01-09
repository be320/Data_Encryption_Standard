from encrypt import encrypt
from decrypt import decrypt
from key_generation import keys_generator

print("Please Enter The key: ")
key = input()

print("Please Enter The PlainText: ")
plainText = input()

print("Please Enter The Number Of Times to run encryption: ")
num = int(input())


keys = keys_generator(key)

cipher = encrypt(plainText, keys, 1, num)

print(cipher)
print()
print()
k = input("DES Algorithm implemented by Ahmed Bahaa")
