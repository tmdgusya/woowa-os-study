#!/bin/bash

false &

wait $!

echo "false 명령어가 종료되었습니다: $?"