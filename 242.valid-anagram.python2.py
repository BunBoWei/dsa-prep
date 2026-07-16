# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import itertools
import math
import operator
import random
import re
import string
from bisect import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from re import *
from string import *

# @leet imports end


# @leet start
class Solution(object):
    def isAnagram(self, s, t):
        letters = dict()
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1 
        for char in t:
            if char not in letters:
                return False
            else:
                letters[char] -= 1
                if letters[char] == 0:
                    letters.pop(char)
        return not letters 

solution = Solution()
# print(solution.isAnagram("anagram", "nagaram"))
# print(solution.isAnagram("rat", "car"))
print(solution.isAnagram("ab", "a"))
# @leet end
