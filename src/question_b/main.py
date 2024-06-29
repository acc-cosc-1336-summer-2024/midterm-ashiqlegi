#add import
from src.question_b.question_b import get_person_category

while True:
    user_input = input("Please enter an age or q to quit the program: ")
    if user_input.lower() == "q":
        break
    category = get_person_category(get_person_category.age)
    print(f"{get_person_category.age} is in the {category}.")

    