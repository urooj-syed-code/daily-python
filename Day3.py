weight = float(input("Enter your weight in kg: "))
height_feet = float(input("Enter your height in feet: "))
height_inches = float(input("Enter your height in inches: "))

total_inches = (height_feet * 12) + height_inches
height_meters = total_inches * 0.0254

bmi = weight / (height_meters ** 2)

print("your BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")    