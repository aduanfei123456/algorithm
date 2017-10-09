"""
Say you have an array for which the ith element
is the price of a given stock on day i.
If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
"""
def max_profit_naive(prices):
    diffs=[]
    #diffs.append(prices[0])
    for i in range(len(prices)-1):
        diffs.append(prices[i+1]-prices[i])
    print(diffs)
    profits=0
    for i in range(len(diffs)):
        temp=0
        max=temp
        if diffs[i]>0:
            for j in range(i,len(diffs)):
                temp+=diffs[j]
                max=temp if temp>max else max
        profits=max if max>profits else profits
    return profits
prices=[7, 6, 4, 3, 1]
print(max_profit_naive(prices))
