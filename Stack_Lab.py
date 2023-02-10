'''Stack Code Lab'''
class Stack:
    '''Create a new stack Lab3'''
    def __init__(self):#Use Auto to Creat Class
        self.data = []
    
    def size(self):
        '''size of stack'''
        return len(self.data)#return

    def is_empty(self):
        '''Empty True or Not'''
        return (len(self.data) == 0)#Check Empty Stack
        
    def push(self, pNew):
        '''Push Data on top Stack'''
        self.data.append(pNew)#Input on Top Stack
        
    def pop(self):
        '''delete data from top Stack'''
        if len(self.data) == 0:
            return None
        else:
            return self.data.pop()#Delete Top Stack
            
    def stackTop(self):
        '''Top Stack'''
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]#Check Latest Input
    
    def printStack(self):
        '''print member'''
        print(self.data)#Output Stack On Screen

dicOper = {'*':2, '/': 2, '+':1, '-' :1} #Use in 4.3 postfix
        
def is_parentheses_matching(exp):
    '''Check "(", ")" matches Lab4.1'''
    condi = (exp.count(')') == exp.count('('))
    if condi:
        print('Parentheses in '+exp+' are matched')
    else:
        print('Parentheses in '+exp+' are unmatched')
    return condi

def copyStack(stack1, stack2):
    '''Copy Stack 4.2'''
    for i in stack1.data:
        stack2.push(i)

def infixToPostfix(exp):
    '''infix To Postfix Lab4.3'''
    stack1 = Stack()
    pnew = []
    for i in exp:
        if i in dicOper.keys():
            if stack1.stackTop() != None and dicOper[stack1.stackTop()] > dicOper[i]:
                for _ in range(len(stack1.data)):
                    pnew.append(stack1.pop())
            stack1.push(i)
        else:
            pnew.append(i)
    for _ in range(len(stack1.data)):
                pnew.append(stack1.pop())
    x= ''.join(pnew)
    return x
    
def main():
    '''use'''
    exp = "A+B*C-D/E"
    postfix = infixToPostfix(exp)
    print('Postfix of', exp, 'is', postfix)
main()
