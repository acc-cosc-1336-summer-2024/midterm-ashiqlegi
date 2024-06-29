#add import
from src.question_d.question_d import get_sum_of_evens

while True:
    user_input = input("Please enter an even number or q to quit the program: ")
    if user_input.lower() == "q":
        break
    else:
        print(f" The sum of all the even numbers upto {get_sum_of_evens.num} is {sum} ")
