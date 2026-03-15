def add(a,b):
    return a+b
    
def times(a,b):
    return a*b
 
def minus(a,b):
    return a-b
    
def divide(a,b):
    return a/b
    
print("\nChoose + × - : ")

choice = input("\nEnter your choice : ")

num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))

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
