# https://open.kattis.com/problems/recipes

for i in range(int(input())):
  values = input().split()
  r, p, d = [int(x) for x in values]
  ingredients = []
  for j in range(r):
    name, weight, percentage = input().split()
    ingredients.append([name, float(weight), float(percentage)])
  
  base = next(filter(lambda x: x[2]  == 100.0, ingredients))

  ratio = d / p
  baseW = base[1] * ratio

  for j in range(len(ingredients)):
    ingredients[j][1] = baseW * (ingredients[j][2] / 100.0)

  print(f"Recipe # {i + 1}")
  for j in ingredients:
    print(f"{j[0]} {j[1]:.1f}")
  print("----------------------------------------")
