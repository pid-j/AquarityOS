import os


def Main(args):
    if len(args) < 1:
        return "Syntax error: Name of directory unspecified"
    os.chdir(f"{os.getcwd()}{'/' if not os.getcwd().endswith('/') else ''}{args[0]}")
    return "Changed current working directory successfully."
