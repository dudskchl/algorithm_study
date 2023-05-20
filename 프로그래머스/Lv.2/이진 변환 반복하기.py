def solution(s):
    v=0 #회차
    del_zero=0  #0을 지운 횟수
    list_s=list(s) 
    one_cnt_tmp=0 #한 회차 당 문자열 내의 1의 개수
    
    while list_s!=['1']:
        for i in list_s:
            if i =='0':
                del_zero+=1
            if i =='1':
                one_cnt_tmp+=1

        #bin()-> 파이썬 내장함수 대신 앞에 ob가 붙음 ex)'ob10110'
        #ob 문자열제거한 뒤의 바이너리 문자열
        bin_list=(list(bin(one_cnt_tmp)))[2:]  
        list_s=bin_list
        
        one_cnt_tmp=0
        v+=1 #회차 증가
        
    answer = [v,del_zero]
    return answer



##
## 멋쟁이
##def solution(s):
##    a, b = 0, 0
##    while s != '1':
##        a += 1
##        num = s.count('1')
##        b += len(s) - num
##        s = bin(num)[2:]
##    return [a, b]
