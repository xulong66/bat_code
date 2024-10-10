from typing import List

class Solution:
    def bpm(self, u, matchR, seen, bpGraph):
        # 尝试为用户 u 匹配工厂店
        for v in range(len(bpGraph[0])):
            if bpGraph[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen, bpGraph):
                    matchR[v] = u
                    return True
        return False

    def washCount(self, g: List[List[int]]) -> int:
        # 初始化工厂店的匹配情况
        matchR = [-1] * len(g[0])
        result = 0
        for i in range(len(g)):
            # 标记该用户尝试访问过的工厂店
            seen = [False] * len(g[0])
            # 尝试为用户 i 匹配工厂店
            if self.bpm(i, matchR, seen, g):
                result += 1
        return result

# 示例输入
g = [[1, 0, 0], [0, 1, 1], [1, 0, 1]]

# 创建Solution对象并调用washCount方法
solution = Solution()
print("最大可匹配的用户数为：", solution.washCount(g))
