# Temperature-convertor
In this project, we'll create a program that can convert temperatures between Celsius and Fahrenheit.
# Step 1: Open a text editor or Python IDE

You can use any text editor or IDE to write your code. Some popular options include Visual Studio Code, PyCharm, and IDLE (which comes with Python).

# Step 2: Get the temperature and units from the user

We will prompt the user to enter the temperature and units using the input() function. Here's how to do it:



temperature = float(input("Enter the temperature: "))

units = input("Enter the units (C or F): ")



Note that we need to convert the temperature to a float using the float() function.

# Step 3: Convert the temperature

We will use the following formulas to convert between Celsius and Fahrenheit:

Celsius to Fahrenheit: (Celsius * 1.8) + 32

Fahrenheit to Celsius: (Fahrenheit - 32) / 1.8

Here's how to convert the temperature:


if units == "C":

    fahrenheit = (temperature * 1.8) + 32
    
    print(f"{temperature}°C is {fahrenheit}°F")
    
elif units == "F":

    celsius = (temperature - 32) / 1.8
    
    print(f"{temperature}°F is {celsius}°C")
    
else:

    print("Invalid units. Please enter C or F.")
    
    
    This code checks if the units are Celsius or Fahrenheit and uses the appropriate formula to convert the temperature. If the units are invalid, it prints an error message.

# Step 4: Put it all together

Here's the complete code:



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

