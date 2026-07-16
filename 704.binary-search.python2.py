# @leet imports start
from bisect import *
from collections import *
from copy import *
from datetime import *
from heapq import *
from math import *
from re import *
from string import *
from random import *
from itertools import *
from functools import *
from operator import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import itertools
import functools
import operator
# @leet imports end

# @leet start
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target: 
                right = mid - 1
        return -1

# solution = Solution()
# print(solution.search([-1,0,3,5,9,12],9))
# print(solution.search([-1,0,3,5,9,12],2))
# print(solution.search([5],5))


        
# @leet end
