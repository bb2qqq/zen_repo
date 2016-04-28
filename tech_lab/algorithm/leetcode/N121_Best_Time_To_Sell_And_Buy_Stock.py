# coding: utf-8
"""

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


Description:
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

# 如果我没理解错的话，这道题是说，在历史股价出来后，一个人在历史上买入和卖出一股股票能获得的最大收益。
# 我们的算法要求的是历史最大差值。
# 最简单的方法是遍历，但是，有没有复杂度比遍历更低的算法呢？
# 先遍历好了，娘腿，再去看别人有没有更聪明的解法
# 2016-04-11 18:09

# 遍历的方法被否决了，那看来有更好的方法
# 遍历的方法，复杂度是 n**2
# 看起来在遍历的时候，可以储存一些差值信息。
# 问题的关键是：前一天的参考信息，对于后一天的遍历有什么意义！
# 我找到钥匙了！
# Oh yeah.
# 后一天的价格对比，将后一天的价格作为基础价格进行对比。
# 1. 如果后一天的价格高于前一天的价格，那么后一天的最高价格差一定小于前一天的最高价格差。
# 2. 如果后一天的价格低于前一天的价格，那么后一天的最高价格差一定高于于前一天的最高价格差。
# 但我们要考虑到，前一天和后一天的价格差这一特殊对比
# 当出现情况1的时候，我们什么也不做，直接去看下一天的情况。
# 如果出现情况2，我们则将后一天的最高价格差与 （前一天和后一天的价格差）进行比较，取其大者储存起来。
# 如此遍历到最后一天，则可得出结果
# 2016-04-12 10:21

# 上面的思路也不行, 当价格是递减序列的情况下，算法复杂度依然是n**n
# 但是，我忽然醍醐灌顶，想到了可以计算每个两天之间的差价，然后根据这个差价的序列来做点文章？
# 仔细想了下，好像也不行。。
class Solution(object):
    def maxProfit(self, prices):
        """
        """

class SolutionFailed_3(object):
    """此种方法，在价格是一个递减序列的情况下，算法复杂度依然是n**n"""
    def maxProfit(self, prices):
        """
        """
        current_top_index = 0
        current_top_price = 0
        top_profit = -float('inf')
        for price_index, price in enumerate(prices):
            # 此价格的日期在最高价格日期之后，需要刷新最高价格日期
            if price_index >= current_top_index:
                top_price, top_price_index = self.find_top_price(prices[price_index:])
                current_top_index = price_index + top_price_index
            # 此价格的日期在最高价格之前
            profit = top_price - price
            if profit > top_profit:
                top_profit = profit
        return top_profit


    def find_top_price(self, price_sequence):
        top_price = max(price_sequence)
        top_price_index = price_sequence.index(top_price)
        return top_price, top_price_index

class SolutionFailed_2(object):
    def maxProfit(self, prices):
        """
        价格有可能会遍历通过topPrice, 比如对于第一天的价格而言，最高价格出现在第10天，但是对于第11天的价格而言，第10天的价格就没什么意义了。
        """
        best_profit = 0
        previous_price = prices[0]
        initialized = False
        top_price = 0
        for index, price in enumerate(prices):
            # 第一次比较的时候遍历所有天数
            if not initialized:
                for sequence_price in prices[index+1 : -1]:
                    profit = sequence_price - price
                    if profit > best_profit:
                        best_profit = profit
                        top_price = sequence_price
            if price >= previous_price:
                continue
            else:
                new_profit = top_price - price
                yesterday_to_today_profit = price - prices[index-1]
                best_profit = max([new_profit, yesterday_to_today_profit])

        print top_price

        return best_profit


class SolutionFailed_1(object):
    """复杂度太高，失败了。"""
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_profit = 0
        for index, i in enumerate(prices):
            for j in prices[index+1 : -1]:
                profit = j - i
                print profit
                if profit > best_profit:
                    best_profit = profit
        return best_profit
