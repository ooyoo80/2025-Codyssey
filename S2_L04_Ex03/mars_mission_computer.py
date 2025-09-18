import random
import json
import time
import psutil
import platform
from threading import Thread


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
        self.env_values["mars_base_internal_temperature"] = random.randint(18, 30)
        self.env_values["mars_base_external_temperature"] = random.randint(0, 21)
        self.env_values["mars_base_internal_humidity"] = random.randint(50, 60)
        self.env_values["mars_base_external_illuminance"] = random.randint(500, 715)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 3)
        self.env_values["mars_base_internal_oxygen"] = random.randint(4, 7)

    def get_env(self) :
        return self.env_values


class MissionComputer :
    def __init__(self, sensor) :
        self.sensor = sensor

    def get_sensor_data(self) :
        while True:
            self.sensor.set_env()              
            self.env_values = self.sensor.get_env()  

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
    runComputer = MissionComputer(ds)

    t1 = Thread(target=runComputer.get_mission_computer_info)
    t2 = Thread(target=runComputer.get_mission_computer_load)
    t3 = Thread(target=runComputer.get_sensor_data)
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__" :
    main()