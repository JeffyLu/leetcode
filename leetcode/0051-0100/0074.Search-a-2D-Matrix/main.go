package main

import (
	"log"
)

func main() {
	cases := []struct {
		matrix [][]int
		target int
		res    bool
	}{
		{
			matrix: [][]int{
				{1, 3, 5, 7},
				{10, 11, 16, 20},
				{23, 30, 34, 60},
			},
			target: 0,
			res:    false,
		},
		{
			matrix: [][]int{
				{1, 3, 5, 7},
				{10, 11, 16, 20},
				{23, 30, 34, 60},
			},
			target: 70,
			res:    false,
		},
		{
			matrix: [][]int{
				{1, 3, 5, 7},
				{10, 11, 16, 20},
				{23, 30, 34, 60},
			},
			target: 1,
			res:    true,
		},
		{
			matrix: [][]int{
				{1, 3, 5, 7},
				{10, 11, 16, 20},
				{23, 30, 34, 60},
			},
			target: 60,
			res:    true,
		},
		{
			matrix: [][]int{
				{1, 3, 5, 7},
				{10, 11, 16, 20},
				{23, 30, 34, 60},
			},
			target: 21,
			res:    false,
		},
		{
			matrix: [][]int{
				{1, 3, 5, 7},
				{10, 11, 16, 20},
				{23, 30, 34, 60},
			},
			target: 6,
			res:    false,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := searchMatrix(c.matrix, c.target); res != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, c.matrix)
		}
	}
}

func searchMatrix(matrix [][]int, target int) bool {
	maxI := len(matrix) - 1
	maxJ := len(matrix[0]) - 1
	if target < matrix[0][0] || target > matrix[maxI][maxJ] {
		return false
	}

	li := 0
	ri := maxI
	var i int
	for li <= ri {
		i = (li + ri) / 2
		if target < matrix[i][0] {
			ri = i - 1
		} else if target > matrix[i][maxJ] {
			li = i + 1
		} else {
			break
		}
	}

	lj := 0
	rj := maxJ
	var j int
	for lj <= rj {
		j = (lj + rj) / 2
		if matrix[i][j] == target {
			return true
		}
		if matrix[i][j] > target {
			rj = j - 1
		} else {
			lj = j + 1
		}
	}
	return false
}
