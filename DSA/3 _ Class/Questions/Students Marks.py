class Student:
    def __init__(self, roll_no, name, age, mobile_no, total_sub):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.mobile_no = mobile_no
        self.total_sub = total_sub
        self.marks = dict()
        self.percent = 0

    def enter_marks(self):
        for i in range(self.total_sub):
            a = input(f"Enter Subject {i+1} Name  : ")
            self.marks[a] = int(input(f"Enter Subject {i+1} Marks : "))
    
    def display_st(self):
        print()
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Mobile  : {self.mobile_no}")
        print(f"Subject : {self.total_sub}")

    def display_sub(self):
        print("\nSubjects :-")
        for i in self.marks.keys():
            print(f"{i} : {self.marks[i]}")

    def percentage(self):
        sum = 0
        for i in self.marks.keys():
            sum += self.marks[i]
        self.percent = (sum*100)/(self.total_sub*100)

        if self.percent > 90:
            print("\nPerformance : Excellent")
        elif self.percent > 70:
            print("\nPerformance : Good")
        else:
            print("\nPerformance : Average")
    


def subjectCount():
    while True:
        sub = int(input("Enter total Subjects : "))
        if sub <= 5 and sub > 0:
            print()
            return sub
        elif sub > 5:
            print("Subjects can't vbe more than 5.\nTry again.")
        else:
            print("Invalid Input! Try Again.")


s1 = Student(54, "Jatin", 22, "8979579642", subjectCount())
s1.enter_marks()
s1.display_st()
s1.display_sub()
s1.percentage()