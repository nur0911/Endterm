
# Task 3
class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self.overall_GPA = None
        self.status = None

    def calculGPA(self):
        total_points = 0
        total_credits = 0

        for course in self.scores:
            score = self.scores[course]['score']
            credits = self.scores[course]['credits']
            total_points += score * credits
            total_credits += credits

        if total_credits != 0:
            self.overall_GPA = round(total_points / total_credits, 2)
        else:
            self.overall_GPA = 0.0

        self.setStatus()

    def setStatus(self):
        if self.overall_GPA is not None:
            if self.overall_GPA >= 1.0:
                self.status = "Passed"
            else:
                self.status = "Not Passed"

    def showGPA(self):
        if self.overall_GPA is not None:
            print(f"GPA for {self.name}: {self.overall_GPA}")
        else:
            print("GPA not calculated yet.")

    def showStatus(self):
        if self.status is not None:
            print(f"Status for {self.name}: {self.status}")
        else:
            print("Status not available yet.")


scores = {
    'Math': {'score': 4.3, 'credits': 4},
    'Chemistry': {'score': 3.3, 'credits': 3},
    'English': {'score': 4.0, 'credits': 4}
}

student1 = Student("Alice", 3, scores)
student1.calculGPA()
student1.showGPA()
student1.showStatus()
