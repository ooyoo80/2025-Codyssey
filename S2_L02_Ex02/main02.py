import numpy as np
import csv

file1_path = "S2_L02_Ex02/mars_base/mars_base_main_parts-001.csv"
file2_path = "S2_L02_Ex02/mars_base/mars_base_main_parts-002.csv"
file3_path = "S2_L02_Ex02/mars_base/mars_base_main_parts-003.csv"

def read_csv_create_array(path) :         
    arr = np.genfromtxt(path, delimiter=",", skip_header=1, dtype=None)

    return arr


def merge_array(arr1, arr2, arr3) :
    merge_arr = np.concatenate([arr1, arr2, arr3], axis=0)

    return merge_arr


def calculate_means(arr) :
    dic_item = {}
    dic_means = {}
    for i in arr :
        name = i[0]
        val = i[1]

    #     if name not in dic_item.keys() :

    # print(dic_item)
        
        
        # else :
        #     if name in dic_means.keys() :
        #         dic_means[name].append(val)


def main() :

    arr1 = read_csv_create_array(file1_path)
    print("========== arr1 출력 ==========")
    print(arr1)
    print("========== arr1 출력 완료 ==========\n")

    arr2 = read_csv_create_array(file2_path)
    # print("========== arr2 출력 ==========")
    # print(arr2)
    # print("========== arr2 출력 완료 ==========\n")

    arr3 = read_csv_create_array(file3_path)
    # print("========== arr3 출력 ==========")
    # print(arr3)
    # print("========== arr3 출력 완료 ==========\n")

    parts = merge_array(arr1, arr2, arr3)
    calculate_means(parts)

if __name__ == "__main__" :
    main()