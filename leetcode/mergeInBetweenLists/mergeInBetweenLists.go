// 1669. Merge In Between Linked Lists
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	list1 := &ListNode{10, &ListNode{1, &ListNode{13, &ListNode{6, &ListNode{9, &ListNode{5, nil}}}}}}
	list2 := &ListNode{1000000, &ListNode{1000001, &ListNode{1000002, nil}}}

	head := mergeInBetween(list1, 3, 4, list2)

	for head != nil {
		fmt.Println(head)
		head = head.Next
	}
}

func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
	var list3 *ListNode
	var head *ListNode

	for i := 0; list1 != nil; i++ {
		if i == a {
			list3.Next = list2
			for list3.Next != nil {
				list3 = list3.Next
			}
		}

		if i >= a && i <= b {
			list1 = list1.Next
			continue
		}

		if list1 != nil {
			if list3 == nil {
				list3 = &ListNode{list1.Val, nil}
				head = list3
			} else {
				list3.Next = &ListNode{list1.Val, nil}
				list3 = list3.Next
			}
		}

		fmt.Println(list1)
		fmt.Println(i)
		fmt.Println(list3)
		fmt.Println("-----")

		list1 = list1.Next
	}

	return head
}
