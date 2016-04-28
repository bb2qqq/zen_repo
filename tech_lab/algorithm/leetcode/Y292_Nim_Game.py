# coding: utf-8
"""
Link: https://leetcode.com/problems/nim-game/

Description:
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

"""

# 在题设里规定每局最多能拿3个，我们可以把这个概念抽象至最多能拿x个。
# 那么如果你能把恰好x+1个stone留给对手拿，你就能获得比赛的胜利。
# 你要如何将x+1个stone留给对手呢？
# 在你的回合，你可以拿1个，或者x个stone来达到这个效果；
# 同时，在对手的上一回合，他是不能够留下x+1个stone的局面给你的
# 那么在对手的上一回合，留给他的必然是2x+2个stone
# 再往上一个回合推，留给对手的必然是3x+3个stone
# 所以，到你的回合，你拿完之后，如果留给对手的stone数是N * (x+1)，你就赢了
# 如果你不能给对手留下这个数目的stone，你就输了。这种情况只有一种，对手已经给你留下了N * (x + 1)数目的stone.
# 因为你每回合只能拿x个石头，所以你没办法将 N * (x + 1) 变成另一个 (x + 1)与某个数的的乘积和，根据我们之前的推断，you lose.

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool

        60 / 60 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        """
        ability = 3
        will_lose = (n % (ability + 1) == 0)
        will_win = not will_lose
        return will_win
