#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        
        for n, _ in enumerate(nums):
            stack = [ nums[n] ]
            
            for num in nums[n + 1: ]:
                if not num in stack:
                    stack.append(num)
                    
                else:
                    break

            res = max(res, sum(stack))
        
        return res
