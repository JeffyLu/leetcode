package main

import (
	"fmt"
	"log"
)

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

func build(n int) *ListNode {
	if n <= 0 {
		return nil
	}

	head := &ListNode{
		Val: 1,
	}
	tmp := head
	for i := 2; i <= n; i++ {
		tmp.Next = &ListNode{
			Val: i,
		}
		tmp = tmp.Next
	}
	tmp.Next = nil
	return head
}

func main() {
	cases := []struct {
		head *ListNode
		k    int
		res  string
	}{
		{build(5), 0, "1,2,3,4,5,"},
		{build(5), 1, "5,1,2,3,4,"},
		{build(5), 2, "4,5,1,2,3,"},
		{build(3), 4, "3,1,2,"},
		{build(3), 3, "1,2,3,"},
		{build(0), 0, ""},
	}
	for _, c := range cases {
		log.Printf("list: %+v, k: %d, res: %s", c.head, c.k, c.res)
		if res := rotateRight(c.head, c.k).String(); res != c.res {
			log.Fatalf("expect: %s, got: %s", c.res, res)
		}
	}
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}

	var length int
	tail := head
	for {
		length++
		if tail.Next == nil {
			break
		}
		tail = tail.Next
	}
	k = k % length
	if k == 0 {
		return head
	}

	tail.Next = head
	for i := 0; i < length-k-1; i++ {
		head = head.Next
	}
	newHead := head.Next
	head.Next = nil
	return newHead
}
