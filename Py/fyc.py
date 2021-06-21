x = '123'
print(*map(int, x))
print(list(map(int, x)))
print(*filter(lambda x: x != 1, map(int, x)))

print("三目运算符") if not x else print("注意结构")
