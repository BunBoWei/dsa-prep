# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Create a DP array, size 'amount + 1'
        # Initialize with a "max" value (amount + 1 is a safe "infinity"
        # since we can never use more than 'amount' coins of value 1)
        dp = [amount + 1] * (amount + 1)
        
        # 2. Base Case: 0 coins are needed to make amount 0
        dp[0] = 0
        
        # 3. Build the DP array from 1 up to amount
        for a in range(1, amount + 1):
            # 4. For each amount 'a', check every coin
            for c in coins:
                if c <= a:
                    # The core logic:
                    # Is it better to use the current coin 'c'?
                    # If so, the cost is 1 (for coin 'c') + dp[a - c]
                    # (the min coins needed for the remaining amount).
                    print("A",a)
                    print("C",c)
                    print("AC",a - c)
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    print(dp)
                   
        # 5. Final check:
        # If dp[amount] is still our "infinity" value, it was never updated,
        # meaning no coin combination could sum to 'amount'.
        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()
print(solution.coinChange([2,5], 3))

        
# @leet end
