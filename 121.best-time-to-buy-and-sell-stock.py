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
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10**4
        for price in prices:
            if min_price > price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


# solution = Solution()
# print(solution.maxProfit([7, 6, 5, 4, 3, 2, 3]))

# @leet end
