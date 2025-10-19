import sys
import subprocess
import os
import json

# # use command line argument to set log_file, otherwise use "log.txt"
if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "log.txt"

storage_file = "history.json"

# run logger.py as a subprocess
logger = subprocess.Popen(
    ["python3", "Logger.py", log_file],
    stdin = subprocess.PIPE,
    text = True
)

# run encrypter.py as a subprocess
encrypter = subprocess.Popen(
    ["python3", "Encrypter.py"],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    text = True
)


# load entire history from json file
def load_history():
    if not os.path.exists(storage_file):
        print("ERROR Unable to load history")
        return
    else:
        with open(storage_file, "r") as f:
            return json.load(f)


# retrieve all entries for a single category from the history
def get_entry(category):
    history = load_history()
    return history.get(category, [])


# allow the user to select an entry from the displayed history for a given category
def select_from_history(category):
    history = load_history()
    items = history.get(category, [])
    if not items:
        error = "ERROR No entries in history"
        print(error)
        logger.stdin.write(f"{error}\n")
        logger.stdin.flush()
        return ""

    print("Select one of the following (enter a number, 0 to exit): ")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

    user_input = input("-> ").strip()
    index = int(user_input) - 1
    if 0 <= index < len(items):
        return items[index]
    elif index == -1:
        return ""
    else:
        error = f"ERROR {user_input} is not a valid option"
        print(error)
        logger.stdin.write(f"{error}\n")
        return ""


logger.stdin.write("START Logging started\n")
logger.stdin.write("START Driver.py started\n")
logger.stdin.flush()

# continue looping the menu until "quit" is received
while True:
    print("Please enter one of the following commands: \npassword \nencrypt \ndecrypt \nhistory \nquit")
    user_input = input("-> ").strip().lower()

    if user_input == "quit":
        encrypter.stdin.write("QUIT\n")
        encrypter.stdin.flush()
        logger.stdin.write("QUIT\n")
        logger.stdin.flush()
        break
    elif user_input == "password":
        print("Please enter 1 or 2: \n1. Select a password from your history \n2. Enter a new password")
        user_input2 = input("-> ").strip()
        if user_input2 == "1":
            password = select_from_history("Passwords")
            if password:
                encrypter.stdin.write("PASS " + password + "\n")
                encrypter.stdin.flush()
                logger.stdin.write("PASS\n")
                logger.stdin.flush()
                encrypter_output = encrypter.stdout.readline()
                print(encrypter_output, flush=True)
                logger.stdin.write(f"{encrypter_output}\n")
                logger.stdin.flush()
        elif user_input2 == "2":
            print("Please enter a password that consists of only alphabetic letters, passwords are not case sensitive")
            password = input("-> ").strip()
            encrypter.stdin.write("PASS " + password + "\n")
            encrypter.stdin.flush()
            logger.stdin.write("PASS\n")
            logger.stdin.flush()
            encrypter_output = encrypter.stdout.readline()
            print(encrypter_output, flush=True)
            logger.stdin.write(f"{encrypter_output}\n")
            logger.stdin.flush()
        else:
            print(user_input2 + "is not a valid option")
    elif user_input == "encrypt":
        print("Please enter 1 or 2: \n1. Select plaintext from your history \n2. Enter new plaintext")
        user_input2 = input("-> ").strip()
        if user_input2 == "1":
            plaintext = select_from_history("Plaintext")
            if plaintext:
                encrypter.stdin.write("ENCRYPT " + plaintext + "\n")
                encrypter.stdin.flush()
                logger.stdin.write("ENCRYPT " + plaintext.upper() + "\n")
                logger.stdin.flush()
                encrypter_output = encrypter.stdout.readline()
                print(encrypter_output, flush=True)
                logger.stdin.write(f"{encrypter_output}\n")
                logger.stdin.flush()
        elif user_input2 == "2":
            print("Please enter a string that consists of only alphabetic letters, strings are not case sensitive")
            plaintext = input("-> ").strip()
            encrypter.stdin.write("ENCRYPT " + plaintext + "\n")
            encrypter.stdin.flush()
            logger.stdin.write("ENCRYPT " + plaintext.upper() + "\n")
            logger.stdin.flush()
            encrypter_output = encrypter.stdout.readline()
            print(encrypter_output, flush=True)
            logger.stdin.write(f"{encrypter_output}\n")
            logger.stdin.flush()
        else:
            print(user_input2 + " is not a valid option")
    elif user_input == "decrypt":
        print("Please enter 1 or 2: \n1. Select ciphertext from history \n2. Enter new ciphertext")
        user_input2 = input("-> ").strip()
        if user_input2 == "1":
            ciphertext = select_from_history("Ciphertext")
            if ciphertext:
                encrypter.stdin.write("DECRYPT " + ciphertext + "\n")
                encrypter.stdin.flush()
                logger.stdin.write("DECRYPT " + ciphertext.upper() + "\n")
                logger.stdin.flush()
                encrypter_output = encrypter.stdout.readline()
                print(encrypter_output, flush=True)
                logger.stdin.write(f"{encrypter_output}\n")
                logger.stdin.flush()
        elif user_input2 == "2":
            print("Please enter a string that consists of only alphabetic letters, strings are not case sensitive")
            ciphertext = input("-> ").strip()
            encrypter.stdin.write("DECRYPT " + ciphertext + "\n")
            encrypter.stdin.flush()
            logger.stdin.write("DECRYPT " + ciphertext.upper() + "\n")
            logger.stdin.flush()
            encrypter_output = encrypter.stdout.readline()
            print(encrypter_output, flush=True)
            logger.stdin.write(f"{encrypter_output}\n")
            logger.stdin.flush()
        else:
            print(user_input2 + " is not a valid option")
    elif user_input == "history":
        history = load_history()
        for category, items in history.items():
            print(f"{category}: {','.join(items)}")
        logger.stdin.write("HISTORY\n")
        logger.stdin.flush()
    else:
        print(user_input + " is not a valid command.")