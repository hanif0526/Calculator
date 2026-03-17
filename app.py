red = "\033[31m"
yellow = "\033[32m"
reset = "\033[0m"
blue = "\033[34m"

def add(a,b):
    return a+b
    
def times(a,b):
    return a*b
 
def minus(a,b):
    return a-b
    
def divide(a,b):
    return a/b
    
print(f"{blue}\nChoose + × - : {reset}")

choice = input(f"{red}\nEnter your choice : {reset}")

num1 = float(input(f"{yellow}Enter your first number : {reset}"))
num2 = float(input(f"{yellow}Enter your second number : {reset}"))

if choice == "+":
    print(f"Result : {add(num1,num2)}")
elif choice == "×":
    print(f"Result : {times(num1,num2)}")
elif choice == "-":
    print(f"Result : {minus(num1,num2)}")
elif choice == ":":
    print(f"Result : {divide(num1,num2)}")
else:
    print("Incorrect input")
