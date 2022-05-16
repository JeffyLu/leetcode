package main

import (
	"fmt"
	"log"
)

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	tmp := head
	i := 0
	var leftOfSubHead *ListNode
	var subHead *ListNode
	for ; i < left; i++ {
		leftOfSubHead = subHead
		if tmp == nil || tmp.Next == nil {
			return head
		}
		subHead = tmp
		tmp = tmp.Next
	}

	subTail := subHead
	subHead.Next = nil
	for ; i < right; i++ {
		n := tmp.Next
		tmp.Next = subHead
		subHead = tmp
		tmp = n
	}

	if leftOfSubHead == nil {
		head = subHead
	} else {
		leftOfSubHead.Next = subHead
	}
	subTail.Next = tmp
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
		head  *ListNode
		left  int
		right int
		res   string
	}{
		{
			head:  build(1, 2, 2, 3, 4, 5),
			left:  2,
			right: 4,
			res:   "1,3,2,2,4,5,",
		},
		{
			head:  build(1, 2, 3, 4, 5),
			left:  2,
			right: 4,
			res:   "1,4,3,2,5,",
		},
		{
			head:  build(5),
			left:  1,
			right: 1,
			res:   "5,",
		},
		{
			head:  build(1, 2, 3),
			left:  1,
			right: 3,
			res:   "3,2,1,",
		},
		{
			head:  build(1, 2, 3, 4),
			left:  3,
			right: 4,
			res:   "1,2,4,3,",
		},
	}
	for _, c := range cases {
		log.Printf("%+v", c)
		if res := reverseBetween(c.head, c.left, c.right); res.String() != c.res {
			log.Fatalf("expect: %+v, got: %+v", c.res, res.String())
		}
	}
}
