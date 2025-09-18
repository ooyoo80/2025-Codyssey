import time
from zipfile import ZipFile
from multiprocessing import Process
from itertools import product


zip_file_path = "S2_L05_Ex01/emergency_storage_key.zip"

def certain_word(pw) :
    list_specific = []
    # 사전단어와 비교
    # 말이 되는 단어면 우선 탐색


def unlock_zip(list_cases) :
    start_time = time.time()
    
    #기능구현 -> 브루투포스 => 솎아내기
    
    print("--- %s seconds ---" % (time.time() - start_time))


def check_pw(file_name, pw) :
    try :
        with ZipFile(file_name, "r") as zip:
            zip.extractall(path="uncompressed", pwd=pw.encode("utf-8"))

        # txt 파일로 저장
        return 1
    
    except RuntimeError :
        return 0
    

def save_txt(file, pw) :
    with open(file, "w", encoding='utf-8') as f :
        f.write(pw)

def main() :
    print(1)


if __name__ == "__main__" :
    main()