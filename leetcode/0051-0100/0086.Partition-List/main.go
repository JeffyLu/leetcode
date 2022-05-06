package main

import (
	"fmt"
	"log"
)

func partition(head *ListNode, x int) *ListNode {
	var toInsert, prev *ListNode
	for tmp := head; tmp != nil; tmp = tmp.Next {
		if tmp.Val >= x {
			prev = tmp
			continue
		}

		if prev == nil {
			toInsert = tmp
			continue
		}

		prev.Next = tmp.Next
		if toInsert == nil {
			tmp.Next = head
			head = tmp
		} else {
			tmp.Next = toInsert.Next
			toInsert.Next = tmp
		}
		toInsert = tmp
		tmp = prev
	}
	return head
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func (n *ListNode) String() string {
	var res string
	for n != nil {
		res += fmt.Sprintf("%d,", n.Val)
		n = n.Next
	}
	return res
}

func build(nums ...int) *ListNode {
	var head *ListNode
	tmp := head
	for _, n := range nums {
		if tmp == nil {
			tmp = &ListNode{
				Val: n,
			}
			head = tmp
			continue
		}
		tmp.Next = &ListNode{
			Val: n,
		}
		tmp = tmp.Next
	}
	return head
}

func main() {
	cases := []struct {
		head *ListNode
		x    int
		res  string
	}{
		{
			head: build(4, 3, 2, 5, 2),
			x:    3,
			res:  "2,2,4,3,5,",
		},
		{
			head: build(2, 1),
			x:    2,
			res:  "1,2,",
		},
		{
			head: build(1, 4, 3, 2, 5, 2),
			x:    3,
			res:  "1,2,2,4,3,5,",
		},
		{
			head: build(3, 4, 5, 6, 1),
			x:    3,
			res:  "1,3,4,5,6,",
		},
		{
			head: build(1),
			x:    3,
			res:  "1,",
		},
	}
	for _, c := range cases {
		log.Printf("list: %+v, x: %d, res: %s", c.head, c.x, c.res)
		if res := partition(c.head, c.x); res.String() != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res.String())
		}
	}
}
