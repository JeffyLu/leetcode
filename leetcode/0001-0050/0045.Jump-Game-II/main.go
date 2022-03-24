package main

import "log"

func main() {
	cases := []struct {
		nums []int
		res  int
	}{
		{
			nums: []int{2, 3, 1, 1, 4},
			res:  2,
		},
		{
			nums: []int{2, 3, 0, 1, 4},
			res:  2,
		},
		{
			nums: []int{3, 1, 1, 1, 1, 4},
			res:  3,
		},
		{
			nums: []int{1},
			res:  0,
		},
		{
			nums: []int{2, 1},
			res:  1,
		},
		{
			nums: []int{7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3},
			res:  2,
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := jump(c.nums); res != c.res {
			log.Fatalf("expect: %d, got: %d", c.res, res)
		}
	}
}

func jump(nums []int) int {
	last := len(nums) - 1
	if last == 0 {
		return 0
	}

	step := 0
	incrStep := 0
	stepReachable := 0
	for i := 0; i <= last; i++ {
		if nums[i]+i > stepReachable {
			stepReachable = nums[i] + i
			if stepReachable >= last {
				step++
				break
			}
		}
		if i == incrStep {
			incrStep = stepReachable
			step++
		}
	}
	return step
}
