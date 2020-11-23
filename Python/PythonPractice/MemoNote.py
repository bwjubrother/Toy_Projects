# 메모를 추가하고 조회하는 프로그램
# python MemoNote.py -a "asdf"

import sys

option = sys.argv[1]  # -a, -v

if option == '-a':
    memo = sys.argv[2]  # content
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
