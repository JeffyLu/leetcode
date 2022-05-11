package main

import (
	"fmt"
	"log"
	"sort"
)

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{
		[]int{},
		[]int{nums[0]},
	}
	lastIdx := 1
	lastNum := nums[0]
	for i := 1; i < len(nums); i++ {
		j := 0
		if nums[i] == lastNum {
			j = lastIdx
		}
		length := len(res)
		for ; j < length; j++ {
			sub := append([]int{}, res[j]...)
			sub = append(sub, nums[i])
			res = append(res, sub)
		}
		lastIdx = length
		lastNum = nums[i]
	}
	return res
}

func main() {
	cases := []struct {
		nums []int
		res  [][]int
	}{
		{
			nums: []int{1, 2, 2},
			res: [][]int{
				{},
				{1},
				{1, 2},
				{1, 2, 2},
				{2},
				{2, 2},
			},
		},
		{
			nums: []int{0},
			res: [][]int{
				{},
				{0},
			},
		},
		{
			nums: []int{1, 1, 2, 1, 1, 2},
			res: [][]int{
				{},
				{1},
				{1, 1},
				{1, 1, 1},
				{1, 1, 1, 1},
				{1, 1, 1, 1, 2},
				{1, 1, 1, 1, 2, 2},
				{1, 1, 1, 2},
				{1, 1, 1, 2, 2},
				{1, 1, 2},
				{1, 1, 2, 2},
				{1, 2},
				{1, 2, 2},
				{2},
				{2, 2},
			},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		res := subsetsWithDup(c.nums)
		if len(res) != len(c.res) {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
		expect := map[string]bool{}
		for _, s := range c.res {
			sort.Ints(s)
			expect[fmt.Sprintf("%+v", s)] = true
		}
		for _, s := range res {
			sort.Ints(s)
			k := fmt.Sprintf("%+v", s)
			if !expect[k] {
				log.Fatalf("expect: %+v, got: %+v", c.res, res)
			}
			delete(expect, k)
		}
	}
}
