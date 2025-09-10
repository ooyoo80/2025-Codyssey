import math

dic_meterial = {
    "유리" : 2.4,
    "알루미늄" : 2.7,
    "탄소강" : 7.85
}

set_thickness = 1


def sphere_area(diameter, meterial, thickness) :



def main() :
    try :
        while True :
            if input_choice == '1' :
                input_choice = input("Choose the operation (1: start, [any other]: quit) : ")
                input_diameter = float(input("Enter the diameter of the sphere (in m) : "))

                while True :
                    input_meterial = input("Enter the meterial of the sphere (유리, 알루미늄, 탄소강) : ")
                    if input_meterial not in dic_meterial.keys() :
                        print("Invalid meterial. Please enter one of the following: (유리, 알루미늄, 탄소강)")
                        continue
                    else :
                        break
                    
                sphere_area(input_diameter, input_meterial, set_thickness)

            else :
                print("Ending the program.")
                break

    except Exception as e :
        print("Error :", e)
        exit()


if __name__ == "__main__" :
    main()