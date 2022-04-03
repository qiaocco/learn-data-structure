package main

/**
 * Definition for a binary tree node.
 */

// 参考：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/jian-dan-yi-dong-javac-pythonjs-er-cha-s-3vyq/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var stack []*TreeNode
	var res []int

	stack = append(stack, root)

	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		res = append(res, cur.Val)

		if cur.Right != nil {
			stack = append(stack, cur.Right)
		}
		if cur.Left != nil {
			stack = append(stack, cur.Left)
		}
	}
	return res
}
