




#해당 2차원 배열
## arr=[[((i+1) if i>=j else (j+1))
##             for j in range(n)]
##         for i in range(n)]


#2차원 배열 기준 left => left/n 행  left%n 열


def arr_t(i, j):

    return i+1 if i>=j else j+1

def solution(n, left , right):

    answer=[]
    for i in range(left, right+1):
        answer.append(arr_t(i//n, i%n))

    return answer



##아래는 시행착오







##
##
##import numpy as np
##import json
##
##
##class NpEncoder(json.JSONEncoder):
##    def default(self, obj):
##        if isinstance(obj, np.integer):
##            return int(obj)
##        if isinstance(obj, np.floating):
##            return float(obj)
##        if isinstance(obj, np.ndarray):
##            return obj.tolist()
##        return json.JSONEncoder.default(self, obj)
##
##    
##def solution(n, left, right):
##
##
##    arr1=[[i+1]*n for i in range(n)]
##
##    
##    
##    arr2=list(map(list, zip(*arr1)))
##
##
##    
##    arr3=np.maximum(arr1, arr2)
##    arr3_json=json.dumps(arr3, cls=NpEncoder)
##    arr3_load=json.loads(arr3_json)
##
##
##    arr4=[]
##    for i in arr3_load:
##        arr4+=i
##
##
##    return arr4[left:right+1]
##
##




    #2차원 배열 선언 주의
    # A if (blahblah) else B  => 블라블라가 맞다면 A, 아니면 B

    """
    arr=[[((i+1) if i>=j else (j+1))
             for j in range(n)]
         for i in range(n)]

    for i in arr3:
        for j in i:
            print(j, end=' ')
        print()

    """



    #CASE1 : sum(iterable[, start])   => 엄청 느림 다른건 고만고만
    #answer=sum(arr, [])


    #CASE2 : iterable method
    #answer=list(chain.from_iterable(arr))
    #answer=list(chain(*arr))

    #CASE3 : numpy => flatten경우 iter보다 수백배 빠름. 그러나 코테에서 안될 가능성을 대비 필
  #  arr_np=np.array(arr)
  #  answer=arr_np.flatten()  #제일 빠름
   # answer=arr_np.reshape(-1) #체인이랑 비슷
    
    #CASE4 : 반복문 사용해서 누적
    # for element in my_list:
    #       answer+=element
   
