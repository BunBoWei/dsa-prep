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
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        string = self.countAndSay(n-1)
        count = 1
        say = ""
        for i in range(1,len(string)):
            if string[i] == string[i-1]:
                count += 1
            else:
                say += str(count) + string[i-1]
                count = 1
        say += str(count) + string[len(string)-1] 
        return say 

solution = Solution()
print(solution.countAndSay(4))

        
# @leet end
