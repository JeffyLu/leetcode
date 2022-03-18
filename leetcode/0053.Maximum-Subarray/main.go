package main

import "log"

func main() {
	cases := []struct {
		nums []int
		res  int
	}{
		{
			nums: []int{-2, 1, -3, 4, -1, 2, 1, -5, 4},
			res:  6,
		},
		{
			nums: []int{1},
			res:  1,
		},
		{
			nums: []int{5, 4, -1, 7, 8},
			res:  23,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := maxSubArray(c.nums); res != c.res {
			log.Fatalf("expected: %d, got: %d", c.res, res)
		}
	}
}

func maxSubArray(nums []int) int {
	sum := nums[0]
	for i := 1; i < len(nums); i++ {
		if s := nums[i] + nums[i-1]; s > nums[i] {
			nums[i] = s
		}
		if nums[i] > sum {
			sum = nums[i]
		}
	}
	return sum
}
