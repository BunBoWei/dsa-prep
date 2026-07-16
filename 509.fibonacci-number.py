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
    def __init__(self):
        self.fib_stash = {} 
    def fib(self, n: int) -> int:
        if n <= 1:
            return n 

        if n in self.fib_stash:
            return self.fib_stash[n]
        result = self.fib(n-1) + self.fib(n-2)
        self.fib_stash[n] = result
        print(self.fib_stash)
        return result
        
solution = Solution()
print(solution.fib(3))
# @leet end
