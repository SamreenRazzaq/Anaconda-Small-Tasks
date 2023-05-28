print("Samreen Razzaq, 2021-CE-13, Computer Engineering from UET Lahore")
#TASK2:

print("    *     ")
print("   ***    ")
print("  *****   ")
print(" *******  ")
print("********* ")
#TASK3:
    
miles=int(input("enter number in miles: "))
kilo=(miles/1.6)
print("number in km is:",kilo)
#TASK4:
    
x=int(input("enter 1st number: " ))
y=int(input("enter 2nd number: " ))
z=x
x=y
y=z
print("after swaping 1st number become", x )
print("after swaping 2nd number become", y )
#TASK5:
    
C = int(input("enter temperature in celcius", ))
F = (9/5)*C + 32
print("temperature in faherenheit is ",F)
#TASK6:
    
hour=int(input("enter number in hour",))
week=(1/168)*hour
day=(1/24)*hour
print("number of hour in hour",hour)
print("number of hour in week",week)
print("number of hour in day",day) 
#TASK7:
    
x=int(input("Enter 1st number: ")) 
y=int(input("Enter 2nd number: "))
if (y==x**3):
    print("True")
else:
    print("False")
#TASK8:

x = int(input("english subject's number is = "))
y = int(input("math subject's number is = "))
z = int(input("urdu subject's number is = "))
if ((x+y+z)/3 >= 75):
    print("admission granted")
else:
    print("you are above standard")
#TASK9:
    
x=int(input("enter your salary: "))
y=int(input("enter your scale: "))
if(y>16):
    bonus=x*40/100
    total=x+bonus
    print ("your total salary is",total)
else :
    bonus=x*20/100
    total=x+bonus
    print ("your total salary is",total) 
#TASK10:
    
x=int(input("enter test score"))
if (x >= 80):
    print("grade A")
elif (x >= 70)and(x <= 79):
    print("grade B")    
elif (x >= 60)and(x <= 69):
    print("grade C")    
elif (x >= 50)and(x <= 59):
    print("grade D")
else:
    print ("grade F")
#TASK11:
    
x=1
while (x<=5):
    print ("Pakistan")
    x=x+1
#TASK12:
    
count=int(input("average of how many numbers"))
i=1
sum=0
while(i<=count):
    print("enter number:",i)
    n=int(input())
    sum=sum+n
    i=i+1
    
    
average=sum/count
print("average is ",average)
#TASK13:
    
x=int(input("Enter number: "))
for i in range(1,11):
    print("%d*%d=%d"%(x,i,x*i))
#TASK14:
    
x = int(input("enter a number to find factorial: "))
y = 1
for i in range(1,x+1):
    y = y * i
print("factorial of a number is:  ",y)
#TASK15:
    
x=int(input("Enter number: "))
for i in range(5):
    if (x>0):
        print("%d is greater than zero" %x)
        
        y=int(input("Enter next number "))
        if (y>0):
            print("%d is also greater than zero"%y)
        elif (y==0):
            print("%d is equal to zero"%y)
        else:
            print("Negative")
            
        break
    if (x<0):
        continue

else:
    print("Negative")
#TASK16:
    
x=int(input("Enter number: "))
for i in range(x):
    if(x%2==0):
        print("%d is even number: "%x)
        y=int(input("Enter next number: "))
        if(y%2==0):
            print("%d is even number "%y)
            break
        break
        print("your number is odd")
#TASK17:
    
print("Block of Stars")
for i in range(5):
    for j in range(5):
        print("*",end=' ')
    print()
#TASK18:
    
print("Right angle Triangle")
for i in range(5) :
    for j in range(i+1):
        print("*",end=' ')
    print()
#TASK19:
    
print("Left angle Triangle")
for i in range(1,6) :
    for j in range(1,6-i):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()
#TASK20:
    
print("Inverted Right angle Triangle")
for i in range(5,0,-1) :
    for j in range(1,i+1):
        print("*",end=' ')
    print()
#TASK21:
    
print("Inverted Left angle Triangle")
for i in range(5,0,-1) :
    for j in range(1,6-i):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()
    


    

        
   