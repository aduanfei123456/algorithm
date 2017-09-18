"""
Given a sorted integer array without duplicates,
return the summary of its ranges
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
def summary_ranges(nums):
    res=[]
    start=nums[0]
    for i in range(len(nums)):
        if i<len(nums)-1and nums[i]+1==nums[i+1]:
            continue
        else:
            if start!=nums[i]:
                res.append(str(start)+'->'+str(nums[i]))
            else:
                res.append(str(start))
            if(i !=len(nums)-1):
                start=nums[i+1]
    return res
nums=[0,1,2,4,5,7]
print(summary_ranges(nums))