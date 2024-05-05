def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")
    print("Enter the temperature value and unit:")
    temp_input = input("Example: 25 C (for Celsius), 80 F (for Fahrenheit), 300 K (for Kelvin): ")

    try:
        temp_value, unit = temp_input.split()
        temp_value = float(temp_value)

        if unit.upper() == "C":
            celsius = temp_value
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f} K")

        elif unit.upper() == "F":
            fahrenheit = temp_value
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C and {kelvin:.2f} K")

        elif unit.upper() == "K":
            kelvin = temp_value
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin} K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F")

        else:
            print("Invalid input. Please provide a valid temperature value followed by C, F, or K.")

    except ValueError:
        print("Invalid input format. Please enter temperature followed by unit (e.g., 25 C)")

if __name__ == "__main__":
    main()
