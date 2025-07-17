def main() :
    try :
        input_num = float(input("Enter number: "))
    except ValueError :
        print("Invalid number input.")
        exit()

    try :
        input_exponent = int(input("Enter exponent: "))
    except ValueError :
        print("Invalid exponent input.")
        exit()

    abs_exponent = abs(input_exponent)


    result = 1



    for i in range(abs_exponent) :
        result *= input_num

    if input_exponent < 0 :
        result = 1/result

    if result.is_integer :
        print(f"Result: {int(result)}")
    else :
        print(f"Result: {round(result,3)}")



if __name__ == "__main__":
    main()