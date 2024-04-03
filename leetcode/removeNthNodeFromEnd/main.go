package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if head.Next == nil {
		return nil
	}

	h := head
	length := 0

	for head != nil {
		head = head.Next
		length++
	}

	if n == length {
		return h.Next
	}

	head = h
	prev := head
	for i := 0; i < length-n; i++ {
		prev = head
		head = head.Next
	}
	prev.Next = head.Next

	return h
}
