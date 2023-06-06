#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upp_char = chr(ord(char) - 32)
        else:
           upp_char =  char
        print(upp_char, end='')
    print()
