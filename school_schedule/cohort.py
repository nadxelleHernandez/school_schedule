# ocelots_cohort = Cohort("Ocelots", [samara, claire])
# ocelots_cohort.get_num_students()  # => 2
# ocelots_cohort.add_student(sylvia)  # => [samara, claire, sylvia]
# ocelots_cohort.get_student_summaries() 
'''
Output of line 58:

Students in Ocelots:
Samara is a junior enrolled in 7 classes
Claire is a freshman enrolled in 6 classes
Sylvia is a senior enrolled in 4 classes
'''

class Cohort: 
    def __init__(self, name, student_list):
        self.name = name
        self.student_list = student_list

    def get_num_students(self):
        return len(self.student_list)

    def add_student(self, new_student):
        self.student_list.append(new_student)

    def get_student_summaries(self):
        result = f"Students in {self.name}: \n"
        for student in self.student_list:
            result += student.summary() + "\n"

        return result
