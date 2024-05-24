package main

func subsets(nums []int) [][]int {
    sets := make([][]int, 0)
    subset := make([]int, 0)

    var dfs func(i int)
    dfs = func(i int) {
        if i >= len(nums) {
			// make([]int, len(subset)) doesn't work because it fills with bs ex. [0,0,0]
			// make([]int, 0, len(subset)) means length=0 capacity=10
			// also don't forget spread! it's just called ellipsis in Go I guess? lame
            cpy := append(make([]int, 0, len(subset)), subset...)
            sets = append(sets, cpy)
            return
        }

        subset = append(subset, nums[i])
        dfs(i + 1)
        subset = subset[:len(subset)-1]
        dfs(i + 1)
    }

    dfs(0)
    return sets
}