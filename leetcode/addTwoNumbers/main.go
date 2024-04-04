// 2. Add Two Numbers

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	head := &ListNode{0, nil}
	h := head
	for l1 != nil && l2 != nil {
		curr := l1.Val + l2.Val + carry
		head.Val = curr % 10
		carry = curr / 10
		head.Next = &ListNode{0, nil}
		head = head.Next
		l1 = l1.Next
		l2 = l2.Next
	}

	chain := func(list *ListNode) *ListNode {
		curr := list.Val + carry
		head.Val = curr % 10
		carry = curr / 10
		head.Next = &ListNode{0, nil}
		head = head.Next
		return list.Next
	}

	for l1 != nil {
		l1 = chain(l1)
	}

	for l2 != nil {
		l2 = chain(l2)
	}

	// get second to last node
	head = h
	for head.Next.Next != nil {
		head = head.Next
	}

	// make the last node carry, if not snip
	if carry != 0 {
		head.Next.Val = carry
	} else {
		head.Next = nil
	}

	return h
}
