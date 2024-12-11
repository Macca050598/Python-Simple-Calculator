def calculator():
    number1 = 0
    number2 = 0
    print("Welcome to the simple calculator")
    print("Choose your first number: ")
    number1 = int(input())
    print("Choose your second number: ")
    number2 = int(input())
    print("\nChoose What Maths you'd like to do...")
    print("1. Add")
    print("2. subtract")
    print("3. divide")
    print("4. Multiply")
    application = input("Choose an option 1 - 4: ")

   
    if application == "1":
        answer = (number1 + number2)
        print(answer)
    elif application == "2":
        print(number1 - number2)
    elif application == "3":
        print(number1 / number2)
    elif application == "4":
        print((number1) * (number2))
    else: 
        print("Please pick a number between 1 and 4")

def main():
    calculator()
if __name__ == "__main__":
    main()