def Fibo(n):
    
    Fibo_arr=[0,1]

    if n<2:
        return Fibo_arr[n]
    else:
        for i in range(2, n+1):
            result=Fibo_arr[i-2]+Fibo_arr[i-1]
            Fibo_arr.append(result)
        return Fibo_arr[n]

   
    
def solution(n):
   

    fibo_num=Fibo(n)
    answer=fibo_num%1234567
    
    
    return answer

