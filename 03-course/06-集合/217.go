package main

import "fmt"

func containsDuplicate(nums []int) bool {
	type void struct{}
	var v void

	set := make(map[int]void)
	for _, item := range nums {
		_, exists := set[item]
		if exists {
			return true
		} else {
			set[item] = v
		}
	}
	return false
}

func main() {
	nums := []int{1, 2, 3, 1}
	fmt.Println(containsDuplicate(nums))
}
