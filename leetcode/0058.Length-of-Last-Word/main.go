package main

import "log"

func main() {
	cases := []struct {
		str    string
		length int
	}{
		{"Hello World", 5},
		{" Hello", 5},
		{"Hello ", 5},
		{"   fly me   to   the moon  ", 4},
		{"luffy is still joyboy", 6},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := lengthOfLastWord(c.str); res != c.length {
			log.Fatalf("expect length of last word: %d, got: %d", c.length, res)
		}
	}
}

func lengthOfLastWord(s string) int {
	var length int
	startCounter := false
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == ' ' {
			if startCounter {
				return length
			}
			continue
		} else {
			length++
			startCounter = true
		}
	}
	return length
}
