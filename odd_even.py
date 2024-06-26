# def is_even(num):
#     return num % 2 == 0

# def get_number():
#     return int(input("Enter a number: "))

# def main():
#     print("Odd or even checker")
#     number = get_number()
#     if is_even(number):
#         print(f"{number} is an even number")
#     else:
#         print(f"{number} is an odd number")

# # Run the main function
# main()



# Creating a function to receive a number and determin if it is even or odd:
# 1. Create a function to obtain the number:
def get_number ():
    return int(input("Enter a number: "))

# 2. Define a function to determine if get_number is even:
def even_number (num):
    return num % 2 == 0

# 3. Create a function to evaluate is get_number is odd or even:
def odd_or_even ():
    print("Odd or even checker -->")
    number = get_number()
    if even_number(number):
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

odd_or_even()