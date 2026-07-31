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
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

        for char in t:
            if char not in char_map:
                return False
            else:
                char_map[char] -= 1
                if char_map[char] == 0:
                    char_map.pop(char)

        return len(char_map) == 0


# solution = Solution()
# print(solution.isAnagram("anagram", "nagaram"))


# @leet end

