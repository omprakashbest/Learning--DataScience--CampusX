"""
-> Best Team with No Conflicts 

You are teh manager of a basketball team. For the upcoming tournament, you want to choose the team with the 
highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts.  conflict exist if a younger player has a strictly
higher score than an older player. A conflict does nt occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, 
respectively, return the highest overall score of all possible basketball teams.

"""

class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int])-> int:
        pairs = sorted(zip(scores, ages))
        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            mScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if mAge >= age:
                    dp[i] = max(dp[i], mScore + dp[j])
        return max(dp)

obj = Solution()
scores, ages = [1,3,5,10,15], [1,2,3,4,5]
print(obj.bestTeamScore(scores, ages))