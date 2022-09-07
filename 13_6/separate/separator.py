def separator(ls):
    even , odd = [] , []
    for i in ls:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
#     even , odd = [i for i in ls if i%2 == 0] , [i for i in ls if i%2 != 0]
    return (even , odd)
