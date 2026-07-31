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
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    print("111")
                    right = mid - 1
                else:
                    print("222")
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    print("333")
                    left = mid + 1
                else:
                    print("444")
                    right = mid - 1

        return -1


solution = Solution()
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
# print(solution.search([1], 0))
# print(solution.search([6, 8, 1, 2, 3, 4, 5], 6))
# print(solution.search([5, 6, 7, 8, 4], 8))
print(solution.search([6, 1, 2, 3, 4], 6))


# @leet end
