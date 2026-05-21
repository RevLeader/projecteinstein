from constant import SEPARATOR, DIVIDER

#registring buyer
def register_buyer():
    details = ["name", "number", "location", "item", "budget"]
    buyer_data = {} #initialising buyer data variable

    for info in details:
        while True:
            value = input(f"Please enter your {info.capitalise()}")
            