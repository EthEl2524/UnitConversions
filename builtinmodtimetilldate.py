import datetime  # converting string to datetime value


user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(": ")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")  # Take good note of the date(Year) format to be used
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
#  calculate how many days from now till deadline


print(f"Dear User!, Time remaining for your goal: {goal} is {time_till.days} days")





