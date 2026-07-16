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
    def longestPalindrome(self, s):
        max = s[0] 
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                # print("i:",i,"j:",j)
                if j-i+1 > len(max):
                    if self.isPalindrome(s,i,j+1):
                        max = s[i:j+1]
        return max   
                        
    def isPalindrome(self, s, i, j):
        string = s[i:j]
        return string[::-1] == string


# solution = Solution()
# print(solution.longestPalindrome("babad"))
# print(solution.longestPalindrome("cbbd"))
        
# @leet end
