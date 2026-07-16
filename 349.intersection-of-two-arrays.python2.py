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
    def intersection(self, nums1, nums2):
        num_set = set()
        for num in nums1:
            num_set.add(num)

        result = []
        for num in nums2:
            if num in num_set:
                result.append(num)
                num_set.remove(num)
        return result

solution = Solution()
print(solution.intersection([1,2,2,1],[2,2]))
print(solution.intersection([4,9,5],[9,4,9,8,4]))
# @leet end
