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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)
        return heap[0]


solution = Solution()
# print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(solution.findKthLargest([10, 30, 20, 40, 35], k=2))

# @leet end
