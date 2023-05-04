def solution(n):
    
    cnt=0 #표현 가능 수
    
    for i in range(1,n+1): #무슨 숫자로 시작하는지 
        sum=0
        k=i   #k는 시작하는 숫자
        while k<=n: 
            sum+=k   #sum=k+ k+1+ k+2....
            if sum==n:  #sum이 딱 n과 맞아떨어지면 flag에 해당 index값
                cnt+=1
                break
            elif sum>n: #n과 맞아떨어지지 않고 계속 sum이 증가하는 경우 break
                break
            k+=1

    return cnt

solution(100)
