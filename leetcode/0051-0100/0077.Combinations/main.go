package main

import (
	"log"
)

func main() {
	cases := []struct {
		n, k int
		res  [][]int
	}{
		{
			n: 1,
			k: 1,
			res: [][]int{
				{1},
			},
		},
		{
			n: 4,
			k: 1,
			res: [][]int{
				{1},
				{2},
				{3},
				{4},
			},
		},
		{
			n: 4,
			k: 2,
			res: [][]int{
				{1, 2},
				{1, 3},
				{1, 4},
				{2, 3},
				{2, 4},
				{3, 4},
			},
		},
		{
			n: 4,
			k: 3,
			res: [][]int{
				{1, 2, 3},
				{1, 2, 4},
				{1, 3, 4},
				{2, 3, 4},
			},
		},
		{
			n: 4,
			k: 4,
			res: [][]int{
				{1, 2, 3, 4},
			},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		res := combine(c.n, c.k)
		if len(res) != len(c.res) {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
		for i := 0; i < len(c.res); i++ {
			for j := 0; j < len(c.res[i]); j++ {
				if c.res[i][j] != res[i][j] {
					log.Fatalf("expect: %+v, got: %+v", c.res, res)
				}
			}
		}
	}
}

func combine(n int, k int) [][]int {
	var tmp [][]int
	for i := 1; i <= n-k+1; i++ {
		tmp = append(tmp, []int{i})
	}

	var res [][]int
	for len(tmp) > 0 {
		t := tmp[0]
		tmp = tmp[1:]

		if len(t) == k {
			res = append(res, t)
			continue
		}

		last := t[len(t)-1]
		for i := last + 1; i <= n; i++ {
			comb := append([]int{}, t...)
			comb = append(comb, i)
			tmp = append(tmp, comb)
		}
	}
	return res
}
