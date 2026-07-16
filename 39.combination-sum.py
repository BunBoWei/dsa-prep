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
        def backtrack(arr, sum, index):
            print(arr,sum, index)
            if sum == target:
                result.append(arr[:])
                return

            if sum > target:
                return

            for i in range(index, len(candidates)):
                sum += candidates[i] 
                arr.append(candidates[i])
                backtrack(arr, sum, i)
                arr.pop()
                sum -= candidates[i]

        backtrack([], 0, 0)

        return result

solution = Solution()
print(solution.combinationSum([7,8,3,4],11))
        
# @leet end
