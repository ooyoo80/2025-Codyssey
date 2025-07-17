def main() :
    try:
        input_num = input()

        if not input_num :
            print("Invalid input.")
            exit()
    

        list_num = [float(x) for x in input_num.split()]
        
        if len(list_num) == 1:
            print("Invalid input.")
            exit()
        
        leng = len(list_num)
        for i in range(leng):
            for j in range(leng - i - 1):
                if list_num[j] > list_num[j + 1]:
                    list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]


    # 9 6 1 7
        
        print("Sorted:", *list_num)

    except ValueError :
        print("Invalid input.")
        exit()


if __name__ == "__main__" :
    main()