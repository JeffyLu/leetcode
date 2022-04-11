package main

import (
	"log"
)

func subsets(nums []int) [][]int {
	res := [][]int{{}}
	for _, i := range nums {
		length := len(res)
		for j := 1; j < length; j++ {
			tmp := append([]int{}, res[j]...)
			tmp = append(tmp, i)
			res = append(res, tmp)
		}
		res = append(res, []int{i})
	}
	return res
}

func main() {
	cases := []struct {
		nums []int
		res  [][]int
	}{
		{
			nums: []int{1},
			res: [][]int{
				{},
				{1},
			},
		},
		{
			nums: []int{1, 2, 3},
			res: [][]int{
				{},
				{1},
				{1, 2},
				{2},
				{1, 3},
				{1, 2, 3},
				{2, 3},
				{3},
			},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		res := subsets(c.nums)
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
