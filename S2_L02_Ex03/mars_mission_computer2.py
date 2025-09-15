import random
import json
import time
import psutil
import platform
from multiprocessing import Process


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
        self.env_values = {}
        self.dic_info = {}
        self.dic_load = {}

    def get_sensor_data(self, sensor) :
        while True:
            sensor.set_env()              
            self.env_values = sensor.get_env()  

            json_env = json.dumps(self.env_values, indent=4)

            print("========== sensor_data 출력 ==========")
            print(json_env)
            print("========== sensor_data 출력 완료 ==========\n") 

            time.sleep(5)

    def get_mission_computer_info(self) :
        while True:
            os_name = platform.system()
            os_version = platform.version()

            cpu_type = platform.processor()
            cpu_count_physical = psutil.cpu_count(logical=False)

            memory_total = psutil.virtual_memory().total
            memory_gb = round(memory_total / (1024**3), 2)

            self.dic_info = {
                "os name": os_name,
                "os version": os_version,
                "cpu type": cpu_type,
                "num of cpu cores": cpu_count_physical,
                "memory size": memory_gb
            }

            json_info = json.dumps(self.dic_info)
            print("========== computer_info 출력 ==========")
            print(json_info)
            print("========== computer_info 출력 완료 ==========\n")

            time.sleep(20)
    
    def get_mission_computer_load(self) :
        while True :
            cpu_usage = psutil.cpu_percent(interval=1) 
            memory = psutil.virtual_memory().percent 

            self.dic_load = {
                "cpu usage": cpu_usage,
                "memory": memory
            }

            json_load = json.dumps(self.dic_load)
            print("========== computer_load 출력 ==========")
            print(json_load)
            print("========== computer_load 출력 완료 ==========\n")

            time.sleep(20)


def main() :
    ds = DummySensor()
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    p1 = Process(target=runComputer1.get_mission_computer_info)
    p2 = Process(target=runComputer2.get_mission_computer_load)
    p3 = Process(target=runComputer3.get_sensor_data, args=(ds,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    

if __name__ == "__main__" :
    main()