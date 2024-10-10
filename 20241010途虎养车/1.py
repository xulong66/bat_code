def reverse_words(s: str) -> str:
    # 将字符串按空格分隔为单词列表
    words = s.split()
    # 翻转每个单词
    reversed_words = [word[::-1] for word in words]
    # 用空格重新拼接这些单词
    return ' '.join(reversed_words)

# 获取用户输入
input_str = input()
# 调用函数并输出结果
output_str = reverse_words(input_str)
print( output_str)
