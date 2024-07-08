#!/bin/bash

<<COMMENT
1번 필드: 확보한 메모리 영역의 크기
2번 필드: 확보한 물리 메모리 크기
3번 필드: 메이저 폴트 횟수
4번 필드: 마이너 폴트 횟수
COMMENT

PID=$(pgrep -f "demand-paging\.py")

if [ -z "${PID}" ]; then
    echo "demanding.py 프로세스가 존재하지 않습니다. $0 실행 전에 실행하기 바랍니다." >&2
    exit 1
fi

while true; do
    DATE=$(date | tr -d '\n')
    INFO=$(ps -h -o vsz,rss,maj_flt,min_flt -p ${PID})
    if [ $? -ne 0 ]; then
        echo "$DATE: demand-paging.py 프로세스가 종료했습니다." >&2
        exit 1
    fi
    echo "${DATE}: ${INFO}"
    sleep 1
done