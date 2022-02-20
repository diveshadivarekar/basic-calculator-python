num1=int(input("enter first number = "))
num2=int(input("enter second number = "))

print("\nnumber for your operator\n1 add\n2 subt \n3 multiplication\n4 divide\n5 modulus\n")
op=str(input("enter your operator = "))

if op == "+" or op == "1":
    print(f"answer{num1+num2}")
elif op == "-" or op == "2":
    print(f"answer{num1-num2}")
elif op == "*" or op == "3":
    print(f"answer{num1*num2}")
elif op == "/" or op == "4":
    print(f"answer{num1/num2}")
elif op == "%" or op == "5":
    print(f"answer : {num1%num2}")
else :
    print("invalid operator")
print("thanks for using my calculator")