# number of weeks per day

calculation_to_days = 7
name_of_unit = "Weeks"


def num_of_days():
    print(f"20 days are {20 / calculation_to_days} {name_of_unit}")
    print("Correct!")
    print(f"35 days are {35 / calculation_to_days} {name_of_unit}")
    print("Good!")
    print(f"50 days are {50 / calculation_to_days} {name_of_unit}")
    print("Perfect!")
    print(f"110 days are {110 / calculation_to_days} {name_of_unit}")
    print("Nice!")


def scope_check(calculated_days):
    my_var = "Variable inside function"
    my_days_num = 1, 2, 3, 4, 5, 6, 7
    print(my_var)
    print(name_of_unit)
    print(calculated_days)
    print(my_days_num)


scope_check(7)


num_of_days()
