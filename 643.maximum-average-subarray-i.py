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
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = 0
        left = 0
        max_avg = -math.inf

        for right in range(len(nums)):
            sum_k += nums[right]
            window_length = right - left + 1
            if window_length == k:
                max_avg = max(max_avg, sum_k / window_length)
                sum_k -= nums[left]
                left += 1
        return max_avg


# solution = Solution()
# print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
# print(solution.findMaxAverage([5], 1))

# @leet end

