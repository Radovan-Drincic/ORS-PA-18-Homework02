def can_string_be_float(user_value):

    allowed_characters=['0','1','2','3','4','5','6','7','8','9','.','-']
    for ch in user_value:
        if ch not in allowed_characters:
            return False
        number_of_points = 0
        for ch in user_value:
            if ch == '.':
                number_of_points = number_of_points + 1
        if number_of_points > 1:
            return False
        number_of_minuses = 0
        for ch in user_value:
            if ch=='-':
                number_of_minuses=number_of_minuses + 1
        if number_of_minuses > 1:
            return False
        if number_of_minuses == 1:
            if user_value[0] != '-':
                return False
    return True

def main():
    user_value= (input("Enter lenght in kilometers: "))
    if can_string_be_float(user_value):
        print("The lenght in miles is: ", float(user_value) * 0.6214)
    else:
        print("Your input is not valid!")

main()