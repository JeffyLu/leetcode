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
	var i, j, tmp int
	for i = 1; i < len(nums); i++ {
		tmp = nums[i]
		j = i - 1
		for ; j >= 0; j-- {
			if nums[j] <= tmp {
				break
			}
			nums[j+1] = nums[j]
		}
		nums[j+1] = tmp
	}
}
