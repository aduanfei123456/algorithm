"""
Contributed by izanbf1803.
Example:
-------------------------------------------------------------------------------------------------
    Code:
        |   exp = "2452 * (3 * 6.5 + 1) * 6 / 235"
        |   print("Expression:", exp)
        |   print("Parsed expression:", mp.parse(exp))
        |   print("Evaluation result:", mp.evaluate(exp))
    Output:
        |   Expression: 2452 * (3 * 6 + 1) * 6 / 235
        |   Parsed expression: ['2452', '*', '(', '3', '*', '6', '+', '1', ')', '*', '6', '/', '235']
        |   Evaluation result: 1189.4808510638297
-------------------------------------------------------------------------------------------------
"""
from collections import deque
import re

numeric=re.compile("\d+(\.\d+)?")
operator='+-*/'
priority={
    '+':0,
    '-':0,
    '*':1,
    '/':1
}
def GetResult(n1,n2,op):
    assert op in operator
    print(n1,n2,op)
    return eval(n2+op+n1)

def ParseExpression(expression):
    result=[]
    number=""
    for i in expression:
        if i.isdigit() or i=='.':
            number+=i
        else:
            if number:
                result.append(number)
                number=""
            if i:
                result.append(i)
    if number:
        result.append(number)
    return result
def IsNumber(exp):
    ren=re.compile('[0-9]')
    res=ren.match(exp)
    return 1 if res else 0
def IsOper(exp):
    return exp in operator
def ComPor(op1,op2):
    return priority[op2]>priority[op1]
def evaluate(op_stack,number_stack):
    n1 = number_stack.pop()
    n2 = number_stack.pop()
    temps = GetResult(n1, n2, op_stack.pop())
    number_stack.append(str(temps))
def Scanner(exps):

    print(exps)
    op_stack=[]
    number_stack=[]
    i=0
    while i< (len(exps)):
        exp=exps[i]
        if IsNumber(exp):

            number_stack.append(exp)
        else :
            if exp=='(':
               # a new Scanner
                rescan=Scanner(exps[i+1:])
                number_stack.append(rescan[0])
                i+=rescan[1]+1

            if exp==')':
                while op_stack:
                    evaluate(op_stack, number_stack)
                return [number_stack.pop(),i]
            if IsOper(exp):
                if op_stack:
                    if ComPor(op_stack[-1],exp):
                        op_stack.append(exp)
                    else:
                        while(op_stack and not ComPor(op_stack[-1],exp)):
                            assert len(number_stack)>=2
                            evaluate(op_stack,number_stack)

                        op_stack.append(exp)
                else:
                    op_stack.append(exp)
        i+=1
        print(op_stack,number_stack)

    while op_stack:
        evaluate(op_stack,number_stack)

    #return number_stack.pop()
    print(number_stack.pop())
expression="(1+1*(1-2))/2*(3-2)"
exps=ParseExpression(expression)
print(Scanner(exps))