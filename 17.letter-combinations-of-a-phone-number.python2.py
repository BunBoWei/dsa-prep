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
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        phone_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        result = []
        def backtrack(index, string):
            if len(string) == len(digits):
                result.append(string)
                return

            print(digits[0])
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index+1, string + letter)

        backtrack(0,"")
        return result
#
# solution = Solution()
# print(solution.letterCombinations("23"))
# print(solution.letterCombinations(""))
# print(solution.letterCombinations("2"))
# @leet end
