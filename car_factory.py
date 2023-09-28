from car import Car

from engine import Engine
from engines.capulet_engine import CapuletEngine
from engines.willoughby_engine import WilloughbyEngine
from engines.sternman_engine import SternmanEngine

from battery import Battery
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine: Engine = CapuletEngine(current_mileage, last_service_mileage)
        battery: Battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine: Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery: Battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        engine: Engine = SternmanEngine(warning_light_on)
        battery: Battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_rorscach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine: Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery: Battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine: Engine = CapuletEngine(current_mileage, last_service_mileage)
        battery: Battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
