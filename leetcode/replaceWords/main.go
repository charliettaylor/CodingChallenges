package main

import (
	"strings"
)

func replaceWords(dictionary []string, sentence string) string {
	split := strings.Split(sentence, " ")

	for _, word := range dictionary {
		for i := range len(split) {
			curr := split[i]

			// make sure to not go past len of either
			maxCompLen := min(len(curr), len(word))
			if word == curr[:maxCompLen] {
				split[i] = word
			}
		}
	}

	return strings.Join(split, " ")
}
