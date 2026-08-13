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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(arr, remaining, index):
            if remaining == 0:
                result.append(arr.copy())
                return

            if remaining < 0:
                return

            for i in range(index, len(candidates)):
                arr.append(candidates[i])
                backtrack(arr, remaining - candidates[i], i)
                arr.pop()

        backtrack([], target, 0)

        return result


# solution = Solution()
# print(solution.combinationSum([2, 3, 6, 7], 7))
# print(solution.combinationSum([2, 3, 5], 8))
# print(solution.combinationSum([2], 1))
#

# @leet end
