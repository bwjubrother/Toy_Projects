'''
def solution(info, query):
    answer = []
    infos = []
    # 언어 직무 경력 음식 점수
    for inf in info:
        infos.append(inf.split(' '))
    for que in query:
        tmp = []
        cnt = 0
        for q in que.split(' '):
            if q != 'and' and q != '-':
                tmp.append(q)
        score = int(tmp.pop(-1))
        for inf in infos:
            if len(set(tmp) - set(inf)) == 0 and int(inf[-1]) >= score:
                cnt += 1
        answer.append(cnt)
    return answer
'''

from itertools import combinations
from collections import defaultdict


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for comb in combinations(info_key, i):
                tmp = ''.join(comb)
                info_dict[tmp].append(info_val)

    for key in info_dict.keys():
        info_dict[key].sort()

    for que in queries:
        tmp = []
        for q in que.split(' '):
            if q != 'and' and q != '-':
                tmp.append(q)
        score = int(tmp.pop())
        q_key = ''.join(tmp)

        if q_key in info_dict:
            scores = info_dict[q_key]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while start < end:
                    mid = (start+end) // 2
                    if scores[mid] >= score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))