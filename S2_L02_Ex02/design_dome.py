import math

dic_meterial = {
    "유리" : 2.4,
    "알루미늄" : 2.7,
    "탄소강" : 7.85
}
set_thickness = 1


def sphere_area(diameter, meterial, thickness) :
    density = dic_meterial[meterial]
    R_outer = (diameter*100)/2 # m -> cm
    R_inner = R_outer - thickness

    surface_area = 2 * math.pi * (R_outer ** 2)

    volume = (2/3) * math.pi * (R_outer**3 - R_inner**3)
    
    mass = (volume * density) / 1000 # g -> kg
    mars_weight = mass * 0.38 # kgf

    if diameter.is_integer() :
        diameter = int(diameter)

    return {"재질": meterial, 
            "지름": diameter,
            "두께": thickness,
            "면적": round(surface_area, 3),
            "무게": round(mars_weight, 3)
        }


def main() :
    while True :
        input_choice = input("Choose the operation (1: start, [any other]: quit) : ")
        if input_choice == '1' :

            while True :
                try :
                    input_diameter = float(input("Enter the diameter of the sphere (in m) : "))
                    if input_diameter <= 0 :
                        print("Diameter must be greater than 0. Try again.")
                        continue
                    break
                except ValueError :
                    print("You entered a wrong type. Try again.")

            while True :
                input_meterial = input("Enter the meterial of the sphere (유리, 알루미늄, 탄소강) : ")
                if input_meterial not in dic_meterial.keys() :
                    print("Invalid meterial. Please enter one of the following: (유리, 알루미늄, 탄소강)")
                    continue
                break

            dic_info = sphere_area(input_diameter, input_meterial, set_thickness)

            print("\n")
            for key, val in dic_info.items() :
                print(f"{key} => {val}", end=", ")
            print("\n")   


        else :
            print("Ending the program.")
            break


if __name__ == "__main__" :
    main()