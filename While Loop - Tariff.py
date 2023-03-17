#  Lists

comm_tariff = 4473
comm_srv_tariff = 2000
vat = 0.18
unit = "Cubics"
currency = "Ugx"


#  Commercial


def conversion_to_units_commercial(num_of_units):
    if num_of_units > 0:
        return f"{num_of_units} {unit} are {num_of_units * comm_tariff + comm_srv_tariff * vat} {currency}"
    elif num_of_units == 0:
        return ", Account has not registered any consumption, verify meter functionality"


def validation_and_execute():
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


user_input = ""
while user_input != "exit":
    user_input = input("Hello, Capture readings and they will be converted to the Com Bill Amount, VAT Inclusive!\n")
    validation_and_execute()
