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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] not in mp:
                mp[nums[i]] = i
            else:
                res = [mp[target - nums[i]], i]
        return res


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))


# @leet end
