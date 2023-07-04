class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        # Write your code here.
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        ans = count_paths(0, 0, n, m, dp)
        if m==1 and n==1:
            return ans
        return dp[0][0]

def count_paths(i, j, n, m, dp):
	if i==n-1 and j==m-1:
		return 1
	if i>=n or j>=m:
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	
	dp[i][j] = count_paths(i+1, j, n, m, dp) + count_paths(i, j+1, n, m, dp)
	return dp[i][j]