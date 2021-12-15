import os
import sys
import array as arr
from typing import List



def twoSum(nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if target == nums[i]+nums[j]:
                        return [i,j]


def twoSum2(nums: List[int], target: int) -> List[int]:
  diff_dict = {}
  for num1, num2 in enumerate(nums):    #searches the numbers list for the two numbers that equal the target when summed 
    if num2 in diff_dict.keys():        #if there is a number on the dictionary equal to num2, then we know num1 + num2 = target and return both numbers        
        return [diff_dict[num2], num1]
    else:
        diff_dict[target-num2] = num1  #if there isn't a number on the dictionary equal to num2, then we subtract num2 to target and place the result in dictionary
                    

def main():
    nums = [2, 7, 11 ,15] 
    target = 9
    result=twoSum2(nums,target)
    print(result)


if __name__ == '__main__':
    main()
