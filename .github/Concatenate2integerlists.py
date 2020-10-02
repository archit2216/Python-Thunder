def concat(l1,l2):
  l1.extend(l2)

  return l1

l1=[int(x) for x in input()]
l2=[int(y) for y in input()]

print(concat(l1,l2))