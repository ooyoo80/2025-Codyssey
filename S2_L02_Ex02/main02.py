import numpy as np
import csv

file1_path = "S2_L02_Ex02/mars_base/mars_base_main_parts-001.csv"
file2_path = "S2_L02_Ex02/mars_base/mars_base_main_parts-002.csv"
file3_path = "S2_L02_Ex02/mars_base/mars_base_main_parts-003.csv"
csv_file_path = "S2_L02_Ex02/mars_base_result/parts-to-work-on.csv"
new_header_format = ['parts', 'strength_mean']


def read_csv_create_array(path) :         
    arr = np.genfromtxt(path, delimiter=",", skip_header=1, dtype=None)
        
    return arr


def merge_array(arr1, arr2, arr3) :
    merge_arr = np.concatenate([arr1, arr2, arr3], axis=0)

    print("========== 병합 arr 출력 ==========")
    print(merge_arr)
    print("========== 병합 arr 출력 완료 ==========\n")

    return merge_arr


def calculate_means(arr) :
    dic_means = {}
    for i in arr :
        name = str(i[0])
        val = int(i[1])

        if name not in dic_means.keys() :
            dic_means[name] = [val]
        else :
            dic_means[name].append(val)

    for key in dic_means.keys() :
        total = sum(dic_means[key]) / len(dic_means[key])
        dic_means[key] = round(total, 3)
    
    print("========== 전체 평균 출력 ==========")
    for key, val in dic_means.items() :
        print(f"{key} : {val}")
    print("========== 전체 평균 출력 완료 ==========\n")

    return dic_means
        

def filter_by_means(dic) :
    dic_filtered = {}
    
    for key, val in dic.items() :
        if val >= 50 :
            dic_filtered[key] = val

    print("========== 필터링 값 출력 ==========")
    for key, val in dic_filtered.items() :
        print(f"{key} : {val}")
    print("========== 필터링 값 출력 완료 ==========\n")

    list_filtered = list(dic_filtered.items())

    return list_filtered


def save_to_csv(header, data, file_name) :
    try :
        with open(file_name, 'w', newline='', encoding='utf-8') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(header)

            csv_out.writerows(data)

        # with open(file_name, 'w', newline='', encoding='utf-8') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(header)   # 헤더 작성
        #     writer.writerows(data)    # 데이터 작성

        print(f"CSV 파일 저장 완료 → {file_name}")

    except FileNotFoundError :
        print("File not found")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()


def main() :

    arr1 = read_csv_create_array(file1_path)
    print("========== arr1 출력 ==========")
    print(arr1)
    print("========== arr1 출력 완료 ==========\n")

    arr2 = read_csv_create_array(file2_path)
    print("========== arr2 출력 ==========")
    print(arr2)
    print("========== arr2 출력 완료 ==========\n")

    arr3 = read_csv_create_array(file3_path)
    print("========== arr3 출력 ==========")
    print(arr3)
    print("========== arr3 출력 완료 ==========\n")

    parts = merge_array(arr1, arr2, arr3)
    dic_means = calculate_means(parts)
    list_filtered = filter_by_means(dic_means)

    save_to_csv(new_header_format, list_filtered, csv_file_path)


if __name__ == "__main__" :
    main()