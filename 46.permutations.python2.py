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
    def permute(self, nums):
        results = []  
        def backtrack(path, used):
            if len(path) == len(nums):
                results.append(path[:]) 
                return

            for i in range(len(nums)):
                if not used[i]:
                    
                    path.append(nums[i])
                    used[i] = True       
                    
                    backtrack(path, used) 
                    
                    path.pop() 
                    used[i] = False

        used = [False] * len(nums)
        
        backtrack([], used)
        
        return results

sol = Solution()
print(sol.permute([1, 2, 3]))                    
        
# @leet end
