n = int(input())
v =[]
b = input()
v = b.split()
for i in range(n):
    v[i] = int(v[i])

print(max(v))