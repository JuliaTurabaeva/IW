import math
n = int(input("Введите n: "))
sum = 0
for i in range(1,n+1,1):
  localsum = 0
  for j in range(1,i+1,1):
      localsum = localsum + math.sin(j)
  sum = sum + 1/localsum
print(sum)


x = float(input("Введите x: "))
n = int(input("Введите n: "))
result = x
for i in range(1,n**2+1,1):
  result = result * (x - i*n)
print(result)



x = float(input("Введите x: "))
n = int(input("Введите n: "))
sum = 1/x
for i in range(1,n+1,1):
  localresult = 1
  for j in range(1,i+1,1):
      localresult = localresult * (x + j)
  sum = sum + 1/localresult
print(sum)



x = float(input("Введите x: "))
n = int(input("Введите n: "))
sum = 0
for i in range(1,n+1,1):
  factorial = 1
  for j in range(1,i+1,1):
    factorial = factorial * j
  sum = sum + (x**i)/factorial
print(sum)



