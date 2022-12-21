import re   

def person_f_n_valid(first_name):
    patron = '^[a-zA-Z]+$'

    return bool (re.search(patron,first_name))

    