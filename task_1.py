def iterativeFactorial(n):
    result = 0
    try:
        if n < 0:
            raise ValueError("Cannot find factorial of negative number")
        elif n < 2:
            result = 1
        else:
            factorial = 1
            while(n >= 2):
                factorial = factorial * n
                n = n - 1
            result = factorial
        
        return result
    except Exception as e:
        print(e)

def recursiveFactorial(n):
    try:
        if n < 0:
            raise ValueError("Cannot find factorial of negative number")
        elif n < 2:
            return 1
        else:
            return n * recursiveFactorial(n - 1)
    except Exception as e:
        print(e)

def decideCalculation():
    print("\t Select 1 for iteration \n\t Select 2 for recursion \n")
    
    try:
        choice = int(input("Enter from the mentioned choice: "))
        fact = 0
        if choice in range(1,3):
            n = int(input("Enter a number: "))
            if choice == 1:
                fact = iterativeFactorial(n)
            elif choice == 2:
                fact = recursiveFactorial(n)
        else:
            raise ValueError("\nError input. \n Run the program again and please select correct choice from above")

        print(f"Factorial of {n} is {fact}")
    except ValueError as e:
        print(e)

decideCalculation()