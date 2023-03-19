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


def validation_and_execute():
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


user_input = ""
while user_input != "exit":
    user_input = input("Hello, Enter number of units and conversion currency!\n")
    units_and_conv = user_input.split(":")
    print(units_and_conv)
    units_and_currency_conversion = {"Units":   units_and_conv[0],
                                     "Ushs":    units_and_conv[1]}
    print(units_and_currency_conversion)
    validation_and_execute()

#  data types and their syntax

message = "enter some value"
units = 70
price = 99.10
valid_number = True
exit_input = False
list_of_days = [20, 40, 20, 100]
list_of_months = ["January", "February", "March"]
set_of_days = {66, 72, 89, 100}
sets_syntax_data = {"Units": 20, "Currency": "Ushs"}
