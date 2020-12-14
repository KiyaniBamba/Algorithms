#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # create variable for max profit
  max_profit = prices[1] - prices[0]

  #  create a variable for the min price
  min_price = prices[0]

  #  for loop which loops in the range of 1 and the lenght of array/prices
  for i in range(1, len(prices)):
    # if max profit < current price - min_price
    if max_profit < prices[i] - min_price:
      # change the var max profit to current price - min price
      max_profit = prices[i] - min_price
    if min_price > prices[i]:
      min_price = prices[i]
      
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))