def validate_name(value):
    #if the name is empty
    if not value:
        return False, "Please name cannot be empty"

    #if name is not 2 or more words long
    if len(value.split()) < 2:
        return False, "Enter your full name"
    
    #return true if all passes
    return True, None
    
    #validation for number input
def validate_number(value):
    #if the number is int
    if not value.isdigit():
        return False, "Number must be all digits(0-9)"
    
    #if the number starts with 0
    if not value.startswith("0"):
        return False, "Number must start with 0"
    
    #if the number is exactly 10character long
    if len(value) != 10:
        return False, "Number must be exactly 10numbers long" 
    
    return True, None
    