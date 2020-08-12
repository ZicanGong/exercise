class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        if board[0][0] == word:
            return True

        def dfs(a,b,s,history):
            
            if a > 0:
                if board[a-1][b] == s[0] and (a-1,b) not in history:
                    if len(s) == 1:
                        return True
                    else:
                        if dfs(a-1,b,s[1:],history+[(a-1,b)]): return True
            if a < m-1:
                if board[a+1][b] == s[0] and (a+1,b) not in history:                   
                    if len(s) == 1:
                        return True
                    else:
                        if dfs(a+1,b,s[1:],history+[(a+1,b)]): return True
            if b > 0:
                if board[a][b-1] == s[0] and (a,b-1) not in history:                  
                    if len(s) == 1:
                        return True
                    else:
                        if dfs(a,b-1,s[1:],history+[(a,b-1)]): return True
            if b < n-1:
                if board[a][b+1] == s[0] and (a,b+1) not in history:
                    if len(s) == 1:
                        return True
                    else:
                        if dfs(a,b+1,s[1:],history+[(a,b+1)]): return True
            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    if not word[1:]:
                        return True
                    if dfs(i,j,word[1:],[(i,j)]): 
                        return True
        return False

# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
