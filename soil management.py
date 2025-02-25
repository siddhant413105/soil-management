class Soil:
    def __init__(self, location, soil_type, ph_level, nutrients):
        self.location = location
        self.soil_type = soil_type
        self.ph_level = ph_level
        self.nutrients = nutrients

    def __str__(self):
        return f"Location: {self.location}, Soil Type: {self.soil_type}, pH Level: {self.ph_level}, Nutrients: {self.nutrients}"

class SoilManagement:
    def __init__(self):
        self.soils = []

    def add_soil(self, location, soil_type, ph_level, nutrients):
        soil = Soil(location, soil_type, ph_level, nutrients)
        self.soils.append(soil)

    def view_soils(self):
        if not self.soils:
            print("No soil data available.")
            return
        for soil in self.soils:
            print(soil)

    def remove_soil(self, location):
        self.soils = [soil for soil in self.soils if soil.location != location]

# Example usage
soil_management = SoilManagement()
soil_management.add_soil("Field 1", "Loam", 6.5, {"Nitrogen": "High", "Phosphorus": "Medium", "Potassium": "Low"})
soil_management.add_soil("Field 2", "Clay", 5.8, {"Nitrogen": "Medium", "Phosphorus": "High", "Potassium": "Medium"})

print("Current Soil Data:")
soil_management.view_soils()

print("\nRemoving soil data for 'Field 1'")
soil_management.remove_soil("Field 1")

print("\nUpdated Soil Data:")
soil_management.view_soils()