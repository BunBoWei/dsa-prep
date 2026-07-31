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
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_length = 0
        for num in nums:
            if num - 1 not in num_set:
                count = 0
                while num in num_set:
                    num += 1
                    count += 1
                max_length = max(max_length, count)
        return max_length


# @leet end
