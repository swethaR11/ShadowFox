#Python program that calculates BMI and determines the category based on user input
# Ask user to input height and weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI using the formula
bmi = weight / (height ** 2)

# Determine and print the BMI category
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

