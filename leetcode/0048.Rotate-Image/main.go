package main

import (
	"fmt"
	"log"
)

func main() {
	cases := []struct {
		m   [][]int
		res [][]int
	}{
		{
			m: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			res: [][]int{
				{7, 4, 1},
				{8, 5, 2},
				{9, 6, 3},
			},
		},
		{
			m: [][]int{
				{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16},
			},
			res: [][]int{
				{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11},
			},
		},
	}
	for _, c := range cases {
		fmt.Printf("%+v\n", c)
		rotate(c.m)
		for i := 0; i < len(c.m); i++ {
			for j := 0; j < len(c.m); j++ {
				if c.m[i][j] != c.res[i][j] {
					log.Fatalf("expect val(%d,%d): %d, got: %d", i, j, c.m[i][j], c.res[i][j])
				}
			}
		}
	}
}

func rotate(m [][]int) {
	length := len(m)
	if length == 1 {
		return
	}

	for i := 0; i < length/2; i++ {
		m[i], m[length-i-1] = m[length-i-1], m[i]
	}

	for i := 0; i < length; i++ {
		for j := i + 1; j < length; j++ {
			m[i][j], m[j][i] = m[j][i], m[i][j]
		}
	}
}
