#!/usr/bin/python3

import os, sys

ret = os.fork()
if ret == 0:
    print(f"자식 프로세스: pid : {os.getpid()}, 부모 프로세스의 pid : {os.getppid()}")
    os.execve("/bin/echo", ["echo", f"{os.getpid()}에서 안녕"],{})
    exit()
elif ret > 0:
    print(f"부모 프로세스: pid : {os.getpid()}, 자식 프로세스의 pid : {ret}")
    exit()

sys.exit(1)