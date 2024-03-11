"""
Like in any other programming language python also has it's set of operators
Operators in Python are:
Operators are the mathmatical and logical symbols to perform operators in a programming language. 
1. Arithmetic operators
2. Logical operators
3. Relational operators
4. Assignment operators
5. Membership operators
6. Identity operators
"""

#1. Arithmetic operators
print("\nARITHMETIC OPERATORS")

#Addition(+)
a = 1 #a is a variable, + is operator and 1 is a data of integer type
b = 2 
print(f"{a} + {b} = ",a + b) # print() is a python built-in function to view the results in a console

#Subtraction(-)
a = 20 
b = 7
print(f"{a} - {b} = ",a - b)

#Division(/)
a = 30
b = 20
print(f"{a} / {b} = ",a / b)

#Multiplication(*)
a = 9
b = 8
print(f"{a} * {b} = ",a * b)

#Exponentiation(**)
a = 4
b = 2
print(f"{a} ** {b} = ",a ** b)

#Floor Division(//)
a = 10
b = 3
print(f"Floor Division ({a} // {b}) =",a//b)

#Modulus
a = 10
b = 3
print(f"Quotient give Remainder ({a} % {b}) =", a % b)


"""  
2. Logical Operators (and, or, not)
Lets see the truth table of each logical operators
"""
print("\n\nLOGICAL OPERATOR")

print("\nLogical And")
print(f"0 and 0 = ",False and False)
print(f"0 and 1 = ",False and True)
print(f"1 and 0 = ",True and False)
print(f"1 and 1 = ",True and True)

print("\nLogical Or")
print(f"0 or 0 = ",False or False)
print(f"0 or 1 = ",False or True)
print(f"1 or 0 = ",True or False)
print(f"1 or 1 = ",True or True)

print("\nNot Operator")
print(f"not false = ",not False)
print(f"not true = ",not True)

"""
Relational operators
<, >, <=, >=, !=, == are the relational operators
Result of relational operators is boolean (True/False)
"""
print("\n\nRELATIONAL OPERATOR")

print("5 > 2 = ", 5 > 2)
print("2 > 9 = ", 2 > 9)
print("2 < 2 = ", 2 < 2)

print("3 >= 3",3 >= 3)
print("4 != 2",4 != 2)
print("4 != 4",4 != 4)
print("5 == 5",5 == 5)

"""
Assignment Operators
=, +=, -+, *= are the assignment operators 
"""
print("\n\nASSIGNMENT OPERATORS")
a = 1
print(f"a = {a}")

a += 1
print(f"a += {a}")

a -= 1
print(f"a -= {a}")

_ = 3
print(f"_ = {_}")

"""
Membership operators (in and not in) 
Result of membership operation is in boolean (True/False)
Checks whether an element is a member of iterable
Iterable means sequence of data. List, tuple etc. are the iterable in python
"""
print("\n\nMEMBERSHIP OPERATORS")
vowels = ["a", "e", "i", "o", "u"]
print(vowels)

print("Check b in vowels")
print("b" in vowels)

print("Check b not in vowels")
print("b" not in vowels)

"""
Identity operator (is, is not)
They check whether two identities are same object or not
"""
print("\n\nPYTHON IDENTITY OPERATORS")
a = 1
b = 1
print("a is b")
print(a is b)

print("\na is not b")
print(a is not b)

a = []
b = []
print("\nPython List")
print("a is b")
print(a is b)
print("\na is not b")
print(a is not b)







