package main

import (
	"log"
)

func grayCode(n int) []int {
	res := make([]int, 1<<n)
	for i := 0; i < 1<<n; i++ {
		res[i] = i>>1 ^ i
	}
	return res
}

func main() {
	cases := []struct {
		n   int
		res []int
	}{
		{
			n:   2,
			res: []int{0, 1, 3, 2},
		},
		{
			n:   1,
			res: []int{0, 1},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		res := grayCode(c.n)
		for i, x := range res {
			if x != c.res[i] {
				log.Fatalf("expect: %+v, got: %+v", c.res, res)
			}
		}
	}
}
