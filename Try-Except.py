#  Lists

commercial_tariff = 4473
commercial_service_tariff = 2000
vat_all_tariffs = 0.18
name_of_unit = "Cubics"
currency = "Shillings"


#  Commercial


def conversion_to_units_commercial(num_of_units):
    if num_of_units > 0:
        return f"{num_of_units} {name_of_unit} are {num_of_units * commercial_tariff + commercial_service_tariff * vat_all_tariffs} {currency}"
    elif num_of_units == 0:
        return ", Account has not registered any consumption, verify meter functionality"


def validation_input():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = conversion_to_units_commercial(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a zero, please enter a valid positive number!")
        else:
            print("You entered a negative number, please enter a positive number")

    except ValueError:
        print("You need to input a value")


user_input = input("Hello User, Capture readings and they will be converted to the Com Bill Amount, VAT Inclusive!\n")
validation_input()