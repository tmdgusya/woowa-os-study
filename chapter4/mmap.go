package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strconv"
	"syscall"
)

const (
	ALLOC_SIZE = 1024 * 1024 * 1024
)

func main() {
	pid := os.Getpid()
	fmt.Println("*** 새로운 메모리 영역 확보전 메모리 맵핑 ***")
	command := exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err := command.Run()
	if err != nil {
		log.Fatal("cat 실행에 실패했습니다.")
	}

	// mmap() 시스템 콜을 호출해서 1GB 메모리 영역 확보
	data, err := syscall.Mmap(-1, 0, ALLOC_SIZE, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_ANON|syscall.MAP_PRIVATE)
	if err != nil {
		log.Fatal("mmap()에 실패했습니다.")
	}

	fmt.Println("")
	fmt.Printf("*** 새로운 메모리 영역: 주소 = %p, 크기 = 0x%x ***\n", &data[0], ALLOC_SIZE)
	fmt.Println("")
	
	fmt.Println("*** 새로운 메모리 영역 확보 후 메모리 매핑 ***")
	command = exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err = command.Run()
	if err != nil {
		log.Fatal("cat 실행에 실패했습니다.")
	}

}