package main

import (
	"log"
)

func main() {
	cases := []struct {
		intervals   [][]int
		newInterval []int
		res         [][]int
	}{
		{
			intervals:   [][]int{{1, 3}, {6, 9}},
			newInterval: []int{2, 5},
			res:         [][]int{{1, 5}, {6, 9}},
		},
		{
			intervals:   [][]int{{1, 5}},
			newInterval: []int{0, 0},
			res:         [][]int{{0, 0}, {1, 5}},
		},
		{
			intervals:   [][]int{{2, 7}},
			newInterval: []int{1, 5},
			res:         [][]int{{1, 7}},
		},
		{
			intervals:   [][]int{{1, 5}},
			newInterval: []int{2, 7},
			res:         [][]int{{1, 7}},
		},
		{
			intervals:   [][]int{{1, 5}},
			newInterval: []int{2, 3},
			res:         [][]int{{1, 5}},
		},
		{
			intervals:   [][]int{},
			newInterval: []int{5, 7},
			res:         [][]int{{5, 7}},
		},
		{
			intervals:   [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}},
			newInterval: []int{4, 8},
			res:         [][]int{{1, 2}, {3, 10}, {12, 16}},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		res := insert(c.intervals, c.newInterval)
		if len(res) != len(c.res) {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
		for i := 0; i < len(res); i++ {
			if res[i][0] != c.res[i][0] || res[i][1] != c.res[i][1] {
				log.Fatalf("expect: %+v, got: %+v", c.res, res)
			}
		}
	}
}

func insert(intervals [][]int, newInterval []int) [][]int {
	var interval []int
	inserted := false
	i := 0
	if len(intervals) == 0 || newInterval[0] < intervals[0][0] {
		interval = newInterval
		inserted = true
	} else {
		interval = intervals[i]
		i++
	}

	var res [][]int
	for {
		last := len(res) - 1
		if last < 0 || interval[0] > res[last][1] {
			res = append(res, interval)
		} else if interval[0] < res[last][0] {
			res[last][0] = interval[0]
		} else if interval[1] > res[last][1] {
			res[last][1] = interval[1]
		}

		if inserted && i == len(intervals) {
			return res
		}
		if i < len(intervals) && (intervals[i][0] < newInterval[0] || inserted) {
			interval = intervals[i]
			i++
		} else {
			interval = newInterval
			inserted = true
		}
	}
}
