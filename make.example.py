#!/bin/python3

from os import system

APP="_text"
TARGETS=[

]

def deploy()->None:
    for target in TARGETS:
        system(f"cp {APP} {target}")

def main()->None:
    deploy()

if __name__ == "__main__":
    main()
