# There is a parking lot with only one empty spot. Given the initial state
# of the parking lot and the final state. Each step we are only allowed to
# move a car
# out of its place and move it into the empty spot.
# The goal is to find out the least movement needed to rearrange
# the parking lot from the initial state to the final state.

# Say the initial state is an array:

# [1,2,3,0,4],
# where 1,2,3,4 are different cars, and 0 is the empty spot.

# And the final state is

# [0,3,2,1,4].
# We can swap 1 with 0 in the initial array to get [0,2,3,1,4] and so on.
# Each step swap with 0 only.
# Edited by cyberking-saga

def getdiff(initial,final):
    for i in range(len(final)):
        if initial[i]!=final[i]:
            return i
def garage(initial,final):
    assert 0 in initial
    count = 0
    index = initial.index(0)
    flag=True
    while initial!=final:
        while initial[index]!=final[index]:
            temp=index
            value=initial[index]
            index=initial.index(final[index])
            initial[temp] = final[temp]
            initial[index]=value
            count=count+1 if flag else count+3
            print(initial,count)
        flag = False
        index=getdiff(initial,final)

    return count
initial=[1,0,2,4,3]
final=[0,3,2,1,4]
print(garage(initial,final))
