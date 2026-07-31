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
    def equalMaps(self, m1: dict, m2: dict) -> bool:
        for key, value in m2.items():
            if key not in m1 or value != m1[key]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for ch1 in s1:
            need[ch1] = need.get(ch1, 0) + 1

        window = {}
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if self.equalMaps(need, window):
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            if self.equalMaps(need, window):
                return True
            left += 1

        return False


# solution = Solution()
# print(solution.checkInclusion("ab", "eidbaooo"))
# print(solution.checkInclusion("ab", "eidboaoo"))
# print(solution.checkInclusion("abc", "bbbca"))
# print(solution.checkInclusion("adc", "dcda"))
# print(solution.checkInclusion("hello", "ooolleoooleh"))
# print(solution.checkInclusion("ky", "ainwkckifykxlribaypk"))


# @leet end
