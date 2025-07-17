def main() :
    input_num = input()
    list_num = [float(x) for x in input_num.split()]
   
    max = 0

    for i in range(len(list_num)) :
        if list_num[i] > max :
            max = list_num[i]
    

    min = max

    for i in range(len(list_num)) :
        if list_num[i] < min :
            min = list_num[i]


    print(f"Min: {min}, Max: {max}")


if __name__ == "__main__" :
    main()