package main

import (
	"fmt"
	"log"
)

func main() {
	cases := []struct {
		arr []int
		res string
	}{
		{
			arr: []int{1, 2, 3},
			res: "124",
		},
		{
			arr: []int{9, 9, 9},
			res: "1000",
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		var res string
		for _, i := range plusOne(c.arr) {
			res += fmt.Sprintf("%d", i)
		}
		if res != c.res {
			log.Fatalf("expect: %s, got: %s", c.res, res)
		}
	}
}

func plusOne(digits []int) []int {
	add := 1
	for i := len(digits) - 1; i >= 0; i-- {
		digits[i] += add
		if digits[i] != 10 {
			return digits
		}

		digits[i] = 0
	}
	return append([]int{1}, digits...)
}
