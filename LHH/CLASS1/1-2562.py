result = []
max=0
for i in range(9):
    line = input()
    result.append(line)
result = list(map(int, result))
for i in result:
    if max < i:
        max=i
print(max)
position=result.index(max)
print(position+1)