# 1528. Shuffle String


def restoreString(s: str, indices: list[int]) -> str:
  d = dict()
  for i in range(len(s)):
    # map index to char
    d[indices[i]] = s[i]

  return "".join(d[i] for i in range(len(s)))


if __name__ == "__main__":
  # Should output 'leetcode'
  print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
