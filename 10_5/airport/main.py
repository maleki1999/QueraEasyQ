def take_off(air_id,air_status,bound_status,free_b):
    air_st = air_status[air_id]
    if air_st == 1 and len(free_b)==0:
        print("NO FREE BOUND")
    elif air_st == 2 :
        print("YOU ARE TAKING OFF")
    elif air_st == 3 :
        print("YOU ARE LANDING NOW")
    elif air_st == 4 :
        print("YOU ARE NOT HERE")
    else :
        air_status[air_id] = 2
        bound_status[free_b.pop(0)]=air_id
        
def landing(air_id,air_status,bound_status,free_b):
    air_st = air_status[air_id]
    if air_st == 1 :
        print("YOU ARE HERE")
    elif air_st == 2 :
        print("YOU ARE TAKING OFF")
    elif air_st == 3 :
        print("YOU ARE LANDING NOW")
    elif air_st == 4 and len(free_b)==0:
        print("NO FREE BOUND")
    else :
        air_status[air_id] = 3
        bound_status[free_b.pop()]=air_id
       
    
n , k = [int(i) for i in input().split()]
airplanes_id = [input() for _ in range(n)]
n_ord = int(input())
orders = [input() for _ in range(n_ord)]
airplanes_status = {}
bound_status = {}
for i in airplanes_id : airplanes_status[i] = 1
for i in range(k) : bound_status[i+1] = "FREE"
free_bound = [key for key in bound_status.keys() if bound_status[key] == "FREE"]
free_bound.sort() 

for order in orders :
    q,air_id = order.split()
    if airplanes_status.get(air_id) == None :
        airplanes_status[air_id] = 4
    if q=="TAKE-OFF":
        take_off(air_id,airplanes_status,bound_status,free_bound)
    elif q=="LANDING":
        landing(air_id,airplanes_status,bound_status,free_bound)
    elif q=="PLANE-STATUS":
        print(airplanes_status[air_id])
    elif q=="BAND-STATUS":
        print(bound_status[int(air_id)])