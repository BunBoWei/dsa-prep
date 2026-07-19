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
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                # print("left", left)
                # print("right", right)
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return res


solution = Solution()
# print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
# print(solution.threeSum([0, 1, 1]))
# print(solution.threeSum([-2, 0, 1, 1, 2]))
# print(solution.threeSum([-100, -70, -60, 110, 120, 130, 160]))
print(solution.threeSum([-4, -1, -1, 0, 0, 4, 5, 5]))


# @leet end
