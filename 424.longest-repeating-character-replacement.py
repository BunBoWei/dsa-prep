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
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        left = 0

        longest_sub = 0
        max_freq = 0
        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            max_freq = max(max_freq, freq_map[s[right]])

            if (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1

            longest_sub = max(longest_sub, right - left + 1)

        return longest_sub


# solution = Solution()
# print(solution.characterReplacement("ABAB", 2))
# print(solution.characterReplacement("AABABBA", 1))


# @leet end
