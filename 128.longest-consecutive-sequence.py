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
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                count = 1
                while num + 1 in nums:
                    count += 1
                    num += 1
                max_length = max(count, max_length)

        return max_length


# solution = Solution()
# print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(solution.longestConsecutive([1, 0, 1, 2]))


# @leet end
