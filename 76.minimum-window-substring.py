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
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        missing = len(t)
        left = 0
        best_left, best_right = 0, -1

        for right in range(len(s)):
            need[s[right]] = need.get(s[right], 0)
            if need[s[right]] > 0:
                missing -= 1

            need[s[right]] -= 1
            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if best_right == -1 or best_right - best_left > right - left:
                    best_right = right
                    best_left = left

                need[s[left]] += 1
                missing += 1
                left += 1
        return s[best_left : best_right + 1]


# solution = Solution()
# print(solution.minWindow("ADOBECODEBANC", "ABC"))
# print(solution.minWindow("a", "b"))
# print(solution.minWindow("a", "a"))
# print(solution.minWindow("a", "aa"))
#
# @leet end
