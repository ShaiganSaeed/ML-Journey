name =input("Enter Your Name: ")

name.strip() # removes the white spaces from the beginning and end of the string
print(f"Hello, {name}")

name=name.title() # makes the first letter of "each" word capitalized
print(f"Hello, {name}")

name= name.capitalize() # Capitalizes the first letter of the string and makes the rest of the letters lowercase
print(f"Hello, {name}")

name=name.title().capitalize() # using more than one function in a single line of code
print(f"Hello, {name}")

name=input("Enter your name: ").strip().title().capitalize() # doing all the above in a single line of code

# splitting first and last name
first,last=name.split(" ")

print(f"Hello, {last}")


