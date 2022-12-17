pile1 = [1, 2, 3, 4, 5]
pile2 = [6, 7, 8, 9]


print(pile1)
print(pile2)
print("")

# pile2.append(pile1.pop())

print(pile1[-4:])

pile2.extend(pile1[-4:])
# del(pile1[-4:])

print(pile1)
print(pile2)