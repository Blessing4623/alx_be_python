value = int(input("Enter the temperature to convert: "))
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 * value
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if choice == "C" or choice == "c":
    print(f"{value}°C is {convert_to_fahrenheit(value)}°F")
elif choice == "F" or choice == "f":
    print(f"{value}°F is {convert_to_celsius(value)}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")