// 143. Reorder List

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	// tortoise hare to find mid
	slow, fast := head, head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// reverse the second half of the list
	second := slow.Next
	var prev *ListNode = nil
	slow.Next = nil
	for second != nil {
		next := second.Next
		second.Next = prev
		prev = second
		second = next
	}

	// second is nil, so set to prev
	first, second := head, prev
	// first is the head, prev is the tail
	// link first to the second as it moves backwards along the second half
	// link second to the next first as it moves forwards along the first half
	for second != nil {
		ft, st := first.Next, second.Next
		first.Next = second
		// second needs to be one ahead because head stays same
		second.Next = ft
		first, second = ft, st
	}
}
