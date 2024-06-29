#add import

from src.question_a.question_a import is_prime

while True:
    user_input = input("Please enter a number or q to exit): ")
    if user_input.lower() == "q":
        break
    num = int(user_input)
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

