a=int(input("Enter a Number:"))
b = a%2
fact = 1
temp=a
rev=0
if b!=0:
   print("It is Odd")
   print("The digit present in this factorial are",end = " = ")
   for i in range(1,a+1):
       print(i,end=" ")
       fact = fact*i
   print()     
   print("The factorial of the number is",end = " = ")
   print(fact)
else:
   print("It is even")
   while(a>0):
        dig= a % 10
        rev=rev*10+dig
        a=a//10
   if(temp==rev): 
       print("The number is a palindrome!")   
   else:
         print("The number isn't a palindrome!")
       
  
