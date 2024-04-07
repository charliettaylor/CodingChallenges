// 74. Search a 2D Matrix

package main

func searchMatrix(matrix [][]int, target int) bool {
	var list []int
	if len(matrix) == 1 {
		list = matrix[0]
	} else {
		rowL, rowR := 0, len(matrix)-1
		for rowR >= rowL {
			mid := (rowR + rowL) >> 1
			row := matrix[mid]
			if row[0] <= target && row[len(row)-1] >= target {
				list = matrix[mid]
				break
			} else if matrix[mid][0] > target {
				rowR = mid - 1
			} else {
				rowL = mid + 1
			}
		}
	}

	if list == nil {
		return false
	}

	l, r := 0, len(list)-1
	for r >= l {
		mid := (l + r) >> 1
		if list[mid] == target {
			return true
		} else if list[mid] > target {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return false
}
