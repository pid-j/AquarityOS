import os
import time
import tui as tui


os.system("")  # Force terminal mode

terminal = tui.Terminal()

firstTimeSetup = False

global username
global password
global pcName
# noinspection PyRedeclaration
username, password, pcName = "", "", ""

with open(".auth.txt") as auth:
    if len(auth.readlines()) < 3:
        firstTimeSetup = True

if firstTimeSetup:
    terminal.buffer.write("\x1b[31;1mERROR\x1b[0m: No authentication found.", True)
    terminal.buffer.input("Run first time setup? (Y/N): ")
    if not terminal.buffer.mostRecentlyAccessedInput.lower() == "n":
        terminal.buffer.flush()
        from pkg.firsttimesetup import Main as FTSetup
        result = FTSetup([])
        if result.startswith("Invalid"):
            terminal.buffer.write("Invalid parameter used, please restart the shell", True)
            exit(-1)
        terminal.buffer.flush()
    else:
        exit()

time.sleep(1)

with open(".auth.txt", "r") as auth:
    lines = auth.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    pcName = lines[2].upper().strip()

terminal.buffer.write(
    "Aquarity v1.0a - Perching Pigeon\n"
    "aqx shell - Type help for more info\n"
    "-----------------------------",
    True
)

cwd = "~"

while True:
    terminal.input(f"{username}@{pcName}{cwd}$ ")
