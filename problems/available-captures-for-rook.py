# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/29 9:43
# 文件名：available-captures-for-rook.py
# 开发工具：PyCharm
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row, col = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    row = i
                    col = j
        i, j = row, col
        ans = 0
        while i >= 0:
            if board[i][j] == "B":
                break
            if board[i][j] == "p":
                ans += 1
                break
            i -= 1

        i, j = row, col
        while i < len(board):
            if board[i][j] == "B":
                break
            if board[i][j] == "p":
                ans += 1
                break
            i += 1

        i, j = row, col
        while j >= 0:
            if board[i][j] == "B":
                break
            if board[i][j] == "p":
                ans += 1
                break
            j -= 1

        i, j = row, col
        while j < len(board[0]):
            if board[i][j] == "B":
                break
            if board[i][j] == "p":
                ans += 1
                break
            j += 1

        return ans

test = Solution()
print(test.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
))
