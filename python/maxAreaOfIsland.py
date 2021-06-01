#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        connected = {}
        mmax, kmax = len(grid), len(grid[0])
        
        for m in range(mmax):
            for k in range(kmax):
                if grid[m][k]:
                    coords = [None, None, None, None]
                    
                    if m - 1 >= 0 and grid[m - 1][k]:
                        coords[0] = (m - 1, k)
                    
                    if k + 1 < kmax and grid[m][k + 1]:
                        coords[1] = (m, k + 1)
                    
                    if m + 1 < mmax and grid[m + 1][k]:
                        coords[2] = (m + 1, k)
                    
                    if k - 1 >= 0 and grid[m][k - 1]:
                        coords[3] = (m, k - 1)
                    
                    connected[(m, k)] = coords
        
        return connected

if __name__ == "__main__":
    test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution()
    res = sol.maxAreaOfIsland(test)

    for k, v in res.items():
        print(k, ": ", v)
    
