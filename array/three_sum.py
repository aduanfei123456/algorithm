"""
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def three_sum(nums):
    length=len(nums)
    nums=sorted(nums)
    res=[]
    for i in range(length-2):
        for j in range(i+1,length-1):
            if (nums[i]+nums[j]+nums[j])>0:
               break

            for k in range(j+1,length):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=sorted([nums[i],nums[j],nums[k]])
                    if temp not in res:
                        res.append(temp)
                if nums[i]+nums[j]>0:
                    break
    return res
def three_sums(nums):
    nums=sorted(nums)

s= [-1, 0, 1, 2, -1, -4]
print(three_sum(s))