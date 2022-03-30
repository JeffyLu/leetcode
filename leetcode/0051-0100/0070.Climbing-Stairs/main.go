package main

import "log"

func main() {
	cases := []struct {
		x   int
		res int
	}{
		{1, 1},
		{2, 2},
		{3, 3},
		{4, 5},
		{5, 8},
		{45, 1836311903},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := climbStairs(c.x); res != c.res {
			log.Fatalf("expect: %d, got: %d", c.res, res)
		}
	}
}

func climbStairs(n int) int {
	if n <= 3 {
		return n
	}

	x := 2
	y := 3
	for i := 4; i <= n; i++ {
		y = x + y
		x = y - x
	}
	return y
}
