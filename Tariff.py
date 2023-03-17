#  Converting Cons to Billing using Tariffs

commercial_tariff = 4473
commercial_service_tariff = 2000
domestic_tariff = 3727
domestic_service_tariff = 1000
institution_tariff = 3771
institution_tariff_service = 2000
psp_tariff = 1060
psp_tariff_service = 1000
vat_all_tariffs = 0.18
name_of_unit = "Cubics"
currency = "Shillings"


#  Commercial


def conversion_to_units_commercial(num_of_units):
    if num_of_units > 0:
        return f"{commercial_tariff * num_of_units + commercial_service_tariff * vat_all_tariffs}"
    elif num_of_units == 0:
        return ", Account has not registered any consumption, verify meter functionality"
    else:
        return ", You have entered an negative value, Please recheck meter reading!"


user_input = input("Hello User, Capture readings and they will be converted to the Com Bill Amount, VAT Inclusive!\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    if user_input_number > 0:
        calculated_value = conversion_to_units_commercial(user_input_number)
        print(f"{user_input_number} {name_of_unit} is {calculated_value} {name_of_unit}")
else:
    print("Error, Strictly Input Number")


# Domestic


def conversion_to_units_domestic(num_of_units):
    if num_of_units > 0:
        return f"{domestic_tariff * num_of_units + domestic_service_tariff * vat_all_tariffs}"
    elif num_of_units == 0:
        return ", Account has not registered any consumption, verify meter functionality"
    else:
        return ", You have entered an negative value, Please recheck meter reading!"


user_input = input("Hello User, Capture readings and they will be converted to the Dom Bill Amount, VAT Inclusive!\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = conversion_to_units_domestic(int(user_input_number))
    print(f"{user_input_number} {name_of_unit} is {calculated_value} {name_of_unit}")
else:
    print("Error, Strictly Input Number")


# Institution


def conversion_to_units_institution(num_of_units):
    if num_of_units > 0:
        return f"{institution_tariff * num_of_units + institution_tariff_service * vat_all_tariffs}"
    elif num_of_units == 0:
        return ", Account has not registered any consumption, verify meter functionality"
    else:
        ", You have entered an negative value, Please recheck meter reading!"


user_input = input("Hello User, Capture readings and they will be converted to the Inst Bill Amount, VAT Inclusive!\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = conversion_to_units_institution(int(user_input_number))
    print(f"{user_input_number} {name_of_unit} is {calculated_value} {name_of_unit}")
else:
    print("Error, Strictly Input Number")


# PSP - Public Stand Post


def conversion_to_units_psp(num_of_units):
    if num_of_units > 0:
        return f"{psp_tariff * num_of_units + psp_tariff_service * vat_all_tariffs}"
    elif num_of_units == 0:
        return ", Account has not registered any consumption, verify meter functionality"
    else:
        return " ,You have entered an negative value, Please recheck meter reading!"


user_input = input("Hello User, Capture readings and they will be converted to the PSP Bill Amount, VAT Inclusive!\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = conversion_to_units_psp(int(user_input_number))
    print(f"{user_input_number} {name_of_unit} is {calculated_value} {name_of_unit}")
else:
    print("Error, Strictly Input Number")
