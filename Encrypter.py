import sys
import json
import os

sys.stdout.reconfigure(line_buffering=True)

passkey = ""
letter_to_num = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,
    "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12,
    "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18,
    "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
num_to_letter = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G",
    7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M",
    13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S",
    19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"
}


def split_string(s):
    if " " in s:
        first, second = s.split(" ", 1)
        return first, second
    else:
        return s, ""


# check if given command and argument are valid
def process_input(s):
    s = s.upper()
    command, arg = split_string(s)

    if not arg:
        print("ERROR No argument was given")
    else:
        arg = arg.replace(" ", "")
        if not arg.isalpha():
            print("ERROR Please only enter alphabetical letters")
        elif command in commands:
            commands[command](arg)
        else:
            print("ERROR " + command + " is not a valid command")


# PASS (set passkey for vigenere cipher)
def set_pass(s):
    global passkey
    passkey = s
    print("RESULT")
    return


# ENCRYPT (encrypt given plaintext with the currently set passkey)
def encrypt(plaintext):
    if not passkey:
        print("ERROR Passkey not set")
        return

    plaintext_nums = []
    passkey_nums = []
    ciphertext = ""

    for i, letter in enumerate(plaintext):
        passkey_index = i % len(passkey)
        passkey_nums.append(letter_to_num[passkey[passkey_index]])

        plaintext_nums.append(letter_to_num[plaintext[i]])

        ciphertext += num_to_letter[(plaintext_nums[i] + passkey_nums[i]) % 26]

    print("RESULT", ciphertext)
    return


# DECRYPT (decrypt given ciphertext with currently set passkey)
def decrypt(ciphertext):
    if not passkey:
        print("ERROR Passkey not set")
        return

    ciphertext_nums = []
    passkey_nums = []
    plaintext = ""

    for i, letter in enumerate(ciphertext):
        passkey_index = i % len(passkey)
        passkey_nums.append(letter_to_num[passkey[passkey_index]])

        ciphertext_nums.append(letter_to_num[ciphertext[i]])

        plaintext += num_to_letter[(ciphertext_nums[i] - passkey_nums[i]) % 26]

    print("RESULT", plaintext)
    return


commands = {
    "PASS": set_pass,
    "ENCRYPT": encrypt,
    "DECRYPT": decrypt
}

# read stdin from driver.py program until "QUIT" is received
while True:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        elif line.upper() == "QUIT":
            break
        else:
            process_input(line)
