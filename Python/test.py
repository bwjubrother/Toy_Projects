def solution(n, costs):
    answer = 0
    # sorted(costs, key = lambda x : x[2])
    costs.sort(key = lambda x : x[2])
    routes = {costs[0][0]}
    for cost in costs:
        print(cost)
        if cost[0] in routes or cost[1] in routes:
            if cost[0] in routes and cost[1] in routes:
                continue
            else:
                routes.add(cost[0])
                routes.add(cost[1])
                answer += cost[2]
        if len(routes) == n:
            break
    return answer


def solution2(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) 
    routes = set([costs[0][0]]) 
    while len(routes)!=n:
        for cost in costs:
            print(cost)
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                break
        print(routes)
    return ans


print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))
print(solution2(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))