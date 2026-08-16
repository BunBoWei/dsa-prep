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
        last_seen = {}
        longest_sub = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] in last_seen:
                left = max(left, last_seen[s[right]] + 1)

            last_seen[s[right]] = right
            longest_sub = max(longest_sub, right - left + 1)

            right += 1

        return longest_sub


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
# print(solution.lengthOfLongestSubstring("pwwkew"))


# @leet end
