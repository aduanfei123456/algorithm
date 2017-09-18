## find missing ranges between low and high in the given array.
# ex) [3, 5] lo=1 hi=10 => answer: [1->2, 4, 6->10]
def missing_ranges(nums, lo, hi):
    outs=[]
    start=lo
    for n in nums:
        if start<n:
            outs.append(get_range(start,n))
            start=n+1
        else :
            if start==n:
                start+=1
        print(start," ",n)
    if start<=hi:
        outs.append(get_range(start,hi+1))
    return outs
def get_range(start,end):
    return str(start)+"->"+str(end-1) if start<end-1 else start
nums = [3, 5, 10, 11, 12, 15, 19]
print(missing_ranges(nums,1,20))

