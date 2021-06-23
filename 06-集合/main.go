package main

import "fmt"

type void struct{}

var member void

func main() {
	set := make(map[string]void)

	// add element
	set["foo"] = member
	set["bar"] = member

	// for loop
	for k := range set {
		fmt.Println(k)
	}

	// delete element
	delete(set, "foo")

	// size
	fmt.Println(len(set))

	// membership
	_, exists := set["foo"]
	fmt.Println(exists)

}
