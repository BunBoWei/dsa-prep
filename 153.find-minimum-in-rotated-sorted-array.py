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
    def findMin(self, nums: List[int]) -> int:
        min = math.inf
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < min:
                min = nums[mid]
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return int(min)


# solution = Solution()
# print(solution.findMin([3, 4, 5, 1, 2]))
# print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
# print(solution.findMin([11, 13, 15, 17]))


# @leet end

