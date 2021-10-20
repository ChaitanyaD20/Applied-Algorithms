class EditDistance:
	def editDistance(self,word1, word2):
		len1=len(word1)
		len2=len(word2)
		dp = [[0 for x in range(len2 + 1)] for x in range(len1 + 1)]

		for i in range(len1 + 1):
			for j in range(len2 + 1):
				if i == 0:				#If word1 is empty, then fill in all values of word2 into word1.
					dp[i][j] = j
				elif j == 0:			#If word2 is empty, then remove all values from word1.
					dp[i][j] = i
				elif word1[i-1] == word2[j-1]:		#If the last values of word1 and word2 are the same, recur from the second-last value.
					dp[i][j] = dp[i-1][j-1]
				else:								#If the last values of word1 and word2 are different, find the minimum value of the 3 options: Insertion, Deletion and Substitution of characters.	
					dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j], dp[i-1][j-1])
		return dp[len1][len2]
