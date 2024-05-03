def Main(args):
    if len(args) < 2:
        return "Syntax error: Name/contents of file unspecified"
    with open(f"{os.getcwd()}{'/' if not os.getcwd().endswith('/') else ''}{args[0]}", "a") as file:
        file.write(args[1])
    return "Created successfully."
