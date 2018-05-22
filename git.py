#!/usr/bin/env python3
import subprocess
import datetime


def run():
    subprocess.call(["git", "add", "--all"])
    print('Enter Message')
    msg = input()
    time = str(datetime.datetime.now())
    subprocess.call(["git", "commit", "-m", f'{msg} | submit at {time}'])
    subprocess.call(["git", "push", "origin", "master"])


def main():
    run()


if __name__ == '__main__':
    main()
