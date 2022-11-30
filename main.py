from school_schedule.student import Student
from school_schedule.cohort import Cohort
from school_schedule.comparison import get_student_with_more_classes

# first Student instance
samara = Student(
            "Samara", 
            "junior", 
            [ 
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition" 
            ]
        )

samara.add_class("Painting")  # => [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition", "Painting" ]
samara.get_num_classes()  # => 7
samara.summary()  # => "Samara is a junior enrolled in 7 classes"

# second Student instance
claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )
claire.add_class("Painting")  # => [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science", "Painting" ]
claire.get_num_classes()  # => 6
claire.summary()  # => "Claire is a freshman enrolled in 6 classes"

# comparison function
get_student_with_more_classes(claire, samara)  # => samara

# third Student instance
sylvia = Student( 
            "Sylvia", 
            "senior", 
            [ 
                "Calc I", 
                "Spanish Literature", 
                "Biology", 
                "Gym"
            ]
        )

# first Cohort instance
ocelots_cohort = Cohort("Ocelots", [samara, claire])
ocelots_cohort.get_num_students()  # => 2
ocelots_cohort.add_student(sylvia)  # => [samara, claire, sylvia]
print(ocelots_cohort.get_student_summaries()) 
'''
Output of line 58:

Students in Ocelots:
Samara is a junior enrolled in 7 classes
Claire is a freshman enrolled in 6 classes
Sylvia is a senior enrolled in 4 classes
'''