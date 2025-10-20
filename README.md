# Overview
This project implements a vigenere cipher through three programs that 
communicate via interprocess communication (pipes):
- Encrypter - Handles encryption and decryption using the vigenere cipher
- Logger - Records log messages with time stamps to a log file chosen by the user
- Driver - Provides a command-line interface for user interaction and manages communication between driver and logger

# How to Run
1. Compile/run from the terminal
`python3 driver.py filename.txt`
or
`python3 driver.py` to create/use "log.txt" to store logs
2. The driver program will start the logger and encrypter processes and display a list of commands.

# Files
- Encrypter.py - Encrypts and decrypts strings using the vigenere cipher
- Logger.py - Records log messages with time stamps to a specified log file
- Driver.py - Manages processes, user input, and interprocess communication
- devlog.md - Development log and notes