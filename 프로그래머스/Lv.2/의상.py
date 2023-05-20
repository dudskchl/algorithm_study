#해시함수 문제


hash_table=[ 0 for _ in range(30)]

def hash_function(key):
    return hash(key) % 30

def set_data(key, value):
    hash_value=hash_function(key)
    hash_table[hash_value]=value

def get_data(key):
    hash_value=hash_function(key)
    return hash_table[hash_value]

def solution(clothes):

    case_num=1

    for i in clothes:
        set_data(i[0],i[1])

    #각 종류에 해당하는 의상 갯수 구하기
    # (A+1) X (B+1)......- 1  => 하나도 없는 경우 x
    
    clothes_dic={}

    for i in clothes:
        if i[1] in clothes_dic.keys(): #의상 딕셔너리에 있으면 개수 추가
            clothes_dic[i[1]]+=1
        else:
            clothes_dic[i[1]]=1     #의상 딕셔너리에 없으면 값 하나 부여
    
    for value in clothes_dic.values():
        case_num*=(value+1)
    
    case_num-=1  #하나도 없는 경우 빼기

    return case_num















##SHA-256
##import hashlib
##
##
##
##def get_key(data):
##    hast_object=hashlib.sha256() #어떤 해시 알고리즘 쓸지 선택
##    hast_object.update(data.encode()) #어떤 값을 해싱할지 선정
##    hex_dig=hash_object.hexdigest()  #16진수로 해쉬 값을 리턴
##    return hash(hex_dig)
##
##
##def hash_functioin(key):
##    return key % 16
##
##
##def save_data_hash_table(data, value):
##    index_key=get_key(data)
##    hash_address=hash_function(index_key)
##    if hash_table[hash_address]!=None:
##        for index in range(len(hash_table[hash_address])):
##            if hash_table[hash_address][index][0]==index_key:
##                hash_table[hash_address][index][1]=value
##                return
##        hash_table[hash_address].append([index_key, value])
##    else:
##        hash_table[hash_address]=[[index_key, value]]
##
##def get_data_hash_table(data):
##    index_key=get_key(data)
##    hash_address=hash_function(index_key)
##    if hash_table[hash_address]!=None:
##        for index in range(len(hash_table[hash_address])):
##            if hash_table[hash_address][index][0]==index_key:
##                reutnr hash_table[hash_address][index][1]
##        return None
##    else:
##        return None
