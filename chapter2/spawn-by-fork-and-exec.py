#!/usr/bin/python3

import os

ret = os.fork()
if ret == 0:
    os.execve("/bin/echo", ["echo", "fork()와 execve()로 생성"],{})
elif ret > 0:
    print("echo 명령어를 생성했습니다")