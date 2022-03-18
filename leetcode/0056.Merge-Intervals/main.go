package main

import (
	"fmt"
	"log"
	"sort"
)

type I [][]int

func (intervals I) Len() int {
	return len(intervals)
}

func (intervals I) Less(i int, j int) bool {
	return intervals[i][0] < intervals[j][0]
}

func (intervals I) Swap(i int, j int) {
	intervals[i], intervals[j] = intervals[j], intervals[i]
}

func (intervals I) String() string {
	sort.Sort(intervals)
	var res string
	for _, i := range intervals {
		res += fmt.Sprintf("{%d,%d},", i[0], i[1])
	}
	return res
}

func main() {
	cases := []struct {
		intervals [][]int
		res       [][]int
	}{
		{
			intervals: [][]int{{2, 3}, {4, 5}, {6, 7}, {8, 9}, {1, 10}},
			res:       [][]int{{1, 10}},
		},
		{
			intervals: [][]int{{1, 1}},
			res:       [][]int{{1, 1}},
		},
		{
			intervals: [][]int{{1, 1}, {1, 1}},
			res:       [][]int{{1, 1}},
		},
		{
			intervals: [][]int{{1, 1}, {2, 2}},
			res:       [][]int{{1, 1}, {2, 2}},
		},
		{
			intervals: [][]int{{1, 4}, {4, 5}},
			res:       [][]int{{1, 5}},
		},
		{
			intervals: [][]int{{4, 5}, {1, 2}},
			res:       [][]int{{4, 5}, {1, 2}},
		},
		{
			intervals: [][]int{{4, 5}, {1, 4}},
			res:       [][]int{{1, 5}},
		},
		{
			intervals: [][]int{{1, 2}, {2, 6}, {8, 10}, {15, 18}},
			res:       [][]int{{1, 6}, {8, 10}, {15, 18}},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		got := I(merge(c.intervals)).String()
		expect := I(c.res).String()
		if expect != got {
			log.Fatalf("expect: %s, got: %s", expect, got)
		}
	}
}

func merge(intervals [][]int) [][]int {
	var res [][]int
	for _, i := range intervals {
		newInterval := true
		for j := 0; j < len(res); j++ {
			if i[1] < res[j][0] || i[0] > res[j][1] {
				continue
			}

			if i[0] < res[j][0] {
				res[j][0] = i[0]
			}
			if i[1] > res[j][1] {
				res[j][1] = i[1]
			}
			newInterval = false
			break
		}
		if newInterval {
			res = append(res, i)
		}
	}
	if len(res) == len(intervals) {
		return res
	}
	return merge(res)
}
