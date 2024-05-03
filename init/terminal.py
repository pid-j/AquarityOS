import os
import tui as tui


os.system("")  # Force terminal mode

terminal = tui.Terminal()

firstTimeSetup = False

global username
global password
global pcName
username, password, pcName = "", "", ""

with open(".auth.txt", "r") as auth:
    lines = auth.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    pcName = lines[2].upper().strip()

terminal.buffer.write(
    "Aquarity v1.0beta - Perching Pigeon\n"
    "aqx shell - Type help for more info\n"
    "-----------------------------",
    True
)

os.chdir("fs")
while True:
    terminal.input(f"{username}@{pcName} {os.getcwd()}$ ")
