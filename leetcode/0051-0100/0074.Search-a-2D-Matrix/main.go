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
	lenI := len(matrix)
	lenJ := len(matrix[0])

	left := 0
	right := lenI*lenJ - 1
	var i, j, mid int
	for left <= right {
		mid = (left + right) / 2
		i = mid / lenJ
		j = mid % lenJ
		if matrix[i][j] == target {
			return true
		}
		if matrix[i][j] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return false
}
