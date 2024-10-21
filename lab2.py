print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    x = input("Enter some numbers separated by commas (e.g. 5,67,32): ")
    
    listofnumbers = [float(num.strip()) for num in x.split(",")]
    return listofnumbers
    

def calc_average_temperature(values):
    return sum(values)/len(values)

def main():
    output = display_main_menu()
    averageval= calc_average_temperature(output)
    print("Average value =",averageval)


main()

