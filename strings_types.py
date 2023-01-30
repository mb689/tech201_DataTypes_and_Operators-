# # # Strings
# #
# # Single_quotes = 'Look! Single quotes'
# # Double_quotes = "Look! Double quotes"
# #
# # print(Single_quotes)
# # print(Double_quotes)
# #
# # escape_example = 'I said \'Wow!\''
# # print(escape_example)
# #
# # quote_in_quote = 'I said "Wow!"'
# # print(quote_in_quote)
# #
# # reverse_quotes = "I said 'Wow!'"
# # print(reverse_quotes)
#
# # String Slicing
#
# Hw = "Hello World!"
#
# print(Hw[7:]) # orld!
# print(Hw[-5:]) # orld!
# print(Hw[:5]) # Hello
# print(Hw[0:5])
#
# # String methods
#
# # strip()
#
# White_space = "Lot's of white space at the end                               "
# print(len(White_space)) # 62
# print(len(White_space.strip())) # 31
#
# # A few more ....
#
# example_text = "Here's some text with lot's of text"
#
# # Count a substring within a string
# print(example_text.count("text")) # 2
#
# # Make everything lowercase
# print(example_text.lower())
#
# # Make everything uppercase
# print(example_text.upper())
#
# # Capitalise things
# print(example_text.capitalize())
#
# # Replace characters/text
# print(example_text.replace("with", ","))
#
# # Concatenation
#
# a = "here "
# b = "more "
# c = "much more"
#
# print(a + b + c)
#
# # Casting
#
# x = 2
# y = 5.4
# z = " There's a number 25.4 unless we put a space"
#
# print(str(x) + str(y) + z)
#
# # String to numeric
#
# int_string = "6"
# print(int(int_string))
# print(type(int(int_string)))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and is {height_cm} cm tall")

name = "snoopy"
years = 52

print(f"{name.upper()} is {years * 7} years old in dog years")

# F-strings to specify precision in rounding and decimals

pi = 3.1459265259

print(f"Pi to 3 decimal places: {pi:.3f}")
print(f"Pi to 3 decimal places: {pi:.5f}")


score = 16
max_score = 26

print(f"You scored {score/max_score : .0%}")