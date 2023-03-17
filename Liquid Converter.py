# converting liters into milliliters

a_liter = 1000
name_of_unit = "milliliters"


def liter_to_milliliters(ltr_to_ml):
    return f"{ltr_to_ml} are {a_liter / ltr_to_ml} {name_of_unit}"


user_input = input("Hello User!, Input your number of Liters and I will convert them to milliliters!\n")
user_input_number = int(user_input)

calculated_value = liter_to_milliliters(user_input_number)
print(calculated_value)
