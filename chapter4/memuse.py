#!/usr/bin/python3

import subprocess

size = 10000000

print("메모리 사용 전의 전체 시스템 메모리 사용량을 표시합니다.")
subprocess.run("free")

array = [0] * size
print("메모리 사용 후의 전체 시스템 메모리 남은 용량을 표시합니다.")
subprocess.run("free")


