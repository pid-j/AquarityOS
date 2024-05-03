def Main(args):
    if len(args) >= 1:
        return f"\t{args[0]}\n\t{'-' * 36}\n\t{GetHelp(args[0])}"
    return """Commands
\tappendfile [name] [contents]   help [cmd(Optional)]
\tcd [directory]                 mkdir [directory]
\tclr                            mkfile [name] [contents]
\techo [text]                    rm [path]
\tfetchdist                      sudo [command]"""


def GetHelp(cmd):
    if cmd == "appendfile":
        return "Appends text to a file."
    if cmd == "cd":
        return "Change directory."
    if cmd == "mkdir":
        return "Make directory."
    if cmd == "mkfile":
        return "Make file with contents."
    if cmd == "rm":
        return "Remove file/directory."
    if cmd == "echo":
        return "Prints text to the standard output."
    if cmd == "fetchdist":
        return "Shows the Aquarity OS version."
    if cmd == "help":
        return "Shows this help text and exits."
    if cmd == "clr":
        return "Clears the output."
    if cmd == "exit":
        return "Exits the terminal."
    return "Invalid command"
