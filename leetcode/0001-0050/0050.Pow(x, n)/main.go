package main

import (
	"log"
)

func main() {
	cases := []struct {
		x      float64
		n      int
		expect float64
	}{
		{2, 2, 4},
		{2, 10, 1024},
		{2, -2, 0.25},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if got := myPow(c.x, c.n); got != c.expect {
			log.Fatalf("expect: %f, got: %f", c.expect, got)
		}
	}
}

func myPow(x float64, n int) float64 {
	if n < 0 {
		x = 1 / x
		n = -n
	}

	var res float64 = 1
	for n > 0 {
		if n&1 == 1 {
			res *= x
		}
		x *= x
		n = n >> 1
	}
	return res
}
