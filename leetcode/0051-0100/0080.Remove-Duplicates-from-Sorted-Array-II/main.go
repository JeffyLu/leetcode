package main

import (
	"log"
)

func removeDuplicates(nums []int) int {
	j := 2

	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[i-1] {
			return i
		}

		if j >= len(nums) {
			return i + 1
		}

		if nums[i] > nums[i-1] {
			nums[j], nums[i+1] = nums[i+1], nums[j]
			j++
			continue
		}

		for ; j < len(nums); j++ {
			if nums[j] > nums[i] {
				nums[j], nums[i+1] = nums[i+1], nums[j]
				break
			}
			if j == len(nums)-1 {
				return i + 1
			}
		}
		j++
	}
	return len(nums)
}

func main() {
	cases := []struct {
		nums []int
		res  []int
	}{
		{
			nums: []int{1},
			res:  []int{1},
		},
		{
			nums: []int{1, 1},
			res:  []int{1, 1},
		},
		{
			nums: []int{1, 2},
			res:  []int{1, 2},
		},
		{
			nums: []int{1, 1, 1},
			res:  []int{1, 1},
		},
		{
			nums: []int{1, 1, 2, 2},
			res:  []int{1, 1, 2, 2},
		},
		{
			nums: []int{1, 1, 1, 2, 2, 3},
			res:  []int{1, 1, 2, 2, 3},
		},
		{
			nums: []int{0, 0, 1, 1, 1, 1, 2, 3, 3},
			res:  []int{0, 0, 1, 1, 2, 3, 3},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		length := removeDuplicates(c.nums)
		if length != len(c.res) {
			log.Fatalf("expect: %+v, got: %+v", c.res, c.nums[:length])
		}
		for i, n := range c.res {
			if c.nums[i] != n {
				log.Fatalf("expect: %+v, got: %+v", c.res, c.nums[:length])
			}
		}
	}
}
