# solution_q1.py

import sys

def setup_conversions():
    """Sets up the data structure for all unit conversions."""
    conversions = {
        "1": {
            "name": "Length",
            "units": {
                "m": 1.0, "ft": 3.28084, "km": 0.001, "mile": 0.000621371
            },
            "formulas": None
        },
        "2": {
            "name": "Mass",
            "units": {
                "kg": 1.0, "lb": 2.20462
            },
            "formulas": None
        },
        "3": {
            "name": "Temperature",
            "units": None, # Temperature uses formulas, not simple factors
            "formulas": {
                "c_to_f": lambda c: (c * 9/5) + 32,
                "f_to_c": lambda f: (f - 32) * 5/9
            }
        }
    }
    return conversions

def convert_by_factor(value, unit_from, unit_to, units_dict):
    """Converts a value using multiplication/division factors."""
    value_in_base_unit = value / units_dict[unit_from]
    final_value = value_in_base_unit * units_dict[unit_to]
    return final_value

def main():
    """Main loop for the unit converter application."""
    conversions = setup_conversions()
    
    print("Welcome to the Unit Converter!")

    while True:
        # --- Category Selection ---
        print("\nAvailable categories:")
        for key, cat in conversions.items():
            print(f"[{key}] {cat['name']}")
        cat_choice = input("Choose a category (or 'q' to quit): ").lower()

        if cat_choice == 'q':
            sys.exit("Goodbye!")
        
        if cat_choice not in conversions:
            print("Invalid category. Please try again.")
            continue
            
        selected_category = conversions[cat_choice]

        # --- Unit Selection and Calculation ---
        try:
            if selected_category["name"] == "Temperature":
                print("Choose conversion: [1] Celsius to Fahrenheit, [2] Fahrenheit to Celsius")
                temp_choice = input("> ")
                value = float(input("Enter temperature value: "))
                if temp_choice == '1':
                    result = selected_category["formulas"]["c_to_f"](value)
                    print(f"Result: {value}°C is equal to {result:.2f}°F")
                elif temp_choice == '2':
                    result = selected_category["formulas"]["f_to_c"](value)
                    print(f"Result: {value}°F is equal to {result:.2f}°C")
                else:
                    print("Invalid choice.")
            else: # Length, Mass, etc.
                units_dict = selected_category["units"]
                print(f"Available units for {selected_category['name']}: {list(units_dict.keys())}")
                unit_from = input("Convert from: ").lower()
                unit_to = input("Convert to: ").lower()
                
                if unit_from not in units_dict or unit_to not in units_dict:
                    print("Invalid unit(s). Please try again.")
                    continue
                
                value = float(input("Enter value: "))
                result = convert_by_factor(value, unit_from, unit_to, units_dict)
                print(f"\nResult: {value} {unit_from} is equal to {result:.4f} {unit_to}")

        except ValueError:
            print("Invalid number. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()