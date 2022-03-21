package main

import (
	"fmt"
	"log"
)

func main() {
	cases := []struct {
		matrix [][]int
		res    string
	}{
		{
			matrix: [][]int{
				{1},
			},
			res: "1,",
		},
		{
			matrix: [][]int{
				{1, 2},
			},
			res: "1,2,",
		},
		{
			matrix: [][]int{
				{1},
				{2},
			},
			res: "1,2,",
		},
		{
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			res: "1,2,3,6,9,8,7,4,5,",
		},
		{
			matrix: [][]int{
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
			},
			res: "1,2,3,4,8,12,11,10,9,5,6,7,",
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		var res string
		for _, i := range spiralOrder(c.matrix) {
			res += fmt.Sprintf("%d,", i)
		}
		if res != c.res {
			log.Fatalf("expect: %s, got: %s", c.res, res)
		}
	}
}

func spiralOrder(matrix [][]int) []int {
	var res []int
	var i, j int
	maxi := len(matrix) - 1
	maxj := len(matrix[0]) - 1
	nexti := 0
	nextj := 1
	truned := 0
	for {
		if i > maxi || i < 0 || j > maxj || j < 0 || matrix[i][j] == -1000 {
			return res
		}

		res = append(res, matrix[i][j])
		matrix[i][j] = -1000

		_i := i + nexti
		_j := j + nextj
		if _i < 0 || _i > maxi || _j < 0 || _j > maxj || matrix[_i][_j] == -1000 {
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
}
