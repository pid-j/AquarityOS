# AquarityOS

An OS written in Python.

## What is AquarityOS?

AquarityOS is a text-based "operating system" which is made entirely from Python.

## Is it an operating system?

While it has the same behavior as Linux, for example, it is not an operating system.
Real operating systems are packed in an .iso file and allow you to flash it to a source of media.

## What exists in AquarityOS?

Not much for now, just some simple commands, such as:

- **echo** - Prints something to the standard output.
- **fetchdist** - A basic ripoff of neofetch with less features.
- **sudo** - Execute something with high-level privileges (currently unneccesary because package managers don't exist)

Update v1.0 has introduced file system commands.

## When will I make an update?

Depends on how tired or lazy I feel.

# Setup

## Run Steps

Install Python >=3.1 (add to PATH), then download the archive, extract it, then:

- **For Windows Users** Run the `run.bat` file.
- **For Linux Users** Run the `run.sh` file with bash.

## Manual Execution

This supports most operating systems:

1. Install Python >=3.1 (Add it to PATH)
2. Download the archive (zip/tar.gz)
3. Extract it to any folder
4. Open the extracted folder, then find `requirements.txt`
5. Open the folder containing the `requirements.txt` file in the terminal.
6. Run `pip install -r requirements.txt`. If it doesn't work, try `pip3 install -r requirements.txt`, or adding Python to the path.
7. Run `python init/terminal.py`, or `python3 init/terminal.py`. It is important you run it in the terminal.
8. All done!

## Changing the User

There is a file named `.auth.txt` in the `init` directory. It looks something like this:

```
root
admin
ROOT
```

The first line is the username, the second line is the password, and the last line is the OS PC name respectively.

For example, if I wanted to become a user named `boy` with the password `1234` on an OS PC named `BOY`, I would update the `.auth.txt` file to this:

```
boy
1234
BOY
```

# PRECAUTION

You can destroy your file system with this thing.
How?
Since the filesystem directory is not an important system component, atleast to your **real** operating system, you can `rm` it through AquarityOS.

Not that it really matters because the entire **real** OS ***that you have*** is a file system.
