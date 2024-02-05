import re
txt="hello karthik"
x=re.findall("^hello",txt)
if x:
    print("yes,thr string with'hello'")
    else:
    print("no match")
