package main

import (
	"log"
)

func main() {
	cases := []struct {
		nums []int
		res  []int
	}{
		{[]int{2, 0, 2, 1, 1, 0}, []int{0, 0, 1, 1, 2, 2}},
		{[]int{2, 0, 1}, []int{0, 1, 2}},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		sortColors(c.nums)
		for i := 0; i < len(c.nums); i++ {
			if c.res[i] != c.nums[i] {
				log.Fatalf("expect: %+v, got: %+v", c.res, c.nums)
			}
		}
	}
}

func sortColors(nums []int) {
	left := 0
	right := len(nums) - 1
	for i := 0; i <= right; {
		if nums[i] == 0 {
			nums[i], nums[left] = nums[left], nums[i]
			if i == left {
				i++
			}
			left++
		} else if nums[i] == 2 {
			nums[i], nums[right] = nums[right], nums[i]
			right--
		} else {
			i++
		}
	}
}
