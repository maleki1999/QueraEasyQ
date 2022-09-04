n , m =[int(i) for i in input().split()]
javad = set(input().split())
mostafa = set(input().split())
subscription = javad.intersection(mostafa)

if javad == mostafa :
    print("Both")
elif len(javad - subscription)==0 :
    print("Mohammad Javad")
elif len(mostafa - subscription)==0 :
    print("Mostafa")
else:
    print("None")