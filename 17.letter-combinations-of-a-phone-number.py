# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import io
import itertools
import json
import math
import operator
import random
import re
import statistics
import string
import sys
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *

# @leet imports end


# @leet start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        def backtrack(index, string):
            if len(string) == len(digits):
                result.append(string)
                return
            
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index+1, string + letter)

        backtrack(0, "")
        return result
            

solution = Solution()
print(solution.letterCombinations("23"))


# @leet end
