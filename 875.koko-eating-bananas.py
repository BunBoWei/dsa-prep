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
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = 1
        for pile in piles:
            if pile > max_speed:
                max_speed = pile

        min_eating_speed = max_speed
        while min_speed <= max_speed:
            mid = (max_speed + min_speed) // 2
            hour_take = 0
            for pile in piles:
                hour_take += ceil(pile / mid)
            if hour_take <= h:
                min_eating_speed = min(min_eating_speed, mid)
                max_speed = mid - 1
            else:
                min_speed = mid + 1
        return min_eating_speed


solution = Solution()
# print(solution.minEatingSpeed([3, 6, 7, 11], 8))
# print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(solution.minEatingSpeed([3], 2))

# @leet end
