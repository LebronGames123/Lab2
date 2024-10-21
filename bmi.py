def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    bmi = weight/height**2
    print("Your BMI is =" + str(bmi))

    if bmi<18.5:
        print ("Under Weight")
    elif bmi>=18.5 and bmi<=25:
        print ("Normal Weight")
    elif bmi>25:
        print("Over Weight")    
calculate_bmi(weight=81,height=1.77)

