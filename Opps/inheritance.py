class Employee:
    start_time = "10 am"
    end_time = "6 am"

class Teacher(Employee):
    
    def __init__(self , subject):
        self.subject = subject


t1 = Teacher("Maths")

print(f"teacher start time {t1.start_time} and end time {t1.end_time} and the subject is {t1.subject}")
        