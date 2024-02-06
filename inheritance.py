class student:
    def __init__(self,name,branch,section):
        self.name=name
        self.branch=branch
        self.section=section
    def show(self):
        print("name is",self.name)
        print("branch is",self.branch)
        print("section is",self.section)
s1=student("abhi","mech","A")
s1.show()
class s2(student):
    def show_s2(self):
        print("name is",self.name)
        print("branch is",self.branch)
        print("section is",self.section)
student2=s2("sai","civil","C")
student2.show_s2()
class s3(student):
    def show3(self):
        print("name is",self.name)
        print("branch is",self.branch)
        print("section is",self.section)
s=s3("mahi","EEE","D")
s.show3()
