# 318. Maximum Product of Word Lengths


def maxProduct(words: list[str]) -> int:
    uniques = []
    for word in words:
        temp = set()
        for char in word:
            temp.add(char)
        uniques.append(temp)

    max_prod = 0
    for i in range(len(words) - 1):
        for j in range(1, len(words)):
            if uniques[i].isdisjoint(uniques[j]):
                curr = len(words[i]) * len(words[j])
                if curr > max_prod:
                    max_prod = curr

    return max_prod


if __name__ == "__main__":
    print(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
