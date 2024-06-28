#!/usr/bin/python3

import os
import subprocess
import sys
import mmap

ALLOC_SIZE = 100 * 1024 * 1024
PAGE_SIZE = 4096

def access(data):
    for i in range(0, ALLOC_SIZE, PAGE_SIZE):
        data[i] = 0

def show_meminfo(msg, process):
    print(msg)
    print("free 명령어 실행 결과:")
    subprocess.run("free")
    print(f"{process}의 메모리 관련 정보")
    subprocess.run(["ps","-orss,maj_flt,min_flt", str(os.getpid())])
    print()

data = mmap.mmap(-1, ALLOC_SIZE, flags = mmap.MAP_PRIVATE)
access(data)
show_meminfo("*** 자식 프로세스 생성 전 ***", "부모 프로세스")

pid = os.fork()

if pid < 0:
    print("fork()에 실패했습니다.", file=os.stderr)
elif pid == 0:
    show_meminfo("*** 자식 프로세스 생성 직후 ***", "자식 프로세스")
    access(data)
    show_meminfo("*** 자식 프로세스의 메모리 접근 후 ***", "자식 프로세스")
    sys.exit(0)

os.wait()