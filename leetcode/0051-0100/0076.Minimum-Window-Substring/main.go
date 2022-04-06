package main

import (
	"log"
)

func main() {
	cases := []struct {
		s, t, res string
	}{
		{"ADOBECODEBANC", "ABC", "BANC"},
		{"a", "a", "a"},
		{"a", "aa", ""},
		{"cabwefgewcwaefgcf", "cae", "cwae"},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := minWindow(c.s, c.t); res != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
	}
}

func minWindow(s string, t string) string {
	chars := map[byte]int{}
	for i := 0; i < len(t); i++ {
		chars[t[i]]++
	}

	res := ""
	left := -1
	right := 0
	for ; right < len(s); right++ {
		if _, ok := chars[s[right]]; !ok {
			continue
		}

		if left == -1 {
			left = right
		}
		chars[s[right]]--

		for ; left <= right; left++ {
			if _, ok := chars[s[left]]; !ok {
				continue
			}
			if !matched(chars) {
				break
			}
			if res == "" || len(res) > right-left {
				res = s[left : right+1]
			}
			chars[s[left]]++
		}
	}
	return res
}

func matched(chars map[byte]int) bool {
	for _, cnt := range chars {
		if cnt > 0 {
			return false
		}
	}
	return true
}
