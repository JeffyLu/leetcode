package main

import (
	"log"
)

func main() {
	cases := []struct {
		matrix [][]int
		res    [][]int
	}{
		{
			matrix: [][]int{
				{0, 0, 0, 5},
				{4, 3, 1, 4},
				{0, 1, 1, 4},
				{1, 2, 1, 3},
				{0, 0, 1, 1}},
			res: [][]int{
				{0, 0, 0, 0},
				{0, 0, 0, 4},
				{0, 0, 0, 0},
				{0, 0, 0, 3},
				{0, 0, 0, 0},
			},
		},
		{
			matrix: [][]int{
				{1, 1, 1},
				{1, 0, 1},
				{1, 1, 1},
			},
			res: [][]int{
				{1, 0, 1},
				{0, 0, 0},
				{1, 0, 1},
			},
		},
		{
			matrix: [][]int{
				{0, 1, 2, 0},
				{3, 4, 5, 2},
				{1, 3, 1, 5},
			},
			res: [][]int{
				{0, 0, 0, 0},
				{0, 4, 5, 0},
				{0, 3, 1, 0},
			},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		setZeroes(c.matrix)
		for i := 0; i < len(c.matrix); i++ {
			for j := 0; j < len(c.matrix[0]); j++ {
				if c.matrix[i][j] != c.res[i][j] {
					log.Fatalf("expect: %+v, got: %+v", c.res, c.matrix)
				}
			}
		}
	}
}

func setZeroes(matrix [][]int) {
	is := map[int]bool{}
	js := map[int]bool{}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if matrix[i][j] == 0 {
				is[i] = true
				js[j] = true
			}
		}
	}

	for i := range is {
		for j := 0; j < len(matrix[0]); j++ {
			matrix[i][j] = 0
		}
	}
	for j := range js {
		for i := 0; i < len(matrix); i++ {
			matrix[i][j] = 0
		}
	}
}
