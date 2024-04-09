// 2073. Time Needed to Buy Tickets

package main

func timeRequiredToBuy(tickets []int, k int) int {
	total := 0
	for i := range len(tickets) {
		if i <= k {
			total += min(tickets[k], tickets[i])
		} else {
			total += min(tickets[k]-1, tickets[i])
		}
	}

	return total
}
