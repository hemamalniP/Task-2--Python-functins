def unique(a):
    val=[]
    for i in a:
        if i not in val:
            val.append(i)
    return val
            
print(unique([1,2,0,7,2,99,8,9]))
