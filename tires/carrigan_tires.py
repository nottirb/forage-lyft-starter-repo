from .tires import Tires
import numpy as np


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        return np.any(np.array(self.tire_wear) >= 0.9)
