from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        # 统计迷宫中所有字母的数量
        board_counts = Counter()
        for row in board:
            board_counts.update(row)

        # 统计目标单词中每个字母的数量
        word_counts = Counter(word)

        # 神技一：频率核对(验资)
        # 如果单词里某个字母的需求量，超过了迷宫里的存货量，直接判死刑
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        # 神技二：捏软柿子 (首尾反转优化)
        # 如果单词首字母在迷宫里泛滥，而尾字母很稀缺，就把单词倒过来找！
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]


        def dfs(row,column,i):
            # 如果已经匹配完整个 word，说明成功
            if i == len(word):
                return True

            # 越界，失败
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return False

            # 当前格子已经用过，失败
            if board[row][column] == "#":
                return False

            # 当前字符不匹配，失败
            if board[row][column] != word[i]:
                return False


            # 标记当前格子已使用
            temp = board[row][column]
            board[row][column] = "#"

            found = (
                dfs(row - 1, column, i + 1) or
                dfs(row + 1, column, i + 1) or
                dfs(row, column - 1, i + 1) or
                dfs(row, column + 1, i + 1)
            )

            # 恢复当前格子，给其他路径使用
            board[row][column] = temp

            return found

        # 从每一个格子作为起点尝试
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == word[0] and dfs(row, column, 0):
                    return True

        return False

# 统计字符串里每个字母的次数
# c1 = Counter("apple")
# print(c1)
# 输出: Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})

# 统计列表里每个元素的次数
# c2 = Counter(['张三', '李四', '张三', '王五'])
# print(c2)
# 输出: Counter({'张三': 2, '李四': 1, '王五': 1})

# c = Counter("apple")
# print(c['p'])  # 输出: 2
# print(c['z'])  # 输出: 0  (不会报错！这在算法里省去了大量的 if 判断)

# c = Counter("apple")      # 现在 p 有 2 个
# c.update("pineapple")     # 又来了 3 个 p
# print(c['p'])             # 输出: 5

# c1 = Counter("aab")
# c2 = Counter("a")
# # 减法：把 c1 里减去 c2 的字母数量
# print(c1 - c2)
# 输出: Counter({'a': 1, 'b': 1})

# c = Counter("abracadabra")
# # 找出出现次数最多的前 2 个元素
# print(c.most_common(2))
# 输出: [('a', 5), ('r', 2)]  （返回的是一个排好序的元组列表）












