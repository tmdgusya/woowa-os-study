#!/usr/bin/python3

import os
import sys

data = 1000

print(f"자식 프로세스 생산전 데이터 값: {data}")
pid = os.fork()

if pid < 0:
    print("fork()에 실패했습니다.", file=os.stderr)
elif pid == 0:
    data *= 2
    sys.exit(0)

os.wait()
print(f"자식 프로세스 종료 후 데이터 값: {data}")