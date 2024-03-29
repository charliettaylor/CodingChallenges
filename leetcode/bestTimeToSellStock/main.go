// 121. Best Time to Buy and Sell Stock

package main

func maxProfit(prices []int) int {
	b := 0
	s := 1
	big := 0

	// until right ptr hits the end
	for s < len(prices) {
		// if we're going to make profit
		if prices[b] < prices[s] {
			// check if it's the max
			big = max(prices[s]-prices[b], big)
		} else {
			// move left ptr fwd
			b = s
		}
		// always advance right ptr
		s++
	}

	return big
}
