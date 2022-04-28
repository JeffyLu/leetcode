package main

import (
	"fmt"
	"log"
)

func deleteDuplicates(head *ListNode) *ListNode {
	tmp := head
	head = nil
	var tail *ListNode
	for tmp != nil {
		drop := false
		next := tmp.Next
		for ; next != nil; next = next.Next {
			if next.Val != tmp.Val {
				break
			}
			drop = true
		}
		if !drop {
			if tail == nil {
				tail = tmp
				head = tail
			} else {
				tail.Next = tmp
				tail = tail.Next
			}
			tail.Next = nil
		}
		tmp = next
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
		res  string
	}{
		{
			head: build(1, 1, 2, 3, 3),
			res:  "2,",
		},
		{
			head: build(1, 2, 3, 3, 4, 4, 5),
			res:  "1,2,5,",
		},
		{
			head: build(1, 1, 1, 2, 3),
			res:  "2,3,",
		},
		{
			head: build(),
			res:  "",
		},
		{
			head: build(1),
			res:  "1,",
		},
		{
			head: build(1, 1),
			res:  "",
		},
	}
	for _, c := range cases {
		log.Printf("list: %+v, res: %s", c.head, c.res)
		if res := deleteDuplicates(c.head); res.String() != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res.String())
		}
	}
}
