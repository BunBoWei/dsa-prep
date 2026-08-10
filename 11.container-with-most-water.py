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
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_water = 0
        while left < right:
            if height[left] < height[right]:
                max_water = max(max_water, (right - left) * height[left])
                left += 1
            else:
                max_water = max(max_water, (right - left) * height[right])
                right -= 1

        return max_water


# @leet end
