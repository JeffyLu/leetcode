package main

import "log"

func main() {
	cases := []struct {
		n   int
		res [][]int
	}{
		{n: 1, res: [][]int{{1}}},
		{n: 2, res: [][]int{{1, 2}, {4, 3}}},
		{n: 3, res: [][]int{{1, 2, 3}, {8, 9, 4}, {7, 6, 5}}},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		res := generateMatrix(c.n)
		if len(res) != c.n || len(res[0]) != c.n {
			log.Fatalf("expect length of matrix: %d, got: %d", c.n, len(res))
		}
		for i := 0; i < c.n; i++ {
			for j := 0; j < c.n; j++ {
				if res[i][j] != c.res[i][j] {
					log.Fatalf("expect: %+v, got: %+v", c.res, res)
				}
			}
		}
	}
}

func generateMatrix(n int) [][]int {
	res := make([][]int, n)
	for i := 0; i < n; i++ {
		res[i] = make([]int, n)
	}

	nexti := 0
	nextj := 1
	i := 0
	j := 0
	truned := 0
	for num := 1; num <= n*n; num++ {
		res[i][j] = num
		_nexti := i + nexti
		_nextj := j + nextj
		if _nexti < 0 || _nexti >= n || _nextj < 0 || _nextj >= n || res[_nexti][_nextj] != 0 {
			switch truned % 4 {
			case 0:
				nexti = 1
				nextj = 0
			case 1:
				nexti = 0
				nextj = -1
			case 2:
				nexti = -1
				nextj = 0
			case 3:
				nexti = 0
				nextj = 1
			}
			truned++
		}
		i += nexti
		j += nextj
	}
	return res
}
