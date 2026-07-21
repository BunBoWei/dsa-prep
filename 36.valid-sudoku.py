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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        column_check = [set() for _ in range(9)]
        box_check = [set() for _ in range(9)]

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == ".":
                    continue
                num = int(board[row][column])

                box = column // 3 + 3 * (row // 3)
                if (
                    num in row_check[row]
                    or num in column_check[column]
                    or num in box_check[box]
                ):
                    return False

                row_check[row].add(num)
                column_check[column].add(num)

                box_check[box].add(num)
        return True


# solution = Solution()
# print(
#     solution.isValidSudoku(
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#         ]
#     )
# )
#

# @leet end

