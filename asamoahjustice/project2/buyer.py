from constant import SEPARATOR, DIVIDER, PRICE_RANGES, FILE_NAME
from validators import validate_name, validate_number
import json

#registring buyer
def register_buyer():
    details = ["name", "number", "location", "item", "budget"]
    buyer_data = {} #initialising buyer data variable

    for info in details:
        while True:

            if info == "budget":
                print("Tip: type 'idk' or press enter if you don't know your budget yet")

            #taking input for each field
            value = input(f"Please enter your {info.capitalize()}").strip()

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

            if info == "budget":

                if not value or value == "idk":
                    item = buyer_data["item"] #grab item they already entered

                    if item in PRICE_RANGES:
                        print(f"Typical price range for {item}: GHS {PRICE_RANGES[item]['min']:,} - {PRICE_RANGES[item]['max']:,}")
                    
                    else:
                        print("We don't have a price range for that item yet. Enter your budget.")

                    continue #asks for the budget again
                try:
                    value = int(value)

                except ValueError:
                    print("Budget must be a number")
                    continue

            buyer_data[info] = value
            break
        
    #taking purpose or specs
    print("Do you know the specifications(specs) for the items you need? yes/no?")
    specf = input("Enter yes/no: \n").upper()

    buyer_data["specs"] = {}

    if specf in ('YES', 'Y'):
        while True:
            value = input("Enter specs (e.g. 16GB RAM, i7, SSD): ").strip()
            if not value:
                print("Specs cannot be empty. Try again")
                continue

            buyer_data["specs"] = value
            buyer_data["purpose"] = ""
            break
                    
            

    else:
        while True:
            value = input("Enter purpose the item is going to be used for: ").strip()
            if not value:
                print("Purpose cannot be empty. Try again")
                continue
            
            buyer_data["purpose"] = value
            buyer_data["specs"] = ""
            break

    try:

        #reading saved old data
        with open(FILE_NAME, "r") as file:
            all_data = json.load(file)
        
        #saving buyer data to all data
        all_data["buyers"].append(buyer_data)

        #writing everything back
        with open(FILE_NAME, "w") as file:
            json.dump(all_data, file)

    except FileNotFoundError:
        all_data = {"buyers": [], "sellers": []}
        all_data["buyers"].append(buyer_data)

        with open(FILE_NAME, "w") as file:
            json.dump(all_data, file)

            


            