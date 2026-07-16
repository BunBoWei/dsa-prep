# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import itertools
import math
import operator
import random
import re
import string
from bisect import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from re import *
from string import *

# @leet imports end

# @leet start
class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        total_water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1
                
        return total_water  

# solution = Solution()
# print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(solution.trap([4,2,0,3,2,5]))

# @leet end
