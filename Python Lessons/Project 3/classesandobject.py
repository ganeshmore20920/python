class student():
    def check(self):
        if(self.marks >= 40):
            return True
        return False

student1 = student()
student1.name = "Harry"
student1.marks = 85
check2 = student1.check()
print(check2)
student2 = student()
student2.marks = 38
check3 = student2.check()
print(check3)