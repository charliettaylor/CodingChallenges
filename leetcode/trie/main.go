package main

type Trie struct {
	children map[rune]*Trie
	isEnd    bool
}

func Constructor() Trie {
	return Trie{make(map[rune]*Trie, 0), false}
}

func (this *Trie) Insert(word string) {
	for _, char := range word {
		if this.children[char] == nil {
			node := Constructor()
			this.children[char] = &node
		}
		this = this.children[char]
	}

	this.isEnd = true
}

func (this *Trie) Search(word string) bool {
	for _, char := range word {
		if this.children[char] == nil {
			return false
		}
		this = this.children[char]
	}

	return this.isEnd
}

func (this *Trie) StartsWith(prefix string) bool {
	for _, char := range prefix {
		if this.children[char] == nil {
			return false
		}
		this = this.children[char]
	}

	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
