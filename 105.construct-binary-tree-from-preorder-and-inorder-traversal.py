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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {val: i for i, val in enumerate(inorder)}
        
        self.preorder_index = 0
        
        return self.build_helper(preorder, 0, len(inorder) - 1)
    
    def build_helper(self, preorder, inorder_left, inorder_right):
        print(inorder_left, inorder_right, self.preorder_index)
        if inorder_left > inorder_right:
            return None
        
        root_val = preorder[self.preorder_index]
        self.preorder_index += 1  # Move to the next item for future calls
        
        root = TreeNode(root_val)
        root_inorder_index = self.inorder_map[root_val]
        
        root.left = self.build_helper(preorder, inorder_left, root_inorder_index - 1)
        
        root.right = self.build_helper(preorder, root_inorder_index + 1, inorder_right)
        
        return root

solution = Solution()
print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))
            

            
# @leet end
