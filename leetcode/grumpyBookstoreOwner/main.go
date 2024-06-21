// 1052. Grumpy Bookstore Owner

package main

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	// total happy with tech starting at 0
	base := 0
	for i, cust := range customers {
		if grumpy[i] == 0 || i < minutes {
			base += cust
		}
	}

	best := base
	for i := 1; i+minutes-1 < len(customers); i++ {
		// if the thing we're passing was supposed to be grump
		// then we reduce total satisfied
		if grumpy[i-1] == 1 {
			base -= customers[i-1]
		}

		// if the thing we're coming toward is grump
		// reduce cuz it's now part of the tech
		if grumpy[i+minutes-1] == 1 {
			base += customers[i+minutes-1]
		}

		best = max(base, best)
	}

	return best
}
