n = int(input())

# بالای لوزی
for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + 1))

# وسط لوزی
print("*" * (2 * n + 1))

# پایین لوزی
for i in range(n - 1, -1, -1):
    print(" " * (n - i ) + "*" * (2 * i + 1))
