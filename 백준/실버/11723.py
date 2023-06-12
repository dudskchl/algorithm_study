

#첫번 째 시도 => 시간초과
# sys.stdin.readline()
import sys

S=set()

def add(x):
    global S
    if x not in S:
        S.add(x)

def remove(x):
    global S
    if x in S:
        S.remove(x)

def check(x):
    global S
    if x in S:
        print(1)
    else:
        print(0)

def toggle(x):
    global S
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all():
    global S
    S=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def empty():
    global S
    S=set()

def input_sentence(s):
    global S
    op=''
    num=0
    if ' ' in s:
        op=s.split()[0]
        num=int(s.split()[1])
    
    if s=='all':
        all()
    elif s=='empty':
        empty()
    elif op=='add':
        add(num)
    elif op=='remove':
        remove(num)
    elif op=='check':
        check(num)
    elif op=='toggle':
        toggle(num)
   
        
M=int(input())

while M>0:
    string=sys.stdin.readline().replace('\n','')
    input_sentence(string)

    M-=1




