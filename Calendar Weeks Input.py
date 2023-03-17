# user input for number of weeks

num_of_week_days = 7
name_of_unit = "Weeks"


def days_in_weeks(num_of_days):
    return f"{num_of_days} days are {num_of_days / num_of_week_days} {name_of_unit}"


user_input = input("Hey User, Enter a number of Days and I will compute it to Weeks!\n")
user_input_number = int(user_input)

calculated_value = days_in_weeks(user_input_number)
print(calculated_value)