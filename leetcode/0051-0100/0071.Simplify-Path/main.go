package main

import (
	"log"
	"strings"
)

func main() {
	cases := []struct {
		path string
		res  string
	}{
		{"/a//b////c/d//././/..", "/a/b/c"},
		{"/home/", "/home"},
		{"/..", "/"},
		{"/../", "/"},
		{"/home//foo/", "/home/foo"},
		{"/a/./b/../../c/", "/c"},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := simplifyPath(c.path); res != c.res {
			log.Fatalf("expect: %s, got: %s", c.res, res)
		}
	}
}

func simplifyPath(path string) string {
	var res []string
	seg := ""
	for i := 1; i <= len(path); i++ {
		if i < len(path) && path[i] != '/' {
			seg += path[i : i+1]
			continue
		}

		if seg == ".." {
			if len(res) != 0 {
				res = res[:len(res)-1]
			}
		} else if seg != "." && seg != "" {
			res = append(res, seg)
		}
		seg = ""
	}
	return "/" + strings.Join(res, "/")
}
