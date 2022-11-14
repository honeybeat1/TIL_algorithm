def solution(cost, x):
    print(len(cost), x)
    if min(cost) > x:
        return 0
    result = []
    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum < x:
            lst = []
            for i in path:
                lst.append(2**i)
            result.append(sum(lst))
        for i in range(index, len(cost)):
            dfs(csum-cost[i], i+1, path+[i])

    dfs(x, int(len(cost)/2), [])
    
    return max(result)%(10**9+7)
