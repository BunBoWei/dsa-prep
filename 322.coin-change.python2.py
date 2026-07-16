# @leet imports start
from bisect import *
from collections import *
from copy import *
from datetime import *
from heapq import *
from math import *
from re import *
from string import *
from random import *
from itertools import *
from functools import *
from operator import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import itertools
import functools
import operator
# @leet imports end

# @leet start
class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        self.min = 100000
        def backtrack(coins, sum, num_coins):
            if num_coins >= self.min:
                return 
            if sum == amount:
                self.min = num_coins
                return
            elif sum > amount:
                return

            for i in range(len(coins)):
                backtrack(coins, sum + coins[i], num_coins + 1)
            
            return self.min
        backtrack(coins, 0, 0)

        return self.min if self.min != 100000 else -1  


solution = Solution()
print(solution.coinChange([1,2,5], 100))
# print(solution.coinChange([2], 3))
# print(solution.coinChange([1], 0))
        
# @leet end
