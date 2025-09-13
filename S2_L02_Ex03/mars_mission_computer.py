import random
import json
import time


class DummySensor :
    def __init__(self) :
        self.env_values = {
    "mars_base_internal_temperature": 0,
    "mars_base_external_temperature": 0,
    "mars_base_internal_humidity": 0,
    "mars_base_external_illuminance": 0,
    "mars_base_internal_co2": 0,
    "mars_base_internal_oxygen": 0
    }

    def set_env(self) :
        for key in self.env_values.keys() :
            if key == "mars_base_internal_temperature" :
                rand_int = random.randint(18, 30)
                self.env_values[key] = rand_int
            elif key == "mars_base_external_temperature" :
                rand_int = random.randint(0, 21)
                self.env_values[key] = rand_int
            elif key == "mars_base_internal_humidity" :
                rand_int = random.randint(50, 60)
                self.env_values[key] = rand_int
            elif key == "mars_base_external_illuminance" :
                rand_int = random.randint(500, 715)
                self.env_values[key] = rand_int
            elif key == "mars_base_internal_co2" :
                rand_float = random.uniform(0.02, 0.1)
                self.env_values[key] = round(rand_float, 3)
            else :
                rand_int = random.randint(4, 7)
                self.env_values[key] = rand_int

    def get_env(self) :
        return self.env_values


class MissionComputer :
    def __init__(self) :
        self.env_values = {
        "mars_base_internal_temperature": 0,
        "mars_base_external_temperature": 0,
        "mars_base_internal_humidity": 0,
        "mars_base_external_illuminance": 0,
        "mars_base_internal_co2": 0,
        "mars_base_internal_oxygen": 0
    }
        
    def get_sensor_data(self, sensor) :
        while True:
            sensor.set_env()              
            self.env_values = sensor.get_env()  

            json_env = json.dumps(self.env_values, indent=4)
            print(json_env) 

            time.sleep(5)


def main() :
    ds = DummySensor()
    RunComputer = MissionComputer()
    
    RunComputer.get_sensor_data(ds)
    

if __name__ == "__main__" :
    main()