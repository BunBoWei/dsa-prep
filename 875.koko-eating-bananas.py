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
        max_speed = max(piles)

        while min_speed < max_speed:
            mid = (min_speed + max_speed) // 2
            hour_taken = 0
            for pile in piles:
                hour_taken += ceil(pile / mid)
            if hour_taken <= h:
                max_speed = mid
            else:
                min_speed = mid + 1
        return min_speed


# solution = Solution()
# print(solution.minEatingSpeed([3, 6, 7, 11], 8))

# @leet end
