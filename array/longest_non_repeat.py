# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.
def longest_non_repeat(s):
    i=0
    j=1
    max=0
    length=len(s)
    while j<length:
       r=i
       flag=False
       for r in range(0,j-i):
           if s[i+r]==s[j]:
               flag=True
               break
       print(s[i:j])
       if flag:
           max=j-i if  j-i>max else max
           i+=r+1
       else:
           j+=1
    return max
a = "abcabcdefbb"
print(a)
print(longest_non_repeat(a))