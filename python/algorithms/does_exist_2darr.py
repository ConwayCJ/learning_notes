def does_name_exist(first_names, last_names, full_name):
    for first in first_names:
        for last in last_names:
            full = first + " " + last
            if full == full_name:
                return True
    return False    