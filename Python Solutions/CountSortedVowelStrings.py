class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = 'aeiou'
        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        for j in range(5):
            dp[0][j] = 1
        
        for i in range(1, n+1):
            
            for j in range(5):
                
                for k in range(j+1):
                    dp[i][j] += dp[i-1][k]
        
        for i in dp: print(i)

        return sum(dp[n-1])