# 1000미만의 3의 배수와 5의 배수 숫자들의 합

result = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)