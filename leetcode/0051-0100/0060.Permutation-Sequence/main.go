package main

import (
	"log"
)

func main() {
	cases := []struct {
		n   int
		k   int
		res string
	}{
		{3, 1, "123"},
		{3, 2, "132"},
		{3, 3, "213"},
		{3, 6, "321"},
		{4, 9, "2314"},
		{9, 30000, "179586432"},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := getPermutation(c.n, c.k); res != c.res {
			log.Fatalf("expect: %s, got: %s", c.res, res)
		}
	}
}

func getPermutation(n int, k int) string {
	var nums []string
	numStrs := []string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}
	for i := 0; i < n; i++ {
		nums = append(nums, numStrs[i])
	}
	return selectNum(nums, k)
}

func selectNum(nums []string, k int) string {
	if len(nums) == 1 {
		return nums[0]
	}

	total := 1
	for i := 1; i <= len(nums); i++ {
		total *= i
	}
	group := total / len(nums)

	selected := (k - 1) / group
	var next []string
	for _, s := range nums {
		if s != nums[selected] {
			next = append(next, s)
		}
	}
	return nums[selected] + selectNum(next, (k-1)%group+1)
}
