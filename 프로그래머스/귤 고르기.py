



def solution(k, tangerine):
    result=0  #귤 종류 개

    delNum=len(tangerine)-k  #제외하는 귤 개수

          
    tan_dict={}   #귤 번호별 개수 딕셔너리   
   

    for i in tangerine:         #idx별 귤 개수 더하기
        if i in tan_dict.keys():
            tan_dict[i]+=1
        else:
            tan_dict[i]=1

    #idx가 작은~큰 개수대로 정렬
    sorted_tan_dict=dict(sorted(tan_dict.items(), key=lambda x:x[1], reverse=False))


   
    for key in sorted_tan_dict:
        while sorted_tan_dict[key]>0:
            if delNum>0:
                sorted_tan_dict[key]-=1
                delNum-=1
            else:
                break
            
        if delNum<=0:
            break


    for key in sorted_tan_dict.keys():  
        if sorted_tan_dict[key]!=0:
            result+=1

    return result

