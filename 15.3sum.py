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
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return res


# solution = Solution()
# print(solution.threeSum([-1, 0, 1, 2, -1, -4]))


# @leet end
