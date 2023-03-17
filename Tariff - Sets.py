#  Sets(built in python datatype, like lists used to store multiple items of data)
#  - Does not allow Inputting of duplicate entries i.e. stop app from running/skipping already input values

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

        user_input_number = int(num_of_units_elements)
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
    user_input = input("Hello, Capture readings in CSV form and they will be converted to Com Bill Amount, VAT Incl!\n")
    list_of_units = user_input.split(", ")

    print(list_of_units)  # This is a list
    print(set(list_of_units))

    print(type(list_of_units))  # This is a set
    print(type(set(list_of_units)))

    for num_of_units_elements in set(list_of_units):  # application of set built-in datatype mo like filtering
        validation_and_execute()
