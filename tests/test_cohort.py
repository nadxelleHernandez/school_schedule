from school_schedule.cohort import Cohort
from school_schedule.student import Student

def test_initialization_with_students():
    #Arrange
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

    # Act
    new_cohort = Cohort("Ocelots", [claire, sylvia])

    # Assert
    assert new_cohort.name == "Ocelots"
    assert len(new_cohort.student_list) == 2
    assert claire in new_cohort.student_list
    assert sylvia in new_cohort.student_list

def test_add_valid_student_to_cohort():
    #Arrange
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
    
    new_cohort = Cohort("Ocelots", [claire])

    # Act
    new_cohort.add_student(sylvia)

    # Assert
    assert len(new_cohort.student_list) == 2
    assert claire in new_cohort.student_list
    assert sylvia in new_cohort.student_list