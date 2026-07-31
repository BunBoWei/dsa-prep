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
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_count = 0
        left = 0
        for i in range(len(s)):
            if s[i] in map:
                left = max(left, map[s[i]] + 1)

            map[s[i]] = i
            max_count = max(max_count, i - left + 1)
        return max_count


# solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))
# print(solution.lengthOfLongestSubstring("bbbbbbb"))
# print(solution.lengthOfLongestSubstring("pwwkew"))


# @leet end
