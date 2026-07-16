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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        sorted_keys = sorted(freq, key=lambda k: (-freq[k], k))
        return sorted_keys[:k]


solution = Solution()
print(
    solution.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4
    )
)
# @leet end

