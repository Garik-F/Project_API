num1 = set(input())
num2 = set(input())
if len(num1.union(num2)) != len(list(num1) + list(num2)):
    print("YES")
else:
    print("NO")
