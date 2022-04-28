package main

import (
	"log"
)

func search(nums []int, target int) bool {
	left := 0
	right := len(nums) - 1
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target || nums[left] == target || nums[right] == target {
			return true
		}

		if nums[left] == nums[right] {
			left++
			right--
			continue
		}

		if nums[mid] > target {
			if nums[left] > target && nums[left] <= nums[mid] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		} else {
			if nums[right] < target && nums[right] >= nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		}
	}
	return false
}

func main() {
	cases := []struct {
		nums   []int
		target int
		res    bool
	}{
		{
			nums:   []int{2, 2, 2, 0, 0, 1},
			target: 0,
			res:    true,
		},
		{
			nums:   []int{0, 1, 1, 2, 0, 0},
			target: 2,
			res:    true,
		},
		{

			nums:   []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1},
			target: 2,
			res:    true,
		},
		{
			nums:   []int{1, 0, 1, 1, 1},
			target: 0,
			res:    true,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 5,
			res:    true,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 6,
			res:    true,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 0,
			res:    true,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 3,
			res:    false,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 2,
			res:    true,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 0,
			res:    true,
		},
		{
			nums:   []int{2, 5, 6, 0, 0, 1, 2},
			target: 1,
			res:    true,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := search(c.nums, c.target); res != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
	}
}
