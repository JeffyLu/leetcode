package main

import (
	"log"
	"sort"
	"strings"
)

func main() {
	cases := []struct {
		strs []string
		res  [][]string
	}{
		{
			strs: []string{"eat", "tea", "tan", "ate", "nat", "bat"},
			res:  [][]string{{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}},
		},
		{
			strs: []string{""},
			res:  [][]string{{""}},
		},
		{
			strs: []string{"a"},
			res:  [][]string{{"a"}},
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		var expect, got []string
		for _, s := range groupAnagrams(c.strs) {
			sort.Strings(s)
			got = append(got, strings.Join(s, ","))
		}
		for _, s := range c.res {
			sort.Strings(s)
			expect = append(expect, strings.Join(s, ","))
		}
		sort.Strings(expect)
		sort.Strings(got)
		if strings.Join(expect, ",") != strings.Join(got, ",") {
			log.Fatalf("expect: %+v, got: %+v", expect, got)
		}
	}
}

func groupAnagrams(strs []string) [][]string {
	var res [][]string
	if len(strs) == 0 {
		return res
	}

	bucket := map[string][]string{}
	for _, s := range strs {
		chars := []rune(s)
		sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
		key := string(chars)
		bucket[key] = append(bucket[key], s)
	}

	for _, v := range bucket {
		res = append(res, v)
	}
	return res
}
