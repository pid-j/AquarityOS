def Main(args):
    if len(args) >= 1:
        return f"\t{args[0]}\n\t{'-' * 36}\n\t{GetHelp(args[0])}"
    return "Commands\n\tclr\n\techo [args]\n\texit\n\tfetchdist\n\tftsetup\n\thelp [args?]"


def GetHelp(cmd):
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
    if cmd == "ftsetup":
        return "Engage first-time setup (if not already finished)"
    return "Invalid command"
