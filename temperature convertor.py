temperature = float(input("Enter the temperature: "))
units = input("Enter the units (C or F): ")
if units == "C":
    fahrenheit = (temperature * 1.8) + 32
    print(f"{temperature}°C is {fahrenheit}°F")
elif units == "F":
    celsius = (temperature - 32) / 1.8
    print(f"{temperature}°F is {celsius}°C")
else:
    print("Invalid units. Please enter C or F.")
