print("Hello, doing DevOps practical")

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

if(a>b):
    a = a-b
    b = a+b

    print(f"Value of a : {a} & b : {b}")
else:
    b = b-a
    a = b+a

    print(f"Value of a : {a} & b : {b}")   
