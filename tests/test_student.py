from school_schedule.student import Student
import pytest


# test constructor
def test_init_construction_method():
    name = "Yvette"
    grade = "senior"
    classes = ["Calc I", "Calc II"]

    yvette = Student(name, grade, classes)
    assert yvette.name == name
    assert yvette.grade == grade
    assert yvette.classes == classes
    assert len(yvette.classes) == 2
    assert classes[0] in yvette.classes
    assert classes[1] in yvette.classes

def test_invalid_constructor_parameters():
    with pytest.raises(ValueError):
        name = None
        grade = None
        classes = None
        yvette = Student(name, grade, classes)


def test_add_valid_class_to_Student():
    name = "Nadxelle"
    grade = "senior"
    classes = ["Calc I", "Physics"]
    nad = Student(name, grade, classes)

    class_name = "Geometry"
    nad.add_class(class_name)
    assert class_name in nad.classes
    assert len(nad.classes) == 3


def test_add_none_or_empty_class():
    name = "Yvette"
    grade = "senior"
    classes = ["Calc I", "Calc II"]
    yvette = Student(name, grade, classes)

    class_name1 = None
    class_name2 = ""
    yvette.add_class(class_name1)
    yvette.add_class(class_name2)

    assert len(yvette.classes) == 2


def test_get_num_classes():
    name = "Yvette"
    grade = "senior"
    classes = ["Calc I", "Calc II"]
    yvette = Student(name, grade, classes)

    assert yvette.get_num_classes() == 2

def test_get_num_classes_with_empty_classes():
    name = "Yvette"
    grade = "senior"
    classes = []
    yvette = Student(name, grade, classes)

    assert yvette.get_num_classes() == 0

def test_summary():
    name = "Yvette"
    grade = "senior"
    classes = ["Calc I", "Calc II"]
    yvette = Student(name, grade, classes)

    assert yvette.summary() == "Yvette is a senior enrolled in 2 classes"


def test_summary_no_classes():
    name = "Yvette"
    grade = "senior"
    classes = []
    yvette = Student(name, grade, classes)

    assert yvette.summary() == "Yvette is a senior enrolled in 0 classes"