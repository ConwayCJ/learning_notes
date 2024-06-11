package main

import (
	"fmt"
)

type cost struct {
	day   int
	value float64
}

func main() {
	r := 0
	c := 0
	matrix := [][]int{}
	row := []int{}

	for c <= 10 {

		for r <= 10 {
			row = append(row, r)
			r += 1
		}
		matrix = append(matrix, row)
		row = []int{}
		c += 1
	}

	fmt.Println(matrix)
}
