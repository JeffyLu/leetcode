package main

import (
	"log"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	last := m + n - 1
	for j := n - 1; j >= 0; {
		if m-1 < 0 || nums2[j] > nums1[m-1] {
			nums1[last] = nums2[j]
			j--
		} else {
			nums1[last] = nums1[m-1]
			m--
		}
		last--
	}
}

func main() {
	cases := []struct {
		nums1 []int
		m     int
		nums2 []int
		n     int
		res   []int
	}{
		{
			nums1: []int{1, 2, 3, 0, 0, 0},
			m:     3,
			nums2: []int{2, 5, 6},
			n:     3,
			res:   []int{1, 2, 2, 3, 5, 6},
		},
		{
			nums1: []int{1},
			m:     1,
			nums2: []int{},
			n:     0,
			res:   []int{1},
		},
		{
			nums1: []int{0},
			m:     0,
			nums2: []int{1},
			n:     1,
			res:   []int{1},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		merge(c.nums1, c.m, c.nums2, c.n)
		for i, x := range c.res {
			if x != c.nums1[i] {
				log.Fatalf("expect: %+v, got: %+v", c.res, c.nums1)
			}
		}
	}
}
