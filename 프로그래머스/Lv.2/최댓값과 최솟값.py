def solution(s):
    
    s_list= list(map(int,s.split(' ')))
 
    max_num, min_num=max(s_list), min(s_list)

    answer=str(min_num)+' '+str(max_num) 
    return answer

