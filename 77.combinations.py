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
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def generateCombination(arr, start_index): 
            if len(arr) == k:
                result.append(arr.copy())
                return
            for i in range(start_index, n+1):
                arr.append(i)
                generateCombination(arr, i+1)
                arr.pop()
        generateCombination([], 1)
        return result

# solution = Solution()
# print(solution.combine(4,2))
# print(solution.combine(1,1))

# @leet end
