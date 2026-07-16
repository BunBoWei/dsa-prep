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
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            width = (right - left)
            if height[right] > height[left]:
                area = height[left] * width 
                left += 1
            else:
                area = height[right] * width 
                right -= 1
            if area > max_area:
                max_area = area

        return max_area

# solution = Solution()
# print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
# print(solution.maxArea(([1,1])))
# print(solution.maxArea([1]))
# @leet end
