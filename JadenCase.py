def solution(s):
    
    
    s=list(s.lower()) #일단 전부다 소문자로 변경
    
    ## 이 밑은 조건에 맞는 경우 대문자로 변경
    s[0]=s[0].upper()
    
    for i in range(1,len(s)):
        if s[i-1]==' ':
            s[i]=s[i].upper()
    
    answer=''.join(s)
    return answer
