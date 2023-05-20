

class Stack:
    def __init__(self):
        self.box=[]

    def push(self, item):
        self.box.append(item)

    def pop(self):
        return self.box.pop()

    def top(self):
        return self.box[-1]

    def size(self):
        return len(self.box)



def Check(string:str):
    
    checker=Stack()

    for ch in string:
        if checker.size()==0:
            checker.push(ch)
        else:
            if ch =='(' or ch=='[' or ch=='{':
                checker.push(ch)

            elif ch==')':
                if checker.top()=='(':
                    checker.pop()
                else:
                    checker.push(ch)

            elif ch==']':
                if checker.top()=='[':
                    checker.pop()
                else:
                    checker.push(ch)

            elif ch=='}':
                if checker.top()=='{':
                    checker.pop()
                else:
                    checker.push(ch)


    if checker.size()!=0:
        
        return False
    else:
     
        return True


def rotate(string):
    new_str=string[1:]+string[0]
    return new_str    



def solution(s):
    
    result=0

    if Check(s)==True:
        result+=1
            
    for i in range(len(s)-1):
        
        s=rotate(s)         #왼쪽으로 한 칸씩 회전
        if Check(s)==True:
            result+=1

    return result





                

                
