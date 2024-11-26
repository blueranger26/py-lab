# Integer Operations
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
add = x + y
sub = x - y
mul = x * y
div = x / y  # Float result
expo = x ** y
mod = x % y

print("Integer Operations:")
print(f"Addition: {add} (Type: {type(add)})")
print(f"Subtraction: {sub} (Type: {type(sub)})")
print(f"Multiplication: {mul} (Type: {type(mul)})")
print(f"Division: {div} (Type: {type(div)})")
print(f"Exponential: {expo} (Type: {type(expo)})")
print(f"Modulus: {mod} (Type: {type(mod)})")

# String Operations
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
concat = str1 + str2
repeat = str1 * 3  # Repeat the string 3 times

print("\nString Operations:")
print(f"Concatenation: {concat} (Type: {type(concat)})")
print(f"Repetition: {repeat} (Type: {type(repeat)})")

# Boolean Operations
bool1 = bool(int(input("Enter 1 (True) or 0 (False) for first Boolean: ")))
bool2 = bool(int(input("Enter 1 (True) or 0 (False) for second Boolean: ")))
and_op = bool1 and bool2
or_op = bool1 or bool2
not_op = not bool1

print("\nBoolean Operations:")
print(f"AND Operation: {and_op} (Type: {type(and_op)})")
print(f"OR Operation: {or_op} (Type: {type(or_op)})")
print(f"NOT Operation: {not_op} (Type: {type(not_op)})")
