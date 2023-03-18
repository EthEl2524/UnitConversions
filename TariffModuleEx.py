#  Using Dictionaries for currency conversion derived from consumption

#  Commercial
conversion_Ushs_USD = 3694.16
conversion_Ushs_Kshs = 29.04
commercial_tariff = 4720


def conversion_to_units_currency(num_of_units, conversion_unit):
    if conversion_unit == "Ushs":
        return f"{num_of_units} units are {commercial_tariff *  num_of_units} Ushs"
    elif conversion_unit == "USD":
        return f"{num_of_units} units are USD {commercial_tariff / conversion_Ushs_USD *  num_of_units}"
    else:
        return "Unsupported Unit Conversion"


def validation_and_execute(units_and_currency_conversion):
    try:

        user_input_number = int(units_and_currency_conversion["Units"])
        if user_input_number > 0:
            calculated_value = conversion_to_units_currency(user_input_number, units_and_currency_conversion["Ushs"])
            print(calculated_value)

        elif user_input_number == 0:
            print("You entered a zero, please enter a valid positive number!")
        else:
            print("You entered a negative number, please enter a positive number")
    except ValueError:
        print("You need to input a value")
