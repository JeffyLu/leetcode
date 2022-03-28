package main

import (
	"log"
)

func main() {
	cases := []struct {
		arr [][]int
		res int
	}{
		{
			arr: [][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}},
			res: 7,
		},
		{
			arr: [][]int{{1, 2, 3}, {4, 5, 6}},
			res: 12,
		},
		{
			arr: [][]int{{0}},
			res: 0,
		},
		{
			arr: [][]int{{1, 2}, {1, 2}},
			res: 4,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := minPathSum(c.arr); res != c.res {
			log.Fatalf("expect: %d, got: %d", c.res, res)
		}
	}
}

func minPathSum(grid [][]int) int {
	for i := 1; i < len(grid); i++ {
		grid[i][0] += grid[i-1][0]
	}
	for j := 1; j < len(grid[0]); j++ {
		grid[0][j] += grid[0][j-1]
	}

	for i := 1; i < len(grid); i++ {
		for j := 1; j < len(grid[0]); j++ {
			if grid[i-1][j] < grid[i][j-1] {
				grid[i][j] += grid[i-1][j]
			} else {
				grid[i][j] += grid[i][j-1]
			}
		}
	}
	return grid[len(grid)-1][len(grid[0])-1]
}
