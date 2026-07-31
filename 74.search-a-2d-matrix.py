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
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][m - 1]:
                return self.binary_search(matrix[mid], target)
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


solution = Solution()
print(
    solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
)
print(
    solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=12)
)


# @leet end

