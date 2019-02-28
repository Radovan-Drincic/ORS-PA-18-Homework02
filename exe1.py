def can_string_be_float(user_value):
    dozvoljeni_string=['0','1','2','3','4','5','6','7','8','9','.','-']
    for ch in user_value:
        if ch not in dozvoljeni_string:
            return False
        broj_tacaka=0
        for ch in user_value:
            if ch == ".":
                broj_tacaka=broj_tacaka + 1
        if broj_tacaka > 1:
            return False
    broj_minusa=0
    if ch == "-":
        broj_minusa=broj_minusa + 1
    if broj_minusa > 1:
        return False
    if (user_value[0])!="-":
        return False
    return True

def main():
    user_value=input("Can string be float:")
    print(can_string_be_float(user_value))

main()