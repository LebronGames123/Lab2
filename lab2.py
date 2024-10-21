print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    x = input("Enter some numbers separated by commas (e.g. 5,67,32): ")
    
    listofnumbers = [float(num.strip()) for num in x.split(",")]
    return listofnumbers
    

def calc_average_temperature(values):
    return sum(values)/len(values)

def calc_median_value(median):
    sorted_median= sorted(median)
    n = len(sorted_median)

    if n%1==1:
        median = sorted_median=[n//2]
    else:
        median = (sorted_median[n//2-1] + sorted_median[n//2])/2

    return median        


def main():
    output = display_main_menu()
    averageval= calc_average_temperature(output)
    medianval=calc_median_value(output)

    print("Average value =",averageval)
    print("Median value =",medianval)


main()

