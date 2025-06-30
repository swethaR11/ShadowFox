#Write a function that takes two arguments, 145 and 'o' , and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.
def format_value(number, format_spec):
    return format(number, format_spec)

# Call the function with 145 and 'o'
result = format_value(145, 'o')

# Print the result
print("Formatted result:", result)
