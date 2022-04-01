#CALCUATOR

num1 = float(input("Enter your firstnumber: "))
operator = input("Operator:  ")
num2 = float(input("Enter your secondnumber: "))

if num1 + num2 and operator == "+":
     ans1 = num1 + num2
     print(ans1)
elif num1 * num2 and  operator=="*":
    ans2 = num1*num2
    print(ans2)
elif num1 / num2 and operator=="/":
    ans3 = num1/num2
    print(ans3)
elif num1 - num2 and operator=="-":
    ans4 = num1-num2
    print(ans4)    
             