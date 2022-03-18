package main

import "log"

func main() {
	cases := []struct {
		nums []int
		res  bool
	}{

		{
			nums: []int{2, 3, 1, 1, 4},
			res:  true,
		},
		{
			nums: []int{3, 2, 1, 0, 4},
			res:  false,
		},
		{
			nums: []int{1},
			res:  true,
		},
		{
			nums: []int{2, 0},
			res:  true,
		},
		{
			nums: []int{0},
			res:  true,
		},
		{
			nums: []int{0, 0, 1},
			res:  false,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := canJump(c.nums); res != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
	}
}

func canJump(nums []int) bool {
	reachable := 0
	last := len(nums) - 1
	for i := 0; i <= reachable; i++ {
		if r := i + nums[i]; r > reachable {
			reachable = r
		}
		if reachable >= last {
			return true
		}
	}
	return false
}
