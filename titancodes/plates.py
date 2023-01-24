with open('plates.txt') as f:
  plates = [x.strip() for x in f.readlines()]

for line in plates:
  # print(line)
  if len(line) == 7 and line[0].isdigit() and line[1:4].isalpha() and line[4:].isdigit():
    print('T', end='')
  else:
    print('F', end='')



#DLLLDDD