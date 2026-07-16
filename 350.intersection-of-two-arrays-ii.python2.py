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
    def intersect(self, nums1, nums2):
        freq_map = dict()
        for i in range(len(nums1)):
            if nums1[i] in freq_map:
                freq_map[nums1[i]] += 1 
            else:
                freq_map[nums1[i]] = 1

        result = []
        print(freq_map)
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                print(num)
                result.append(num)
                freq_map[num] -= 1
        return result

        
# @leet end
