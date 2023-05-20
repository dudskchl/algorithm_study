
import numpy as np

def solution(arr1, arr2):


    A=np.array(arr1)
    B=np.array(arr2)
    T=np.dot(A,B)
    answer=T.tolist()

    
    return answer
