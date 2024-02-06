#number palindrome
n=int(input("enter a number"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("its a palindrome")
else:
    print("its not a palindrome")

#string palindrome
str="mom"
rev_str=""
for i in str:
    rev_str=rev_str+i
if(rev_str==str): 
    print("it is a palindrome")
else:
    print("its not a palindrome")
