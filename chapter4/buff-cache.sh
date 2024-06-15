#!/bin/bash

echo "파일 작성 전의 시스템 전체 메모리 사용향을 표시합니다."
free
echo "1GB 파일을 새로 작성합니다. 커널은 메모리에 1GB 페이지 캐시 영역을 사용합니다."
dd if=/dev/zero of=testfile bs=1M count=1K

echo "페이지 캐시 사용 후의 시스템 전체 메모리 사용량을 표시합니다."
free

echo "파일 삭제 후, 즉 페이지 캐시 삭제 후의 시스템 전체 메모리 사용량을 표시합니다."

re testfile
free
