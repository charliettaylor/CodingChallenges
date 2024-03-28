package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{Val: 0, Next: nil}
	og := head
	for list1 != nil {
		if list2 == nil || list1.Val <= list2.Val {
			head.Next = list1
			list1 = list1.Next
		} else {
			head.Next = list2
			list2 = list2.Next
		}
		head = head.Next
	}

	for list2 != nil {
		head.Next = list2
		list2 = list2.Next
		head = head.Next
	}

	return og.Next
}
