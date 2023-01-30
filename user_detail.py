# Details
name = input("What is your name? ")
age = input("What is your age? ")
height = input("What is your  height? ")
DOB = input("What is your DOB? ")

print(f"Hello {name.capitalize()}, you are {age} years old. Your DOB is {DOB} and you are {float(height):.1f} cm tall ")

# Address Details
house_number = input("House number? ")
house_name = input("House name? ")
street_address = input("Street Address? ")
postcode = input("Postcode? ")

print(f"Your address: {house_number} {house_name.capitalize()} {street_address.capitalize()}, {postcode}")