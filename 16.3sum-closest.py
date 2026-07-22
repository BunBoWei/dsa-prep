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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest_sum = sys.maxsize
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            # print("left", nums[left])
            # print("right", nums[right])
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum)
                if diff < abs(target - closest_sum):
                    closest_sum = sum
                if sum > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    return sum
        return closest_sum


# solution = Solution()
# print(solution.threeSumClosest([-1, 2, 1, -4], 1))
# print(solution.threeSumClosest([0, 0, 0], 1))
# print(solution.threeSumClosest([0, 1, 2], 3))
# print(solution.threeSumClosest([0, 0, 1, 2, 0, 0], 3))
# print(solution.threeSumClosest([-4, 2, 2, 3, 3, 3], 0))

# @leet end

