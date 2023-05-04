def solution(n):
    
    binary_list=list('0'+bin(n)[2:]) #n을 이진수 문자열 list로 바꾸기 맨앞 0
    flag=0
    one_cnt=0 #flag부터의 1의 갯수

   
    for i in range(len(binary_list)-1, -1, -1): #끝에서부터 탐색
        if binary_list[i]=='1' and binary_list[i-1]=='0':
            binary_list[i-1]='1' 
            binary_list[i]='0'  #0을 한자리 앞으로 이동
            flag=i+1 #다음문장에서 i+1부터 1검사 시작
            break
    
    for i in range(flag, len(binary_list)):   #자리 바꾼 인덱스 이후로부터 1의 갯수 탐색
        if binary_list[i]=='1':
            one_cnt+=1
    
    for i in range(len(binary_list)-1, flag-1, -1 ): #자리 바꾼 인덱스 이후로부터 1들을 전부 맨 뒷자리로 이동    
        if one_cnt>0:
            binary_list[i]='1'
            one_cnt-=1
        else:
            binary_list[i]='0'


    decimal=int('0b'+''.join(binary_list), 2)  #십진수로 변환
    
    return decimal
