from utils import calculate_bmi, is_adult

print("Running Tests...\n")

print("Test BMI:", calculate_bmi(70, 1.75))  # ~22.86
print("Is 17 adult?", is_adult(17))         # False
print("Is 21 adult?", is_adult(21))         # True
