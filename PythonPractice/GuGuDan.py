# 1 GuGuDan

print('몇 단을 출력하시겠습니까? ')
n = int(input())

ans = []

for i in range(1, 10):
    ans.append(n * i)

print(ans)