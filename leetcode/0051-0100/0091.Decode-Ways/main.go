package main

import (
	"log"
)

func numDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}

	a := 1
	res := 1
	for i := 1; i < len(s); i++ {
		left := s[i-1]
		if left == '1' {
			if s[i] == '0' {
				res = a
			} else {
				res = res + a
				a = res - a
			}
		} else if left == '2' {
			if s[i] == '0' {
				res = a
			} else if s[i] <= '6' {
				res = res + a
				a = res - a
			} else {
				a = res
			}
		} else {
			if s[i] == '0' {
				return 0
			} else {
				a = res
			}
		}
	}
	return res
}

func main() {
	cases := []struct {
		s   string
		res int
	}{
		{"12312", 6},
		{"123123", 9},
		{"1201", 1},
		{"12012", 2},
		{"120123", 3},
		{"1201234", 3},
		{"112201", 3},
		{"112220", 5},
		{"112230", 0},
		{"11229", 5},
		{"1122201", 5},
		{"1122210", 8},
		{"112221", 13},
		{"1122", 5},
		{"21226", 8},
		{"0", 0},
		{"112200", 0},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := numDecodings(c.s); res != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
	}
}
