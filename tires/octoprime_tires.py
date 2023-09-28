from .tires import Tires
import numpy as np


class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        return np.sum(self.tire_wear) >= 3
