#!/usr/bin/python3

import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)

while True:
    pass
