lines: [str] = []

with open('in.txt') as f:
    lines = f.readlines()

cumsum = 0

for line in lines:
    first, last = "", ""
    for i in range(len(line)):
        if line[i].isnumeric() and first == "":
            first = line[i]
        
        if line[len(line) - i - 1].isnumeric() and last == "":
            last = line[len(line) - i - 1]

    cumsum += int(first + last)

print(cumsum)