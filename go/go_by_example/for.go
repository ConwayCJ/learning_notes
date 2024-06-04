package main

import "fmt"

func for_loop() {
	// "while" loop, but in go
	i := 1
	for i < 10 {
		fmt.Println(i)
		i += 1
	}

	// for loop

	for j := 0; j <= 10; j++ {
		fmt.Println(j)
	}

	// for loop with range

	for i := range 10 {
		fmt.Println("range ", i)
	}

	// break / continue keyword
}
