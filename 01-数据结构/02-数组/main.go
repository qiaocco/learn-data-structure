package main

import "fmt"

func main() {
	// 创建
	var arr [5]int

	// 添加元素
	arr[0] = 0
	arr[1] = 1
	arr[2] = 2
	fmt.Printf("arr=%v\n", arr)

	// 访问元素
	fmt.Println(arr[0])

	// 修改元素
	arr[0] = 100
	fmt.Println(arr[0])

}
