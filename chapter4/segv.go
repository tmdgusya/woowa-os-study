package main

import "fmt"

func main(){
	var p * int = nil
	fmt.Println("비정상 메모리 접근 전")
	*p = 0
	fmt.Println("비정상 메모리 접근 후")
}