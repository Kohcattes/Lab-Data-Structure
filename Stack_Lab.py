'''Stack Code Lab'''
class Stack:
    '''Create a new stack Lab3'''
    def __init__(self):
        self.data = []
    
    def size(self):
        '''size of stack'''
        return len(self.data)

    def is_empty(self):
        '''Empty True or Not'''
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def push(self, pNew):
        '''Push Data on top Stack'''
        self.data.append(pNew)
        
    def pop(self):
        '''delete data from top Stack'''
        if len(self.data) == 0:
            return None
        else:
            return self.data.pop()
            
    def stackTop(self):
        '''Top Stack'''
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]
    
    def printStack(self):
        '''print member'''
        print(self.data)

def is_parentheses_matching(exp):
    '''Check "(", ")" matches Lab4.1'''
    first = exp.count('(')
    end = exp.count(')')
    if first == end:
        print('Parentheses in '+exp+' are matched')
        return True
    else:
        print('Parentheses in '+exp+' are unmatched')
        return False

def copyStack(stack1, stack2):
    '''Copy Stack 4.2'''
    for i in stack1.data:
        stack2.push(i)

dicOper = {'*':2, '/': 2, '+':1, '-' :1} #use in 4.3 postfix

def infixToPostfix(exp):
    '''infixToPostfix Lab4.3'''
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
