def main() :
    try :
        input_num = input()

        if not input_num :
            print("Invalid input.")
            exit()

        list_num = [float(x) for x in input_num.split()]
    
        max = min = list_num[0]

        for num in list_num[1:] :
            if num > max :
                max = num
            elif num < min :
                min = num


        print(f"Min: {min}, Max: {max}")

    except ValueError :
        print("Invalid input.")
        exit()


if __name__ == "__main__" :
    main()