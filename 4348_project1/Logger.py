import sys
from datetime import datetime

# use command line argument to set log_file, otherwise use "log.txt"
if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "log.txt"

# read stdin from driver.py until "QUIT" is received
while True:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if line.strip().upper() == "QUIT":
            # log message is in the format: YYYY-MM-DD HH:MM [ACTION] MESSAGE
            time = datetime.now().strftime("%Y-%m-%d %H:%M")
            log = f"{time} [QUIT] Driver.py finished\n{time} [QUIT] Logging finished\n"
            with open (log_file, "a") as f:
                f.write(log)
            break

        if " " in line:
            action, msg = line.split(" ", 1)
        else:
            action, msg = line, ""

        log = datetime.now().strftime("%Y-%m-%d %H:%M")
        log += " [" + action + "] " + msg

        with open(log_file, "a") as f:
            f.write(log + "\n")





