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
    def combine(self, n, k):
        result = []
        def generateCombination(arr, start_index): 
            if len(arr) == k:
                copy = arr[:]
                result.append(copy)
                return
            for i in range(start_index, n+1):
                arr.append(i)
                generateCombination(arr, i+1)
                arr.pop()
        generateCombination([], 1)
        return result

        
# @leet end
