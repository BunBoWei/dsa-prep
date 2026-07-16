# @leet imports start
from bisect import *
from collections import *
from copy import *
from datetime import *
from heapq import *
from math import *
from re import *
from string import *
from random import *
from itertools import *
from functools import *
from operator import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import itertools
import functools
import operator
# @leet imports end

# @leet start
class Solution(object):
    def groupAnagrams(self, strs):
        groups = dict()
        for word in strs:
            key = ''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        result = []
        for value in groups.values():
            result.append(value)
        return result

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# @leet end
