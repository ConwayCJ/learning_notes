package main

import "fmt"

func variables() {
	/* Variable declaration IMPLICIT */

	// single var declaration
	var a = "initial"
	fmt.Println(a)
	// multi var declaration
	var b, c int = 1, 2
	fmt.Println(b, c)

	var d = true
	fmt.Println(d)
	/* Variable declaration IMPLIED */

	f := "apple"
	fmt.Println(f)

	g, h := "pear", "watermelon"
	fmt.Println(g, h)

}
