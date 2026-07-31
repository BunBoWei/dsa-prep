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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        print(res)

        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]

        return res


solution = Solution()
print(solution.productExceptSelf([4, 2]))
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))


# @leet end
