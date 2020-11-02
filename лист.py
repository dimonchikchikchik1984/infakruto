from random import randint
a = []
n = int(input())
for i in range(n):
    a.append(randint(0, 1991))

for i in a:
    a[0] = 6

print(a)
print('Возможно')
