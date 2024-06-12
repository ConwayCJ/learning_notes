package main

import "fmt"

func getLogger(formatter func(string, string) string) func(string, string) {
	return func(x, y string) {
		fmt.Println(formatter(x, y))
	}
}
