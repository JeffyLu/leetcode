package main

import (
	"log"
)

func main() {
	cases := []struct {
		m   int
		n   int
		res int
	}{
		{1, 1, 1},
		{2, 3, 3},
		{4, 4, 2},
		{3, 7, 28},
		{23, 12, 193536720},
		{51, 9, 1916797311},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := uniquePaths(c.m, c.n); res != c.res {
			log.Fatalf("expect: %d, got: %d", c.res, res)
		}
	}
}

func uniquePaths(m int, n int) int {
	arr := make([][]int, m)
	for i := 0; i < m; i++ {
		arr[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i-1 < 0 || j-1 < 0 {
				arr[i][j] = 1
				continue
			}
			arr[i][j] = arr[i-1][j] + arr[i][j-1]
		}
	}
	return arr[m-1][n-1]
}
