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
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        left = 0
        min_sub = len(nums) + 1
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_sub = min(min_sub, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return min_sub if min_sub != len(nums) + 1 else 0


solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(1, [1, 4, 4]))
print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))

# @leet end

