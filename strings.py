# how to do indexing and slicing
wish="Hello World"
print(wish[2])
print(wish[0:5])
print(wish[::-1]) #print value in reverse order
print(wish[::2])
#concatenation
a="python"
b="3"
print(a+b)
#len of str
print(len(wish))
#membership operators
print("y"in"python")
print("y"not in "python")
#to remove the spaces
wish="  Hello World   "
b=wish.strip()
print(b)
#how to use find operator
wish="Hello World"
b=wish.find("W")
print(b)
b=wish.index("World")
print(b)
#replace function
b=wish.replace("World","Saikiran")
print(b)
print(id(b))
#split function
message="Python programming language"
a=message.split()
print(a)
#join function
list=['python','programming','language']
a="-".join(list)
print(a)
#how to change cases of string 
a="Python programming language"
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.capitalize())
print(a.title())
#count function
a=("python python python")
b=a.count("python")
print(b)



