package main

import "log"

func main() {
	cases := []struct {
		x   int
		res int
	}{
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 1},
		{4, 2},
		{5, 2},
		{6, 2},
		{7, 2},
		{8, 2},
		{9, 3},
		{2147483647, 46340},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := mySqrt(c.x); res != c.res {
			log.Fatalf("expect: %d, got: %d", c.res, res)
		}
	}
}

func mySqrt(x int) int {
	if x <= 1 {
		return x
	}

	left := 1
	right := x
	for left <= right {
		mid := (left + right) / 2
		n := mid * mid
		if n == x {
			return mid
		}

		if n < x {
			left = mid + 1
			continue
		}

		right = mid - 1
		if right*right <= x {
			return right
		}
	}
	return right
}
