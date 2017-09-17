"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
class Interval(object):
    def __initial__(self,s=0,e=0):
        self.start=s
        self.end=e
def Sortstandard(i1,i2):
    return i1[0]<i2[0]
def merge(intervals):
    i=0
    while i<len(intervals)-1:
        while i<len(intervals)-1 and intervals[i][0]<intervals[i+1][0]and intervals[i+1][0]<intervals[i][1]:
            intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
            intervals.pop(i+1)
        i+=1
    return intervals
def merge2(intervals):
    out=[]
    for i in sorted(intervals,key=lambda i:i[0]):
        if out and out[-1].end>i.start:
            out[-1].end=max(out[-1].end,i.end)
        else:
            out+=i
    return out

intervals=[[1,3],[2,6],[5,10],[9,18]]
print(merge(intervals))