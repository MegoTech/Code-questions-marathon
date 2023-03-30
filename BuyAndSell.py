#this quistion is for the 29/03/2023 daily coding problem
#
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

def best_deal(prices: list) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] - prices[j] < max_profit:
                max_profit = (prices[i] - prices[j])
    return abs(max_profit)


