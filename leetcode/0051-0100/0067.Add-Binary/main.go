package main

import "log"

func main() {
	cases := []struct {
		a   string
		b   string
		res string
	}{
		{
			a:   "1",
			b:   "11",
			res: "100",
		},
		{
			a:   "1010",
			b:   "1011",
			res: "10101",
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := addBinary(c.a, c.b); res != c.res {
			log.Fatalf("expect: %s, got: %s", c.res, res)
		}
	}
}

func addBinary(a string, b string) string {
	if len(a) < len(b) {
		a, b = b, a
	}
	padding := len(a) - len(b)

	var res string
	one := 0
	for i := len(a) - 1; i >= 0; i-- {
		if a[i] == '1' {
			one++
		}
		if j := i - padding; j < len(b) && j >= 0 && b[j] == '1' {
			one++
		}

		if one == 1 || one == 3 {
			res = "1" + res
		} else {
			res = "0" + res
		}
		if one > 1 {
			one = 1
		} else {
			one = 0
		}
	}
	if one == 0 {
		return res
	}
	return "1" + res
}
