import os
from commands import CommandList as commands


class Buffer:
    def __init__(self):
        self.buffer = ""
        self.mostRecentlyAccessedInput = ""
        self.opened = (True, "StandardOutput")

    def open(self, stdName: str = "StandardOutput"):
        self.opened = (True, stdName)

    def close(self):
        self.opened = (False,)

    def __repr__(self):
        return self.buffer

    def read(self, portion: slice = slice(None, None)):
        return self.buffer[portion]

    def write(self, text, createNewLine: bool = False):
        if not self.opened[0]:
            raise IOError("The buffer is not open, please call the 'open' method to open it")
        self.buffer += text
        print("", end=text)
        if createNewLine:
            print("")

    def flush(self):
        self.buffer = ""
        os.system("cls" if os.name == "nt" else "clear")

    def input(self, inputText: str = ""):
        self.mostRecentlyAccessedInput = input(inputText)
        self.buffer += (inputText + self.mostRecentlyAccessedInput + "\n")


class InputParser:
    def __init__(self):
        self.tree = {}
        self.split = []

    def parse(self, inp: str) -> dict:
        inp = inp.strip()
        self.tree = {"error": None}
        if not inp:
            return self.tree
        self.split = inp.split('"')
        self.tree["root"] = inp.split(" ")[0]
        self.tree["params"] = inp.split(" ")[1::1]
        return self.tree


class Terminal:
    def __init__(self):
        self.buffer = Buffer()
        self.parser = InputParser()

    def input(self, inputText: str = ""):
        self.buffer.input(inputText)
        parse = self.parser.parse(self.buffer.mostRecentlyAccessedInput)
        if not len(parse):
            return
        if parse["error"]:
            print(parse["error"])
            return
        if commands.Has(parse["root"]):
            result = commands.Get(parse["root"]).callback(parse["params"])
            if result is not None:
                print(result)
            return
        print("Syntax error: No command found named %s" % parse["root"])
