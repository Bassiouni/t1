my_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20,
           'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

d: dict = {}

for x in my_dict.values():
  if x in d:
    d[x] += 1
  else:
    d[x] = 1

print(d)
