

#알파벳 갯수 딕셔너리
alpha=dict()
for i in range(ord('A'),ord('Z')+1,1):
    alpha[chr(i),chr(i+32)]=0


#단어 입력
word=input()
for i in word:
    for key in alpha:
        if i in key:
            alpha[key]+=1


#key값이 가장 큰 경우 탐색
MxNum=0
MxKey=''

for key,value in alpha.items():
    if value>MxNum:
        MxNum=value
        MxKey=key[0] #대문자로 출력


#MxNum이 2개 이상인지 체크
check_Mx=0
for value in alpha.values():
    if value==MxNum:
        check_Mx+=1


print("?") if check_Mx>=2 else print(MxKey)

