def is_valid_number(num_str):
    #Checks if a string contains only numeric digits
    if (len(num_str) == 0):
        return False
    for char in num_str:
        if (char < '0' or char > '9'):
            return False
    return True

def string_to_int(num_str):
    #Converts a valid string into an integer.
    if is_valid_number(num_str):
        return int(num_str)
    else:
        return None