def bpm(u, matchR, seen, bpGraph):
    # 尝试为用户 u 匹配工厂店
    for v in range(len(bpGraph[0])):
        if bpGraph[u][v] and not seen[v]:
            seen[v] = True
            if matchR[v] == -1 or bpm(matchR[v], matchR, seen, bpGraph):
                matchR[v] = u
                return True
    return False

def maxBPM(bpGraph):
    # bpGraph[i][j] == 1 表示用户 i 能接受工厂店 j 的服务
    matchR = [-1] * len(bpGraph[0])
    result = 0
    for i in range(len(bpGraph)):
        seen = [False] * len(bpGraph[0])
        if bpm(i, matchR, seen, bpGraph):
            result += 1
    return result

# 示例输入
bpGraph = [[1, 0, 0], [0, 1, 1], [1, 0, 1]]
print("最大可匹配的用户数为：", maxBPM(bpGraph))
