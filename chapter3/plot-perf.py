#!/usr/bin/python3

import sys
import plot_sched

def usage():
    print("사용법: {} <최대 프로세스 개수>")
    sys.exit(1)

progname = sys.argv[0]

if len(sys.argv) < 2:
    usage()

max_nproc = int(sys.argv[1])
plot_sched.plot_avg_tat(max_nproc)
plot_sched.plot_throughput(max_nproc)