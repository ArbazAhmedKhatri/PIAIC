a = int(input("enter first numer : "))
b = str(input("enter operator : "))
c = int(input("enter second numer : "))

if   b=="+": print("Your answer is : ",a+c)
elif b=="-": print("Your answer is : ",a-c)
elif b=="*": print("Your answer is : ",a*c)
elif b=="/": print("Your answer is : ",a/c)
elif b=="%": print("Your answer is : ",a%c)
else : print("invalid operator")