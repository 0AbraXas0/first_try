

# function to validate an input in range of 2 integers no to write exception for no int inputs

def valid_button(min, max):
    print(f"Choose between {min} - {max}\n")
    button = 0
    while button < min & button > max:
        button = int(input(f"Choose between {min} - {max}\n"))
    return button


# out of time to complete validation for dates

def valid_date(msg):
    date = str(input(msg))
    return date
