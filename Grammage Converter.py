# converting a kilo into grams

a_kilo = 1000
name_of_unit = "Grams"


def kilo_to_grams(num_of_grams):
    return f"{num_of_grams} are {a_kilo / num_of_grams} {name_of_unit}"


user_input = input("Hello User, Input your number of Kilos and I will convert it to Grams!\n")
user_input_number = int(user_input)

calculated_value = kilo_to_grams(user_input_number)
print(calculated_value)
