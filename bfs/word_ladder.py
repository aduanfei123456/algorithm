"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence
from beginWord to endWord, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
.
Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
import logging
log=logging.warning
'''import copy
def FindWord(wordList,beginWord,endWord):
    if(len(wordList)==0):
        return 0
    wordlen=len(wordList[0])
    counter=len(wordList)
    #for word in GetDiff(beginWord,wordList):
    shortest_distance=BfsList(beginWord,endWord,wordList,counter)
    shortest_distance=5-shortest_distance
    return shortest_distance
def wrapper(beginWord,endWord,wordList,counter,ws):
    def f():
        return BfsList(beginWord,  endWord,wordList, counter,ws)
    return f

def BfsList(beginWord,endWord,wordLIst,counter,ws=[]):
    if(counter<0):
        return 0
    fs=[]
    ws.append(beginWord)
    for word in GetDiff(beginWord,wordList):
     #   print(counter,endWord)
        if word==endWord:
            print(ws)
            return counter
        else:
            fs.append(wrapper(word,endWord,wordList,counter-1,copy.deepcopy(ws)))
    counter=0
    for f in fs:
        temp=f()
        counter=temp if temp>counter else counter
    return counter

def GetDiff(word,wordList):
    wl=[]

    #print(word,wordList)
    for w in wordList:
        diff = 0
        for i in range(len(word)):
          if w[i]!=word[i]:
              diff+=1
        if diff==1 and w !=word:
            wl.append(w)
    #print(word,wl)
    return wl
'''
def ladderLength(beginWord,endWord,wordList):
    beginSet=set()
    endSet=set()
    beginSet.add(beginWord)
    endSet.add(endWord)
    result=2
    while len(beginSet)!=0 and len(endSet)!=0:
        nextBegin=set()
        for curWord in beginSet:
            for rangeWord in wordRange(curWord):
                if rangeWord in endSet:
                    return result
                if rangeWord in wordList:
                    nextBegin.add(rangeWord)
                    wordList.remove(rangeWord)
        result+=1
        print(nextBegin)
        beginSet=nextBegin
    return 0
def wordRange(word):
    for ind in range(len(word)):
        tempC=word[ind]
        for x in [chr(x) for x in range(ord('a'),ord('z')+1)]:
            if x !=tempC:
                yield word[:ind]+x+word[ind+1:]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord,endWord,wordList))