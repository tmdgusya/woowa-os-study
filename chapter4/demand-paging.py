#!/usr/bin/python3

import mmap
import time
import datetime

ALLOC_SIZE = 100 * 1024 * 1024
ACCESS_UNIT = 10 * 1024 * 1024
PAGE_SIZE = 4096

def show_message(msg):
    print("{}: {}".format(datetime.datetime.now().strftime("%H:%M:%S"), msg))

show_message("새로운 메모리 영역 확보 전. 엔터 키를 누르면 100메가 새로운 메모리 영역을 확보합니다")

input()

# mmap 시스템 콜 호출로 100Mib 메모리 영역 확보

memregion = mmap.mmap(-1, ALLOC_SIZE, flags=mmap.MAP_PRIVATE)
show_message("새로운 메모리 영역을 확보했습니다. 엔터 키를 누르면 1초당 1MiB씩, 합계 100MiB 새로운 메모리 영역에 접근합니다:")
input()

for i in range(0, ALLOC_SIZE, PAGE_SIZE):
    memregion[i] = 0
    if i%ACCESS_UNIT == 0 and i!=0:
        show_message("{} MiB 진행 중".format(i//(1024*1024)))
        time.sleep(1)

show_message("새롭게 확보한 메모리 영역에 모두 접근했습니다. 엔터키를 누르면 종료합니다.")
input()