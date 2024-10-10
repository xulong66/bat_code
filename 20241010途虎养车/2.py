def max_profit(funds):
    if not funds:
        return 0

    # 初始化最小价格为无穷大，最大利润为0
    min_price = float('inf')
    max_profit = 0

    # 遍历价格数组
    for price in funds:
        # 更新最低价格
        if price < min_price:
            min_price = price
        # 计算当前价格卖出时的利润，并更新最大利润
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# 示例输入
funds = list(map(int, input("请输入基金价格数组，用逗号分隔：").split(',')))
# 输出最大利润
print("最大利润为：", max_profit(funds))
