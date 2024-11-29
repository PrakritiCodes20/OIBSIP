# BMI Calculator
def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)
    return bmi
# User input for weight and height
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in m:"))
#  Calculate BMI using function
result = calculate_bmi(weight,height)
print("Your BMI is", result)
# Interpretation of BMI  categories
if result < 18.5:
 print("You are Underweight.")
elif 18.5 <= result <= 24.9:
 print("You have a normal weight.")
elif 25 <=  result <= 29.9:
  print("You are Overweight.")
else:
  print("You are Obese.")

    