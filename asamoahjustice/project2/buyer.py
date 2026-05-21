from constant import SEPARATOR, DIVIDER, PRICE_RANGES
from validators import validate_name, validate_number

#registring buyer
def register_buyer():
    details = ["name", "number", "location", "item", "budget"]
    buyer_data = {} #initialising buyer data variable

    for info in details:
        while True:
            #taking input for each field
            value = input(f"Please enter your {info.capitalise()}")

            #at name input
            if info == "name":
                is_valid, error_msg = validate_name(value)

                #if false was returned from the function, print the error msg
                if not is_valid:
                    print(error_msg) #print specific error
                    continue

                value = value.upper() #uppercase all if it passes

            if info == "number":
                is_valid, error_msg = validate_number(value)

                #if false was returned from the function, print the error msg
                if not is_valid:
                    print(error_msg)
                    continue #force it to be re-entered

            if info == "location":
                #check if it's not empty
                if not value:
                    print(f"{info.capitalize()} cannot be empty. Try again")
                    continue
                value = value.upper()

            if info == "item":
                if not value:
                    print(f"{info.capitalize()} cannot be empty. Try again")
                    continue

                value = value.lower()
            