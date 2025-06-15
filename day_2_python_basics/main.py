from utils import calculate_bmi, is_adult

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

print(f"\n👋 Hello {name}")
print("✅ You are an adult." if is_adult(age) else "❌ You are not an adult.")
print(f"📊 Your BMI is: {calculate_bmi(weight, height)}")
