class TempConversion :
    def __init__(self, temp, curr_unit, to_unit):
        self.temp=temp
        self.curr_unit=curr_unit
        self.to_unit=to_unit

    def convertCelToFah(self):
        return f"{(self.temp * 9/5) + 32:.2f} F"

    def convertFahToKel(self):
        return f"{((self.temp - 32) * 5/9) + 273.15:.2f} K"

    def convertKelToCel(self):
        return f"{(self.temp - 272.15):.2f} °C"

    @staticmethod
    def conversion(temp, curr_unit, to_unit):
        tempConvert = TempConversion(temp, curr_unit, to_unit)
        if(tempConvert.curr_unit == 'C' and tempConvert.to_unit == 'F'):
            return tempConvert.convertCelToFah()
        elif(tempConvert.curr_unit == 'F' and tempConvert.to_unit == 'K'):
            return tempConvert.convertFahToKel()
        elif(tempConvert.curr_unit == 'K' and tempConvert.to_unit == 'C'):
            return tempConvert.convertKelToCel()
        else:
            return("We only support Cel to Feh, Fah to Kel, Kel to Cel")

if __name__ == "__main__":
    temp = float(input("Temp: "))
    curr_unit = str(input("Current Unit (C/F/K): ")).upper()
    to_unit = str(input("Convert Unit to (F/K/C): ")).upper()
    output = TempConversion.conversion(temp, curr_unit, to_unit)
    print(output)

# Celsius to Fahrenheit:
# F = (C × 9/5) + 32

# Fahrenheit to Kelvin:
# K = (F − 32) × 5/9 + 273.15

# Kelvin to Celsius:
# C = K − 273.15


# [1] Add input validation for temperature and unit inputs using try/except.
# [2] Replace unit string literals ('C', 'F', 'K') with Enum for safety and clarity.
# [3] Implement a conversion map (dict of tuples) to support all unit combinations (C↔F, F↔K, etc.).




