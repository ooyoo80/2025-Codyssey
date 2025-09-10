import csv

file1_path = "S2_L02_Ex02/mars_base/Mars_Base_Inventory_List.csv"

def read_inventory(path) :
    with open(path, "r", encoding="utf-8") as f :
        reader = csv.reader(f)
        header = next(reader)

        print("=========== 전체 출력 ===========")
        for row in reader :
            print(*row, end="\n")
        print("=========== 전체 출력 완료 ===========\n")

    return header


def change_inventory_to_list(path) : 
    list_inventory = []
    with open(path, "r", encoding="utf-8") as f :
        reader = csv.reader(f)
        header = next(reader)

        for row in reader :
            for i in range(len(row)) :
                try :
                    row[i] = float(row[i])
                except ValueError :
                    continue
            list_inventory.append(row)
    
    print("=========== 리스트 출력 ===========")
    for row in list_inventory :
        print(row)
    print("=========== 리스트 출력 완료 ===========\n")

    return list_inventory


def sorted_list_flammability(list_inventory, index) :
    flammability_index = 0
    
    for inx in range(len(index)):
        if index[inx] == "Flammability" :
            flammability_index = inx
            break
     
    list_reversed = sorted(list_inventory, key=lambda x: x[flammability_index], reverse=True)
    print("=========== flammability 역순 정렬 후 출력 ===========")
    for row in list_reversed :
        print(row)
    print("=========== flammability 역순 정렬 후 출력 완료 ===========\n")

    return list_reversed


def filter_as_flammability(index, list_inventory) :
    list_filter = []
    flammability_index = 0
    
    for inx in range(len(index)):
        if index[inx] == "Flammability" :
            flammability_index = inx
            break

    for row in list_inventory :
        
        row_val = float(row[flammability_index])

        if row_val >= 0.7 :
            list_filter.append(row)

    print("=========== flammability 0.7 이상 필터링 출력 ===========")
    for row in list_filter :
        print(row)
    print("=========== flammability 0.7 이상 필터링 출력 완료 ===========\n")

    return list_filter


def main() :
    try: 
        header = read_inventory(file1_path)
        list_necessary = change_inventory_to_list(file1_path)
        list_reversed = sorted_list_flammability(list_necessary, header)
        filter_as_flammability(header, list_reversed)

    except FileNotFoundError :
        print("File not found")
        exit()
        

if __name__ == "__main__" :
    main()