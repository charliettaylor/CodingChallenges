// 67. Add Binary
package main

func addBinary(a, b string) string {
	if len(a) < len(b) {
		a, b = b, a
	}

	indexB := len(b) - 1
	result := make([]byte, len(a))
	var shifter, sum byte
	for i := len(a) - 1; i >= 0; i-- {
		sum = shifter + a[i]
		if indexB >= 0 {
			sum += b[indexB]
			indexB--
		}

		result[i] = sum%2 + '0'
		shifter = sum >> 1 % 2
	}

	if shifter == 0 {
		return string(result)
	}

	return "1" + string(result)
}
