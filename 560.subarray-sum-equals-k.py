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
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        pref_sum = {}

        count = 0

        for num in nums:
            cur_sum += num
            # print(cur_sum)

            if cur_sum == k:
                # print("in")
                count += 1

            if cur_sum - k in pref_sum:
                count += pref_sum[cur_sum - k]

            pref_sum[cur_sum] = pref_sum.get(cur_sum, 0) + 1
        return count


# solution = Solution()
# print(solution.subarraySum([-1, 1, 0], 0))
# print(solution.subarraySum([1, -1, 0, 0, 0], 0))
# print(solution.subarraySum([28, 54, 7, -70, 22, 65, -6], 100))
# print(solution.subarraySum([100, 1, 2, 3, 4], 6))
# print(solution.subarraySum([1, 2, 1, 1, 1, 1], 4))


# @leet end

