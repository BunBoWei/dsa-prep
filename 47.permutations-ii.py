# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import io
import itertools
import json
import math
import operator
import random
import re
import statistics
import string
import sys
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *

# @leet imports end


# @leet start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        first_occurrences = {}

        for i in range(len(nums)):
            if nums[i] not in first_occurrences:
                first_occurrences[nums[i]] = i

        def backtrack(path, used):
            if len(path) == len(nums):
                results.append(path[:])
                return

            for i in range(len(nums)):
                if i != 0 and nums[i] in duplicates:
                    return
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True

                    backtrack(path, used)

                    path.pop()
                    used[i] = False

        used = [False] * len(nums)

        backtrack([], used)
        return list(results)


solution = Solution()
print(solution.permuteUnique([1, 1, 2]))


# @leet end

