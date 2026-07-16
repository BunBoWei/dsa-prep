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
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

# solution = Solution()
# print(solution.reverseString(["h","e","l","l","o"]))
# print(solution.reverseString(["H","a","n","n","a","h"]))

# @leet end
