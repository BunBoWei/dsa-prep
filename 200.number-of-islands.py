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
    DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def _flood(self, grid, r, c, visited) -> None:
        print("asdfasdf")
        """Mark every land cell connected to (r, c), iteratively."""
        rows, cols = len(grid), len(grid[0])
        stack = [(r, c)]
        visited[r][c] = True

        while stack:
            cr, cc = stack.pop()
            for dr, dc in self.DIRECTIONS:
                nr, nc = cr + dr, cc + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == "1"
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = True  # mark on PUSH
                    stack.append((nr, nc))
        print(visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    self._flood(grid, r, c, visited)
                    islands += 1

        return islands


solution = Solution()
print(
    solution.numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

# @leet end

