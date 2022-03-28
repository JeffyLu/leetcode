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
			arr: [][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}},
			res: 2,
		},
		{
			arr: [][]int{{0, 1, 0}, {0, 0, 0}, {0, 0, 0}},
			res: 3,
		},
		{
			arr: [][]int{{0, 0, 1}, {0, 0, 0}, {0, 0, 0}},
			res: 5,
		},
		{
			arr: [][]int{{0, 0, 0, 0}, {1, 0, 0, 0}, {0, 0, 0, 0}},
			res: 6,
		},
		{
			arr: [][]int{{0, 1}, {0, 0}},
			res: 1,
		},
		{
			arr: [][]int{{1}},
			res: 0,
		},
		{
			arr: [][]int{{0}},
			res: 1,
		},
		{
			arr: [][]int{{0, 1}},
			res: 0,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := uniquePathsWithObstacles(c.arr); res != c.res {
			log.Fatalf("expect: %d, got: %d", c.res, res)
		}
	}
}

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {
		return 0
	}

	obstacleGrid[0][0] = 1
	for i := 0; i < len(obstacleGrid); i++ {
		for j := 0; j < len(obstacleGrid[0]); j++ {
			if obstacleGrid[i][j] == 1 && !(i == 0 && j == 0) {
				obstacleGrid[i][j] = 0
				continue
			}

			if i-1 >= 0 {
				obstacleGrid[i][j] += obstacleGrid[i-1][j]
			}
			if j-1 >= 0 {
				obstacleGrid[i][j] += obstacleGrid[i][j-1]
			}
		}
	}
	return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
}
