import csv
import json
from datetime import datetime


file_path = "S2_L02_Ex01/mission_computer_main.log"
json_file = "S2_L02_Ex01/mission_computer_main.json"

# important_word = ["explosion", "unstable"]


# def filter_important_phrases(path, phrases) :
#     important_lines = []

#     with open(path, "r", encoding="utf-8") as f:
#         f = f.readlines()
    
#     for line in f:
#         line = line.strip()
#         for phrase in phrases:
#             if phrase in line:
#                 important_lines.append(line)
#                 break
    
#     print(important_lines)


def print_info(path) :
    list_separ = []

    with open(path, "r", encoding = "utf-8") as f :
            reader = csv.reader(f)
            header = next(reader)

            print("=========== 전체 출력 ===========")
            for row in reader :
                timestamp = row[0]
                message = row[2]
                list_separ.append([timestamp, message])
                print(*row, end="\n")
            print("=========== 전체 출력 완료 ===========\n")


    print("=========== 타임스탬프, 메시지 출력 ===========")
    print(list_separ)
    print("=========== 타임스탬프, 메시지 출력 완료 ===========\n")


    list_reversed = sorted(list_separ, key=lambda x: datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"), reverse=True)

    print("=========== 역순 정렬 후 출력 ===========")
    print(list_reversed)
    print("=========== 역순 정렬 후 출력 완료 ===========\n")


    dict_separ = {timestamp: message for timestamp, message in list_reversed}
    print("=========== 딕셔너리 변환 후 출력 ===========")
    print(dict_separ)
    print("=========== 딕셔너리 변환 후 출력 완료 ===========\n")
    
    return dict_separ


def save_to_json(dict_separ, file_name) :
    with open(file_name, "w", encoding="utf-8") as jf:
        json.dump(dict_separ, jf, ensure_ascii=False, indent=4)

    print(f"JSON 파일 저장 완료 → {file_name}")


def main() :
    try :
        save_to_json(print_info(file_path), json_file)
        # filter_important_phrases(file_path, important_word)
    except FileNotFoundError :
        print("File not found")
        exit()
    except UnicodeDecodeError :
        print("File is not in utf-8 format")
        exit()
    except Exception as e :
        print(f"An error occurred: {e}")
        exit()


if __name__ == "__main__" :
    main()