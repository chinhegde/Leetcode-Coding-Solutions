# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        players = list(range(1, n+1))
        start = 0

        while len(players) != 1:
            l = (start + k - 1)%len(players)
            players.pop(l)
            start = l
        
        return players[0]