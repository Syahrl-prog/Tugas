from abc import ABC, abstractmethod

# Abstract class
class Kendaraan(ABC):
    @abstractmethod
    def __init__(self, jarak, bahan_bakar):
        self.jarak = jarak
        self.bahan_bakar = bahan_bakar

    @abstractmethod
    def konsumsi_bahan_bakar(self):
        pass

# Subclass Mobil
class Mobil(Kendaraan):
    def __init__(self, jarak, bahan_bakar):
        super().__init__(jarak, bahan_bakar)

    def konsumsi_bahan_bakar(self):
        return self.jarak / self.bahan_bakar

# Subclass Motor
class Motor(Kendaraan):
    def __init__(self, jarak, bahan_bakar):
        super().__init__(jarak, bahan_bakar)

    def konsumsi_bahan_bakar(self):
        return self.jarak / self.bahan_bakar

# Penggunaan
mobil = Mobil(500, 50)  # Jarak 500 km dengan 50 liter bahan bakar
motor = Motor(300, 10)  # Jarak 300 km dengan 10 liter bahan bakar

print("Konsumsi Bahan Bakar Mobil:", mobil.konsumsi_bahan_bakar(), "km/liter")
print("Konsumsi Bahan Bakar Motor:", motor.konsumsi_bahan_bakar(), "km/liter")
