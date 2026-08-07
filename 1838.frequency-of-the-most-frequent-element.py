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
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            # cost to raise everything in [left, right] up to nums[right]
            print(nums[right] * (right - left + 1) - window_sum)
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)

        return best


solution = Solution()
print(solution.maxFrequency([1, 2, 4], 5))
# print(solution.maxFrequency([1, 4, 8, 13], 5))
# print(solution.maxFrequency([3, 9, 6], 2))


# @leet end

