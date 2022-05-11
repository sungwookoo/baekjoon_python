x, y, w, h = map(int,input().split())
result = []
result.append(w-x)
result.append(h-y)
result.append(x)
result.append(y)

print(min(result))