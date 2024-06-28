package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strconv"
	"syscall"
)

func main(){
	pid := os.Getpid()
	fmt.Println("*** testfile 메모리 맵 이전의 프로세스 가상 주소 공간 ***")
	command := exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err := command.Run()

	if err != nil {
		log.Fatal("cat 실행에 실패했습니다")
	}
	file, err := os.OpenFile("testfile", os.O_RDWR, 0)
	if err != nil {
		log.Fatal("testfile을 열지 못했습니다")
	}
	defer file.Close()

	data, err := syscall.Mmap(int(file.Fd()),0,1,syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_SHARED)
	if err != nil {
		log.Fatal("mmap() 실행에 실패했습니다")
	}
	fmt.Println("")
	fmt.Printf("testfile을 매핑한 주소: %p\n", &data[0])
	fmt.Println("")

	fmt.Println("*** testfile 메모리 맵 이후의 프로세스 가상 주소 공간 ***")
	command = exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err = command.Run()

	if err != nil {
		log.Fatal("cat 실행에 실패했습니다")
	}

	replaceBytes := []byte("HELLO")
	for i, _ := range data {
		data[i] = replaceBytes[i]
	}

}