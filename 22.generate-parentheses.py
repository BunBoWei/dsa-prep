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
    def generateParenthesis(self, n: int) -> List[str]:
        results = [] 
        def addParenthesis(string, open_num, close_num):
            if len(string) == 2*n:
                results.append(string)
                return
            if open_num < n:
                addParenthesis(string+"(", open_num+1, close_num)
            if close_num < open_num:
                addParenthesis(string+")", open_num, close_num+1)

        addParenthesis("", 0, 0)

        return results

solution = Solution()
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(4))
print(solution.generateParenthesis(5))
print(solution.generateParenthesis(6))
print(solution.generateParenthesis(7))
print(solution.generateParenthesis(8))
# @leet end
