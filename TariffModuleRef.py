import TariffModuleEx

user_input = ""
while user_input != "exit":
    user_input = input("Hello, Enter number of units and conversion currency!\n")
    units_and_conv = user_input.split(":")
    print(units_and_conv)
    units_and_currency_conversion = {"Units":   units_and_conv[0],
                                     "Ushs":    units_and_conv[1]}
    print(units_and_currency_conversion)
    TariffModuleEx.validation_and_execute(units_and_currency_conversion)
