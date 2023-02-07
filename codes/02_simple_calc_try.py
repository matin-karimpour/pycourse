first_num  = input("Please enter first number: ")
operator   = input("Please enter operator (+ - * /): ")
second_num = input("Please enter second number: ")

try:
    if operator == "+":
        result = float(first_num) + float(second_num)
        print(result)
    elif operator == "-":
        result = float(first_num) - float(second_num)
        print(result)
    elif operator == "*":
        result = float(first_num) * float(second_num)
        print(result)
    elif operator == "/":
        result = float(first_num) / float(second_num)
        print(result)
    else:
        print("you select wrong operator :/")
except:
    print("please enter a number")