import os


def Main(args):
    if len(args) < 1:
        return "Syntax error: Name of file unspecified"
    os.remove(f"{os.getcwd()}{'/' if not os.getcwd().endswith('/') else ''}{args[0]}")
    return "Deleted successfully."
