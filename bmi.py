def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / height ** 2
    print("Your BMI is = " + str(bmi))

    if bmi < 18.5:
        return -1  # Underweight
    elif 18.5 <= bmi < 25:
        return 0   # Normal weight
    else:
        return 1   # Overweight

# Example usage
result = calculate_bmi(weight=81, height=1.77)
print("Classification Code:", result)
