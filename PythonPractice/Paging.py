# m개의 게시물을 n개씩 보여준다면 몇 페이지가 필요한가


def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1


print(getTotalPage(30, 10))