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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf

        def dfs(node) -> int:
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum


# solution = Solution()
# node1 = TreeNode(1)
# node2 = TreeNode(-2)
# node3 = TreeNode(3)
# # node4 = TreeNode(0)
# # node5 = TreeNode(0)
# # node6 = TreeNode(15)
# # node7 = TreeNode(7)
# node1.left = node2
# node1.right = node3
# # node2.left = None
# # node2.right = None
# # node3.left = node6
# # node3.right = node7
#
#
# print(solution.maxPathSum(node1))

# @leet end

