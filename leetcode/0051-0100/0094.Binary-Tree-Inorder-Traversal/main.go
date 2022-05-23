package main

import (
	"fmt"
	"log"
)

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	res := append(inorderTraversal(root.Left), root.Val)
	return append(res, inorderTraversal(root.Right)...)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (n *TreeNode) String() string {
	if n == nil {
		return ""
	}

	var res string
	if n.Left != nil {
		res += n.Left.String()
	}
	res += fmt.Sprintf("%d,", n.Val)
	if n.Right != nil {
		res += n.Right.String()
	}
	return res
}

func build(nums ...int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	root := &TreeNode{
		Val: nums[0],
	}
	tmp := []*TreeNode{
		root,
	}
	for i := 1; i < len(nums); i++ {
		node := tmp[0]
		if i%2 == 0 {
			tmp = tmp[1:]
		}

		if nums[i] <= 0 {
			continue
		}

		n := &TreeNode{
			Val: nums[i],
		}
		tmp = append(tmp, n)
		if i%2 == 1 {
			node.Left = n
		} else {
			node.Right = n
		}
	}
	return root
}

func main() {
	cases := []struct {
		root *TreeNode
		res  []int
	}{
		{
			root: build(1, 0, 2, 3),
			res:  []int{1, 3, 2},
		},
		{
			root: build(),
			res:  []int{},
		},
		{
			root: build(1),
			res:  []int{1},
		},
	}
	for _, c := range cases {
		log.Printf("tree: %s, res: %+v", c.root.String(), c.res)
		res := inorderTraversal(c.root)
		if len(res) != len(c.res) {
			log.Fatalf("expect: %+v, got: %+v", c.res, res)
		}
		for i := 0; i < len(res); i++ {
			if res[i] != c.res[i] {
				log.Fatalf("expect: %+v, got: %+v", c.res, res)
			}
		}
	}
}
