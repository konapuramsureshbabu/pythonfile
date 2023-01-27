def fun1(list_a,num):
    result=[]
    if num==2:
        result.append(tuple(list_a))
    elif num>2:
        for i in range(len(list_a)):
            if len(list_a)==1:
                break 
            else:
                result.append(tuple(list_a[0:2]))
                for i in list_a[0:2]:
                    list_a.remove(i)
    return result 

list_a=[1,3,4,5,7,8]
num=len(list_a)
result=fun1(list_a,num)   
print(*result)