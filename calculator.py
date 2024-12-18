#defining function for the addition
def addition(num1,num2):
    return num1+num2
#defining function for the subtraction
def subtraction(num1,num2):
    return num1-num2
#defining function for the multiplication
def multiplication(num1,num2):
    return num1*num2
#defining function for the division
def division(num1,num2):
    if num2==0:
        return "Error divisionby the zero"
    return num1/num2

   #defining main method for the calculator
def calculator():
    while True:
        print("Select operation for the calculator:")
        print("1.Add")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit from the calculator")
        
        Selection = input("Enter selection(1/2/3/4/5): ")
        if Selection == '5':
            print("exiting the calculator")
            break
        if Selection in ['1','2','3','4']:
            try:
                num1 = float(input("Enter the value of num1: "))
                num2 = float(input("Enter the value of num2: "))

            except ValueError:
                print("Invalid input!")
                continue
            if Selection == '1':
                print(f"{num1} + {num2} = {addition(num1,num2)}")
            elif Selection == '2':
                print(f"{num1} - {num2} = {subtraction(num1,num2)}")
            elif Selection =='3':
                print(f"{num1} * {num2} = {multiplication(num1,num2)}")
            elif Selection =='4':
                print(f"{num1} / {num2} = {division(num1,num2)}")
        else:
            print("please enter the valid operation")

calculator()
