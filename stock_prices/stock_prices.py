#!/usr/bin/python

import argparse

# takes list of stock prices
# Find max profit from single buy and sell
# buy first before selling
# find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530 - 3800 minus 270
# find maximum difference between the smallest and largest prices in the list
# max profit is computed by subtracting highest price by lowest price that comes _before_ the highest.
# Keep track of `current_min_price_so_far` and `max_profit_so_far` ? ?

# for i in range(len(prices)):
#   if current_min_price > prices[i]:
#     current_min_price = prices[i]
#     for j in range(i + 1, len(prices)):
#       if current_min_price < prices[j]:
#         max_num = prices[j]
#       if max_num - current_min_price > max_profit:
#         max_profit = max_num - current_min_price

# First solution above, passes test but not certain custom input.


def find_max_profit(prices):
    current_min_price = prices[0]
    max_profit = prices[1] - current_min_price

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
