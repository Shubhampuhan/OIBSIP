def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = get_user_input("Enter your weight in kilograms: ")
    height = get_user_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print("BMI Category:", category)

if __name__ == "__main__":
    main()
