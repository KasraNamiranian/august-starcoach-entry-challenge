def sum_of_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum
input_str = input()
m , s = map(int, input_str.split())
matrix = []
t=1
for i in range (m):
    t=t*10
l = t//10
for j in range(l,t+1):
    if sum_of_digits(j) == s:
        matrix.append(j)
if not matrix:
    print(-1,-1)
else:
    max_matrix = max(matrix)
    min_matrix = min(matrix)
    print(min_matrix,max_matrix)