print("*** welcome to  YUMMY WORLD ***")

print("ans yes or no")

a=input(" would you like to add toppings on your pizza?:")
a=a.lower()
print(a)
n=int(input("how many toppings would you like to add ?"))

i=1
print("enter your topping choices and if u are done say quit")
for i in range(1,n+i):
    toppings =input ("your toppings...your choice...*** ENTER YOUR CHOICE***  : ")
    toppings=toppings.lower()
    print(i ,".",toppings )
    
    if toppings!="quit":
        print ("WE WILL ADD ",i,".",toppings, "TO  YOUR YUMMY PIZZA")
        i=i+1
        
    else:
        toppings=="quit"
        
        break
print("THANK YOU.... FOR VISITING  AND YOUR YUMMY PIZZA.... IS  GETTING READY FOR YOU...HAVE A GREAT DAY")
    
