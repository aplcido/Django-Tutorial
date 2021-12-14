import os
import sys
import array as arr
from typing import List



def twoSum(nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if target == nums[i]+nums[j]:
                        return [i,j]
                    

def main():
    nums = [2,7,11,15] 
    target = 9
    result=twoSum(nums,target)
    print(result)


if __name__ == '__main__':
    main()
