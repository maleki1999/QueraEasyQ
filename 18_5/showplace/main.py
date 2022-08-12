def creat_L_R(k):
    global c
    if c < k :
        c+=1
        return f"{'ghorfe'+str(c)}" 
    else:
        return f"{'.'*7}" 
    
k = int(input())
last = f"{'#'*23}"
odd = f"{'#'*8}{'.'*7}{'#'*8}"
global c
c=0

for i in range(1,9):
    if i%2 == 0:
        print(f"#{creat_L_R(k)}"+f"{'.'*7}"+f"{creat_L_R(k)}#")
    else:
        print(odd)
print(last)