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
import copy
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

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
wordList.append(endWord)
print(FindWord(wordList,beginWord,endWord))