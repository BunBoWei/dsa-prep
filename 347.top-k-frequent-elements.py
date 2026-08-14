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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for num, cnt in counts.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]


# solution = Solution()
# print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
# print(solution.topKFrequent([1], 1))
# print(solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
# print(solution.topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 2))


# @leet end

