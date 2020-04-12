# def maxProfit(prices):
#     sell = []
#     buy = []
#     if len(prices) == 1:
#         return 0
#     for i in range(len(prices)):
#         if i == 0:
#             if prices[i] <= prices[i + 1]:
#                 buy.append(prices[i])
#
#         if 0 < i < len(prices) - 1:
#             if prices[i] >= prices[i - 1] and prices[i] > prices[i + 1]:
#                 sell.append(prices[i])
#             if prices[i] < prices[i - 1] and prices[i] <= prices[i + 1]:
#                 buy.append(prices[i])
#
#         if i == len(prices) - 1:
#             if prices[i] >= prices[i - 1]:
#                 sell.append(prices[i])
#
#     profit = 0
#     for i in range(len(sell)):
#         profit += sell[i] - buy[i]
#     return profit


# money = [7, 1, 5, 3, 6, 4]
# print(maxProfit(money))

# money = [1,2,3,4,5]
# print(maxProfit(money))

# def maxProfit(prices):
#     profit = 0
#     if len(prices) == 1:
#         return 0
#     for i in range(len(prices)):
#         if i == 0:
#             if prices[i] <= prices[i + 1]:
#                 profit -= prices[i]
#
#         if 0 < i < len(prices) - 1:
#             if prices[i] >= prices[i - 1] and prices[i] > prices[i + 1]:
#                 profit += prices[i]  # sell
#             if prices[i] < prices[i - 1] and prices[i] <= prices[i + 1]:
#                 profit -= prices[i]  # buy
#
#         if i == len(prices) - 1:
#             if prices[i] >= prices[i - 1]:
#                 profit += prices[i]
#
#     return profit

# def maxProfit(prices):
#     profit = 0
#     for i in range(1, len(prices)):
#         if prices[i] - prices[i - 1] > 0:
#             profit += prices[i] - prices[i - 1]
#     return profit


def maxProfit(prices):
    max = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[i-1]
        if profit > 0:
            max += profit
    return max

# python 3.8 特性
# def maxProfit(prices):
#     max = 0
#     for i in range(1, len(prices)):
#         if profit := prices[i] - prices[i-1] > 0:
#             max += profit
#     return max

money = [7,1,5,3,6,4]
print(maxProfit(money))

money = [1,2,3,4,5]
print(maxProfit(money))

money =  [7,6,4,3,1]
print(maxProfit(money))

money = [1]
print(maxProfit(money))

money = [3,3,5,0,0,3,1,4]
print(maxProfit(money))

money = [8,6,4,3,3,2,3,5,8,3,8,2,6]
print(maxProfit(money))