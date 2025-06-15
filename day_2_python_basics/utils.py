def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def is_adult(age):
    return age >= 18
