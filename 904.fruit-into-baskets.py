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
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}

        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            if right == 0 or fruits[right] != fruits[right - 1]:
                baskets[fruits[right]] = right
            if len(baskets) > 2:
                left = baskets[fruits[right - 1]]
                baskets.pop(fruits[left - 1])
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits


# solution = Solution()
# print(solution.totalFruit([1, 2, 1]))
# print(solution.totalFruit([0, 1, 2, 2]))
# print(solution.totalFruit([1, 2, 3, 2, 2]))
# print(solution.totalFruit([2, 3, 0, 3, 3, 2, 2, 2, 2, 2]))

# @leet end
