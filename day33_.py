spams = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
# spams = []

def org_list(lsts):
    if not lsts:
        return ""
    string = ""
    for lst in lsts:
        if lst != lsts[-1]:
            string += lst
            string += ", "
        else:
            string += "and "
            string += lst
    return string


print(org_list(spams))
